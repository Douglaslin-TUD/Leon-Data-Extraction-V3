# 路面层次标准化分类框架
# Pavement Layers Standardization Framework

**版本：** v2.0
**日期：** 2025-11-05
**状态：** 框架文档 - 供Leon确认后集成到配置文件

---

## 文档概述

本文档定义了荷兰道路工程中三个主要路面层次的标准化分类框架：

1. **Deklaag (Surface Layer / 面层)** - 字段17
2. **Tussenlaag (Binder Course / 中间层)** - 字段19
3. **Onderlaag (Base Course / 基层)** - 待分析

**路面典型四层结构（由上至下）：**
```
1. Deklaag (Surface/Wearing Course)   - 面层/磨耗层 [字段17] ✅ 已分类
2. Tussenlaag (Binder/Intermediate)   - 中间层/粘结层 [字段19] ✅ 已分类
3. Onderlaag (Base Course)            - 基层 [待分析]
4. Fundatie (Sub-base/Foundation)      - 垫层/底基层
```

---

## 第一层：DEKLAAGSOORT (面层) 四维标准化分类

### 分类维度定义

| 维度 | 英文 | 含义 | 取值示例 |
|------|------|------|----------|
| 面层家族 | surf_family | 混合料类型家族 | ZOAB, DZOAB, SMA, AC, DGD, EAB |
| 结构层位 | surf_structure | 层位/结构形式 | single, tweelaags_top, tweelaags_bottom, dunne_inlage |
| 粒径细度 | surf_gradation | 最大粒径或细度 | 8, 11, 16, fijn, standard |
| 特性标记 | surf_feature | 耐久/降噪/颜色等 | durable, low_noise, colored_geel, standard |

### ZOAB 系列完整映射表

| 原始值 | surf_family | surf_structure | surf_gradation | surf_feature | 中文名称 | 待确认 |
|--------|-------------|----------------|----------------|--------------|----------|--------|
| **DZOAB** | DZOAB | single | standard | durable | 耐久多孔沥青（单层） | - |
| **ZOAB+** | ZOAB | single | standard | durable | 耐久多孔沥青（单层） | - |
| **ZOAB** | ZOAB | single | standard | standard | 标准多孔沥青（单层） | - |
| **ZOABTW DL** | ZOABTW | tweelaags_top | fijn | standard | 双层ZOAB-上层（细级配） | ⚠️ DL=上层？ |
| **ZOABTW TL** | ZOABTW | tweelaags_top | fijn | standard | 双层ZOAB-上层（细级配） | ⚠️ TL=Toplaag？ |
| **ZOABTW OL** | ZOABTW | tweelaags_bottom | grof | standard | 双层ZOAB-下层（粗级配） | - |
| **ZOABTW fijn** | ZOABTW | tweelaags_top | fijn | standard | 双层ZOAB-上层（fijn冗余） | - |
| **ZOABTW-fijn DL** | ZOABTW | tweelaags_top | fijn | standard | 双层ZOAB-上层（fijn冗余） | - |
| **ZOABTW fijn OL** | ZOABTW | tweelaags_bottom | fijn | standard | 双层ZOAB-下层（fijn异常？） | ⚠️ OL通常粗级配 |
| **ZOABTW** | ZOABTW | tweelaags_unspecified | unknown | standard | 双层ZOAB（未指定层位） | - |
| **ZOABDI** | ZOABDI | dunne_inlage | standard | thin_overlay | ZOAB薄层罩面 | - |
| **ZOEAB** | ZOEAB | emulsie_overlay | standard | life_extension | ZOAB寿命延长层（乳化） | - |

### SMA 系列完整映射表

| 原始值 | surf_family | surf_structure | surf_gradation | surf_feature | 中文名称 | 待确认 |
|--------|-------------|----------------|----------------|--------------|----------|--------|
| **SMA** | SMA | single | standard | standard | 标准SMA面层 | - |
| **SMA-NL 11B** | SMA-NL | single | 11 | type_B | 荷兰11B型SMA | - |
| **SMA-NL 11** | SMA-NL | single | 11 | standard | 荷兰11型SMA | - |
| **SMA 8G+** | SMA | single | 8 | low_noise_Gplus | 8mm静音型SMA(G+) | - |
| **SMA 8 Geel** | SMA | single | 8 | colored_geel | 黄色8mm SMA | ⚠️ 性能待确认 |
| **SMA-NL 11B PMB SBS Bestone** | SMA-NL | single | 11 | type_B_modified | 荷兰11B型SMA(改性) | 注：PMB/SBS/Bestone应分离 |

