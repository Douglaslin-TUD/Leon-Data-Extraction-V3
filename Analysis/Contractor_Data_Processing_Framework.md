# 原始Contractor数据处理框架
# Contractor Data Processing Framework

**版本：** v1.0
**日期：** 2025-11-05
**状态：** 框架设计 - Phase 1启动

---

## 框架概述

### 当前状态
✅ **Phase 0完成：** Template标准化
- 26个字段完整定义（field_mapping_2022.json）
- 1,592行标准数据分析（Template 2022）
- 完整字段参考文档（Template_2022_Complete_Field_Reference.md, 188K）

🎯 **Phase 1目标：** Contractor数据映射
- 22个原始文件（2021年12个 + 2022年10个）
- 建立原始值→标准值的映射关系
- 处理格式混乱、命名不统一问题

---

## 五阶段处理流程

### 阶段1：数据发现 (Discovery Phase) 🔍

**目标：** 从原始contractor文件中提取所有字段和可能值

**输入：**
- `Data/FW_/Validator/2021/Origineel/` - 12个原始Excel文件
- `Data/FW_/Validator/2022/Origineel/` - 10个原始Excel文件

**处理步骤：**

```python
# 1. 扫描所有原始文件
for excel_file in contractor_files:
    # 2. 识别数据范围（找到表头和数据区域）
    header_row, data_range = identify_data_structure(excel_file)

    # 3. 提取所有字段名（原始命名）
    original_field_names = extract_field_names(header_row)

    # 4. 提取每个字段的所有唯一值
    for field in original_field_names:
        unique_values = extract_unique_values(field, data_range)
        value_frequency = count_frequency(unique_values)

        # 5. 记录到发现日志
        discovery_log[contractor][field] = {
            "unique_values": unique_values,
            "frequency": value_frequency,
            "total_rows": len(data_range),
            "null_count": count_nulls(field)
        }
```

**输出：**
1. **Contractor字段发现报告** (`contractor_field_discovery.json`)
   ```json
   {
     "contractor_name": "Heijmans_2022",
     "file_path": "Data/FW_/Validator/2022/Origineel/Heijmans.xlsx",
     "discovered_fields": [
       {
         "original_field_name": "Weg nr",
         "column_index": "A",
         "data_type": "string",
         "sample_values": ["A1", "A2", "A4"],
         "unique_count": 245,
         "null_percentage": 0.0
       },
       {
         "original_field_name": "Baan code",
         "column_index": "B",
         "data_type": "string",
         "sample_values": ["1HRR", "1HRL", "0VW"],
         "unique_count": 8,
         "null_percentage": 0.2
       }
     ],
     "total_rows": 1250,
     "sheet_name": "Sheet1"
   }
   ```

2. **字段值汇总报告** (`contractor_value_discovery.json`)
   ```json
   {
     "field_name_group": "BAAN_variants",
     "standard_field": "BAAN",
     "contractors": {
       "Heijmans_2022": {
         "field_name": "Baan code",
         "values": ["1HRR", "1HRL", "0VW", "PWL"],
         "frequency": {"1HRR": 450, "1HRL": 380, "0VW": 320, "PWL": 100}
       },
       "VolkerWessels_2022": {
         "field_name": "Baancode",
         "values": ["1HRR", "1HRL", "VW"],
         "frequency": {"1HRR": 320, "1HRL": 290, "VW": 140}
       }
     },
     "all_unique_values": ["1HRR", "1HRL", "0VW", "PWL", "VW", "1HRM"],
     "needs_mapping": true
   }
   ```

---

### 阶段2：映射建立 (Mapping Phase) 🔗

**目标：** AI辅助建立原始值→标准值的映射关系

**处理逻辑：**

