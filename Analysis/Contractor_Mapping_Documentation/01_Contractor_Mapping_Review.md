# Contractor数据映射审核表
**生成日期：** 2025-11-05 21:08
**审核人：** Leon
**状态：** ⏸️ 待审核

---

## 📋 审核说明

### 审核标记：
- ✅ **正确** - 映射关系正确，通过
- ❌ **错误** - 映射关系错误，需要修改
- ⚠️ **需修改** - 基本正确但需要调整

### 审核方法：
1. 检查每个映射关系
2. 在"审核"列填写 ✅/❌/⚠️
3. 如有问题，在"备注"列填写说明
4. 完成后通知AI进行下一步处理

---

## 📊 审核统计

- **字段名映射总数：** 14
  - 自动验证（置信度≥95%）：13
  - 需人工审核：1
- **字段值映射总数：** 67
  - 自动验证（置信度≥95%）：59
  - 需人工审核（置信度<85%）：8

---

## Part 1: 字段名映射审核

检查每个contractor的字段名是否正确映射到标准字段。

### 字段 2: DISTRICT (区域)

| Contractor | 原始字段名 | 列位置 | 置信度 | 方法 | 审核 | 备注 |
|------------|-----------|--------|--------|------|------|------|
| 20220316-Formulier_2021 - uitv | DISTRICT | 1 | 100% | exact_match | ✅ | |
| AB7 MN PCZ en PCN asfalt LVO 2 | DISTRICT | 1 | 100% | exact_match | ✅ | |
| Asfalt 2022 Zuid Nederland_202 | DISTRICT | 1 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | DISTRICT | 1 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | DISTRICT | 1 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | DISTRICT | 1 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | DISTRICT | 1 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | DISTRICT | 1 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | DISTRICT | 1 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7_ | DISTRICT | 1 | 100% | exact_match | ✅ | |
| Formulier_2022 - uitvraag AB7  | DISTRICT | 1 | 100% | exact_match | ✅ | |
| Formulier_2022 - uitvraag AB7  |   | 20 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2022 - uitvraag AB7_ |   | 20 | 85% | fuzzy_match | ⏸️ | |
| Mourik WNZZ Template_deklagen_ | DISTRICT | 0 | 100% | exact_match | ✅ | |
| WNZ2 Formulier_2021 - uitvraag | DISTRICT | 1 | 100% | exact_match | ✅ | |
| asfalt productiedashboard 2022 | DISTRICT | 1 | 100% | exact_match | ✅ | |

**匹配率：** 18/19 (94.7%)

### 字段 3: ZAAKNUMMER (案件编号)

| Contractor | 原始字段名 | 列位置 | 置信度 | 方法 | 审核 | 备注 |
|------------|-----------|--------|--------|------|------|------|
| 20220316-Formulier_2021 - uitv | ZAAKNUMMER, | 2 | 85% | fuzzy_match | ⏸️ | |
| AB7 MN PCZ en PCN asfalt LVO 2 | Zaaknr (2) | 3 | 75% | fuzzy_match | ⏸️ | |
| Asfalt 2022 Zuid Nederland_202 | ZAAKNUMMER | 2 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | ZAAKNUMMER, | 2 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | ZAAKNUMMER, | 2 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | ZAAKNUMMER, | 2 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | ZAAKNUMMER, | 2 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | ZAAKNUMMER | 2 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | ZAAKNUMMER, | 2 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7_ | ZAAKNUMMER, | 2 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2022 - uitvraag AB7  | ZAAKNUMMER, | 2 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2022 - uitvraag AB7  | ZAAKNUMMER, | 2 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2022 - uitvraag AB7_ | ZAAKNUMMER, | 2 | 85% | fuzzy_match | ⏸️ | |
| WNZ2 Formulier_2021 - uitvraag | ZAAKNUMMER, | 2 | 85% | fuzzy_match | ⏸️ | |
| asfalt productiedashboard 2022 | ZAAKNUMMER, | 2 | 85% | fuzzy_match | ⏸️ | |

**匹配率：** 15/19 (78.9%)

### 字段 4: Weg (道路编号)

