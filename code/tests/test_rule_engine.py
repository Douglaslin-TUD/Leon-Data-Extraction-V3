"""
规则引擎测试
"""

import sys
sys.path.insert(0, '/data/AI Life/Work/RWS_Road_Engineer/01-Projects/Leon_Data_Extraction/code')

from validators.rule_engine import RuleEngine

def test_basic_validation():
    """测试基本验证功能"""
    print("="*80)
    print("测试1：基本规则验证")
    print("="*80)

    engine = RuleEngine('/data/AI Life/Work/RWS_Road_Engineer/01-Projects/Leon_Data_Extraction/config/validation_rules_2022.json')

    # 测试用例1：STROOK=ALL但Aantal rijstroken为空（应该报错）
    print("\n测试用例1：条件必填规则")
    test_row_1 = {
        'Weg': 28,
        'BAAN': '1HRL',
        'VAN': 100.0,
        'TOT': 105.0,
        'STROOK': 'ALL',
        'Aantal rijstroken': None,
        'DIKTE VERHARDING': 0.05
    }

    results = engine.validate_row(test_row_1)
    print(f"预期：应该有1个错误（STROOK=ALL时Aantal rijstroken必填）")
    print(f"实际：{len(results)}个错误")
    for r in results:
        print(f"  {r}")

    # 测试用例2：TOT < VAN（应该报错）
    print("\n测试用例2：跨字段逻辑规则")
    test_row_2 = {
        'Weg': 28,
        'BAAN': '1HRL',
        'VAN': 105.0,
        'TOT': 100.0,  # TOT < VAN，错误！
        'STROOK': '1R-L',
        'Aantal rijstroken': 1,
        'DIKTE VERHARDING': 0.05
    }

    results = engine.validate_row(test_row_2)
    print(f"预期：应该有1个错误（TOT必须>=VAN）")
    print(f"实际：{len(results)}个错误")
    for r in results:
        print(f"  {r}")

    # 测试用例3：所有规则都通过
    print("\n测试用例3：所有规则通过")
    test_row_3 = {
        'Weg': 28,
        'BAAN': '1HRL',
        'VAN': 100.0,
        'TOT': 105.0,
        'STROOK': '1R-L',
        'Aantal rijstroken': 1,
        'DIKTE VERHARDING': 0.05
    }

    results = engine.validate_row(test_row_3)
    print(f"预期：应该有0个错误")
    print(f"实际：{len(results)}个错误")
    if results:
        for r in results:
            print(f"  {r}")
    else:
        print("  ✓ 所有规则通过")


def test_enum_validation():
    """测试枚举验证"""
    print("\n" + "="*80)
    print("测试2：枚举值验证")
    print("="*80)

    engine = RuleEngine('/data/AI Life/Work/RWS_Road_Engineer/01-Projects/Leon_Data_Extraction/config/validation_rules_2022.json')

    # 测试无效的BAAN值
    print("\n测试用例：无效的BAAN值")
    test_row = {
        'Weg': 28,
        'BAAN': 'INVALID_VALUE',  # 无效值
        'VAN': 100.0,
        'TOT': 105.0,
        'STROOK': '1R-L',
        'DIKTE VERHARDING': 0.05
    }

    results = engine.validate_row(test_row)
    print(f"预期：应该有1个错误（BAAN值不在允许列表中）")
    print(f"实际：{len(results)}个错误")
    for r in results:
        print(f"  {r}")


def test_range_validation():
    """测试范围验证"""
    print("\n" + "="*80)
    print("测试3：范围验证")
    print("="*80)

    engine = RuleEngine('/data/AI Life/Work/RWS_Road_Engineer/01-Projects/Leon_Data_Extraction/config/validation_rules_2022.json')

    # 测试超出范围的厚度
    print("\n测试用例：厚度超出范围")
    test_row = {
        'Weg': 28,
        'BAAN': '1HRL',
        'VAN': 100.0,
        'TOT': 105.0,
        'STROOK': '1R-L',
        'DIKTE VERHARDING': 0.500  # 500mm，太厚了！
    }

    results = engine.validate_row(test_row)
    print(f"预期：应该有1个警告（厚度超出范围）")
    print(f"实际：{len(results)}个错误/警告")
    for r in results:
        print(f"  {r}")


if __name__ == '__main__':
    test_basic_validation()
    test_enum_validation()
    test_range_validation()

    print("\n" + "="*80)
    print("✓ 测试完成")
    print("="*80)