```python
# 1. 字段名映射（原始字段名 → 标准字段名）
def map_field_names(original_field, standard_fields, ai_assist=True):
    """
    使用模糊匹配 + AI语义理解建立字段映射
    """
    # 规则匹配
    if "weg" in original_field.lower() and "nr" in original_field.lower():
        return "Weg", confidence=0.95

    # AI语义匹配
    if ai_assist:
        prompt = f"原始字段名: '{original_field}'\n标准字段列表: {standard_fields}\n请判断最可能的映射关系"
        ai_suggestion = query_ai(prompt)
        return ai_suggestion, confidence=0.80

    return None, confidence=0.0

# 2. 字段值映射（原始值 → 标准值）
def map_field_values(field, original_value, standard_enum_values):
    """
    建立值映射关系
    """
    # 精确匹配
    if original_value in standard_enum_values:
        return original_value, confidence=1.0

    # 模糊匹配
    fuzzy_match = find_fuzzy_match(original_value, standard_enum_values)
    if fuzzy_match.score > 0.85:
        return fuzzy_match.value, confidence=fuzzy_match.score

    # AI推理
    prompt = f"字段: {field}\n原始值: '{original_value}'\n标准值列表: {standard_enum_values}\n请推断映射关系"
    ai_mapping = query_ai(prompt)
    return ai_mapping, confidence=0.70
```

**输出：**

1. **字段名映射配置** (`contractor_field_name_mapping.json`)
   ```json
   {
     "mapping_version": "1.0",
     "last_updated": "2025-11-05",
     "field_mappings": [
       {
         "standard_field": "Weg",
         "standard_field_number": 1,
         "contractor_variants": {
           "Heijmans_2022": {
             "original_name": "Weg nr",
             "column": "A",
             "confidence": 0.95,
             "mapping_method": "rule_based",
             "verified": false
           },
           "VolkerWessels_2022": {
             "original_name": "Wegnummer",
             "column": "B",
             "confidence": 0.90,
             "mapping_method": "fuzzy_match",
             "verified": false
           }
         }
       },
       {
         "standard_field": "BAAN",
         "standard_field_number": 2,
         "contractor_variants": {
           "Heijmans_2022": {
             "original_name": "Baan code",
             "column": "B",
             "confidence": 0.95,
             "mapping_method": "rule_based",
             "verified": false
           }
         }
       }
     ]
   }
   ```

2. **字段值映射配置** (`contractor_value_mapping.json`)
   ```json
   {
     "mapping_version": "1.0",
     "field": "BAAN",
     "standard_values": ["1HRR", "1HRL", "0HRM", "0VW", "PWL"],
     "value_mappings": [
       {
         "original_value": "VW",
         "standard_value": "0VW",
         "confidence": 0.85,
         "mapping_method": "ai_inference",
         "reasoning": "VW是Verbindingsweg的缩写，标准写法是0VW",
         "verified": false,
         "contractors_using": ["VolkerWessels_2022", "BAM_2021"]
       },
       {
         "original_value": "1HRM",
         "standard_value": "0HRM",
         "confidence": 0.70,
         "mapping_method": "ai_inference",
         "reasoning": "1HRM可能是0HRM的输入错误（主干道中间车道）",
         "verified": false,
         "needs_expert_review": true,
         "contractors_using": ["Strukton_2022"]
       },
       {
         "original_value": "1HRR",
         "standard_value": "1HRR",
         "confidence": 1.0,
         "mapping_method": "exact_match",
         "verified": true,
         "contractors_using": ["all"]
       }
     ]
   }
   ```

---

### 阶段3：人工审核 (Review Phase) ✅

**目标：** Leon审核AI建议的映射关系

**审核界面设计：**

**方式A：Markdown审核文档（推荐）**

创建人类友好的审核文档：`Contractor_Mapping_Review.md`

