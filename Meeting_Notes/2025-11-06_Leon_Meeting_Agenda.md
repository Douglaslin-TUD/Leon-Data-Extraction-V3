# Leon会议议程 - 2025年11月6日

**会议目的：** Template 2022数据分析问题讨论
**参会人：** Peng, Leon
**项目：** Leon_Data_Extraction (RWS-Leon-002)

---

## 议题清单

### 1. 字段3：ZAAKNUMMER 数据类型问题 ⚠️

**问题描述：**
ZAAKNUMMER字段在Excel中被读取为`float64`类型，导致所有值都带有小数点（如`311181260135.0`），但实际上这是**项目编号**，不应该是浮点数。

**数据分析结果：**

**基本统计：**
- 总行数: 1,592
- 非空值: 1,050 (66.0%)
- 空值: 542 (34.0%)
- 唯一项目编号: 24个

**数据类型问题：**
- Pandas读取类型: `float64` ❌
- 所有1,050个值都带`.0`后缀
- 期望类型: 字符串（String）或整数（Integer）

**长度分布：**
- 两种格式并存：
  - **8位编号**: 268个值 (25.5%) - 例如：`31142564`
  - **12位编号**: 782个值 (74.5%) - 例如：`311181260135`

**出现频率最高的项目编号（Top 10）：**
| 项目编号 | 出现次数 | 当前格式 | 期望格式 |
|----------|---------|----------|----------|
| 311181260135 | 139 | 311181260135.0 | 311181260135 |
| 311181260147 | 88 | 311181260147.0 | 311181260147 |
| 31142564 | 78 | 31142564.0 | 31142564 |
| 311181260143 | 70 | 311181260143.0 | 311181260143 |
| 311181260139 | 65 | 311181260139.0 | 311181260139 |
| 311181260132 | 64 | 311181260132.0 | 311181260132 |
| 31142566 | 63 | 31142566.0 | 31142566 |
| 311181260148 | 56 | 311181260148.0 | 311181260148 |
| 311181260138 | 56 | 311181260138.0 | 311181260138 |
| 311181260146 | 53 | 311181260146.0 | 311181260146 |

**所有24个唯一项目编号：**
```
8位编号 (4个):
  31118127    (29次)
  31142564    (78次)
  31142566    (63次)
  31143621    (7次)
  31143622    (47次)
  31150507    (6次)
  31153856    (22次)
  31163605    (16次)

12位编号 (16个):
  311181260060  (7次)
  311181260112  (26次)
  311181260121  (4次)
  311181260124  (31次)
  311181260132  (64次)
  311181260133  (23次)
  311181260135  (139次)
  311181260138  (56次)
  311181260139  (65次)
  311181260143  (70次)
  311181260145  (39次)
  311181260146  (53次)
  311181260147  (88次)
  311181260148  (56次)
  311181260150  (29次)
  311181260151  (32次)
```

**需要确认的问题：**

1. **项目编号格式规范**
   - ❓ 为什么存在8位和12位两种格式？
   - ❓ 8位和12位编号是否代表不同类型的项目？
   - ❓ 是否有标准的编号命名规则？

2. **数据类型处理**
   - ❓ 应该按字符串存储还是整数存储？
   - ❓ 是否需要保留前导零（如果有）？
   - ✅ **推荐：VARCHAR(12)**
     - 理由1：这是标识符，不是数量，不需要数学运算
     - 理由2：12位数字`311181260135`接近INT上限，用BIGINT浪费
     - 理由3：如果将来编号格式改变（加字母/符号），不需要改表结构
     - 理由4：与STROOK字段类似（`1R-L`混合格式），保持一致性
   - 备选方案：BIGINT（如果确定永远只有纯数字）

3. **空值处理**
   - ❓ 34%的数据没有ZAAKNUMMER，这是否合理？
   - ❓ 缺失项目编号的数据行如何处理？是否应该标记为错误？

4. **数据验证规则**
   - ❓ ZAAKNUMMER是否应该是必填字段？
   - ❓ 是否需要验证编号格式（8位或12位纯数字）？
   - ❓ 是否需要与RWS项目数据库进行对照验证？

**建议的解决方案：**

```python
# 方案1: 读取时指定为字符串
df = pd.read_excel(file, dtype={'ZAAKNUMMER': str})

# 方案2: 读取后转换（移除.0后缀）
df['ZAAKNUMMER'] = df['ZAAKNUMMER'].apply(
    lambda x: str(int(x)) if pd.notna(x) else None
)
```

**对系统设计的影响：**
- 数据库Schema: 应使用`VARCHAR(12)`而非`FLOAT`或`INTEGER`
- 验证规则: 需要添加格式验证（8或12位纯数字）
- 数据清洗: 移除`.0`后缀，统一为字符串格式

---

### 2. 字段9：STROOK 类型验证问题 ⚠️

**问题描述：**
STROOK字段定义了车道类型和位置，格式为 `[编号][类型]-[方向]`。根据Leon的说明和BPS文档，我们发现了以下待确认问题。

**已确认的STROOK类型（从BPS_boek_concept.pdf）：**

| 代码 | 荷兰语 | 英文 | 中文 | 来源 |
|------|--------|------|------|------|
| **R-** | Rijstrook | Regular lane | 常规车道 | Leon + PDF |
| **I-** | Invoegstrook | Entrance/Acceleration lane | 加速车道 | Leon + PDF |
| **U-** | Uitrijstrook | Exit/Deceleration lane | 减速车道 | Leon + PDF |
| **W-** | Weefstrook | Weaving lane | 交织车道 | Leon + PDF |
| **Q-** | Spitsstrook | Rush hour lane | 高峰车道 | Leon + PDF |
| **B-** | Busstrook | Bus lane | 公交车道 | PDF确认 ✅ |
| **V-** | Vluchtstrook | Emergency lane | 应急车道 | PDF（编号问题⚠️） |

**其他PDF中定义但数据中未见的类型：**
C-(修正车道), F-(自行车道), S-(建议车道), P-(停车车道), L-(爬坡车道), K-(边线), D-(车道分隔线), A-(中心线)