| Contractor | 原始字段名 | 列位置 | 置信度 | 方法 | 审核 | 备注 |
|------------|-----------|--------|--------|------|------|------|
| 20220316-Formulier_2021 - uitv | WEGLET (zie toelichting blad 2) | 5 | 85% | fuzzy_match | ⏸️ | |
| AB7 MN PCZ en PCN asfalt LVO 2 | Wegnummer  | 4 | 85% | fuzzy_match | ⏸️ | |
| Asfalt 2022 Zuid Nederland_202 | WEGLET (zie toelichting blad 2) | 5 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | WEGLET (zie toelichting blad 2) | 5 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | WEGLET (zie toelichting blad 2) | 5 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | WEGLET (zie toelichting blad 2) | 6 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | WEGLET (zie toelichting blad 2) | 5 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | WEGLET 
(zie toelichting blad 2) | 6 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | WEGLET (zie toelichting blad 2) | 5 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7_ | WEGLET (zie toelichting blad 2) | 5 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2022 - uitvraag AB7  | WEGLET (zie toelichting blad 2) | 5 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2022 - uitvraag AB7  | WEGLET (zie toelichting blad 2) | 5 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2022 - uitvraag AB7_ | WEGLET (zie toelichting blad 2) | 5 | 85% | fuzzy_match | ⏸️ | |
| Mourik WNZZ Template_deklagen_ | WEG | 1 | 100% | exact_match | ✅ | |
| WNZ2 Formulier_2021 - uitvraag | WEGLET (zie toelichting blad 2) | 5 | 85% | fuzzy_match | ⏸️ | |
| asfalt productiedashboard 2022 | WEGLET (zie toelichting blad 2) | 5 | 85% | fuzzy_match | ⏸️ | |

**匹配率：** 30/19 (157.9%)

### 字段 5: BAAN (车道类型)

| Contractor | 原始字段名 | 列位置 | 置信度 | 方法 | 审核 | 备注 |
|------------|-----------|--------|--------|------|------|------|
| 20220316-Formulier_2021 - uitv | Aantal rijstroken - in geval van rijbaanbreed (ALL) | 9 | 85% | fuzzy_match | ⏸️ | |
| AB7 MN PCZ en PCN asfalt LVO 2 | Aantal rijstroken - in geval van rijbaanbreed (ALL) | 7 | 85% | fuzzy_match | ⏸️ | |
| Asfalt 2022 Zuid Nederland_202 | Aantal rijstroken - in geval van rijbaanbreed (ALL) | 9 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | Aantal rijstroken - in geval van rijbaanbreed (ALL) | 9 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | Aantal rijstroken - in geval van rijbaanbreed (ALL) | 9 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | Aantal rijstroken - in geval van rijbaanbreed (ALL) | 10 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | Aantal rijstroken - in geval van rijbaanbreed (ALL) | 9 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | Aantal rijstroken - in geval van rijbaanbreed (ALL) | 10 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | Aantal rijstroken - in geval van rijbaanbreed (ALL) | 9 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7_ | Aantal rijstroken - in geval van rijbaanbreed (ALL) | 9 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2022 - uitvraag AB7  | Aantal rijstroken - in geval van rijbaanbreed (ALL) | 9 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2022 - uitvraag AB7  | Aantal rijstroken - in geval van rijbaanbreed (ALL) | 9 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2022 - uitvraag AB7_ | Aantal rijstroken - in geval van rijbaanbreed (ALL) | 9 | 85% | fuzzy_match | ⏸️ | |
| Lijst (asfalterings)werkzaamhe | RW | Baan | Hmp-Hmp | Object | Object naam | 3 | 85% | fuzzy_match | ⏸️ | |
| Mourik WNZZ Template_deklagen_ | BAAN | 2 | 100% | exact_match | ✅ | |
| WNZ2 Formulier_2021 - uitvraag | Aantal rijstroken - in geval van rijbaanbreed (ALL) | 9 | 85% | fuzzy_match | ⏸️ | |
| asfalt productiedashboard 2022 | Aantal rijstroken - in geval van rijbaanbreed (ALL) | 9 | 85% | fuzzy_match | ⏸️ | |

**匹配率：** 32/19 (168.4%)

### 字段 6: WEGLET (道路字母标识)

| Contractor | 原始字段名 | 列位置 | 置信度 | 方法 | 审核 | 备注 |
|------------|-----------|--------|--------|------|------|------|
| Mourik WNZZ Template_deklagen_ | WEGLET | 3 | 100% | exact_match | ✅ | |

**匹配率：** 1/19 (5.3%)

### 字段 7: VAN (起始位置)