```markdown
# Contractor数据映射审核表
**审核日期：** 2025-11-05
**审核人：** Leon
**状态：** 待审核

---

## 字段1：Weg (道路编号)

### 字段名映射审核

| Contractor | 原始字段名 | 标准字段 | 置信度 | 审核 | 备注 |
|------------|-----------|---------|-------|------|------|
| Heijmans_2022 | Weg nr | Weg | 0.95 | ✅ 正确 / ❌ 错误 / ⚠️ 需修改 |  |
| VolkerWessels | Wegnummer | Weg | 0.90 | ✅ 正确 / ❌ 错误 / ⚠️ 需修改 |  |
| BAM_2021 | Weg nummer | Weg | 0.92 | ✅ 正确 / ❌ 错误 / ⚠️ 需修改 |  |

**总结：** [ ] 全部通过 [ ] 需要修改

---

## 字段2：BAAN (车道类型)

### 字段名映射审核
[同上格式]

### 字段值映射审核

#### 映射1: "VW" → "0VW"
- **原始值：** VW
- **建议标准值：** 0VW
- **置信度：** 0.85
- **AI推理：** VW是Verbindingsweg的缩写，标准写法是0VW
- **出现频率：** 2个contractor共320次
- **审核：** ✅ 正确 / ❌ 错误 / ⚠️ 需修改
- **Leon备注：** ___________________________________________

#### 映射2: "1HRM" → "0HRM" ⚠️ 低置信度
- **原始值：** 1HRM
- **建议标准值：** 0HRM
- **置信度：** 0.70
- **AI推理：** 1HRM可能是0HRM的输入错误（主干道中间车道）
- **出现频率：** 1个contractor共45次
- **⚠️ 需要专家确认**
- **审核：** ✅ 正确 / ❌ 错误 / ⚠️ 需修改
- **Leon备注：** ___________________________________________

---

## 审核统计

- **总映射数：** 1,245
- **高置信度（>0.9）：** 980 (78.7%)
- **中置信度（0.7-0.9）：** 215 (17.3%)
- **低置信度（<0.7）：** 50 (4.0%)
- **需要专家审核：** 50
```

**方式B：Excel审核表格**

创建交互式Excel审核表：`Contractor_Mapping_Review.xlsx`
- Sheet 1: 字段名映射审核
- Sheet 2: 字段值映射审核（按字段分tab）
- 使用Excel数据验证（下拉菜单：✅正确 / ❌错误 / ⚠️需修改）
- 条件格式标记低置信度项

**审核工作流：**

```
1. AI生成初始映射 → 2. 生成审核文档 → 3. Leon审核
   ↓                    ↓                      ↓
   contractor_*.json    Mapping_Review.md     填写✅/❌/⚠️
                        ↓
4. 解析审核结果 → 5. 更新配置文件 → 6. 保存最终映射
   ↓                ↓                  ↓
   parse_review()   update_json()      contractor_mapping_final.json
```

---

### 阶段4：配置保存 (Configuration Phase) 💾

**目标：** 将审核通过的映射保存为可执行的配置文件

**最终配置文件结构：**

**1. `contractor_field_mapping_final.json`** - 字段映射（已审核）
```json
{
  "version": "1.0",
  "last_updated": "2025-11-05",
  "reviewed_by": "Leon",
  "review_date": "2025-11-05",
  "status": "approved",

  "field_mappings": {
    "Weg": {
      "standard_field_number": 1,
      "standard_field_name": "Weg",
      "contractors": {
        "Heijmans_2022": {
          "original_field_name": "Weg nr",
          "column_index": "A",
          "verified": true,
          "verified_by": "Leon",
          "verification_date": "2025-11-05"
        },
        "VolkerWessels_2022": {
          "original_field_name": "Wegnummer",
          "column_index": "B",
          "verified": true,
          "verified_by": "Leon",
          "verification_date": "2025-11-05"
        }
      }
    },

    "BAAN": {
      "standard_field_number": 2,
      "standard_field_name": "BAAN",
      "contractors": {
        "Heijmans_2022": {
          "original_field_name": "Baan code",
          "column_index": "B",
          "verified": true
        }
      }
    }
  }
}
```