**需要确认的问题：**

#### **问题2.1：V-类型编号应急车道 ⚠️**

**数据中发现：** `1V-L`, `1V-R`, `2V-R`（共3个值）

**BPS文档说明：**
- V- = Vluchtstrook（应急车道）
- 应急车道定义：仅在特殊情况下可使用的车道

**疑问：**
1. ❓ 为什么应急车道有编号（1V, 2V）？
   - 正常应急车道应该只有一条，不需要编号
2. ❓ 为什么应急车道有方向（-L, -R）？
   - 应急车道通常只在一侧，为何有左右之分？
3. ❓ `1V-L/R` 是数据错误还是特殊用途？
   - 是否应该标记为无效值？

**数据示例（需要Leon确认是否正确）：**
```
行123: BAAN=1HRL, STROOK=1V-L  → 是否有效？
行456: BAAN=1HRR, STROOK=2V-R  → 是否有效？
```

#### **问题2.2：Plusstroken的数据标识 ⚠️**

**BPS文档说明（第30页）：**
> "NB Een spitsstrook, gelegen aan de binnenzijde van de doorgaande rijstroken, wordt aangeduid als 1e rijstrook (1 R- R of 1 R- L)."

**翻译：** 内侧高峰车道（Plusstroken）被标记为**第1条常规车道（1R-R 或 1R-L）**

**Leon的说明：**
> "Plusstroken were (and are) situated on the left side of the carriage way. They are usually referred to as lane 1 (1R-L or 1R-R)."

**疑问：**
1. ❓ 如何区分永久性第1车道和临时性Plusstroken？
   - 编码上都是 `1R-L` 或 `1R-R`
2. ❓ 是否有其他字段标识Plusstroken的特殊性？
   - 例如：备注字段、时间限制、特殊标记
3. ❓ 验证规则是否需要特殊处理？
   - 还是将Plusstroken视为普通的第1车道？

**对系统设计的影响：**
- 如果无法区分，可能需要增加额外字段标识临时车道
- 或者在备注/说明字段中查找关键词（"Plusstrook", "Spitsstrook"）

#### **问题2.3：Q-车道（Spitsstroken）位置规则验证**

**Leon的说明：**
> "These lanes are always on the right side of the carriage way."

**BPS文档补充：**
- 外侧高峰车道（Q-）总在右侧
- 内侧高峰车道（Plusstroken）在左侧，但编码为R-

**需要确认：**
1. ❓ 数据中 `1Q-L`, `2Q-L` 是否有效？
   - Leon说Q-车道总在右侧，但数据中可能有-L后缀
2. ❓ 验证规则：Q-R 只能出现在 BAAN=1HRR/0HRM/0VW？
   - 需要强制验证还是仅警告？

**建议的验证规则：**
```json
{
  "rule_id": "CROSS-004",
  "description": "Q-R类型只能出现在右侧或中间车道",
  "validation": {
    "if": {"field": "STROOK", "pattern": "^[12]Q-R$"},
    "then": {"field": "BAAN", "must_be_in": ["1HRR", "0HRM", "0VW"]}
  },
  "severity": "warning"
}
```

---

### 3. 字段5：BAAN 与 0HRM 车道组成规则 ⚠️

**问题描述：**
BAAN=0HRM（中间车道）的具体车道组成规则不明确。

**Leon的说明：**
> "A 0HRM carriage way consists of one 1R-R and one 1R-L lane, while uitvoegstroken (1U-R, 2U-R, 1U-L or 1U-L) and invoegstroken (1I-R, 2I-R, 1I-L or 1I-L) may also occur."

**已知信息：**
- ✅ 0HRM 必须有：`1R-R`（右向第1车道）+ `1R-L`（左向第1车道）
- ✅ 0HRM 可能有：I-车道（加速）、U-车道（减速）
- ❓ 0HRM 是否可以有：2R-R, 3R-R, 2R-L, 3R-L（多条常规车道）？
- ❓ 0HRM 是否可以有：W-车道（交织）、Q-车道（高峰）、B-车道（公交）？

**BPS文档：**
- 定义了0HRM为"中间主车道"
- **未说明**具体车道组成限制

**数据示例（需要Leon确认）：**
```
场景1：0HRM 只有基本车道
  BAAN=0HRM, STROOK=1R-R  → 有效
  BAAN=0HRM, STROOK=1R-L  → 有效

场景2：0HRM 有多条常规车道？
  BAAN=0HRM, STROOK=2R-R  → 是否有效？
  BAAN=0HRM, STROOK=3R-L  → 是否有效？

场景3：0HRM 有其他类型车道？
  BAAN=0HRM, STROOK=1W-R  → 是否有效？
  BAAN=0HRM, STROOK=1Q-L  → 是否有效？
```

**需要确认：**
1. ❓ 0HRM 是否只能有各1条常规车道（1R-R + 1R-L）？
2. ❓ 还是可以有多条常规车道（2R, 3R等）？
3. ❓ W/Q/B车道是否允许出现在0HRM？
4. ❓ 0HRM的I/U车道数量是否有限制？

**对验证规则的影响：**
```json
{
  "rule_id": "CROSS-005",
  "description": "0HRM必须同时有1R-R和1R-L车道",
  "validation": {
    "if": {"field": "BAAN", "value": "0HRM"},
    "then": {
      "field": "STROOK",
      "must_contain_both": ["1R-R", "1R-L"]
    }
  },
  "severity": "error"
}
```

---

### 4. 字段6：WEGLET 编码系统确认 ✅

**问题描述：**
WEGLET字段用于标识连接道（匝道）的类型和方向。

**BPS文档说明（Tabel 3）：**

根据主路hectometer方向和匝道类型，WEGLET使用字母编码：

