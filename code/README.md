# 规则引擎使用指南

## 📚 概述

本规则引擎是一个**配置驱动的数据验证框架**，用于验证Excel数据是否符合RWS道路养护数据标准。

**核心优势：**
- ✅ 配置与代码分离 - 修改规则无需改代码
- ✅ 模块化设计 - 每种规则类型独立实现
- ✅ 易于扩展 - 添加新规则类型只需继承BaseValidator
- ✅ 测试友好 - 每个验证器可独立测试

---

## 🏗️ 架构

```
config/
├── validation_rules_2022.json   ← 验证规则配置
└── enum_values_2022.json         ← 枚举值定义

code/
├── validators/
│   └── rule_engine.py            ← 规则引擎核心
└── tests/
    └── test_rule_engine.py       ← 单元测试
```

---

## 🎯 支持的规则类型

### 1. **必填字段** (required_field)
验证字段不能为空

```json
{
  "rule_id": "REQ-001",
  "category": "required_field",
  "field": "Weg",
  "validation": {
    "type": "not_null"
  }
}
```

### 2. **枚举值** (enum)
验证字段值必须在允许列表中

```json
{
  "rule_id": "ENUM-001",
  "category": "enum",
  "field": "BAAN",
  "validation": {
    "type": "in_list",
    "allowed_values": ["1HRL", "1HRR", "0VW"]
  }
}
```

### 3. **范围验证** (range)
验证数值在指定范围内

```json
{
  "rule_id": "RANGE-001",
  "category": "range",
  "field": "DIKTE VERHARDING",
  "validation": {
    "type": "numeric_range",
    "min": 0.020,
    "max": 0.150
  }
}
```

### 4. **条件必填** (conditional_required)
当字段A满足条件时，字段B必须有值

```json
{
  "rule_id": "COND-001",
  "category": "conditional_required",
  "validation": {
    "type": "conditional_required",
    "condition": {
      "field": "STROOK",
      "operator": "equals",
      "value": "ALL"
    },
    "then": {
      "field": "Aantal rijstroken",
      "required": true
    }
  }
}
```

### 5. **跨字段逻辑** (cross_field_logic)
验证两个字段之间的关系

```json
{
  "rule_id": "CROSS-001",
  "category": "cross_field_logic",
  "validation": {
    "type": "comparison",
    "field1": "TOT",
    "operator": ">=",
    "field2": "VAN"
  }
}
```

### 6. **计算字段** (calculated_field)
验证字段值是否等于计算结果

```json
{
  "rule_id": "CALC-001",
  "category": "calculated_field",
  "validation": {
    "type": "calculated_value",
    "target_field": "Lengte",
    "formula": "(TOT - VAN) * 100",
    "tolerance": 0.01
  }
}
```

### 7. **格式验证** (format)
使用正则表达式验证格式

```json
{
  "rule_id": "FORMAT-001",
  "category": "format",
  "field": "STROOK",
  "validation": {
    "type": "regex",
    "pattern": "^\\d{1}[RWUIQBV]-[LR]$"
  }
}
```

---

## 🚀 快速开始

### 1. 基本使用

```python
from validators.rule_engine import RuleEngine

# 加载规则
engine = RuleEngine('config/validation_rules_2022.json')

# 验证单行数据
row_data = {
    'Weg': 28,
    'BAAN': '1HRL',
    'VAN': 100.0,
    'TOT': 105.0,
    'STROOK': '1R-L'
}

results = engine.validate_row(row_data)

# 检查结果
for result in results:
    if not result.passed:
        print(result)  # 打印错误信息
```

### 2. 验证整个DataFrame

```python
import pandas as pd
from validators.rule_engine import RuleEngine

# 读取Excel
df = pd.read_excel('template.xlsx')

# 验证
engine = RuleEngine('config/validation_rules_2022.json')
report = engine.validate_dataframe(df)

# 输出报告
print(f"总行数: {report['summary']['total_rows']}")
print(f"错误行数: {report['summary']['rows_with_errors']}")
print(f"总错误数: {report['summary']['total_errors']}")

# 导出错误列表
errors_df = pd.DataFrame(report['errors'])
errors_df.to_excel('validation_errors.xlsx', index=False)
```

---

## ➕ 如何添加新规则

### 方法1：使用现有规则类型

直接在`config/validation_rules_2022.json`中添加：

```json
{
  "rule_id": "NEW-001",
  "category": "enum",
  "enabled": true,
  "field": "DEKLAAGSOORT",
  "description": "面层类型必须在标准列表中",
  "validation": {
    "type": "in_list",
    "allowed_values": ["DZOAB", "ZOAB", "SMA", "AC 16 Surf"]
  },
  "error_message": "字段'DEKLAAGSOORT'值'{value}'不是标准面层类型",
  "severity": "warning"
}
```

### 方法2：创建新的规则类型

1. **在rule_engine.py中创建新验证器：**

```python
class CustomValidator(BaseValidator):
    """自定义验证器"""
    def validate(self, rule: Dict, row_data: Dict) -> ValidationResult:
        # 实现你的验证逻辑
        ...
```

2. **在RuleEngine中注册：**

```python
self.validators = {
    # ...现有验证器
    'custom_type': CustomValidator()
}
```

3. **在JSON中使用：**

```json
{
  "rule_id": "CUSTOM-001",
  "category": "custom_type",
  "validation": {
    "type": "custom_validation"
  }
}
```

---

## 🧪 运行测试

```bash
# 运行所有测试
python3 code/tests/test_rule_engine.py

# 预期输出：所有测试通过 ✓
```

---

## 📋 待完成的工作

### 当前状态
✅ 核心框架完成
✅ 7种规则类型实现
✅ 基本测试通过
✅ 示例规则创建

### 下一步（与用户协作）
⏳ 从文档中提取完整的依赖关系
⏳ 添加所有验证规则到JSON配置
⏳ 在真实数据(1592行)上运行验证
⏳ 根据结果调整规则
⏳ 扩展到2021模板

---

## 💡 设计原则

1. **配置驱动** - 业务规则在JSON中，不在代码里
2. **单一职责** - 每个验证器只做一件事
3. **开闭原则** - 对扩展开放，对修改封闭
4. **测试优先** - 每个验证器都有测试用例
5. **错误友好** - 清晰的错误信息，包含字段名和值

---

## 🤝 协作方式

**你的角色（业务专家）：**
- 提供业务规则
- 确认验证逻辑
- 测试实际数据

**AI的角色（技术实现）：**
- 将规则转换为JSON配置
- 实现验证器代码
- 调试和优化

**协作流程：**
1. 你描述规则（用自然语言）
2. 我转换为JSON配置
3. 你确认规则是否正确
4. 在真实数据上测试
5. 根据结果调整

---

## 📞 问题反馈

发现问题或需要新功能？随时告诉我！

**当前版本：** v1.0
**最后更新：** 2025-11-05