**2. `contractor_value_mapping_final.json`** - 值映射（已审核）
```json
{
  "version": "1.0",
  "reviewed_by": "Leon",
  "status": "approved",

  "BAAN": {
    "standard_field": "BAAN",
    "standard_values": ["1HRR", "1HRL", "0HRM", "0VW", "PWL"],

    "value_mappings": {
      "VW": {
        "standard_value": "0VW",
        "verified": true,
        "verified_by": "Leon",
        "verification_date": "2025-11-05",
        "contractors": ["VolkerWessels_2022", "BAM_2021"],
        "occurrence_count": 320
      },

      "1HRM": {
        "standard_value": "0HRM",
        "verified": true,
        "verified_by": "Leon",
        "verification_date": "2025-11-05",
        "verification_note": "确认为输入错误，应为0HRM",
        "contractors": ["Strukton_2022"],
        "occurrence_count": 45
      },

      "1HRR": {
        "standard_value": "1HRR",
        "verified": true,
        "mapping_type": "exact_match",
        "contractors": ["all"]
      }
    }
  },

  "DEKLAAGSOORT": {
    "standard_field": "DEKLAAGSOORT",
    "standard_values": ["DZOAB", "ZOAB", "ZOABTW TL", "SMA", "AC 16 Surf"],

    "value_mappings": {
      "DZOAB ": {
        "standard_value": "DZOAB",
        "verified": true,
        "transformation": "trim_whitespace",
        "note": "尾随空格需要去除"
      },

      "Duurzaam ZOAB": {
        "standard_value": "DZOAB",
        "verified": true,
        "transformation": "semantic_match",
        "note": "Duurzaam ZOAB = DZOAB"
      }
    }
  }
}
```

**3. `contractor_extraction_config.json`** - 提取执行配置
```json
{
  "version": "1.0",
  "extraction_rules": {
    "Heijmans_2022": {
      "file_path": "Data/FW_/Validator/2022/Origineel/Heijmans.xlsx",
      "sheet_name": "Sheet1",
      "header_row": 1,
      "data_start_row": 2,
      "data_end_row": 1250,

      "field_mappings": {
        "Weg": {"column": "A", "transform": "uppercase"},
        "BAAN": {"column": "B", "transform": "uppercase"},
        "DEKLAAGSOORT": {"column": "P", "transform": "trim_and_standardize"}
      },

      "value_mappings": {
        "BAAN": {"VW": "0VW"},
        "DEKLAAGSOORT": {"DZOAB ": "DZOAB", "Duurzaam ZOAB": "DZOAB"}
      }
    }
  }
}
```

---

### 阶段5：提取应用 (Extraction Phase) 🚀

**目标：** 使用配置文件自动提取和标准化contractor数据

**提取流程：**

```python
# 主提取引擎
class ContractorDataExtractor:
    def __init__(self):
        self.field_mapping = load_json("contractor_field_mapping_final.json")
        self.value_mapping = load_json("contractor_value_mapping_final.json")
        self.extraction_config = load_json("contractor_extraction_config.json")

    def extract_contractor_data(self, contractor_name):
        """提取单个contractor的数据"""
        # 1. 加载配置
        config = self.extraction_config[contractor_name]

        # 2. 读取原始Excel
        df = pd.read_excel(
            config["file_path"],
            sheet_name=config["sheet_name"],
            header=config["header_row"] - 1,
            skiprows=range(0, config["data_start_row"] - 1)
        )

        # 3. 字段名映射
        df_mapped = self.map_field_names(df, contractor_name)

        # 4. 字段值映射
        df_standardized = self.map_field_values(df_mapped, contractor_name)

        # 5. 数据验证
        validation_results = self.validate_data(df_standardized)

        # 6. 生成标准化数据
        return df_standardized, validation_results

    def map_field_names(self, df, contractor):
        """应用字段名映射"""
        rename_dict = {}
        for standard_field, mapping in self.field_mapping["field_mappings"].items():
            if contractor in mapping["contractors"]:
                original_name = mapping["contractors"][contractor]["original_field_name"]
                rename_dict[original_name] = standard_field

        return df.rename(columns=rename_dict)

    def map_field_values(self, df, contractor):
        """应用字段值映射"""
        for field, mappings in self.value_mapping.items():
            if field in df.columns:
                for original_val, mapping_info in mappings["value_mappings"].items():
                    df[field] = df[field].replace(original_val, mapping_info["standard_value"])

        return df
```

**输出：**
1. 标准化数据文件：`standardized_data/{contractor_name}_standardized.xlsx`
2. 验证报告：`validation_reports/{contractor_name}_validation.md`
3. 数据质量报告：`quality_reports/{contractor_name}_quality.json`