| WEGLET | 匝道类型 | Hectometer方向 | 中文 |
|--------|---------|----------------|------|
| **a** | afrit（下匝道） | oplopend（↑顺向） | 下匝道-顺向 |
| **b** | toerit（上匝道） | oplopend（↑顺向） | 上匝道-顺向 |
| **c** | afrit（下匝道） | aflopend（↓逆向） | 下匝道-逆向 |
| **d** | toerit（上匝道） | aflopend（↓逆向） | 上匝道-逆向 |

**数据示例（Leon提供）：**
```
Kruising met de 0VWd van de A10  → WEGLET=d（上匝道-逆向）
Kruising met de 0VWa van de A10  → WEGLET=a（下匝道-顺向）
```

**验证规则：**
```json
{
  "rule_id": "ENUM-002",
  "field": "WEGLET",
  "validation": {
    "type": "in_list",
    "allowed_values": ["a", "b", "c", "d"]
  },
  "error_message": "WEGLET必须是a/b/c/d。a=下匝道顺向, b=上匝道顺向, c=下匝道逆向, d=上匝道逆向"
}
```

**条件必填规则：**
```json
{
  "rule_id": "COND-002",
  "validation": {
    "if": {"field": "BAAN", "value": "0VW"},
    "then": {"field": "WEGLET", "required": true}
  }
}
```

**需要确认：**
1. ✅ WEGLET只有a/b/c/d四个值（已确认）
2. ❓ 数据中是否有其他值（数字、字母组合）？
3. ❓ 是否需要与主路方向字段（如果存在）交叉验证？

---

### 5. 字段计算关系确认 ⚠️

**问题描述：**
部分字段之间存在计算关系，需要确认公式是否正确。

#### **问题5.1：KM_Van 和 KM_Tot 计算**

**预期公式：**
```
KM_Van = VAN / 10
KM_Tot = TOT / 10
```

**单位转换：**
- VAN/TOT：百米 (hectometer)
- KM_Van/KM_Tot：公里 (kilometer)

**⚠️ 数据异常发现：**
在实际数据分析中，发现 `KM_Van` 和 `VAN` 的值**完全相同**（不是除以10关系）

**数据示例：**
```
行1: VAN=123.5, KM_Van=123.5  （预期应该是12.35）
行2: TOT=125.0, KM_Tot=125.0  （预期应该是12.50）
```

**需要确认：**
1. ❓ `KM_Van = VAN / 10` 这个公式是否正确？
2. ❓ 还是 `KM_Van` 和 `VAN` 应该是相同值？
3. ❓ 字段命名是否有误导性？

#### **问题5.2：Lengte 计算**

**公式：**
```
Lengte = (TOT - VAN) × 100
```

**单位：**
- Lengte：米 (meter)
- TOT - VAN：百米 (hectometer)

**验证规则：**
```json
{
  "rule_id": "CALC-001",
  "validation": {
    "target_field": "Lengte",
    "formula": "(TOT - VAN) * 100",
    "tolerance": 0.01
  }
}
```

**需要确认：**
1. ✅ 这个公式是否正确？
2. ❓ 容差值0.01米是否合适？
3. ❓ 是否所有行都应该满足此公式？

#### **问题5.3：Breedte 是否为计算字段**

**数据分析发现：**
- 98.4%的Breedte值都是 `4.3` 米
- 只有1个值是其他数值

**疑问：**
1. ❓ Breedte是实测值还是计算值？
2. ❓ 是否应该根据 `STROOK` 类型或 `Aantal rijstroken` 计算？
3. ❓ 4.3米是否是标准车道宽度？
4. ❓ 如果 `STROOK=ALL` 且 `Aantal rijstroken=2`，是否应该 `Breedte = 4.3 × 2 = 8.6`？

**需要确认计算公式（如果是计算字段）：**
```
可能公式1：Breedte = 标准车道宽度 (4.3m)
可能公式2：Breedte = 4.3 × Aantal_rijstroken
可能公式3：Breedte = 实际测量值（非计算）
```

---

### 6. 字段10：Aantal rijstroken 数据逻辑和格式问题 ⚠️

**问题描述：**
Aantal rijstroken（车道数量）字段用于记录维修覆盖的车道数量，但存在多种格式和逻辑疑问。

**字段含义确认：**
- ✅ 表示**维修覆盖的车道数量**（不是路段总车道数）
- ✅ 条件必填：当 STROOK = "ALL" 时必须填写

**数据格式发现：**

| 值类型 | 示例 | 出现次数 | 含义理解 | 状态 |
|--------|------|---------|---------|------|
| 数字 | 1, 2, 3 | 常见 | X条车道 | ✅ 清晰 |
| 文本 | ALL, Alle | 少见 | 所有车道 | ✅ 清晰 |
| 缩写 | n.v.t. | 常见 | 不适用 | ✅ 清晰 |
| 分数 | 1/2 | ? | **不明确** | ⚠️ 待确认 |

---

#### **问题6.1：1/2 格式的含义** ⚠️

**数据中发现：** `Aantal rijstroken = "1/2"`

**可能的解释：**

1. ❓ **0.5条车道宽度**
   - 理解：维修只覆盖半条车道的宽度
   - 场景：路肩维修、部分车道维修

2. ❓ **1或2条车道（不确定）**
   - 理解：车道数量不明确，可能是1条也可能是2条
   - 场景：数据记录时不确定

3. ❓ **第1和第2车道**
   - 理解：同时覆盖第1车道和第2车道（共2条）
   - 场景：多车道同时维修

4. ❓ **数据错误**
   - 应该是 "1" 或 "2"，输入时错误地写成 "1/2"

**需要确认：**
- ❓ "1/2" 的正确含义是什么？
- ❓ 这种格式是否应该接受？
- ❓ 如果是0.5条车道，应该如何标准化存储？

---

#### **问题6.2：Aantal rijstroken 的数据来源** ⚠️

**场景描述：**

当承包商填写 STROOK = "ALL"（全车道宽度养护）时，需要填写 Aantal rijstroken。

**示例数据：**
```
路段：A28, km 100.0-100.5
STROOK = "ALL"
Aantal rijstroken = 3  ← 这个"3"从哪里来？
```