### AC 系列完整映射表

| 原始值 | surf_family | surf_structure | surf_gradation | surf_feature | 中文名称 | 待确认 |
|--------|-------------|----------------|----------------|--------------|----------|--------|
| **AC 16 Surf** | AC | surface | 16 | standard | 16mm AC面层 | - |
| **AC 11 Surf** | AC | surface | 11 | standard | 11mm AC面层 | - |

### 薄层与乳化养护类映射表

| 原始值 | surf_family | surf_structure | surf_gradation | surf_feature | 中文名称 | 待确认 |
|--------|-------------|----------------|----------------|--------------|----------|--------|
| **DGD** | DGD | thin_layer | standard | low_noise | 薄层降噪面层 | - |
| **EAB** | EAB | cold_mix | standard | emulsion | 乳化沥青混凝土（冷拌） | - |

### DEKLAAGSOORT 统计信息（基于1,592行数据）

| 类别 | 数量 | 占比 | 待确认问题数 |
|------|------|------|--------------|
| DZOAB系列 | 691 | 43.4% | 0 |
| ZOAB系列 | 341 | 21.4% | 0 |
| ZOABTW系列 | 278 | 17.5% | 3个 (DL/TL/fijn OL) |
| SMA系列 | 158 | 9.9% | 1个 (Geel) |
| AC系列 | 78 | 4.9% | 0 |
| 其他 | 46 | 2.9% | 0 |
| **总计** | **1,592** | **100%** | **4个关键问题** |

---

## 第二层：TUSSENLAAG (中间层/粘结层) 三维标准化分类

### 分类维度定义

| 维度 | 英文 | 含义 | 取值示例 |
|------|------|------|----------|
| 家族分类 | tussenlaag_family | 混合料类型家族 | AC, STAB |
| 粒径级配 | tussenlaag_gradation | 最大粒径 | 16, 22, unknown |
| 结构作用 | tussenlaag_role | 在路面结构中的作用 | Bind, Base, Base+Bind |

### TUSSENLAAG 完整映射表

| 原始值 | 标准名称 | family | gradation | role | 中文名称 | 数量 | 占比 |
|--------|----------|--------|-----------|------|----------|------|------|
| **AC 16 Bind** | AC 16 Bind | AC | 16 | Bind | AC 16mm粘结层 | 140 | 63.3% |
| **AC Bind** | AC Bind | AC | **unknown** | Bind | AC粘结层（粒径未知） | 33 | 14.9% |
| **AC Bind 22** | AC 22 Bind | AC | 22 | Bind | AC 22mm粘结层 | 8 | 3.6% |
| **AC Base 22** | AC 22 Base | AC | 22 | Base | AC 22mm基层 | 18 | 8.1% |
| **AC 22 base-bind** | AC 22 Base/Bind | AC | 22 | Base+Bind | AC 22mm混合层 | 4 | 1.8% |
| **AC 16 OL/TL** | AC 16 OL/TL | AC | 16 | Base+Bind | AC 16mm通用层 | 3 | 1.4% |
| **AC 22 TL-C** | AC 22 TL-C | AC | 22 | Bind | AC 22mm粗粒粘结层 | 1 | 0.5% |
| **STAB** | STAB | STAB | - | Base+Bind | 高稳定性沥青混凝土 | 14 | 6.3% |

### 结构作用决策规则

```python
def extract_tussenlaag_role(value):
    """提取结构作用：Bind, Base, 或 Base+Bind"""
    if pd.isna(value):
        return None
    value_str = str(value)

    # STAB 总是 Base+Bind
    if value_str == 'STAB':
        return 'Base+Bind'

    # OL/TL 表示通用层
    if 'OL/TL' in value_str:
        return 'Base+Bind'

    # base-bind 表示混合层
    if 'base-bind' in value_str.lower():
        return 'Base+Bind'

    # 只有 Bind 没有 Base
    if 'Bind' in value_str and 'Base' not in value_str:
        return 'Bind'

    # 只有 Base 没有 Bind
    if 'Base' in value_str and 'Bind' not in value_str:
        return 'Base'

    # TL-C 表示粘结层
    if 'TL-C' in value_str:
        return 'Bind'

    return 'unknown'
```