---

## 文档管理策略

### 问题：Template_2022_Complete_Field_Reference.md 已经很大（188K）

**解决方案：模块化文档架构**

```
Analysis/
├── Template_2022_Complete_Field_Reference.md      # 主文档（标准定义）188K
│   └── 保留内容：26个标准字段的完整定义、统计、验证规则
│
├── Contractor_Mapping_Documentation/              # 新建contractor映射文档目录
│   ├── 00_Contractor_Mapping_Overview.md          # 映射概述
│   ├── 01_Field_Name_Mappings.md                  # 字段名映射汇总
│   ├── 02_Value_Mappings/                         # 值映射（按字段分文件）
│   │   ├── BAAN_value_mappings.md
│   │   ├── DEKLAAGSOORT_value_mappings.md
│   │   ├── STROOK_value_mappings.md
│   │   └── ...
│   ├── 03_Contractor_Profiles/                    # Contractor档案（按contractor分文件）
│   │   ├── Heijmans_2022_profile.md
│   │   ├── VolkerWessels_2022_profile.md
│   │   └── ...
│   └── 04_Mapping_Review_History/                 # 审核历史
│       ├── 2025-11-05_Review_Session_1.md
│       └── ...
│
├── Pavement_Layers_Standardization_Framework.md   # 路面层次框架（已有）
└── Archive/                                        # 归档文件
```

**主文档（Template_2022_Complete_Field_Reference.md）保持职责：**
- ✅ 标准字段定义（26个字段）
- ✅ 标准数据统计（基于Template 2022的1,592行）
- ✅ 标准验证规则
- ✅ 标准枚举值列表
- ❌ 不包含contractor特定的映射关系（移到新文档）

**新文档系列（Contractor_Mapping_Documentation/）：**
- ✅ Contractor字段名变体
- ✅ Contractor值映射关系
- ✅ Contractor数据质量问题
- ✅ 映射置信度和审核状态

**关联方式：**

在主文档中添加链接：
```markdown
### 字段2：BAAN

[标准定义、统计、验证规则...]

**📋 Contractor映射关系：**
详见 [BAAN Contractor映射文档](Contractor_Mapping_Documentation/02_Value_Mappings/BAAN_value_mappings.md)
```

在contractor映射文档中添加反向链接：
```markdown
# BAAN字段 - Contractor值映射

**标准字段定义：** 见 [Template_2022_Complete_Field_Reference.md#BAAN](../Template_2022_Complete_Field_Reference.md#2-baan)

[Contractor特定映射内容...]
```

---

## 实施时间线

### Week 1-2: Discovery Phase
- [ ] 开发数据发现脚本
- [ ] 扫描22个contractor文件
- [ ] 生成字段发现报告
- [ ] 生成值汇总报告

### Week 3-4: Mapping Phase
- [ ] 开发AI辅助映射引擎
- [ ] 建立字段名映射
- [ ] 建立值映射关系
- [ ] 生成审核文档

### Week 5: Review Phase
- [ ] Leon审核映射关系
- [ ] 修正低置信度映射
- [ ] 批准最终映射

### Week 6: Configuration Phase
- [ ] 保存最终配置文件
- [ ] 创建提取执行配置
- [ ] 文档模块化重组

### Week 7-8: Extraction Phase
- [ ] 开发提取引擎
- [ ] 批量提取contractor数据
- [ ] 验证提取质量
- [ ] 生成质量报告

---

## 关键技术点

### 1. 字段名识别（模糊匹配）

```python
from fuzzywuzzy import fuzz, process

def find_field_mapping(original_field, standard_fields, threshold=80):
    """
    使用模糊匹配找到最可能的字段映射
    """
    matches = process.extract(original_field, standard_fields, scorer=fuzz.ratio)
    best_match, score = matches[0]

    if score >= threshold:
        return best_match, score / 100.0
    else:
        return None, 0.0
```

### 2. 值映射推理（AI辅助）