**两种可能的数据来源：**

**方式1：从同一路段的STROOK记录中统计**
```
路段A28, km 100.0-100.5的所有记录：
  记录1: STROOK = "1R-R"  }
  记录2: STROOK = "2R-R"  } → 统计出3条车道
  记录3: STROOK = "3R-R"  }

因此，当STROOK="ALL"时，Aantal rijstroken = 3
```

**方式2：从RWS原有道路数据库中查询**
```
RWS数据库中预先存储了每段路的标准配置：
A28, km 100.0-100.5: 标准配置 = 3条车道

承包商直接填写 Aantal rijstroken = 3
```

**需要确认：**
1. ❓ Aantal rijstroken 的值是**从STROOK记录中统计得出**的？
2. ❓ 还是**从RWS原有道路数据库中查询**的？
3. ❓ 承包商提交数据时，如何知道该填几条车道？
4. ❓ 是否需要与实际STROOK记录进行交叉验证？

**对验证规则的影响：**
```python
# 如果是方式1（从STROOK统计）
验证规则：统计同一路段的STROOK记录数量，与Aantal rijstroken比对

# 如果是方式2（从数据库查询）
验证规则：查询RWS道路数据库，验证Aantal rijstroken是否正确
```

---

#### **问题6.3：STROOK="ALL" 时 Aantal rijstroken 的必填性** ⚠️

**当前规则（COND-001）：**
```json
{
  "rule_id": "COND-001",
  "description": "当STROOK=ALL时，Aantal rijstroken必填"
}
```

**数据中可能的情况：**

| STROOK | Aantal rijstroken | 是否有效？ | 需要确认 |
|--------|------------------|-----------|---------|
| ALL | 3 | ✅ 有效 | - |
| ALL | (空) | ❓ | 是否应该报错？ |
| ALL | n.v.t. | ❓ | 是否有效？ |
| 1R-R | 1 | ❓ | 是否有效？ |
| 1R-R | (空) | ✅ 有效 | - |

**需要确认：**
1. ❓ STROOK="ALL" 时，Aantal rijstroken 必须是**数字**（1/2/3）？
2. ❓ 还是可以是 "n.v.t."（不适用）？
3. ❓ 如果是空值，是否应该报错？
4. ❓ STROOK≠"ALL" 时，Aantal rijstroken 应该是空还是可以有值？

---

#### **问题6.4：数据格式标准化**

**当前数据中的格式变体：**
```
数字格式：1, 2, 3
文本格式：ALL, Alle, n.v.t.
混合格式：1/2
```

**需要确认标准化规则：**

1. **数字类型：**
   - ❓ 存储为整数（INT）还是文本（VARCHAR）？
   - ❓ 范围限制：1-10？1-5？

2. **"ALL" vs "Alle"：**
   - ❓ 是否需要标准化为统一格式？
   - ❓ 推荐：统一为 "ALL"

3. **"n.v.t." 格式：**
   - ❓ 是否接受这个值？
   - ❓ 还是强制要求数字或NULL？

4. **"1/2" 处理：**
   - ❓ 根据问题6.1的答案决定如何处理

---

**建议的验证规则（待Leon确认后实施）：**

```json
{
  "rule_id": "COND-001-ENHANCED",
  "description": "STROOK=ALL时，Aantal rijstroken必须是数字",
  "validation": {
    "if": {"field": "STROOK", "value": "ALL"},
    "then": {
      "field": "Aantal rijstroken",
      "required": true,
      "type": "integer",
      "range": [1, 10]
    }
  }
}
```

```json
{
  "rule_id": "FORMAT-004",
  "description": "Aantal rijstroken格式验证",
  "validation": {
    "field": "Aantal rijstroken",
    "allowed_formats": ["integer", "ALL", "Alle", "n.v.t.", "1/2"],
    "normalize": {
      "Alle": "ALL"
    }
  }
}
```

---

## 待补充议题

### 7. 字段5：BAAN - PWR（右侧平行路）是否存在 ⚠️

**问题背景：**

根据BPS系统的三部分结构：`[baanvolgnummer] + [baansoort] + [baanpositie]`

我们已经确认：
- ✅ **PWL** = (1) + **PW** + **L** = Parallelweg Links（左侧平行路）
- **PW** = Parallelweg（平行路）是一个独立的 baansoort（车道类型）
- **L/R** = Links/Rechts 是 baanpositie（车道位置）

**逻辑推断：**

既然BPS系统中：
- baansoort "PW" 是对称的（可以在左侧或右侧）
- baanpositie "L" 和 "R" 是成对出现的

那么理论上应该同时存在：
- **PWL** = Parallelweg Links（左侧平行路）✅ 已确认
- **PWR** = Parallelweg Rechts（右侧平行路）❓ 待确认

**类比其他BAAN代码：**
```
1HRL（左侧主车道） + 1HRR（右侧主车道）→ 成对存在 ✅
PWL（左侧平行路） + PWR（右侧平行路）→ 应该成对存在？ ❓
```

---

**需要确认的问题：**

#### **问题7.1：PWR 是否是有效的BAAN值？** ⚠️

1. ❓ **PWR** 在RWS道路系统中是否存在？
2. ❓ 为什么2022年模板数据中只出现PWL（4次），没有PWR？
3. ❓ 是否有些道路只有左侧平行路，没有右侧平行路？

**可能的情况：**

**情况A：PWR存在但数据中未见**
- PWR是有效的BPS代码
- 2022年数据恰好没有右侧平行路的维护项目
- 未来数据中可能出现

**情况B：只有PWL，没有PWR**
- Parallelweg通常只建在左侧（特殊设计）
- 右侧通常没有平行路
- PWR理论上无效

**情况C：PWR用不同的命名**
- 右侧平行路可能用其他代码表示
- 例如：其他baansoort组合

---

#### **问题7.2：其他Parallelweg变体** ⚠️

根据BPS系统，理论上还可能存在：

