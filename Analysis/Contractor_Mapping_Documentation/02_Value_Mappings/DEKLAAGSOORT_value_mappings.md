# DEKLAAGSOORT - 字段值映射审核

**标准字段编号：** 17
**中文名称：** 面层类型
**标准定义：** 见 [Template_2022_Complete_Field_Reference.md](../../Template_2022_Complete_Field_Reference.md)

---

## 标准值列表

- `DZOAB`
- `ZOAB`
- `ZOAB+`
- `ZOABTW TL`
- `ZOABTW DL`
- `ZOABTW OL`
- `ZOABTW`
- `ZOABTW fijn`
- `ZOABDI`
- `ZOEAB`
- `SMA`
- `SMA-NL 11B`
- `SMA-NL 11`
- `SMA 8G+`
- `SMA 8 Geel`
- `AC 16 Surf`
- `AC 11 Surf`
- `DGD`
- `EAB`

## 原始值映射表

| 原始值 | → | 标准值 | 置信度 | 推理方法 | 推理说明 | 审核 | Leon备注 |
|--------|---|--------|--------|---------|---------|------|----------|
| `2L ZOAB fijn` | → | `ZOABTW fijn` | 0.80 | fuzzy_match_zoab | ZOAB系列模糊匹配: '2L ZOAB fijn' → 'ZOABTW fijn' | ⚠️ | |
| `2LZOAB` | → | `ZOAB` | 0.80 | fuzzy_match_zoab | ZOAB系列模糊匹配: '2LZOAB' → 'ZOAB' | ⚠️ | |
| `AC16 Surf` | → | `AC 16 Surf` | 0.95 | whitespace_normalized | 去除空格后匹配: 'AC16 Surf' → 'AC 16 Surf' | ✅ | |
| `DGD` | → | `DGD` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `DI-ZOAB` | → | `DZOAB` | 0.80 | fuzzy_match_zoab | ZOAB系列模糊匹配: 'DI-ZOAB' → 'DZOAB' | ⚠️ | |
| `DIZOAB` | → | `DZOAB` | 0.80 | fuzzy_match_zoab | ZOAB系列模糊匹配: 'DIZOAB' → 'DZOAB' | ⚠️ | |
| `DZOAB` | → | `DZOAB` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `Duurzaam ZOAB` | → | `DZOAB` | 0.95 | semantic_equivalence | Duurzaam ZOAB = DZOAB | ✅ | |
| `SMA` | → | `SMA` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `SMA 8G+` | → | `SMA 8G+` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `SMA-NL` | → | `SMA-NL 11` | 0.80 | fuzzy_match_sma | SMA系列模糊匹配: 'SMA-NL' → 'SMA-NL 11' | ⚠️ | |
| `SMA-NL 11` | → | `SMA-NL 11` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `SMA-NL 11 ` | → | `SMA-NL 11` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `SMA-NL 11b` | → | `SMA-NL 11B` | 0.98 | case_insensitive_match | 大小写不同: 'SMA-NL 11b' → 'SMA-NL 11B' | ✅ | |
| `SMA-NL 8G+` | → | `SMA 8G+` | 0.80 | fuzzy_match_sma | SMA系列模糊匹配: 'SMA-NL 8G+' → 'SMA 8G+' | ⚠️ | |
| `ZOAB` | → | `ZOAB` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `ZOAB+` | → | `ZOAB+` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `ZOAB16` | → | `ZOAB` | 0.80 | fuzzy_match_zoab | ZOAB系列模糊匹配: 'ZOAB16' → 'ZOAB' | ⚠️ | |
| `ZOABDI` | → | `ZOABDI` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `ZOABTW` | → | `ZOABTW` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `ZOABTW fijn` | → | `ZOABTW fijn` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |
| `ZOABTW-fijn` | → | `ZOABTW fijn` | 0.80 | fuzzy_match_zoab | ZOAB系列模糊匹配: 'ZOABTW-fijn' → 'ZOABTW fijn' | ⚠️ | |
| `ZOEAB` | → | `ZOEAB` | 1.00 | exact_match | 精确匹配标准值 | ✅ | |