```python
def infer_value_mapping(field, original_value, standard_values, use_ai=True):
    """
    推断值映射关系
    """
    # 精确匹配
    if original_value in standard_values:
        return original_value, 1.0, "exact_match"

    # 模糊匹配
    fuzzy_result = find_fuzzy_match(original_value, standard_values, threshold=85)
    if fuzzy_result:
        return fuzzy_result[0], fuzzy_result[1], "fuzzy_match"

    # AI语义推理
    if use_ai:
        prompt = f"""
        字段: {field}
        原始值: '{original_value}'
        标准值列表: {standard_values}

        请分析原始值的含义，并推荐最合适的标准值映射。
        如果无法映射，返回null。

        返回格式:
        {{
            "mapped_value": "标准值",
            "confidence": 0.0-1.0,
            "reasoning": "推理过程"
        }}
        """
        ai_response = query_ai_model(prompt)
        return ai_response["mapped_value"], ai_response["confidence"], "ai_inference"

    return None, 0.0, "no_match"
```

### 3. 审核解析（从Markdown提取审核结果）

```python
def parse_review_markdown(review_file):
    """
    解析Leon的审核结果
    """
    with open(review_file, 'r', encoding='utf-8') as f:
        content = f.read()

    review_results = {}

    # 使用正则表达式提取审核标记
    pattern = r'\| (.+?) \| (.+?) \| (.+?) \| (✅|❌|⚠️) (.+?) \|'
    matches = re.findall(pattern, content)

    for match in matches:
        contractor, original_field, standard_field, approval, note = match
        review_results[f"{contractor}:{original_field}"] = {
            "approved": approval == "✅",
            "needs_modification": approval == "⚠️",
            "rejected": approval == "❌",
            "note": note.strip()
        }

    return review_results
```

---

## 配置文件与主文档的集成

### 集成策略

**JSON配置文件（config/）：**
- `field_mapping_2022.json` - 标准字段定义（不变）
- `validation_rules_2022.json` - 标准验证规则（不变）
- `enum_values_2022.json` - 标准枚举值（不变）
- **NEW:** `contractor_field_mapping_final.json` - Contractor字段映射
- **NEW:** `contractor_value_mapping_final.json` - Contractor值映射
- **NEW:** `contractor_extraction_config.json` - 提取执行配置

**Markdown文档（Analysis/）：**
- `Template_2022_Complete_Field_Reference.md` - 人类可读的标准定义
- **NEW:** `Contractor_Mapping_Documentation/` - 人类可读的映射文档

**关系：**
```
JSON配置 (机器执行)    ←→    Markdown文档 (人类理解)
         ↓                           ↓
    提取引擎使用              Leon审核和维护
```

**更新流程：**
1. AI生成初始映射 → JSON + Markdown
2. Leon审核 Markdown文档
3. 解析审核结果 → 更新JSON配置
4. JSON配置驱动提取引擎
5. 提取结果反馈 → 更新Markdown文档

---

## 成功指标

### Phase 1完成标准：
- ✅ 22个contractor文件全部扫描完成
- ✅ 所有字段映射关系建立（>95%置信度）
- ✅ 所有值映射关系建立（>90%置信度）
- ✅ Leon审核通过
- ✅ 配置文件保存完成
- ✅ 文档模块化重组完成
- ✅ 提取引擎开发完成
- ✅ 至少1个contractor的数据成功提取并验证

### 质量指标：
- 字段名映射准确率 > 98%
- 值映射准确率 > 95%
- 数据提取完整率 > 95%
- 验证通过率 > 90%

---

## 下一步行动

### 立即开始：
1. ✅ 创建 `Contractor_Mapping_Documentation/` 目录结构
2. ⏸️ 开发数据发现脚本 (`code/discovery/contractor_scanner.py`)
3. ⏸️ 选择1-2个pilot contractor进行测试

### 需要Leon确认：
1. 审核文档格式偏好（Markdown vs Excel）
2. 映射置信度阈值（当前建议：>0.7需审核，>0.9自动通过）
3. Pilot contractor选择（建议：选择数据质量好的和差的各一个）

---

**文档结束**
