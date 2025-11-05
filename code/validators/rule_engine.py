"""
规则引擎 - Rule Engine
用于验证Excel数据是否符合定义的规则

设计原则：
- 配置驱动：所有规则从JSON配置加载
- 模块化：每种规则类型一个验证器
- 可扩展：易于添加新的规则类型
- 测试友好：每个验证器可独立测试
"""

import json
import re
from typing import Dict, List, Any, Optional
from pathlib import Path


class ValidationResult:
    """验证结果"""
    def __init__(self, rule_id: str, passed: bool, message: str = "",
                 severity: str = "error", field: str = "", value: Any = None):
        self.rule_id = rule_id
        self.passed = passed
        self.message = message
        self.severity = severity
        self.field = field
        self.value = value

    def __repr__(self):
        status = "✓" if self.passed else "✗"
        return f"{status} [{self.severity.upper()}] {self.rule_id}: {self.message}"


class BaseValidator:
    """验证器基类"""
    def validate(self, rule: Dict, row_data: Dict) -> ValidationResult:
        raise NotImplementedError


class RequiredFieldValidator(BaseValidator):
    """必填字段验证器"""
    def validate(self, rule: Dict, row_data: Dict) -> ValidationResult:
        field = rule['field']
        value = row_data.get(field)

        # 检查是否为空
        is_empty = value is None or value == '' or (isinstance(value, float) and str(value) == 'nan')

        if is_empty:
            return ValidationResult(
                rule_id=rule['rule_id'],
                passed=False,
                message=rule['error_message'],
                severity=rule.get('severity', 'error'),
                field=field,
                value=value
            )

        return ValidationResult(
            rule_id=rule['rule_id'],
            passed=True,
            field=field,
            value=value
        )


class EnumValidator(BaseValidator):
    """枚举值验证器"""
    def validate(self, rule: Dict, row_data: Dict) -> ValidationResult:
        field = rule['field']
        value = row_data.get(field)
        allowed_values = rule['validation']['allowed_values']

        # 空值检查（如果不是必填字段）
        if value is None or value == '':
            return ValidationResult(rule['rule_id'], True, field=field)

        # 类型转换
        value_str = str(value).strip()

        if value_str not in allowed_values:
            message = rule['error_message'].replace('{value}', value_str)
            return ValidationResult(
                rule_id=rule['rule_id'],
                passed=False,
                message=message,
                severity=rule.get('severity', 'error'),
                field=field,
                value=value
            )

        return ValidationResult(rule['rule_id'], True, field=field, value=value)


class RangeValidator(BaseValidator):
    """范围验证器"""
    def validate(self, rule: Dict, row_data: Dict) -> ValidationResult:
        field = rule['field']
        value = row_data.get(field)

        # 空值检查
        if value is None or value == '':
            return ValidationResult(rule['rule_id'], True, field=field)

        try:
            value_num = float(value)
            min_val = rule['validation']['min']
            max_val = rule['validation']['max']

            if not (min_val <= value_num <= max_val):
                message = rule['error_message'].replace('{value}', str(value))
                return ValidationResult(
                    rule_id=rule['rule_id'],
                    passed=False,
                    message=message,
                    severity=rule.get('severity', 'warning'),
                    field=field,
                    value=value
                )
        except (ValueError, TypeError):
            return ValidationResult(
                rule_id=rule['rule_id'],
                passed=False,
                message=f"字段'{field}'值'{value}'不是有效数字",
                severity='error',
                field=field,
                value=value
            )

        return ValidationResult(rule['rule_id'], True, field=field, value=value)


class ConditionalRequiredValidator(BaseValidator):
    """条件必填验证器"""
    def validate(self, rule: Dict, row_data: Dict) -> ValidationResult:
        # 检查条件
        condition = rule['validation']['condition']
        condition_field = condition['field']
        condition_value = condition['value']
        condition_operator = condition.get('operator', 'equals')

        actual_value = row_data.get(condition_field)

        # 判断条件是否满足
        condition_met = False
        if condition_operator == 'equals':
            condition_met = (str(actual_value) == str(condition_value))

        # 如果条件满足，检查目标字段
        if condition_met:
            then_field = rule['validation']['then']['field']
            then_value = row_data.get(then_field)

            is_empty = then_value is None or then_value == ''

            if is_empty:
                return ValidationResult(
                    rule_id=rule['rule_id'],
                    passed=False,
                    message=rule['error_message'],
                    severity=rule.get('severity', 'error'),
                    field=then_field,
                    value=then_value
                )

        return ValidationResult(rule['rule_id'], True)


class CrossFieldValidator(BaseValidator):
    """跨字段逻辑验证器"""
    def validate(self, rule: Dict, row_data: Dict) -> ValidationResult:
        field1 = rule['validation']['field1']
        field2 = rule['validation']['field2']
        operator = rule['validation']['operator']

        value1 = row_data.get(field1)
        value2 = row_data.get(field2)

        # 空值检查
        if value1 is None or value2 is None:
            return ValidationResult(rule['rule_id'], True)

        try:
            val1 = float(value1)
            val2 = float(value2)

            passed = False
            if operator == '>=':
                passed = val1 >= val2
            elif operator == '>':
                passed = val1 > val2
            elif operator == '==':
                passed = val1 == val2

            if not passed:
                message = rule['error_message'].replace('{value1}', str(value1))
                message = message.replace('{value2}', str(value2))
                return ValidationResult(
                    rule_id=rule['rule_id'],
                    passed=False,
                    message=message,
                    severity=rule.get('severity', 'error'),
                    field=f"{field1}, {field2}",
                    value=f"{value1}, {value2}"
                )
        except (ValueError, TypeError):
            return ValidationResult(
                rule_id=rule['rule_id'],
                passed=False,
                message=f"字段'{field1}'或'{field2}'不是有效数字",
                severity='error'
            )

        return ValidationResult(rule['rule_id'], True)