| Contractor | 原始字段名 | 列位置 | 置信度 | 方法 | 审核 | 备注 |
|------------|-----------|--------|--------|------|------|------|
| 20220316-Formulier_2021 - uitv | DIKTE TUSSENLAAG (indien van toepassing) | 13 | 85% | fuzzy_match | ⏸️ | |
| AB7 MN PCZ en PCN asfalt LVO 2 | DIKTE TUSSENLAAG (indien van toepassing)32 | 12 | 85% | fuzzy_match | ⏸️ | |
| Asfalt 2022 Zuid Nederland_202 | DIKTE TUSSENLAAG (indien van toepassing) in mm | 14 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | DIKTE TUSSENLAAG (indien van toepassing) | 13 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | DIKTE TUSSENLAAG (indien van toepassing) | 13 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | DIKTE TUSSENLAAG (indien van toepassing) | 14 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | DIKTE TUSSENLAAG (indien van toepassing) | 13 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | DIKTE TUSSENLAAG (indien van toepassing) | 14 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | DIKTE TUSSENLAAG (indien van toepassing) | 13 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7_ | DIKTE TUSSENLAAG (indien van toepassing) | 13 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2022 - uitvraag AB7  | DIKTE TUSSENLAAG (indien van toepassing) | 15 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2022 - uitvraag AB7  | DIKTE TUSSENLAAG (indien van toepassing) | 13 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2022 - uitvraag AB7_ | DIKTE TUSSENLAAG (indien van toepassing) | 13 | 85% | fuzzy_match | ⏸️ | |
| Mourik WNZZ Template_deklagen_ | VAN | 4 | 100% | exact_match | ✅ | |
| WNZ2 Formulier_2021 - uitvraag | DIKTE TUSSENLAAG (indien van toepassing) | 13 | 85% | fuzzy_match | ⏸️ | |
| asfalt productiedashboard 2022 | DIKTE TUSSENLAAG (indien van toepassing) | 13 | 85% | fuzzy_match | ⏸️ | |

**匹配率：** 30/19 (157.9%)

### 字段 8: TOT (结束位置)

| Contractor | 原始字段名 | 列位置 | 置信度 | 方法 | 审核 | 备注 |
|------------|-----------|--------|--------|------|------|------|
| 20220316-Formulier_2021 - uitv | TONNEN | 18 | 75% | fuzzy_match | ⏸️ | |
| AB7 MN PCZ en PCN asfalt LVO 2 | TONNEN | 16 | 75% | fuzzy_match | ⏸️ | |
| Asfalt 2022 Zuid Nederland_202 | TONNEN | 19 | 75% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | TONNEN | 18 | 75% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | TONNEN | 18 | 75% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | TONNEN | 19 | 75% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | TONNEN | 18 | 75% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | TONNEN | 19 | 75% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | TONNEN | 18 | 75% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7_ | TONNEN | 18 | 75% | fuzzy_match | ⏸️ | |
| Formulier_2022 - uitvraag AB7  | TONNEN | 18 | 75% | fuzzy_match | ⏸️ | |
| Formulier_2022 - uitvraag AB7  | TONNEN | 18 | 75% | fuzzy_match | ⏸️ | |
| Formulier_2022 - uitvraag AB7_ | TONNEN | 18 | 75% | fuzzy_match | ⏸️ | |
| Mourik WNZZ Template_deklagen_ | TOT | 5 | 100% | exact_match | ✅ | |
| WNZ2 Formulier_2021 - uitvraag | TONNEN | 18 | 75% | fuzzy_match | ⏸️ | |
| asfalt productiedashboard 2022 | TONNEN | 18 | 75% | fuzzy_match | ⏸️ | |

**匹配率：** 30/19 (157.9%)

### 字段 9: STROOK (车道编号)

| Contractor | 原始字段名 | 列位置 | 置信度 | 方法 | 审核 | 备注 |
|------------|-----------|--------|--------|------|------|------|
| 20220316-Formulier_2021 - uitv | STROOK | 8 | 100% | exact_match | ✅ | |
| AB7 MN PCZ en PCN asfalt LVO 2 | Rijstrook  | 6 | 85% | fuzzy_match | ⏸️ | |
| Asfalt 2022 Zuid Nederland_202 | STROOK | 8 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | STROOK | 8 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | STROOK | 8 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | STROOK | 9 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | STROOK | 8 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | STROOK | 9 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | STROOK | 8 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7_ | STROOK | 8 | 100% | exact_match | ✅ | |
| Formulier_2022 - uitvraag AB7  | STROOK | 8 | 100% | exact_match | ✅ | |
| Formulier_2022 - uitvraag AB7  | STROOK | 8 | 100% | exact_match | ✅ | |
| Formulier_2022 - uitvraag AB7_ | STROOK | 8 | 100% | exact_match | ✅ | |
| Mourik WNZZ Template_deklagen_ | STROOK | 6 | 100% | exact_match | ✅ | |
| WNZ2 Formulier_2021 - uitvraag | STROOK | 8 | 100% | exact_match | ✅ | |
| asfalt productiedashboard 2022 | STROOK | 8 | 100% | exact_match | ✅ | |