| BAAN代码 | 结构 | 含义 | 是否有效？ |
|---------|------|------|----------|
| **PWL** | (1) + PW + L | 左侧平行路 | ✅ 已确认 |
| **PWR** | (1) + PW + R | 右侧平行路 | ❓ 待确认 |
| **0PWL** | 0 + PW + L | 0号左侧平行路 | ❓ 待确认 |
| **0PWR** | 0 + PW + R | 0号右侧平行路 | ❓ 待确认 |
| **2PWL** | 2 + PW + L | 第2条左侧平行路 | ❓ 待确认 |

**需要确认：**
1. ❓ 哪些组合是有效的？
2. ❓ baanvolgnummer 为0、1、2时分别代表什么？
3. ❓ 是否可能有多条平行路（编号1、2）？

---

#### **问题7.3：对验证规则的影响** ⚠️

**当前ENUM-001规则：**
```json
{
  "rule_id": "ENUM-001",
  "allowed_values": ["1HRR", "1HRL", "0HRM", "0VW", "PWL"]
}
```

**如果PWR也有效，需要更新为：**
```json
{
  "rule_id": "ENUM-001",
  "allowed_values": ["1HRR", "1HRL", "0HRM", "0VW", "PWL", "PWR"]
}
```

**如果有更多PW变体，需要添加：**
```json
{
  "allowed_values": ["1HRR", "1HRL", "0HRM", "0VW", "PWL", "PWR", "0PWL", "0PWR", ...]
}
```

---

#### **问题7.4：STROOK方向匹配规则** ⚠️

**当前CROSS-003规则：**
```json
{
  "rule_id": "CROSS-003",
  "description": "STROOK后缀-L只能出现在1HRL/0HRM/0VW/PWL"
}
```

**如果PWR存在，需要添加对应规则：**
```json
{
  "rule_id": "CROSS-002-UPDATED",
  "description": "STROOK后缀-R只能出现在1HRR/0HRM/0VW/PWR"
}
```

---

**建议：**

1. **查询RWS BPS官方文档或数据库**
   - 确认完整的Parallelweg编码体系
   - 获取所有有效的PW组合

2. **查询历史数据**
   - 检查2021年和其他年份的数据
   - 确认是否出现过PWR或其他PW变体

3. **确认设计逻辑**
   - 了解Parallelweg的道路设计规范
   - 确认左右对称性是否适用

4. **预留扩展性**
   - 即使当前只有PWL，也应考虑PWR的可能性
   - 验证规则应能够灵活扩展

---

**对系统设计的影响：**

- ✅ **短期：** 基于当前数据，只添加PWL
- ⚠️ **长期：** 设计验证框架时考虑PW系列的扩展性
- ⚠️ **文档：** 明确标注PWR的状态（待确认/不存在/保留）

---

### 8. 字段6：WEGLET - 非标准字母编码问题 ⚠️

**问题背景：**

根据BPS_boek_concept.pdf (Tabel 3)，WEGLET字段应该只使用**4个标准字母**：a, b, c, d

**BPS标准编码（已确认）：**

| WEGLET | 匝道类型 | Hectometer方向 | 中文 |
|--------|---------|----------------|------|
| **a** | afrit（下匝道） | oplopend（↑顺向） | 下匝道-顺向 |
| **b** | toerit（上匝道） | oplopend（↑顺向） | 上匝道-顺向 |
| **c** | afrit（下匝道） | aflopend（↓逆向） | 下匝道-逆向 |
| **d** | toerit（上匝道） | aflopend（↓逆向） | 上匝道-逆向 |

**⚠️ 数据质量发现：**

在2022模板的1,592行数据中：
- **WEGLET填写率：** 196行 (12.3%)
- **缺失率：** 1,396行 (87.7%) - 符合预期（仅0VW需要）
- **唯一值数量：** 22个不同的值

**值分布统计：**

| WEGLET | 次数 | 占比（非空） | 符合BPS标准 | 备注 |
|--------|------|--------------|-------------|------|
| `a` | 30 | 15.3% | ✅ 标准 | 下匝道-顺向 |
| `c` | 29 | 14.8% | ✅ 标准 | 下匝道-逆向 |
| `b` | 26 | 13.3% | ✅ 标准 | 上匝道-顺向 |
| `d` | 24 | 12.2% | ✅ 标准 | 上匝道-逆向 |
| **小计：标准值** | **109** | **55.6%** | ✅ | |
| `m` | 13 | 6.6% | ⚠️ 非标准 | 需确认含义 |
| `n` | 12 | 6.1% | ⚠️ 非标准 | 需确认含义 |
| `y` | 9 | 4.6% | ⚠️ 非标准 | 需确认含义 |
| `g` | 8 | 4.1% | ⚠️ 非标准 | 需确认含义 |
| `h` | 8 | 4.1% | ⚠️ 非标准 | 需确认含义 |
| `f` | 7 | 3.6% | ⚠️ 非标准 | 需确认含义 |
| `r` | 6 | 3.1% | ⚠️ 非标准 | 需确认含义 |
| `s` | 4 | 2.0% | ⚠️ 非标准 | 需确认含义 |
| `j` | 3 | 1.5% | ⚠️ 非标准 | 需确认含义 |
| `q` | 2 | 1.0% | ⚠️ 非标准 | 需确认含义 |
| `t` | 2 | 1.0% | ⚠️ 非标准 | 需确认含义 |
| `p` | 2 | 1.0% | ⚠️ 非标准 | 需确认含义 |
| `e` | 2 | 1.0% | ⚠️ 非标准 | 需确认含义 |
| `x` | 1 | 0.5% | ⚠️ 非标准 | 需确认含义 |
| `u` | 1 | 0.5% | ⚠️ 非标准 | 需确认含义 |
| **小计：非标准字母** | **83** | **42.3%** | ⚠️ | **15个不同字母** |
| `[Parallelweg Li]` | 4 | 2.0% | ❌ 异常值 | 格式错误 |
| `a/b` | 2 | 1.0% | ⚠️ 组合值 | 跨越两个weglet? |
| `c/d` | 1 | 0.5% | ⚠️ 组合值 | 跨越两个weglet? |
| **小计：异常格式** | **7** | **3.6%** | ❌ | |

