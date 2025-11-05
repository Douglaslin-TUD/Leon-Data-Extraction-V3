# STROOK - 字段值映射审核

**标准字段编号：** 9
**中文名称：** 车道编号
**标准定义：** 见 [Template_2022_Complete_Field_Reference.md](../../Template_2022_Complete_Field_Reference.md)

---

## 标准值列表

- `1R-L`
- `2R-L`
- `3R-L`
- `4R-L`
- `1R-R`
- `2R-R`
- `3R-R`
- `4R-R`
- `1W-L`
- `2W-L`
- `1W-R`
- `2W-R`
- `1I-L`
- `1I-R`
- `1U-L`
- `1U-R`
- `1Q-L`
- `1Q-R`
- `1V-L`
- `1V-R`
- `ALL`

## 原始值映射表

| 原始值 | → | 标准值 | 置信度 | 推理方法 | 推理说明 | 审核 | Leon备注 |
|--------|---|--------|--------|---------|---------|------|----------|
| ` ALL ` | → | `ALL` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `1 I- L` | → | `1I-L` | 0.95 | whitespace_normalized | 去除空格后匹配: '1 I- L' → '1I-L' | ✅ | |
| `1 I- R` | → | `1I-R` | 0.95 | whitespace_normalized | 去除空格后匹配: '1 I- R' → '1I-R' | ✅ | |
| `1 R- L` | → | `1R-L` | 0.95 | whitespace_normalized | 去除空格后匹配: '1 R- L' → '1R-L' | ✅ | |
| `1 R- R` | → | `1R-R` | 0.95 | whitespace_normalized | 去除空格后匹配: '1 R- R' → '1R-R' | ✅ | |
| `1 U- L` | → | `1U-L` | 0.95 | whitespace_normalized | 去除空格后匹配: '1 U- L' → '1U-L' | ✅ | |
| `1 U- R` | → | `1U-R` | 0.95 | whitespace_normalized | 去除空格后匹配: '1 U- R' → '1U-R' | ✅ | |
| `1 V- L` | → | `1V-L` | 0.95 | whitespace_normalized | 去除空格后匹配: '1 V- L' → '1V-L' | ✅ | |
| `1 V- R` | → | `1V-R` | 0.95 | whitespace_normalized | 去除空格后匹配: '1 V- R' → '1V-R' | ✅ | |
| `1 W- L` | → | `1W-L` | 0.95 | whitespace_normalized | 去除空格后匹配: '1 W- L' → '1W-L' | ✅ | |
| `1 W- R` | → | `1W-R` | 0.95 | whitespace_normalized | 去除空格后匹配: '1 W- R' → '1W-R' | ✅ | |
| `1I-L` | → | `1I-L` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `1I-R` | → | `1I-R` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `1Q-R` | → | `1Q-R` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `1R-L` | → | `1R-L` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `1R-R` | → | `1R-R` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `1U-L` | → | `1U-L` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `1U-R` | → | `1U-R` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `1U-R ` | → | `1U-R` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `1V-L` | → | `1V-L` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `1V-R` | → | `1V-R` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `1W-L` | → | `1W-L` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `1W-R` | → | `1W-R` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `2 R- L` | → | `2R-L` | 0.95 | whitespace_normalized | 去除空格后匹配: '2 R- L' → '2R-L' | ✅ | |
| `2 R- R` | → | `2R-R` | 0.95 | whitespace_normalized | 去除空格后匹配: '2 R- R' → '2R-R' | ✅ | |
| `2 W- L` | → | `2W-L` | 0.95 | whitespace_normalized | 去除空格后匹配: '2 W- L' → '2W-L' | ✅ | |
| `2I-R` | → | `2I-R` | 0.95 | valid_format | 符合STROOK格式但非标准枚举值 | ✅ | |
| `2R-L` | → | `2R-L` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `2R-L ` | → | `2R-L` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `2R-L  ` | → | `2R-L` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `2R-R` | → | `2R-R` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `2R-R ` | → | `2R-R` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `2U-R` | → | `2U-R` | 0.95 | valid_format | 符合STROOK格式但非标准枚举值 | ✅ | |
| `3 R- L` | → | `3R-L` | 0.95 | whitespace_normalized | 去除空格后匹配: '3 R- L' → '3R-L' | ✅ | |
| `3 R- R` | → | `3R-R` | 0.95 | whitespace_normalized | 去除空格后匹配: '3 R- R' → '3R-R' | ✅ | |
| `3R-L` | → | `3R-L` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `3R-R` | → | `3R-R` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `4 R- L` | → | `4R-L` | 0.95 | whitespace_normalized | 去除空格后匹配: '4 R- L' → '4R-L' | ✅ | |
| `4 R- R` | → | `4R-R` | 0.95 | whitespace_normalized | 去除空格后匹配: '4 R- R' → '4R-R' | ✅ | |
| `4R-L` | → | `4R-L` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `ALL` | → | `ALL` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `R1,2 en 3` | → | `R1,2 en 3` | 1.00 | multi_lane | 多车道值保持原样（提取时拆分） | ✅ | |