**匹配率：** 16/19 (84.2%)

### 字段 10: Aantal rijstroken (车道数量)

| Contractor | 原始字段名 | 列位置 | 置信度 | 方法 | 审核 | 备注 |
|------------|-----------|--------|--------|------|------|------|
| Mourik WNZZ Template_deklagen_ | aantal stroken | 7 | 75% | fuzzy_match | ⏸️ | |

**匹配率：** 1/19 (5.3%)

### 字段 11: KM_Van (起点公里数)

| Contractor | 原始字段名 | 列位置 | 置信度 | 方法 | 审核 | 备注 |
|------------|-----------|--------|--------|------|------|------|
| 20220316-Formulier_2021 - uitv | KM_Van | 10 | 100% | exact_match | ✅ | |
| AB7 MN PCZ en PCN asfalt LVO 2 | Km_van  | 8 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | KM_Van | 10 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | KM_Van | 10 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | KM_Van | 11 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | KM_Van | 10 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | KM_Van | 11 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | KM_Van | 10 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7_ | KM_Van | 10 | 100% | exact_match | ✅ | |
| Formulier_2022 - uitvraag AB7  | KM_Van | 10 | 100% | exact_match | ✅ | |
| Formulier_2022 - uitvraag AB7  | KM_Van | 10 | 100% | exact_match | ✅ | |
| Formulier_2022 - uitvraag AB7_ | KM_Van | 10 | 100% | exact_match | ✅ | |
| WNZ2 Formulier_2021 - uitvraag | KM_Van | 10 | 100% | exact_match | ✅ | |
| asfalt productiedashboard 2022 | KM_Van | 10 | 100% | exact_match | ✅ | |

**匹配率：** 14/19 (73.7%)

### 字段 12: KM_Tot (终点公里数)

| Contractor | 原始字段名 | 列位置 | 置信度 | 方法 | 审核 | 备注 |
|------------|-----------|--------|--------|------|------|------|
| 20220316-Formulier_2021 - uitv | KM_Tot | 11 | 100% | exact_match | ✅ | |
| AB7 MN PCZ en PCN asfalt LVO 2 | Km_tot | 9 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | KM_Tot | 11 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | KM_Tot | 11 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | KM_Tot | 12 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | KM_Tot | 11 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | KM_Tot | 12 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | KM_Tot | 11 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7_ | KM_Tot | 11 | 100% | exact_match | ✅ | |
| Formulier_2022 - uitvraag AB7  | KM_Tot | 11 | 100% | exact_match | ✅ | |
| Formulier_2022 - uitvraag AB7  | KM_Tot | 11 | 100% | exact_match | ✅ | |
| Formulier_2022 - uitvraag AB7_ | KM_Tot | 11 | 100% | exact_match | ✅ | |
| WNZ2 Formulier_2021 - uitvraag | KM_Tot | 11 | 100% | exact_match | ✅ | |
| asfalt productiedashboard 2022 | KM_Tot | 11 | 100% | exact_match | ✅ | |

**匹配率：** 14/19 (73.7%)

### 字段 15: MENGSELCODE (混合料代码)