### TUSSENLAAG 关键点

**✅ 已确认：**
- STAB = Steenslagasfaltbeton (高稳定性沥青混凝土)
- Base vs Bind 区别明确：AC 22 Base (纯基层) vs AC 22 Bind (纯粘结层)
- 标准命名格式：AC [粒径] [层型] (例如：AC 22 Bind)

**⚠️ 待确认：**
- AC Bind (33行) 的粒径：可能是16mm或22mm，当前保持 `unknown`
- AC 22 Base 出现在中间层字段的合理性

### TUSSENLAAG 统计信息（基于221行有中间层的数据）

| 类别 | 数量 | 占比 | 待确认问题数 |
|------|------|------|--------------|
| AC 16 Bind | 140 | 63.3% | 0 |
| AC Bind (unknown粒径) | 33 | 14.9% | 1个 |
| AC 22系列 | 30 | 13.6% | 1个 (Base在中间层) |
| STAB | 14 | 6.3% | 0 |
| 其他 | 4 | 1.8% | 0 |
| **总计** | **221** | **100%** | **2个问题** |

---

## 第三层：ONDERLAAG (基层) - 待分析

**字段信息：** 待确定（可能在字段22之后）

**初步分类维度（待确认）：**
- `onderlaag_family`: AC, STAB, Granular等
- `onderlaag_gradation`: 粒径级配
- `onderlaag_role`: 基层类型

**待分析：**
- 基层类型的完整列表
- 与TUSSENLAAG的区别和关联
- 数据完整度和质量

---

## 待Leon确认的关键问题汇总

### 🔴 DEKLAAGSOORT (面层) - 4个问题

1. **ZOABTW DL 的含义**
   - 当前假设：DL (Deklaag) = 上层面层 = Toplaag
   - 如果正确：ZOABTW DL ≈ ZOABTW TL（都是上层）
   - **需要确认：DL 是否真的等同于 Toplaag？**

2. **ZOABTW TL 的含义**
   - 当前假设：TL = Toplaag（上层）
   - 另一可能：TL = Tussenlaag（中间层/结合层）？
   - **需要确认：TL 的准确含义**

3. **ZOABTW fijn OL 的矛盾**
   - 数据中出现"ZOABTW fijn OL"
   - OL (Onderlaag) 通常是粗级配
   - fijn 表示细级配
   - **需要确认：这是数据错误还是特殊配置？**

4. **SMA 8 Geel 的性能特性**
   - 当前只知道：8mm粒径 + 黄色
   - **需要确认：是否有特殊声学性能？是否有标准配方？**

### ⚠️ TUSSENLAAG (中间层) - 2个问题

5. **AC Bind 粒径补充（33行，14.9%）**
   - 问题："AC Bind" 未指定粒径，可能是16mm或22mm
   - 当前处理：保持 `gradation='unknown'`，不做假设
   - **需要行动：要求承包商补充完整规格**

6. **AC 22 Base 在 TUSSENLAAG 字段的合理性（18行）**
   - 问题：AC 22 Base 是基层材料，为何出现在中间层字段？
   - 可能原因：薄结构路面，中间层直接采用基层混合料
   - **需要确认：这种设计是否符合规范？**

---

## 标准化后的数据结构示例

### 示例1：DEKLAAGSOORT (面层)

**原始数据行：**
```
DEKLAAGSOORT = "ZOABTW DL"
```

**标准化后（四维）：**
```json
{
  "DEKLAAGSOORT_original": "ZOABTW DL",
  "surf_family": "ZOABTW",
  "surf_structure": "tweelaags_top",
  "surf_gradation": "fijn",
  "surf_feature": "standard",
  "standardized_name_cn": "双层ZOAB-上层（细级配）",
  "confidence": "low",
  "needs_verification": true,
  "verification_note": "DL=Toplaag需与Leon确认"
}
```

### 示例2：TUSSENLAAG (中间层)