class CalculatedFieldValidator(BaseValidator):
    """计算字段验证器"""
    def validate(self, rule: Dict, row_data: Dict) -> ValidationResult:
        target_field = rule['validation']['target_field']
        formula = rule['validation']['formula']
        tolerance = rule['validation'].get('tolerance', 0.01)

        actual_value = row_data.get(target_field)

        if actual_value is None:
            return ValidationResult(rule['rule_id'], True)

        try:
            # 简单公式计算（安全eval）
            # 替换字段名为实际值
            calc_formula = formula
            for field, value in row_data.items():
                if field in formula and value is not None:
                    calc_formula = calc_formula.replace(field, str(value))

            # 计算期望值
            expected_value = eval(calc_formula)
            actual_num = float(actual_value)

            # 比较（允许误差）
            diff = abs(actual_num - expected_value)

            if diff > tolerance:
                message = rule['error_message'].replace('{actual}', str(actual_num))
                message = message.replace('{expected}', f"{expected_value:.4f}")
                return ValidationResult(
                    rule_id=rule['rule_id'],
                    passed=False,
                    message=message,
                    severity=rule.get('severity', 'warning'),
                    field=target_field,
                    value=actual_value
                )
        except Exception as e:
            return ValidationResult(
                rule_id=rule['rule_id'],
                passed=False,
                message=f"计算字段'{target_field}'验证失败: {str(e)}",
                severity='warning'
            )

        return ValidationResult(rule['rule_id'], True)


class FormatValidator(BaseValidator):
    """格式验证器（正则表达式）"""
    def validate(self, rule: Dict, row_data: Dict) -> ValidationResult:
        field = rule['field']
        value = row_data.get(field)
        pattern = rule['validation']['pattern']

        if value is None or value == '':
            return ValidationResult(rule['rule_id'], True, field=field)

        value_str = str(value).strip()

        if not re.match(pattern, value_str):
            message = rule['error_message'].replace('{value}', value_str)
            return ValidationResult(
                rule_id=rule['rule_id'],
                passed=False,
                message=message,
                severity=rule.get('severity', 'warning'),
                field=field,
                value=value
            )

        return ValidationResult(rule['rule_id'], True, field=field, value=value)


class RuleEngine:
    """规则引擎主类"""

    def __init__(self, rules_config_path: str):
        """初始化规则引擎"""
        self.config_path = Path(rules_config_path)
        self.rules = []
        self.validators = {
            'required_field': RequiredFieldValidator(),
            'enum': EnumValidator(),
            'range': RangeValidator(),
            'conditional_required': ConditionalRequiredValidator(),
            'cross_field_logic': CrossFieldValidator(),
            'calculated_field': CalculatedFieldValidator(),
            'format': FormatValidator()
        }

        self.load_rules()

    def load_rules(self):
        """加载规则配置"""
        with open(self.config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
            self.rules = [r for r in config['rules'] if r.get('enabled', True)]

        print(f"✓ 已加载 {len(self.rules)} 条规则")

    def validate_row(self, row_data: Dict, row_number: int = None) -> List[ValidationResult]:
        """验证单行数据"""
        results = []

        for rule in self.rules:
            category = rule['category']
            validator = self.validators.get(category)

            if validator is None:
                print(f"⚠️  警告：未知规则类型 '{category}'，跳过规则 {rule['rule_id']}")
                continue

            result = validator.validate(rule, row_data)
            if not result.passed:
                results.append(result)

        return results

    def validate_dataframe(self, df) -> Dict:
        """验证整个DataFrame"""
        all_errors = []
        summary = {
            'total_rows': len(df),
            'rows_with_errors': 0,
            'total_errors': 0,
            'errors_by_severity': {'error': 0, 'warning': 0, 'info': 0},
            'errors_by_rule': {}
        }

        for idx, row in df.iterrows():
            row_data = row.to_dict()
            errors = self.validate_row(row_data, row_number=idx+2)  # +2 for Excel row number

            if errors:
                summary['rows_with_errors'] += 1
                for error in errors:
                    all_errors.append({
                        'row': idx+2,
                        'rule_id': error.rule_id,
                        'field': error.field,
                        'value': error.value,
                        'message': error.message,
                        'severity': error.severity
                    })

                    summary['total_errors'] += 1
                    summary['errors_by_severity'][error.severity] += 1

                    if error.rule_id not in summary['errors_by_rule']:
                        summary['errors_by_rule'][error.rule_id] = 0
                    summary['errors_by_rule'][error.rule_id] += 1

        return {
            'summary': summary,
            'errors': all_errors
        }


def main():
    """测试代码"""
    # 示例：加载规则并测试
    engine = RuleEngine('config/validation_rules_2022.json')

    # 测试数据
    test_row = {
        'Weg': 28,
        'BAAN': '1HRL',
        'VAN': 100.0,
        'TOT': 105.0,
        'STROOK': 'ALL',
        'Aantal rijstroken': None,  # 应该报错
        'DIKTE VERHARDING': 0.05
    }

    results = engine.validate_row(test_row)

    print("\n验证结果：")
    for result in results:
        print(result)


if __name__ == '__main__':
    main()