| Contractor | 原始字段名 | 列位置 | 置信度 | 方法 | 审核 | 备注 |
|------------|-----------|--------|--------|------|------|------|
| 20220316-Formulier_2021 - uitv | MENGSELCODE | 16 | 100% | exact_match | ✅ | |
| AB7 MN PCZ en PCN asfalt LVO 2 | MENGSELCODE | 14 | 100% | exact_match | ✅ | |
| Asfalt 2022 Zuid Nederland_202 | MENGSEL-CODE | 17 | 75% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | MENGSELCODE | 16 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | MENGSELCODE | 16 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | MENGSELCODE | 17 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | MENGSELCODE | 16 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | MENGSELCODE | 17 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | MENGSELCODE | 16 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7_ | MENGSELCODE | 16 | 100% | exact_match | ✅ | |
| Formulier_2022 - uitvraag AB7  | GRANULAIR MENGSEL (0/16, 4/8, 2/6, 0/11, 0/8 enz) | 13 | 75% | fuzzy_match | ⏸️ | |
| Formulier_2022 - uitvraag AB7  | MENGSELCODE | 16 | 100% | exact_match | ✅ | |
| Formulier_2022 - uitvraag AB7_ | MENGSELCODE | 16 | 100% | exact_match | ✅ | |
| WNZ2 Formulier_2021 - uitvraag | MENGSELCODE | 16 | 100% | exact_match | ✅ | |
| asfalt productiedashboard 2022 | MENGSELCODE | 16 | 100% | exact_match | ✅ | |

**匹配率：** 30/19 (157.9%)

### 字段 17: DEKLAAGSOORT (面层类型)

| Contractor | 原始字段名 | 列位置 | 置信度 | 方法 | 审核 | 备注 |
|------------|-----------|--------|--------|------|------|------|
| 20220316-Formulier_2021 - uitv | DEKLAAGSOORT (bijv. ZOAB, SMA, tweelaags ZOAB, duurzaam ZOAB, etc.) | 12 | 85% | fuzzy_match | ⏸️ | |
| AB7 MN PCZ en PCN asfalt LVO 2 | DEKLAAGSOORT (bijv. ZOAB, SMA, tweelaags ZOAB, duurzaam ZOAB, etc.) | 10 | 85% | fuzzy_match | ⏸️ | |
| Asfalt 2022 Zuid Nederland_202 | DIKTE DEKLAAG in mm | 13 | 75% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | DEKLAAGSOORT (bijv. ZOAB, SMA, tweelaags ZOAB, duurzaam ZOAB, etc.) | 12 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | DEKLAAGSOORT (bijv. ZOAB, SMA, tweelaags ZOAB, duurzaam ZOAB, etc.) | 12 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | DEKLAAGSOORT (bijv. ZOAB, SMA, tweelaags ZOAB, duurzaam ZOAB, etc.) | 13 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | DEKLAAGSOORT (bijv. ZOAB, SMA, tweelaags ZOAB, duurzaam ZOAB, etc.) | 12 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | DEKLAAGSOORT (bijv. ZOAB, SMA, tweelaags ZOAB, duurzaam ZOAB, etc.) | 13 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | DEKLAAGSOORT (bijv. ZOAB, SMA, tweelaags ZOAB, duurzaam ZOAB, etc.) | 12 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7_ | DEKLAAGSOORT (bijv. ZOAB, SMA, tweelaags ZOAB, duurzaam ZOAB, etc.) | 12 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2022 - uitvraag AB7  | DEKLAAGSOORT (bijv. ZOAB, SMA, tweelaags ZOAB, duurzaam ZOAB, etc.) | 14 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2022 - uitvraag AB7  | DEKLAAGSOORT (bijv. ZOAB, SMA, tweelaags ZOAB, duurzaam ZOAB, etc.) | 12 | 85% | fuzzy_match | ⏸️ | |
| Formulier_2022 - uitvraag AB7_ | DEKLAAGSOORT (bijv. ZOAB, SMA, tweelaags ZOAB, duurzaam ZOAB, etc.) | 12 | 85% | fuzzy_match | ⏸️ | |
| Mourik WNZZ Template_deklagen_ | DEKLAAGSOORT | 10 | 100% | exact_match | ✅ | |
| ON perceel 3_2021 | ZOAB0/8 | 9 | 75% | fuzzy_match | ⏸️ | |
| WNZ2 Formulier_2021 - uitvraag | DEKLAAGSOORT (bijv. ZOAB, SMA, tweelaags ZOAB, duurzaam ZOAB, etc.) | 12 | 85% | fuzzy_match | ⏸️ | |
| asfalt productiedashboard 2022 | DEKLAAGSOORT (bijv. ZOAB, SMA, tweelaags ZOAB, duurzaam ZOAB, etc.) | 12 | 85% | fuzzy_match | ⏸️ | |

**匹配率：** 19/19 (100.0%)

### 字段 22: AANLEGDATUM (施工日期)

