# DEKLAAGSOORT 四维标准化分类表

## 分类维度定义

| 维度 | 英文 | 含义 | 取值示例 |
|------|------|------|----------|
| 面层家族 | surf_family | 混合料类型家族 | ZOAB, DZOAB, SMA, AC, DGD, EAB |
| 结构层位 | surf_structure | 层位/结构形式 | single, tweelaags_top, tweelaags_bottom, dunne_inlage |
| 粒径细度 | surf_gradation | 最大粒径或细度 | 8, 11, 16, fijn, standard |
| 特性标记 | surf_feature | 耐久/降噪/颜色等 | durable, low_noise, colored_geel, standard |

---

## ZOAB 系列完整映射表

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

---

## SMA 系列完整映射表

| 原始值 | surf_family | surf_structure | surf_gradation | surf_feature | 中文名称 | 待确认 |
|--------|-------------|----------------|----------------|--------------|----------|--------|
| **SMA** | SMA | single | standard | standard | 标准SMA面层 | - |
| **SMA-NL 11B** | SMA-NL | single | 11 | type_B | 荷兰11B型SMA | - |
| **SMA-NL 11** | SMA-NL | single | 11 | standard | 荷兰11型SMA | - |
| **SMA 8G+** | SMA | single | 8 | low_noise_Gplus | 8mm静音型SMA(G+) | - |
| **SMA 8 Geel** | SMA | single | 8 | colored_geel | 黄色8mm SMA | ⚠️ 性能待确认 |
| **SMA-NL 11B PMB SBS Bestone** | SMA-NL | single | 11 | type_B_modified | 荷兰11B型SMA(改性) | 注：PMB/SBS/Bestone应分离 |

---

## AC 系列完整映射表

| 原始值 | surf_family | surf_structure | surf_gradation | surf_feature | 中文名称 | 待确认 |
|--------|-------------|----------------|----------------|--------------|----------|--------|
| **AC 16 Surf** | AC | surface | 16 | standard | 16mm AC面层 | - |
| **AC 11 Surf** | AC | surface | 11 | standard | 11mm AC面层 | - |

---

## 薄层与乳化养护类映射表

| 原始值 | surf_family | surf_structure | surf_gradation | surf_feature | 中文名称 | 待确认 |
|--------|-------------|----------------|----------------|--------------|----------|--------|
| **DGD** | DGD | thin_layer | standard | low_noise | 薄层降噪面层 | - |
| **EAB** | EAB | cold_mix | standard | emulsion | 乳化沥青混凝土（冷拌） | - |

---

## 问题汇总（需与Leon确认）

### 🔴 关键问题

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

### ⚠️ 次要问题

4. **SMA 8 Geel 的性能特性**
   - 当前只知道：8mm粒径 + 黄色
   - **需要确认：是否有特殊声学性能？是否有标准配方？**

5. **材料属性分离**
   - SMA-NL 11B PMB SBS Bestone
   - **建议：PMB/SBS/Bestone 移至材料属性字段（字段15或新字段）**

---

## 标准化后的数据结构示例

### 原始数据行：
```
DEKLAAGSOORT = "ZOABTW DL"
```

### 标准化后（四维）：
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

---

## 实施建议

### 如果四维分类可行：

1. **在 field_mapping_2022.json 添加：**
   - standardization_mapping（完整映射表）
   - verification_required（标记待确认项）

2. **在数据提取阶段：**
   - 保留原始 DEKLAAGSOORT 值
   - 生成四个标准化字段
   - 添加 confidence 和 needs_verification 标记

3. **在数据库设计：**
   ```sql
   CREATE TABLE surface_layers (
     id INT PRIMARY KEY,
     deklaagsoort_original VARCHAR(100),  -- 原始值
     surf_family VARCHAR(50),              -- 标准化家族
     surf_structure VARCHAR(50),           -- 标准化结构
     surf_gradation VARCHAR(20),           -- 标准化粒径
     surf_feature VARCHAR(50),             -- 标准化特性
     needs_verification BOOLEAN,           -- 是否需要确认
     verification_note TEXT                -- 确认说明
   );
   ```

### 如果四维分类不可行：

1. **仅保留原始值 + 简单分组：**
   - ZOAB类
   - SMA类
   - AC类
   - 薄层养护类

2. **待Leon确认后再建立详细分类**

---

## 统计信息（基于1,592行数据）

| 类别 | 数量 | 占比 | 待确认问题数 |
|------|------|------|--------------|
| DZOAB系列 | 691 | 43.4% | 0 |
| ZOAB系列 | 341 | 21.4% | 0 |
| ZOABTW系列 | 278 | 17.5% | 3个 (DL/TL/fijn OL) |
| SMA系列 | 158 | 9.9% | 1个 (Geel) |
| AC系列 | 78 | 4.9% | 0 |
| 其他 | 46 | 2.9% | 0 |
| **总计** | **1,592** | **100%** | **4个关键问题** |