---

#### **问题8.1：非标准字母的含义** ⚠️

**数据中发现15个BPS文档未定义的字母：**
`e, f, g, h, j, m, n, p, q, r, s, t, u, x, y`

这些字母共出现**83次**，占所有非空WEGLET值的**42.3%**。

**需要确认：**

1. ❓ **这些字母是否是有效的WEGLET编码？**
   - 是否存在扩展的BPS编码体系（超出Tabel 3的4个标准值）？
   - 还是这些是承包商的数据录入错误？

2. ❓ **可能的含义推测：**
   - **e-y：** 是否代表同一个交叉口的不同匝道（如e=第5条匝道）？
   - **按字母顺序：** a-d已用（4个方向），e往后是否表示更复杂的交叉口？
   - **特殊类型：** 是否有特殊类型的连接道需要额外编码？

3. ❓ **实际使用场景：**
   - 出现非标准字母的路段特征是什么？
   - 是否集中在特定的道路或承包商？

---

#### **问题8.2：组合值的含义** ⚠️

**数据中发现组合值：**
- `a/b` (2次)
- `c/d` (1次)

**可能的解释：**

1. ❓ **跨越多个匝道**
   - 理解：工程段同时覆盖匝道a和匝道b
   - 场景：大型交叉口维护项目

2. ❓ **不确定类型**
   - 理解：承包商不确定是a还是b，记录为a/b
   - 场景：数据记录时信息不完整

3. ❓ **数据录入错误**
   - 应该是单个字母，错误地写成组合

**需要确认：**
- ❓ 组合值是否是有效格式？
- ❓ 如何解释和验证这种格式？
- ❓ 是否应该拆分为多行记录？

---

#### **问题8.3：异常值 `[Parallelweg Li]`** ❌

**数据中发现：** 4次出现 `[Parallelweg Li]`

**分析：**
- 这明显是格式错误
- 应该是单个字母，不应该是完整单词
- `Parallelweg Li` = Parallelweg Links（左侧平行路）
- 这可能与BAAN=PWL相关

**需要确认：**
1. ❓ 这4行数据的BAAN字段是什么？是否是PWL？
2. ❓ WEGLET字段在PWL情况下是否应该为空？
3. ❓ 还是应该有特定的编码？

**数据清理建议：**
```python
# 检查 [Parallelweg Li] 出现的行
df[df['WEGLET'] == '[Parallelweg Li]'][['BAAN', 'WEGLET', 'Weg']]

# 可能的清理方案：
# 1. 如果BAAN=PWL，则WEGLET应为空
# 2. 如果BAAN=0VW，需要Leon指导如何标准化
```

---

#### **问题8.4：BAAN-WEGLET关联验证** ⚠️

**当前验证规则（COND-002）：**
```json
{
  "rule_id": "COND-002",
  "validation": {
    "if": {"field": "BAAN", "value": "0VW"},
    "then": {"field": "WEGLET", "required": true}
  }
}
```

**需要确认：**

1. ❓ **当BAAN=0VW时，WEGLET的有效值是什么？**
   - 仅限 a/b/c/d？
   - 还是也包括 e-y？

2. ❓ **非标准字母是否只出现在BAAN=0VW的行中？**
   - 需要交叉验证数据

3. ❓ **如果BAAN≠0VW，WEGLET应该为空吗？**
   - 当前规则只规定0VW时必填
   - 未规定其他情况下是否应为空

---

#### **问题8.5：RWS是否有扩展的WEGLET编码系统？** ⚠️

**猜测的可能性：**

**假设A：复杂交叉口的扩展编码**
```
标准交叉口（4个方向）：a, b, c, d
复杂交叉口（多个匝道）：e, f, g, h, ... y
```

**假设B：不同类型连接道的分类**
```
a/b/c/d = 标准匝道
e/f/g/h = 环形匝道
m/n = 临时连接道
...
```

**假设C：按建设顺序或项目阶段编号**
```
a = 第一期建设的匝道
b = 第二期建设的匝道
...
```

**需要确认：**
1. ❓ RWS是否有官方的扩展WEGLET编码文档？
2. ❓ 是否可以查询RWS道路数据库，获取实际使用的WEGLET值？
3. ❓ 其他年份（2021, 2023等）的数据是否也出现这些非标准字母？

---

#### **问题8.6：对数据验证规则的影响** ⚠️

**当前JSON定义：**
```json
{
  "field": "WEGLET",
  "validation_rules": {
    "pattern": "^[a-z]$"
  }
}
```

**当前enum定义（enum_values_2022.json）：**
```json
{
  "WEGLET": {
    "standard_codes": {
      "a": "afrit - oplopend",
      "b": "toerit - oplopend",
      "c": "afrit - aflopend",
      "d": "toerit - aflopend"
    },
    "other_letters_in_data": [
      "e", "f", "g", "h", "j", "m", "n", "p", "q", "r", "s", "t", "u", "x", "y"
    ],
    "notes": [
      "BPS标准只定义了a/b/c/d四个字母",
      "数据中出现的其他字母可能用于特殊情况或非标准匝道",
      "需要与Leon确认e-y字母的含义"
    ]
  }
}
```

**根据Leon的回答，可能需要的更新：**

**情况1：非标准字母有效（有扩展编码体系）**
```json
{
  "rule_id": "ENUM-002-EXTENDED",
  "field": "WEGLET",
  "validation": {
    "type": "in_list",
    "allowed_values": ["a", "b", "c", "d", "e", "f", "g", "h", ...],
    "standard_values": ["a", "b", "c", "d"],
    "extended_values": ["e", "f", "g", "h", ...],
    "warning_for_extended": true
  },
  "error_message": "WEGLET使用了扩展编码（非标准a/b/c/d），请确认是否正确"
}
```