| Contractor | 原始字段名 | 列位置 | 置信度 | 方法 | 审核 | 备注 |
|------------|-----------|--------|--------|------|------|------|
| 20220316-Formulier_2021 - uitv | AANLEGDATUM | 14 | 100% | exact_match | ✅ | |
| AB7 MN PCZ en PCN asfalt LVO 2 | Datum oplevering | 11 | 75% | fuzzy_match | ⏸️ | |
| Asfalt 2022 Zuid Nederland_202 | AANLEG-DATUM | 15 | 75% | fuzzy_match | ⏸️ | |
| Formulier_2021 - uitvraag AB7  | AANLEGDATUM | 14 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | AANLEGDATUM | 14 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | AANLEGDATUM | 15 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | AANLEGDATUM | 14 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | AANLEGDATUM | 15 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7  | AANLEGDATUM | 14 | 100% | exact_match | ✅ | |
| Formulier_2021 - uitvraag AB7_ | AANLEGDATUM | 14 | 100% | exact_match | ✅ | |
| Formulier_2022 - uitvraag AB7  | AANLEGDATUM | 16 | 100% | exact_match | ✅ | |
| Formulier_2022 - uitvraag AB7  | AANLEGDATUM | 14 | 100% | exact_match | ✅ | |
| Formulier_2022 - uitvraag AB7_ | AANLEGDATUM | 14 | 100% | exact_match | ✅ | |
| Mourik WNZZ Template_deklagen_ | AANLEGDATUM | 11 | 100% | exact_match | ✅ | |
| WNZ2 Formulier_2021 - uitvraag | AANLEGDATUM | 14 | 100% | exact_match | ✅ | |
| asfalt productiedashboard 2022 | AANLEGDATUM | 14 | 100% | exact_match | ✅ | |

**匹配率：** 16/19 (84.2%)

---

## Part 2: 字段值映射审核

检查原始值到标准值的映射是否正确。重点关注 ⚠️ 标记的低置信度映射。

### 字段 2: DISTRICT (区域)

**标准值列表：** NN-Oost, Zee en Delta, Noord, Oost, Zuid, West

**原始唯一值数量：** 31

**已映射数量：** 1 (3.2%)


<details>
<summary>✅ 高置信度映射 (1个) - 点击展开</summary>

| 原始值 | 标准值 | 置信度 | 方法 | 说明 |
|--------|--------|--------|------|------|
| `Zuid` | `Zuid` | 1.00 | exact_match | 精确匹配标准值 |
</details>

### 字段 5: BAAN (车道类型)

**标准值列表：** 1HRR, 1HRL, 0HRM, 0VW, PWL

**原始唯一值数量：** 34

**已映射数量：** 1 (2.9%)


<details>
<summary>✅ 高置信度映射 (1个) - 点击展开</summary>

| 原始值 | 标准值 | 置信度 | 方法 | 说明 |
|--------|--------|--------|------|------|
| `1HRL` | `1HRL` | 1.00 | exact_match | 精确匹配标准值 |
</details>

### 字段 9: STROOK (车道编号)

**标准值列表：** 1R-L, 2R-L, 3R-L, 4R-L, 1R-R, 2R-R, 3R-R, 4R-R, 1W-L, 2W-L, 1W-R, 2W-R, 1I-L, 1I-R, 1U-L, 1U-R, 1Q-L, 1Q-R, 1V-L, 1V-R, ALL

**原始唯一值数量：** 102

**已映射数量：** 42 (41.2%)


<details>
<summary>✅ 高置信度映射 (42个) - 点击展开</summary>