**原始数据行：**
```
TUSSENLAAG = "AC Bind"
```

**标准化后（三维）：**
```json
{
  "TUSSENLAAG_original": "AC Bind",
  "TUSSENLAAG_standardized": "AC Bind",
  "tussenlaag_family": "AC",
  "tussenlaag_gradation": "unknown",
  "tussenlaag_role": "Bind",
  "standardized_name_cn": "AC粘结层（粒径未知）",
  "needs_verification": true,
  "verification_note": "粒径未知，需要承包商补充规格"
}
```

---

## 实施建议

### 阶段1：在 field_mapping_2022.json 中集成（当前阶段）

✅ **已完成：**
- 字段17 (DEKLAAGSOORT) - 完整四维分类已添加
- 字段19 (TUSSENLAAG) - 完整三维分类已添加
- verification_required 标记已添加

⏸️ **待进行：**
- 字段 Onderlaag - 待分析和分类

### 阶段2：在数据提取阶段实现

**数据处理流程：**
1. 保留原始值（DEKLAAGSOORT_original, TUSSENLAAG_original）
2. 标准化命名格式
3. 生成标准化字段（surf_family, tussenlaag_role等）
4. 添加 confidence 和 needs_verification 标记
5. 生成验证报告

### 阶段3：数据库设计

```sql
-- 面层类型参考表
CREATE TABLE deklaag_types (
    type_code VARCHAR(100) PRIMARY KEY,
    surf_family VARCHAR(50) NOT NULL,
    surf_structure VARCHAR(50),
    surf_gradation VARCHAR(20),
    surf_feature VARCHAR(100),
    description_nl TEXT,
    description_cn TEXT
);

-- 中间层类型参考表
CREATE TABLE tussenlaag_types (
    type_code VARCHAR(100) PRIMARY KEY,
    tussenlaag_family VARCHAR(50) NOT NULL,
    tussenlaag_gradation VARCHAR(20),
    tussenlaag_role VARCHAR(20) NOT NULL,
    description_nl TEXT,
    description_cn TEXT
);

-- 道路段表（外键关联）
CREATE TABLE road_segments (
    segment_id INT PRIMARY KEY,

    -- 面层
    deklaagsoort VARCHAR(100),
    deklaagsoort_original VARCHAR(100),
    surf_family VARCHAR(50),
    surf_structure VARCHAR(50),
    surf_gradation VARCHAR(20),
    surf_feature VARCHAR(100),

    -- 中间层（可选）
    tussenlaag VARCHAR(100),
    tussenlaag_original VARCHAR(100),
    tussenlaag_family VARCHAR(50),
    tussenlaag_gradation VARCHAR(20),
    tussenlaag_role VARCHAR(20),

    -- 验证标记
    deklaag_needs_verification BOOLEAN DEFAULT FALSE,
    tussenlaag_needs_verification BOOLEAN DEFAULT FALSE,

    -- 外键约束
    FOREIGN KEY (deklaagsoort) REFERENCES deklaag_types(type_code),
    FOREIGN KEY (tussenlaag) REFERENCES tussenlaag_types(type_code)
);
```

---

## 版本历史

**v2.0 (2025-11-05)** - 扩展为三层框架
- ✅ 添加TUSSENLAAG (中间层) 三维分类
- ✅ 重命名文档：DEKLAAGSOORT → Pavement_Layers_Standardization
- ✅ 统一DEKLAAGSOORT和TUSSENLAAG的分类方法
- ⏸️ ONDERLAAG (基层) 待分析

**v1.0 (2025-11-05)** - 初始版本
- ✅ DEKLAAGSOORT (面层) 四维分类框架
- ✅ 24个面层类型完整映射
- ✅ 4个关键问题标识

---

## 参考来源

- 📄 config/field_mapping_2022.json - 字段17、19完整定义
- 📄 Analysis/Template_2022_Complete_Field_Reference.md - 完整字段参考文档
- 📊 真实数据统计 - 1,592行Template 2022数据
- 📖 RAW Bepalingen - 荷兰道路技术规范
- 📖 CROW Publicatie 147 - ZOAB设计和施工指南
- 💬 用户提供的详细分类规则 (2025-11-05)

---

**文档结束**