**情况2：非标准字母无效（数据错误）**
```json
{
  "rule_id": "ENUM-002-STRICT",
  "field": "WEGLET",
  "validation": {
    "type": "in_list",
    "allowed_values": ["a", "b", "c", "d"]
  },
  "error_message": "WEGLET必须是a/b/c/d之一",
  "severity": "error"
}
```

**情况3：组合值的验证规则**
```json
{
  "rule_id": "FORMAT-005",
  "field": "WEGLET",
  "validation": {
    "pattern": "^[a-z]$|^[a-z]/[a-z]$",
    "allow_combination": true
  }
}
```

---

#### **问题8.7：数据清理策略** ⚠️

**需要确认清理策略：**

1. **标准值（a/b/c/d）：** ✅ 保留原样

2. **非标准字母（e-y）：**
   - ❓ 如果Leon确认有效 → 保留，添加到有效值列表
   - ❓ 如果Leon确认无效 → 标记为错误，要求承包商修正

3. **组合值（a/b, c/d）：**
   - ❓ 如果Leon确认有效 → 定义验证规则
   - ❓ 如果应拆分 → 拆分为多行记录

4. **异常值（[Parallelweg Li]）：**
   - ❌ 明确为格式错误
   - 需要根据BAAN值决定如何修正

---

**建议行动：**

1. **立即行动：**
   - 查询这83行非标准WEGLET的详细信息（Weg, BAAN, 承包商等）
   - 分析是否有模式（特定道路、特定承包商）

2. **会议确认：**
   - Leon解释非标准字母的实际含义
   - 确认是否存在扩展编码文档
   - 决定验证规则的严格程度

3. **系统设计：**
   - 根据Leon的回答更新enum_values_2022.json
   - 更新validation_rules_2022.json
   - 设计灵活的验证框架（支持标准/扩展/警告三级）

---

**对系统的影响：**

- **数据质量：** 42.3%的WEGLET值需要确认有效性
- **验证规则：** 可能需要从4个标准值扩展到20+个值
- **用户体验：** 如果非标准值无效，承包商需要修正大量数据
- **文档完整性：** 需要建立完整的WEGLET编码参考表

---

### 9. 字段7-8：VAN/TOT与Hectometer方向系统 🆕 CRITICAL

**问题背景：**

在确认VAN/TOT单位为**公里(km)**后，发现数据中44.5%的行出现VAN > TOT（起点大于终点），这不是数据错误，而是与**oriëntatierichting（道路标准方向）**和**BAAN类型**相关的正常现象。

**核心概念确认：**

> **Hectometer的"增/减"本质上只跟"是否顺着道路的标准方向（oriëntatierichting）开"有关，BAAN只是间接影响：不同BAAN上"正常车流"通常跟这个标准方向同向或反向。**

**精确表述：**

1. 对同一条weg，hectometer沿oriëntatierichting总是递增，反向递减；这一点与BAAN无关。
2. 在典型分离主线布局中：
   - 右侧主线（1HRR）与右侧parallelweg（PWR）的正常行车方向与oriëntatierichting一致，因此顺行时hectometer**递增**（TOT > VAN）
   - 左侧主线（1HRL）与左侧parallelweg（PWL）的正常行车方向与oriëntatierichting相反，因此顺行时hectometer**递减**（VAN > TOT）
   - 中间主线（0HRM）与匝道（0VW）则需结合具体交通方向判定

**BAAN与VAN-TOT关系：**

| BAAN | 正常情况 | 说明 |
|------|---------|------|
| **1HRR** | TOT > VAN ✅ | 右侧主线，递增方向 |
| **1HRL** | VAN > TOT ✅ | 左侧主线，递减方向 |
| **PWR** | TOT > VAN ✅ | 右侧平行路，递增方向 |
| **PWL** | VAN > TOT ✅ | 左侧平行路，递减方向 |
| **0HRM** | 由STROOK决定 | 根据-R/-L后缀判断 |
| **0VW** | ❓ 待确认 | 匝道方向复杂 |

---

#### **问题9.1：0VW（匝道）的VAN-TOT方向判断规则** ⚠️ CRITICAL

**背景：**
- 0VW（verbindingsweg）是匝道/连接道
- 几何形状多变，无法从BAAN值直接判断方向
- 数据中0VW共185行(11.6%)，需要明确验证规则

**需要确认：**

1. ❓ **0VW的VAN-TOT大小关系是否有规律？**
   - 是否有统一规律？
   - 还是完全随机，取决于具体节点布局？

2. ❓ **是否与WEGLET字母（a/b/c/d）相关？**
   - 假设A：上匝道（b/d）→ TOT > VAN?
   - 假设B：下匝道（a/c）→ VAN > TOT?
   - 假设C：oplopend（a/b）vs aflopend（c/d）与方向的关系？

3. ❓ **匝道方向是否与主路BAAN相关？**
   - 例如：接入1HRR的匝道 → 与1HRR同向 → TOT > VAN?
   - 例如：接入1HRL的匝道 → 与1HRL同向 → VAN > TOT?

4. ❓ **是否需要额外字段标识匝道方向？**
   - 当前字段是否足够判断？
   - 还是需要新增"匝道方向"字段？

**当前数据分析请求：**

```python
# 请Leon帮助分析0VW的实际数据模式
df_vw = df[df['BAAN'] == '0VW']

# 分析1：WEGLET与VAN-TOT方向的关系
for weglet in ['a', 'b', 'c', 'd']:
    subset = df_vw[df_vw['WEGLET'] == weglet]
    van_gt_tot = (subset['VAN'] > subset['TOT']).sum()
    tot_gt_van = (subset['TOT'] > subset['VAN']).sum()
    print(f"WEGLET={weglet}: VAN>TOT={van_gt_tot}, TOT>VAN={tot_gt_van}")

# 分析2：是否有其他模式
```

**建议的验证策略（待Leon确认后选择）：**

**选项A：不验证0VW方向（最宽松）**
```json
{
  "rule_id": "CROSS-VAN-TOT-004",
  "description": "0VW匝道不检查VAN-TOT方向",
  "if": {"field": "BAAN", "equals": "0VW"},
  "then": "skip_van_tot_direction_check"
}
```