| 原始值 | 标准值 | 置信度 | 方法 | 说明 |
|--------|--------|--------|------|------|
| ` ALL ` | `ALL` | 1.00 | exact_match | 精确匹配标准值 |
| `1 I- L` | `1I-L` | 0.95 | whitespace_normalized | 去除空格后匹配: '1 I- L' → '1I-L' |
| `1 I- R` | `1I-R` | 0.95 | whitespace_normalized | 去除空格后匹配: '1 I- R' → '1I-R' |
| `1 R- L` | `1R-L` | 0.95 | whitespace_normalized | 去除空格后匹配: '1 R- L' → '1R-L' |
| `1 R- R` | `1R-R` | 0.95 | whitespace_normalized | 去除空格后匹配: '1 R- R' → '1R-R' |
| `1 U- L` | `1U-L` | 0.95 | whitespace_normalized | 去除空格后匹配: '1 U- L' → '1U-L' |
| `1 U- R` | `1U-R` | 0.95 | whitespace_normalized | 去除空格后匹配: '1 U- R' → '1U-R' |
| `1 V- L` | `1V-L` | 0.95 | whitespace_normalized | 去除空格后匹配: '1 V- L' → '1V-L' |
| `1 V- R` | `1V-R` | 0.95 | whitespace_normalized | 去除空格后匹配: '1 V- R' → '1V-R' |
| `1 W- L` | `1W-L` | 0.95 | whitespace_normalized | 去除空格后匹配: '1 W- L' → '1W-L' |
| `1 W- R` | `1W-R` | 0.95 | whitespace_normalized | 去除空格后匹配: '1 W- R' → '1W-R' |
| `1I-L` | `1I-L` | 1.00 | exact_match | 精确匹配标准值 |
| `1I-R` | `1I-R` | 1.00 | exact_match | 精确匹配标准值 |
| `1Q-R` | `1Q-R` | 1.00 | exact_match | 精确匹配标准值 |
| `1R-L` | `1R-L` | 1.00 | exact_match | 精确匹配标准值 |
| `1R-R` | `1R-R` | 1.00 | exact_match | 精确匹配标准值 |
| `1U-L` | `1U-L` | 1.00 | exact_match | 精确匹配标准值 |
| `1U-R` | `1U-R` | 1.00 | exact_match | 精确匹配标准值 |
| `1U-R ` | `1U-R` | 1.00 | exact_match | 精确匹配标准值 |
| `1V-L` | `1V-L` | 1.00 | exact_match | 精确匹配标准值 |
| `1V-R` | `1V-R` | 1.00 | exact_match | 精确匹配标准值 |
| `1W-L` | `1W-L` | 1.00 | exact_match | 精确匹配标准值 |
| `1W-R` | `1W-R` | 1.00 | exact_match | 精确匹配标准值 |
| `2 R- L` | `2R-L` | 0.95 | whitespace_normalized | 去除空格后匹配: '2 R- L' → '2R-L' |
| `2 R- R` | `2R-R` | 0.95 | whitespace_normalized | 去除空格后匹配: '2 R- R' → '2R-R' |
| `2 W- L` | `2W-L` | 0.95 | whitespace_normalized | 去除空格后匹配: '2 W- L' → '2W-L' |
| `2I-R` | `2I-R` | 0.95 | valid_format | 符合STROOK格式但非标准枚举值 |
| `2R-L` | `2R-L` | 1.00 | exact_match | 精确匹配标准值 |
| `2R-L ` | `2R-L` | 1.00 | exact_match | 精确匹配标准值 |
| `2R-L  ` | `2R-L` | 1.00 | exact_match | 精确匹配标准值 |
| `2R-R` | `2R-R` | 1.00 | exact_match | 精确匹配标准值 |
| `2R-R ` | `2R-R` | 1.00 | exact_match | 精确匹配标准值 |
| `2U-R` | `2U-R` | 0.95 | valid_format | 符合STROOK格式但非标准枚举值 |
| `3 R- L` | `3R-L` | 0.95 | whitespace_normalized | 去除空格后匹配: '3 R- L' → '3R-L' |
| `3 R- R` | `3R-R` | 0.95 | whitespace_normalized | 去除空格后匹配: '3 R- R' → '3R-R' |
| `3R-L` | `3R-L` | 1.00 | exact_match | 精确匹配标准值 |
| `3R-R` | `3R-R` | 1.00 | exact_match | 精确匹配标准值 |
| `4 R- L` | `4R-L` | 0.95 | whitespace_normalized | 去除空格后匹配: '4 R- L' → '4R-L' |
| `4 R- R` | `4R-R` | 0.95 | whitespace_normalized | 去除空格后匹配: '4 R- R' → '4R-R' |
| `4R-L` | `4R-L` | 1.00 | exact_match | 精确匹配标准值 |
| `ALL` | `ALL` | 1.00 | exact_match | 精确匹配标准值 |
| `R1,2 en 3` | `R1,2 en 3` | 1.00 | multi_lane | 多车道值保持原样（提取时拆分） |
</details>

### 字段 17: DEKLAAGSOORT (面层类型)

**标准值列表：** DZOAB, ZOAB, ZOAB+, ZOABTW TL, ZOABTW DL, ZOABTW OL, ZOABTW, ZOABTW fijn, ZOABDI, ZOEAB, SMA, SMA-NL 11B, SMA-NL 11, SMA 8G+, SMA 8 Geel, AC 16 Surf, AC 11 Surf, DGD, EAB

