#!/bin/bash

echo "=========================================="
echo "Template_2022_Complete_Field_Reference.md"
echo "质量检查报告"
echo "=========================================="
echo ""

FILE="Template_2022_Complete_Field_Reference.md"

echo "1. 文档基本信息："
echo "   总行数: $(wc -l < "$FILE")"
echo "   总字符数: $(wc -m < "$FILE")"
echo "   文件大小: $(du -h "$FILE" | cut -f1)"
echo ""

echo "2. 字段完整性检查："
echo "   字段1-4（基本信息）:"
for i in {1..4}; do
    count=$(grep -c "^### 字段 $i:" "$FILE")
    echo "      字段 $i: $count 次出现"
done
echo ""

echo "   字段5（BAAN）:"
count=$(grep -c "^### 字段 5:" "$FILE")
echo "      字段 5: $count 次出现"
echo ""

echo "   字段6-8（位置标识）:"
for i in {6..8}; do
    count=$(grep -c "^### 字段 $i:" "$FILE")
    echo "      字段 $i: $count 次出现"
done
echo ""

echo "   字段9-14（车道和尺寸）:"
for i in {9..14}; do
    count=$(grep -c "^### 字段 $i:" "$FILE")
    echo "      字段 $i: $count 次出现"
done
echo ""

echo "   字段15-21（材料规格）:"
for i in {15..21}; do
    count=$(grep -c "^### 字段 $i:" "$FILE")
    echo "      字段 $i: $count 次出现"
done
echo ""

echo "   字段22-26（施工记录）:"
for i in {22..26}; do
    count=$(grep -c "^### 字段 $i:" "$FILE")
    echo "      字段 $i: $count 次出现"
done
echo ""

echo "3. 关键章节检查："
echo "   📊 数据统计: $(grep -c "^#### 📊 数据统计" "$FILE") 次"
echo "   📈 值分布: $(grep -c "^#### 📈 值分布" "$FILE") 次"
echo "   🚨 数据质量问题: $(grep -c "^#### 🚨 数据质量问题" "$FILE") 次"
echo "   🛠️ 数据清洗建议: $(grep -c "^#### 🛠️ 数据清洗建议" "$FILE") 次"
echo "   💾 数据处理流程: $(grep -c "^#### 💾 数据处理流程" "$FILE") 次"
echo "   📋 数据验证规则: $(grep -c "^#### 📋 数据验证规则" "$FILE") 次"
echo "   🗄️ 数据库设计建议: $(grep -c "^#### 🗄️ 数据库设计建议" "$FILE") 次"
echo "   ❓ 需要与Leon确认: $(grep -c "^#### ❓ 需要与Leon确认" "$FILE") 次"
echo ""

echo "4. 代码块统计："
echo "   Python代码块: $(grep -c '```python' "$FILE") 个"
echo "   SQL代码块: $(grep -c '```sql' "$FILE") 个"
echo "   JSON代码块: $(grep -c '```json' "$FILE") 个"
echo ""

echo "5. 特殊标记检查："
echo "   ✅ 符号: $(grep -c "✅" "$FILE") 次"
echo "   ⚠️ 符号: $(grep -c "⚠️" "$FILE") 次"
echo "   ❌ 符号: $(grep -c "❌" "$FILE") 次"
echo "   🔴 符号: $(grep -c "🔴" "$FILE") 次"
echo "   ❓ 符号: $(grep -c "❓" "$FILE") 次"
echo ""

echo "=========================================="
echo "质量检查完成！"
echo "=========================================="