**选项B：基于WEGLET建立规则（中等严格）**
```json
{
  "rule_id": "CROSS-VAN-TOT-005",
  "description": "0VW根据WEGLET判断方向",
  "if": {"field": "BAAN", "equals": "0VW"},
  "then": {
    "if_weglet_in": ["a", "b"],  // oplopend
    "expect": "TOT > VAN",
    "if_weglet_in": ["c", "d"],  // aflopend
    "expect": "VAN > TOT"
  },
  "severity": "warning"
}
```

**选项C：需要额外字段（最严格）**
```json
{
  "新字段建议": "RICHTING_0VW",
  "允许值": ["oplopend", "aflopend"],
  "必填条件": "BAAN = 0VW"
}
```

---

#### **问题9.2：VAN-TOT自动修正策略** ⚠️ CRITICAL

**修正原则确认：**

用户指出：**"BAAN一般不会错，VAN/TOT经常填写错误，所以根据BAAN来对VAN/TOT进行修正"**

**需要确认的修正规则：**

1. ✅ **1HRR/PWR：如果VAN > TOT，自动交换**
   ```python
   if BAAN in ['1HRR', 'PWR'] and VAN > TOT:
       swap(VAN, TOT)
       log("Corrected: VAN-TOT swapped for right-side BAAN")
   ```

2. ✅ **1HRL/PWL：如果TOT > VAN，自动交换**
   ```python
   if BAAN in ['1HRL', 'PWL'] and TOT > VAN:
       swap(VAN, TOT)
       log("Corrected: VAN-TOT swapped for left-side BAAN")
   ```

3. ✅ **0HRM：根据STROOK后缀判断**
   ```python
   if BAAN == '0HRM':
       if '-R' in STROOK and VAN > TOT:
           swap(VAN, TOT)
       elif '-L' in STROOK and TOT > VAN:
           swap(VAN, TOT)
   ```

4. ❓ **0VW：是否自动修正？还是只警告？**
   - 选项A：不修正（太复杂，无规律）
   - 选项B：基于WEGLET修正（如果规律成立）
   - 选项C：只警告，不自动修正，需要人工确认

**需要Leon确认：**
- ❓ 自动修正的严格程度：error（阻止提交）还是warning（允许但标记）？
- ❓ 是否需要生成修正日志，供人工审核？
- ❓ 修正后的数据是否需要承包商重新确认？

---

#### **问题9.3：Lengte字段的计算确认** ✅

**已确认：**
- ✅ Lengte单位是**公里(km)**
- ✅ Lengte **永远是正值（绝对值）**
- ✅ 计算公式：`Lengte = abs(TOT - VAN)`

**验证规则：**
```json
{
  "rule_id": "CALC-LENGTE-001",
  "description": "Lengte必须等于abs(TOT-VAN)",
  "formula": "abs(TOT - VAN)",
  "tolerance": 0.001,
  "severity": "error"
}
```

**无需进一步确认，已明确。**

---

#### **问题9.4：KM_Van和KM_Tot字段的存在意义** ⚠️

**观察：**
- KM_Van与VAN的值相同（38.1%的行完全一致）
- KM_Tot与TOT的值相同
- 似乎是冗余字段

**需要确认：**

1. ❓ **为什么需要KM_Van和KM_Tot这两个字段？**
   - 是历史遗留（旧版模板用百米，新版改为km但保留了字段）？
   - 还是Excel模板中有公式依赖这些字段？
   - 还是数据库系统需要这些字段？

2. ❓ **未来是否可以删除这两个字段？**
   - 如果只是冗余，是否可以简化模板？
   - 删除会影响哪些系统/流程？

3. ❓ **当前如何处理这两个字段？**
   - 选项A：保持同步（KM_Van = VAN, KM_Tot = TOT）
   - 选项B：删除字段
   - 选项C：重新定义字段用途

**建议：**
如果只是冗余字段，建议在下一版模板中删除，简化数据结构。

---

#### **问题9.5：异常大数值的处理** ⚠️

**数据中发现：**
```
VAN = 272,660 km (远超荷兰道路系统范围)
TOT = 272,760 km
VAN = 54,350 km
```

**需要确认：**

1. ❓ **这些异常大数值是什么？**
   - 数据录入错误（多打了几位数字）？
   - 特殊的编码/标记？
   - 其他系统的数据混入？

2. ❓ **正常的VAN/TOT范围是多少？**
   - 建议：0 - 300 km（荷兰最长高速约180km）？
   - 允许负值吗（起点前的路段）？

3. ❓ **如何处理异常值？**
   - 选项A：硬性范围限制（超出范围报错）
   - 选项B：软警告（标记但允许）
   - 选项C：自动修正（除以某个倍数）

**建议验证规则：**
```json
{
  "rule_id": "RANGE-VAN-TOT-001",
  "description": "VAN/TOT正常范围检查",
  "validation": {
    "field": "VAN",
    "min": -10,
    "max": 500,
    "warning_max": 300
  },
  "severity": "warning"
}
```

---

**对系统设计的影响：**

本次更正影响范围极大：
- ✅ 44.5%的"数据错误"判断需要撤销
- ✅ 字段7-8的完整重写
- ✅ 字段11-13的定义修正
- ✅ 所有验证规则的更新
- ✅ 数据清洗/修正策略的制定
- ⚠️ 需要建立BAAN→VAN-TOT方向的自动修正机制

---

## 会议记录区

**日期：** 2025-11-06
**时间：**
**地点：**

### 讨论记录

#### 议题1：ZAAKNUMMER数据类型
- **Leon的回复：**


- **决策：**


- **行动项：**
  - [ ]
  - [ ]

---

## 后续行动

- [ ] 根据会议决策更新字段定义文档
- [ ] 修改数据库Schema设计
- [ ] 更新验证规则配置
- [ ] 更新数据提取脚本的类型处理逻辑

---

**文档创建时间：** 2025-11-05
**最后更新：** 2025-11-05