**原始唯一值数量：** 63

**已映射数量：** 23 (36.5%)


#### ⚠️ 需要审核的映射 (8个)

| 原始值 | 建议标准值 | 置信度 | 推理方法 | 推理说明 | 审核 | Leon备注 |
|--------|-----------|--------|---------|---------|------|----------|
| `2L ZOAB fijn` | `ZOABTW fijn` | 0.80 | fuzzy_match_zoab | ZOAB系列模糊匹配: '2L ZOAB fijn' → 'ZOABTW fijn' | ⏸️ | |
| `2LZOAB` | `ZOAB` | 0.80 | fuzzy_match_zoab | ZOAB系列模糊匹配: '2LZOAB' → 'ZOAB' | ⏸️ | |
| `DI-ZOAB` | `DZOAB` | 0.80 | fuzzy_match_zoab | ZOAB系列模糊匹配: 'DI-ZOAB' → 'DZOAB' | ⏸️ | |
| `DIZOAB` | `DZOAB` | 0.80 | fuzzy_match_zoab | ZOAB系列模糊匹配: 'DIZOAB' → 'DZOAB' | ⏸️ | |
| `SMA-NL` | `SMA-NL 11` | 0.80 | fuzzy_match_sma | SMA系列模糊匹配: 'SMA-NL' → 'SMA-NL 11' | ⏸️ | |
| `SMA-NL 8G+` | `SMA 8G+` | 0.80 | fuzzy_match_sma | SMA系列模糊匹配: 'SMA-NL 8G+' → 'SMA 8G+' | ⏸️ | |
| `ZOAB16` | `ZOAB` | 0.80 | fuzzy_match_zoab | ZOAB系列模糊匹配: 'ZOAB16' → 'ZOAB' | ⏸️ | |
| `ZOABTW-fijn` | `ZOABTW fijn` | 0.80 | fuzzy_match_zoab | ZOAB系列模糊匹配: 'ZOABTW-fijn' → 'ZOABTW fijn' | ⏸️ | |

<details>
<summary>✅ 高置信度映射 (15个) - 点击展开</summary>

| 原始值 | 标准值 | 置信度 | 方法 | 说明 |
|--------|--------|--------|------|------|
| `AC16 Surf` | `AC 16 Surf` | 0.95 | whitespace_normalized | 去除空格后匹配: 'AC16 Surf' → 'AC 16 Surf' |
| `DGD` | `DGD` | 1.00 | exact_match | 精确匹配标准值 |
| `DZOAB` | `DZOAB` | 1.00 | exact_match | 精确匹配标准值 |
| `Duurzaam ZOAB` | `DZOAB` | 0.95 | semantic_equivalence | Duurzaam ZOAB = DZOAB |
| `SMA` | `SMA` | 1.00 | exact_match | 精确匹配标准值 |
| `SMA 8G+` | `SMA 8G+` | 1.00 | exact_match | 精确匹配标准值 |
| `SMA-NL 11` | `SMA-NL 11` | 1.00 | exact_match | 精确匹配标准值 |
| `SMA-NL 11 ` | `SMA-NL 11` | 1.00 | exact_match | 精确匹配标准值 |
| `SMA-NL 11b` | `SMA-NL 11B` | 0.98 | case_insensitive_match | 大小写不同: 'SMA-NL 11b' → 'SMA-NL 11B' |
| `ZOAB` | `ZOAB` | 1.00 | exact_match | 精确匹配标准值 |
| `ZOAB+` | `ZOAB+` | 1.00 | exact_match | 精确匹配标准值 |
| `ZOABDI` | `ZOABDI` | 1.00 | exact_match | 精确匹配标准值 |
| `ZOABTW` | `ZOABTW` | 1.00 | exact_match | 精确匹配标准值 |
| `ZOABTW fijn` | `ZOABTW fijn` | 1.00 | exact_match | 精确匹配标准值 |
| `ZOEAB` | `ZOEAB` | 1.00 | exact_match | 精确匹配标准值 |
</details>

---

## ✅ 审核完成确认

请在完成审核后填写：

- [ ] Part 1 字段名映射审核完成
- [ ] Part 2 字段值映射审核完成
- [ ] 所有问题已标记和说明

**审核完成日期：** ___________

**审核人签名：** ___________
