# 2022 Template Column Definitions
## Verzamelstaat_2022c.xlsx - Blad1 字段定义

**文档版本：** 1.1
**创建日期：** 2025-11-05
**更新日期：** 2025-11-05 (添加字段分类)
**数据源：** Data/FW_ /Template/Verzamelstaat_2022c.xlsx
**参考文档：**
- Documents/Hallo Peng Luuk.txt (Leon的车道类型说明)
- Documents/Validator - rijstroken.xlsx (车道验证数据)
- Documents/Vertaallijst_EN-Nl_def2 (1).xlsx (荷兰语-英语翻译表)

---

## 总览

2022标准模板包含 **26个字段**，用于记录RWS道路养护项目的详细信息。

---

## 字段分类

根据数据重要性和系统架构需求，26个字段分为两类：

### 关键字段 (Critical Fields) - 16个

这些字段是数据库核心字段，必须严格验证和映射：

| 序号 | 字段名 | 用途分类 |
|------|--------|----------|
| 2 | DISTRICT | 组织信息 |
| 3 | ZAAKNUMMER | 项目标识 |
| 4 | Weg | 位置标识 |
| 5 | BAAN | 位置标识 |
| 6 | WEGLET | 位置标识 |
| 7 | VAN | 位置标识 |
| 8 | TOT | 位置标识 |
| 9 | STROOK | 车道标识 |
| 10 | Aantal rijstroken | 车道信息 |
| 11 | KM_Van | 位置标识 |
| 12 | KM_Tot | 位置标识 |
| 13 | Lengte | 工程量 |
| 15 | MENGSELCODE | 材料规格 |
| 16 | GRANULAIR MENGSEL | 材料规格 |
| 17 | DEKLAAGSOORT | 材料规格 |
| 22 | AANLEGDATUM | 施工记录 |

**特点：**
- 用于唯一标识工程段
- 核心业务逻辑依赖
- 必须进行严格验证
- 数据库主表字段

### 非关键字段 (Non-Critical Fields) - 10个

这些字段为补充信息，可选或作为扩展属性存储：

| 序号 | 字段名 | 用途分类 |
|------|--------|----------|
| 1 | NAAM OPDRACHTNEMER | 组织信息 |
| 14 | Breedte | 工程量 |
| 18 | DIKTE VERHARDING | 材料规格 |
| 19 | TUSSENLAAG | 材料规格 |
| 20 | Mengselcode TUSSENLAAG | 材料规格 |
| 21 | DIKTE TUSSENLAAG | 材料规格 |
| 23 | ASFALTCENTRALE | 施工记录 |
| 24 | TONNEN | 工程量 |
| 25 | temperatuur (Productie) | 质量参数 |
| 26 | OPMERKINGENVELD | 备注 |

**特点：**
- 补充性质量和施工信息
- 可能缺失或不完整
- 验证规则相对宽松
- 可存储在扩展表或JSON字段

---

## 字段详细定义

### 1. NAAM OPDRACHTNEMER
**字段分类：** 🔵 非关键字段 (Non-Critical)
**中文名称：** 承包商名称
**英文名称：** Contractor Name
**数据类型：** 文本
**必填：** 是

**含义：**
执行道路养护工程的承包商/公司名称。

**示例值：**
- NN-Oost
- Zee en Delta

---

### 2. DISTRICT
**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 区域
**英文名称：** District
**数据类型：** 文本
**必填：** 是

**含义：**
RWS管理区域划分。荷兰全国划分为7个大区（Regio），每个大区再细分为2-3个地区（District），共计15个地区。

**大区命名体系：**
- **NN** = Noord-Nederland (北荷兰) → 2个地区
- **MN** = Midden-Nederland (中荷兰) → 2个地区
- **ON** = Oost-Nederland (东荷兰) → 3个地区
- **WNN** = West-Nederland Noord (西荷兰北) → 2个地区
- **WNZ** = West-Nederland Zuid (西荷兰南) → 1个地区
- **ZD** = Zuidwest-Nederland (西南荷兰) → 2个地区
- **ZN** = Zuid-Nederland (南荷兰) → 3个地区

**方位代码说明：**
- **N** = Noord (北)
- **Z** = Zuid (南)
- **O** = Oost (东)
- **W** = West (西)
- **M** = Midden (中)
- **ZO** = Zuidoost (东南)

**完整区域列表（标准格式-连字符）：**
```
NN: NN-Oost, NN-West
MN: MN-Noord, MN-Zuid
ON: ON-Noord, ON-Zuid, ON-Oost
WNN: WNN-Noord, WNN-Zuid
WNZ: WNZ-Noord
ZD: ZD-Noord, ZD-Zuid
ZN: ZN-West, ZN-Midden, ZN-Zuidoost
```

**数据格式说明：**
- **标准格式：** 使用连字符 `-`（如 `ON-Zuid`）
- **别名格式：** 部分数据使用下划线 `_`（如 `ON_Zuid`）
- **数据统计：** 连字符格式占92.5% (1472条)，下划线格式占7.5% (119条)
- **验证规则：** 接受两种格式作为输入，输出统一为连字符标准格式

**别名示例：**
- `ON_Zuid` → 标准化为 `ON-Zuid`
- `MN_Zuid` → 标准化为 `MN-Zuid`

---

### 3. ZAAKNUMMER
**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 案件编号/项目编号
**英文名称：** Case Number / Project Number
**数据类型：** 文本/数字
**必填：** 是

**含义：**
RWS内部项目追踪编号，用于识别特定的养护项目。

**格式：**
通常为RWS标准编号格式，可能包含字母和数字组合。

---

### 4. Weg
**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 道路编号
**英文名称：** Road Number / Highway Number
**数据类型：** 文本（VARCHAR(6)）
**必填：** 是

**含义：**
国家公路编号（Rijksweg），RWS管理的主干高速公路标识。每个编号代表一条特定的高速公路。

**当前数据格式：**
- 现有1,592条数据全部为**纯数字格式**（如 `1`, `28`, `50`）
- 共34条不同公路，编号范围：1-835
- 数据完整度：100%（无缺失）

**未来可能的格式变体：**

同一条**国家高速公路**可能出现多种等价表示方式，需要标准化处理：

| 公路类型 | 等价格式 | 说明 |
|---------|---------|------|
| A1（国家高速） | `1`, `A1`, `RW1`, `RW001` | 1号国家高速公路 |
| A28（国家高速） | `28`, `A28`, `RW28`, `RW028` | 28号国家高速公路 |
| N200（省道） | `N200` | 200号省道（**不等价于A200**） |

**格式前缀说明：**
- **A** = Autosnelweg（高速公路，常用表示法）
- **RW** = Rijksweg（国家公路，官方编号，与A等价）
- **N** = Nationale weg（省道，**不是国家高速公路，数据中不应出现**）

**⚠️ 重要说明：**
- **A** 和 **RW** 是同一条路的不同表示：`A1` = `RW1`
- **N** 道路是省道，**不属于RWS管辖的国家高速公路网**
- 当前数据中只有国家高速公路（A/RW系列），没有N道路

**数据统计（基于现有数据）：**

出现频率最高的公路：
- **A28**: 422次 (26.5%) - 数据集中的主要公路
- **A1**: 369次 (23.2%)
- **A50**: 133次 (8.4%)
- **A2**: 120次 (7.5%)
- **A6**: 69次 (4.3%)
- 其他29条公路: 共479次 (30.1%)

## 📋 **数据处理流程：输入 → 存储 → 输出**

### **1️⃣ 输入阶段：多格式接受**

承包商/用户提交数据时，可能出现多种格式变体：

| 输入格式 | 说明 | 标准化后 |
|---------|------|---------|
| `1` | 纯数字（当前数据格式） | `A1` |
| `21` | 纯数字 | `A21` |
| `A1` | 带A前缀 | `A1` |
| `A21` | 带A前缀 | `A21` |
| `RW1` | 带RW前缀（无前导零） | `A1` |
| `RW001` | 带RW前缀（有前导零） | `A1` |
| `RW21` | 带RW前缀（无前导零） | `A21` |
| `RW021` | 带RW前缀（有前导零） | `A21` |

**标准化规则：**
1. 提取数字部分（去掉A/RW前缀）
2. 转换为整数（自动去掉前导零）
3. 添加统一前缀 "A"
4. 结果：`A{数字}`（如 A1, A21, A200）

---

### **2️⃣ 存储阶段：统一格式**

**数据库存储格式：**
```
A1, A2, A4, A6, A7, A9, A10, A12, A15, A16, A17, A18, A21, A22, A27, A28, A200, ...
```

**数据库设计：**
- **字段类型：** `VARCHAR(6)`
  - 可容纳 A1 到 A999
  - 为未来扩展留有空间（如 A1234 最多4位数字）
- **存储值：** 统一为 `A{数字}` 格式，**不含前导零**
- **索引：** 建立索引以加快查询
- **约束：** NOT NULL（必填字段）

**⚠️ 为什么不用INT类型：**
- 需要保留前缀 "A"
- 未来可能出现其他格式（如省道N200）
- 保持与BAAN、STROOK等字段的一致性（都是VARCHAR）

---

### **3️⃣ 输出阶段：Excel导出格式**

**生成标准Excel模板时：**

**输出格式：** 纯数字（去掉 "A" 前缀）

| 数据库存储 | Excel输出 | Excel单元格类型 |
|-----------|----------|----------------|
| `A1` | `1` | 数字 (Number) |
| `A21` | `21` | 数字 (Number) |
| `A28` | `28` | 数字 (Number) |
| `A200` | `200` | 数字 (Number) |

**代码实现示例：**
```python
# 数据库读取
df['Weg'] = "A21"  # 存储格式

# Excel输出转换
df['Weg_Excel'] = df['Weg'].str.replace('A', '', regex=False).astype(int)
# 结果: 21 (整数类型)

# 写入Excel
df[['Weg_Excel']].to_excel('output.xlsx', index=False)
# Excel中显示: 21（不是 "21" 也不是 021）
```

**Excel输出特点：**
- ✅ 去掉前缀 "A"
- ✅ 转换为数字类型（Excel Number格式）
- ✅ 自动去掉前导零（21 不是 021）
- ✅ 与当前模板格式保持一致

---

### **4️⃣ 特殊情况：省道N路**

**如果未来遇到省道数据：**

| 输入 | 存储 | Excel输出 | 处理方式 |
|------|------|----------|---------|
| `N200` | `N200` | `N200` (文本) | ⚠️ 标记警告，保持原样 |
| `N35` | `N35` | `N35` (文本) | ⚠️ 标记警告，保持原样 |

**验证规则：**
- 检测到 `N{数字}` 格式 → 触发警告
- 警告信息："省道(N路)不属于RWS国家高速公路管辖范围，请确认数据正确性"
- 仍然接受数据，但标记为需要人工审核

---

## 📊 **完整示例：数据流**

```
输入阶段（承包商提交）:
  RW021, 28, A1, RW001, A200

↓ 标准化处理

存储阶段（数据库）:
  A21, A28, A1, A1, A200

↓ Excel生成

输出阶段（标准模板）:
  21, 28, 1, 1, 200
  (Excel数字类型)
```

---

## ⚙️ **验证规则**

1. **输入验证：**
   - 接受格式：`^\d{1,3}$` 或 `^A\d{1,3}$` 或 `^RW\d{1,4}$`
   - 拒绝格式：`^N\d{1,3}$`（省道，触发警告）

2. **标准化流程：**
   ```python
   def normalize_weg(input_value):
       # 去掉前缀
       number = re.sub(r'^(A|RW)', '', input_value)
       # 转换为整数（去前导零）
       number = int(number)
       # 添加A前缀
       return f"A{number}"
   ```

3. **范围验证：**
   - 国家高速公路编号：1-999
   - 超出范围应标记为警告

---

## 📝 **注意事项**

- ✅ 当前数据全部为纯数字格式（1, 28, 50等）
- ✅ 系统设计支持未来多格式输入（A, RW前缀及前导零）
- ⚠️ Excel输出时必须转换为纯数字（去掉A前缀）
- ⚠️ 省道N路应标记警告但不阻止导入
- ⚠️ 前导零在标准化时自动去除（RW021 → A21 → 输出21）

---

### 5. BAAN
**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 车道类型/行车道
**英文名称：** Carriageway
**数据类型：** 文本（固定枚举值）
**必填：** 是

**含义：**
车道的基本分类代码，定义道路的方向性和位置。**与STROOK字段有严格的逻辑依赖关系。**

## ✅ **标准值（Leon确认 + BPS文档）**

**BAAN只能是以下5个值之一：**

| BAAN | 荷兰语全称 | 英文 | 中文 | 结构 | 方向性 | 特点 |
|------|-----------|------|------|------|--------|------|
| **1HRR** | Hoofdrijbaan Rechts | Right main carriageway | 右侧主车道 | 1+HR+R | 单向右行 | 只能有-R后缀的STROOK |
| **1HRL** | Hoofdrijbaan Links | Left main carriageway | 左侧主车道 | 1+HR+L | 单向左行 | 只能有-L后缀的STROOK |
| **0HRM** | Hoofdrijbaan Midden | Middle main carriageway | 中间主车道 | 0+HR+M | **双向** | 必须同时有-R和-L的STROOK |
| **0VW** | Verbindingsweg | Connecting road/Ramp | 连接道/匝道 | 0+VW | 双向可能 | 需要WEGLET字段 |
| **PWL** | Parallelweg Links | Left parallel road | 左侧平行路 | (1)+PW+L | 单向左行 | 与主路平行的辅道 |

**PWL 说明：**
- **Parallelweg** = 与主路（Hoofdrijbaan）平行的辅道/平行车道
- 通常用于服务性道路或地方交通
- **结构组成：** (1默认)(baanvolgnummer) + PW(baansoort) + L(baanpositie)
- **数据统计：** 数据中出现4次（0.25%）
- **权威来源：**
  - RWS Geo Services: https://geo.rijkswaterstaat.nl/arcgis/rest/services/GDR/bps_kaart/MapServer/9
  - RWS Productspecificatie Ultimo (2014)
  - NDW NWB基础结构文档

---

## 🔗 **BAAN ↔ STROOK 依赖关系（核心验证逻辑）**

### **规则1：方向匹配规则** ⚠️ **非常关键**

**STROOK后缀与BAAN的匹配关系：**

```
STROOK 后缀 -R（Right右向）只能出现在：
   ✅ BAAN = 1HRR（右侧主车道）
   ✅ BAAN = 0HRM（中间车道）
   ✅ BAAN = 0VW（连接道）

STROOK 后缀 -L（Left左向）只能出现在：
   ✅ BAAN = 1HRL（左侧主车道）
   ✅ BAAN = 0HRM（中间车道）
   ✅ BAAN = 0VW（连接道）
```

**示例：**

| BAAN | STROOK | 是否有效 | 说明 |
|------|--------|---------|------|
| 1HRR | 1R-R | ✅ 有效 | 右侧车道，右向车道 |
| 1HRR | 2R-R | ✅ 有效 | 右侧车道，第2条右向车道 |
| 1HRR | 1R-L | ❌ **错误** | 右侧车道不能有左向车道 |
| 1HRL | 1R-L | ✅ 有效 | 左侧车道，左向车道 |
| 1HRL | 1R-R | ❌ **错误** | 左侧车道不能有右向车道 |
| 0HRM | 1R-R | ✅ 有效 | 中间车道，右向车道 |
| 0HRM | 1R-L | ✅ 有效 | 中间车道，左向车道 |
| 0VW | 1I-R | ✅ 有效 | 连接道，右向加速车道 |

---

### **规则2：0HRM特殊要求** ⚠️ **必须验证**

**0HRM（中间车道）的组成规则：**

**Leon原文：**
> "A 0HRM carriage way consists of one 1R-R and one 1R-L lane, while uitvoegstroken (1U-R, 2U-R, 1U-L or 1U-L) and invoegstroken (1I-R, 2I-R, 1I-L or 1I-L) may also occur."

**翻译和解释：**

1. **必须同时包含：**
   - ✅ `1R-R`（右向第1车道）
   - ✅ `1R-L`（左向第1车道）

2. **可选车道：**
   - ✅ **Uitvoegstroken（减速车道）：** 1U-R, 2U-R, 1U-L, 2U-L
   - ✅ **Invoegstroken（加速车道）：** 1I-R, 2I-R, 1I-L, 2I-L

3. **典型应用场景：**
   - 交叉路口（Kruising）
   - 铁路道口（Spoorwegkruising）
   - 路段通常很短（0.1-0.2 km）

**验证方式：**
```
同一路段（Weg + VAN + TOT相同）内：
IF BAAN = "0HRM"
THEN 必须至少有以下两条记录：
  - 一条记录 STROOK = "1R-R"
  - 一条记录 STROOK = "1R-L"
```

**示例数据：**
```
路段1（0HRM正确示例）：
Weg  BAAN  VAN    TOT    STROOK
A28  0HRM  47.3   47.5   1R-R    ✅
A28  0HRM  47.3   47.5   1R-L    ✅（同时有1R-R和1R-L，有效）
A28  0HRM  47.3   47.5   1I-R    ✅（可选加速车道）

路段2（0HRM错误示例）：
Weg  BAAN  VAN    TOT    STROOK
A28  0HRM  50.0   50.2   1R-R    ✅
A28  0HRM  50.0   50.2   1I-R    ❌（缺少1R-L，错误！）
```

---

### **规则3：0VW连接道规则**

```
IF BAAN = "0VW"
THEN WEGLET 必填（必须是 a/b/c/d 之一）
```

详见字段6：WEGLET的说明。

---

## 📊 **代码结构解析 - BPS系统**

根据RWS的BPS（Beschrijvende Plaatsaanduiding Systematiek）系统，BAAN代码遵循标准化的三部分结构：

### **完整结构：[baanvolgnummer] + [baansoort] + [baanpositie]**

---

#### **1. Baanvolgnummer（车道顺序号）**

表示车道的编号或等级：

| 编号 | 含义 | 应用场景 |
|------|------|---------|
| **0** | 连接道/特殊道 | 用于VW（连接道）、HRM（中间车道） |
| **1** | 第一主车道 | 用于HRL/HRR（左右主车道）、PW（平行路） |
| **2** | 第二主车道 | 理论存在，数据中未见 |

**示例：**
- 0VW → 0（连接道编号）
- 1HRR → 1（第一主车道）
- 0HRM → 0（特殊：中间车道）

---

#### **2. Baansoort（车道类型）**

车道的功能分类：

| 代码 | 荷兰语全称 | 英文 | 中文 | 说明 |
|------|-----------|------|------|------|
| **HR** | Hoofdrijbaan | Main carriageway | 主车道 | 主要通行道路 |
| **VW** | Verbindingsweg | Connecting road | 连接道 | 匝道/进出口 |
| **PW** | Parallelweg | Parallel road | 平行路 | 辅道/服务性道路 |

**示例：**
- 1**HR**R → Hoofdrijbaan（主车道）
- 0**VW** → Verbindingsweg（连接道）
- P**W**L → Parallelweg（平行路）

---

#### **3. Baanpositie（车道位置）**

车道的方向或空间位置：

| 代码 | 荷兰语 | 英文 | 中文 | 说明 |
|------|--------|------|------|------|
| **L** | Links | Left | 左侧 | 左向行驶车道 |
| **R** | Rechts | Right | 右侧 | 右向行驶车道 |
| **M** | Midden | Middle | 中间 | 中间车道（双向） |

**示例：**
- 1HR**R** → Rechts（右侧）
- 1HR**L** → Links（左侧）
- 0HR**M** → Midden（中间）
- PW**L** → Links（左侧平行路）

---

### **完整示例拆解：**

| BAAN代码 | baanvolgnummer | baansoort | baanpositie | 完整含义 |
|---------|---------------|-----------|-------------|---------|
| **1HRR** | 1（第一） | HR（主车道） | R（右侧） | 第一条右侧主车道 |
| **1HRL** | 1（第一） | HR（主车道） | L（左侧） | 第一条左侧主车道 |
| **0HRM** | 0（特殊） | HR（主车道） | M（中间） | 中间主车道（双向） |
| **0VW** | 0（连接道） | VW（连接道） | -（无方向） | 连接道/匝道 |
| **PWL** | (1默认) | PW（平行路） | L（左侧） | 左侧平行路 |

---

### **特殊说明：**

1. **0VW无方向后缀：** 连接道通常不带L/R后缀，因为方向由WEGLET字段（a/b/c/d）决定
2. **PWL的volgnummer：** Parallelweg默认编号为1，通常省略不写
3. **0HRM的特殊性：** 唯一的双向主车道类型，必须同时包含-R和-L方向的STROOK

---

### **BPS结构的优势：**

✅ **系统化命名** - 每个代码遵循统一规则
✅ **可扩展性** - 可以定义新的baansoort类型
✅ **语义清晰** - 从代码即可理解车道功能和位置
✅ **国家标准** - 全荷兰RWS系统统一使用

---

## ⚙️ **验证规则总结**

**关键验证点：**

1. ✅ **ENUM-001**: BAAN必须是5个标准值之一（1HRR, 1HRL, 0HRM, 0VW, PWL）
2. ✅ **CROSS-002**: STROOK后缀-R只能出现在1HRR/0HRM/0VW
3. ✅ **CROSS-003**: STROOK后缀-L只能出现在1HRL/0HRM/0VW/PWL
4. ✅ **CROSS-005**: 0HRM必须同时有1R-R和1R-L车道
5. ✅ **COND-002**: 0VW必须填写WEGLET字段

**参考来源：**
- Leon邮件确认（2025-11）
- Documents/Validator - rijstroken.xlsx
- Documents/BPS_boek_concept.pdf
- RWS Geo Services (PWL确认)
- RWS Productspecificatie Ultimo (2014)

---

### 6. WEGLET (zie toelichting blad 2)
**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 连接道字母编码
**英文名称：** Connecting Road Letter / Ramp Code
**数据类型：** 字母 (单个字符)
**必填：** 条件必填（当BAAN=0VW时）

**含义：**
连接道（匝道）的类型和方向标识字母，与BAAN结合使用精确定位匝道。

**✅ 标准编码系统（BPS_boek_concept.pdf Tabel 3）：**

根据**主路hectometer方向**和**匝道类型**，WEGLET使用以下字母编码：

| WEGLET | 匝道类型（荷兰语） | 匝道类型（英文） | Hectometer方向 | 中文解释 |
|--------|------------------|-----------------|---------------|---------|
| **a** | afrit | Exit ramp | oplopend (↑) | 下匝道-顺向 |
| **b** | toerit | Entrance ramp | oplopend (↑) | 上匝道-顺向 |
| **c** | afrit | Exit ramp | aflopend (↓) | 下匝道-逆向 |
| **d** | toerit | Entrance ramp | aflopend (↓) | 上匝道-逆向 |

**编码逻辑：**
1. **匝道类型：**
   - **afrit（下匝道/出口）：** 从主路离开的匝道 → a 或 c
   - **toerit（上匝道/入口）：** 汇入主路的匝道 → b 或 d

2. **Hectometer方向：**
   - **oplopend（上升/顺向）：** 沿hectometer增长方向 → a 或 b
   - **aflopend（下降/逆向）：** 沿hectometer减少方向 → c 或 d

**实际数据示例（Leon提供）：**
```
Kruising met de 0VWd van de A10  →  WEGLET = d（上匝道-逆向）
Kruising met de 0VWa van de A10  →  WEGLET = a（下匝道-顺向）
```

**示例组合：**
- **0VWa** - 顺向下匝道（离开主路，hectometer增长方向）
- **0VWb** - 顺向上匝道（汇入主路，hectometer增长方向）
- **0VWc** - 逆向下匝道（离开主路，hectometer减少方向）
- **0VWd** - 逆向上匝道（汇入主路，hectometer减少方向）

**条件必填规则：**
```
IF BAAN = "0VW" THEN WEGLET IS REQUIRED
ELSE WEGLET SHOULD BE EMPTY
```

**验证规则：**
- WEGLET必须是：a, b, c, d（仅这4个字母有效）
- 当BAAN不是0VW时，WEGLET应为空

**数据库设计：**
- 类型：CHAR(1)
- 约束：CHECK (WEGLET IN ('a', 'b', 'c', 'd'))
- 外键关联：需要与BAAN字段配合验证

**特别说明：**
模板Blad 2（第二个工作表）应包含更详细的说明和示例。

**参考来源：**
- Documents/BPS_boek_concept.pdf (Tabel 3: Hectometerletters voor verbindingswegen)
- Documents/Hallo Peng Luuk.txt (Leon提供的实际数据示例)

---

### 7. VAN (graag tot min. 10 meter nauwkeurig)
**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 起始位置
**英文名称：** From (Hectometer Position)
**数据类型：** 数值 (精度至10米)
**必填：** 是
**单位：** 百米 (Hectometer, hm)

**含义：**
工程段起始位置的百米桩号。荷兰公路采用百米桩(hectometer)定位系统。

**格式：**
- 整数或小数
- 精度要求：最少到10米（即0.1 hm）
- **可以是负值**（起点前的路段）

**示例值：**
- 23,456 hm (即23.456百米 = 2345.6米)
- -0,3 hm (起点前30米)
- 199,875 hm

**注意：**
- 使用**欧洲数字格式**：逗号作小数点，点作千位分隔符
- 1 hectometer (hm) = 100 米

---

### 8. TOT (graag tot min. 10 meter nauwkeurig)
**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 结束位置
**英文名称：** To (Hectometer Position)
**数据类型：** 数值 (精度至10米)
**必填：** 是
**单位：** 百米 (Hectometer, hm)

**含义：**
工程段结束位置的百米桩号。

**格式规则：** 与VAN相同

**逻辑关系：**
- TOT ≥ VAN (终点大于等于起点)
- 长度 = (TOT - VAN) × 100 米

---

### 9. STROOK
**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 车道编号/车道类型
**英文名称：** Lane / Lane Type
**数据类型：** 文本
**必填：** 是

**含义：**
具体车道的详细标识，包括车道编号和类型。

**标准格式：** [编号][类型]-[L/R]

#### 车道类型代码：

##### R - Rijstrook (Regular lane / 常规车道)
**英文：** Regular traffic lane
**中文：** 主行车道
**示例：**
- 1R-L (第1车道-左侧)
- 1R-R (第1车道-右侧)
- 2R-L, 2R-R, 3R-L, 3R-R, 4R-L, 4R-R

##### W - Weefstrook (Weaving lane / 交织车道)
**英文：** Weaving lane
**中文：** 交织车道
**定义：** 车辆在离开环道前立即与进入高速公路的车辆汇合的车道，形成"交织"冲突区。
**特点：** 荷兰公路网上的交织车道通常较长，以减少冲突。

**示例：**
- 1W-L, 1W-R
- 2W-L, 2W-R

##### I - Invoegstrook (Acceleration/Entrance lane / 加速车道)
**英文：** Acceleration lane / Entrance ramp
**中文：** 入口加速车道
**定义：** 允许进入交通流的车辆在汇入前加速至高速公路速度。

**示例：**
- 1I-L, 1I-R
- 2I-L, 2I-R

##### U - Uitvoegstrook (Deceleration/Exit lane / 减速车道)
**英文：** Deceleration lane / Exit ramp
**中文：** 出口减速车道
**定义：** 与主路相邻的车道，允许驾驶员在离开前减速。

**示例：**
- 1U-L, 1U-R
- 2U-L, 2U-R

##### Q - Spitsstrook (Rush hour lane / Peak lane / 高峰车道)
**英文：** Rush hour lane / Peak hour lane
**中文：** 高峰时段车道
**定义：** 仅在高峰时段开放的车道。

**特点：**
- **外侧Spitsstroken（Q-）：** 总是在车道右侧
- **内侧Plusstroken：** 位于车道左侧，但编码为**1R-L或1R-R**（第1常规车道）

**BPS文档说明（第30页）：**
> "Een spitsstrook, gelegen aan de binnenzijde van de doorgaande rijstroken, wordt aangeduid als 1e rijstrook (1 R- R of 1 R- L)."
>
> 翻译：内侧高峰车道（Plusstroken）被标记为第1条常规车道（1R-R 或 1R-L）

**⚠️ 重要说明：**
- Plusstroken（左侧高峰车道）**不**使用Q-编码
- 而是使用**R-编码**（1R-L 或 1R-R）
- 无法从STROOK编码本身区分永久第1车道和临时Plusstroken
- 需要通过其他字段（备注、说明）识别

**示例：**
- 1Q-R, 2Q-R（右侧外部高峰车道）
- 1R-L（可能是左侧内部高峰车道Plusstrook，也可能是永久第1车道）

##### B - Busstrook (Bus lane / 公交车道) ✅
**英文：** Bus lane
**中文：** 公交专用道
**定义：** 专用于公共交通或货运车辆的车道。

**来源：** BPS_boek_concept.pdf（第30页确认）

**示例：**
- 1B-L, 1B-R

##### V - Vluchtstrook (Emergency lane / 应急车道) ⚠️
**英文：** Emergency lane / Shoulder
**中文：** 应急车道/路肩
**定义：** 仅在特殊情况下可使用或停车的车道。

**来源：** BPS_boek_concept.pdf（第30页）

**⚠️ 数据异常：**
- PDF定义：V- = Vluchtstrook（应急车道）
- 数据中发现：`1V-L`, `1V-R`, `2V-R`（编号应急车道）
- **问题：** 应急车道通常不应有编号（1V, 2V）和方向（-L, -R）
- **状态：** 待Leon确认是否为数据错误

##### 其他车道类型（BPS定义但数据中未见）：

根据BPS_boek_concept.pdf（第29-31页），以下类型也是有效的STROOK代码：

| 代码 | 荷兰语 | 英文 | 中文 | 数据中出现 |
|------|--------|------|------|-----------|
| **C-** | Correctiestrook | Correction strip | 修正车道 | ❌ |
| **F-** | Fietsstrook | Bicycle lane | 自行车道 | ❌ |
| **S-** | Suggestiestrook | Suggestion lane | 建议车道 | ❌ |
| **P-** | Parkeerstrook | Parking lane | 停车车道 | ❌ |
| **L-** | Kruipstrook | Crawler lane | 爬坡车道 | ❌ |
| **K-** | Kantstreep | Edge line | 边线 | ❌ |
| **D-** | Deelstreep | Lane divider | 车道分隔线 | ❌ |
| **A-** | Asstreep | Center line | 中心线 | ❌ |

**注：** 这些类型在2022模板数据中未出现，可能用于其他类型的道路或特殊情况。

##### 特殊值：
- **ALL** - Rijbaanbreed (全车道宽度)
  - 表示整个车道宽度的养护工程
  - 此时参考第10列"Aantal rijstroken"

**参考来源：**
- Documents/Hallo Peng Luuk.txt (Leon提供的详细说明)
- Documents/BPS_boek_concept.pdf (RWS官方BPS系统文档，第29-31页)

---

### 10. Aantal rijstroken - in geval van rijbaanbreed (ALL)
**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 车道数量（全幅宽度情况下）
**英文名称：** Number of Lanes (in case of full carriageway width)
**数据类型：** 整数
**必填：** 当STROOK = "ALL"时必填

**含义：**
当养护工程为全车道宽度(rijbaanbreed)时，涉及的车道总数。

**示例值：**
- 2 (双车道)
- 3 (三车道)
- 4 (四车道)

**使用场景：**
- STROOK = "ALL" → 此列必填
- STROOK = 具体车道编号 → 此列可为空或为1

---

### 11. KM_Van
**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 起点公里数
**英文名称：** Kilometer From
**数据类型：** 数值
**必填：** 是
**单位：** 公里 (km)

**含义：**
工程段起始位置的公里数标识（与VAN百米桩对应，但以公里为单位）。

**格式：**
- 小数形式
- 使用欧洲格式（逗号作小数点）
- 可以是负值

**示例值：**
- 2,345 km
- 23,456 km
- -0,030 km

**与VAN的关系：**
KM_Van = VAN ÷ 10
(因为1 km = 10 hm)

---

### 12. KM_Tot
**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 终点公里数
**英文名称：** Kilometer To
**数据类型：** 数值
**必填：** 是
**单位：** 公里 (km)

**含义：**
工程段结束位置的公里数标识。

**格式规则：** 与KM_Van相同

**与TOT的关系：**
KM_Tot = TOT ÷ 10

---

### 13. Lengte
**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 长度
**英文名称：** Length
**数据类型：** 数值
**必填：** 是
**单位：** 米 (m)

**含义：**
工程段的总长度。

**计算公式：**
Lengte = (TOT - VAN) × 100
或
Lengte = (KM_Tot - KM_Van) × 1000

**示例值：**
- 1.250 (1250米 = 1.25公里)
- 5.680 (5680米)

**注意：** 使用欧洲数字格式

---

### 14. Breedte
**字段分类：** 🔵 非关键字段 (Non-Critical)
**中文名称：** 宽度
**英文名称：** Width
**数据类型：** 数值
**必填：** 是
**单位：** 米 (m)

**含义：**
养护工程段的宽度（路面宽度）。

**示例值：**
- 3,5 (单车道标准宽度)
- 7,0 (双车道)
- 10,5 (三车道)

**注意：**
- 荷兰标准车道宽度通常为3.5米或3.75米
- 全幅宽度 = 车道数 × 单车道宽度

---

### 15. MENGSELCODE
**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 混合料代码
**英文名称：** Mixture Code / Mix Code
**数据类型：** 文本
**必填：** 是

**含义：**
沥青混合料的标准代码，标识所用材料的具体配方。

**格式：**
由字母和数字组成的代码，遵循荷兰沥青混合料命名标准。

**示例值：**
- AC 11 surf
- SMA 11
- ZOAB 16
- PA 8

**相关标准：**
- RAW（荷兰道路与水利工程标准合同条款）
- CROW（荷兰道路标准机构）标准

---

### 16. GRANULAIR MENGSEL (0/16, 4/8, 2/6, 0/11, 0/8 enz)
**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 骨料级配
**英文名称：** Aggregate Gradation / Grain Size
**数据类型：** 文本
**必填：** 是

**含义：**
混合料中骨料的粒径范围，表示最小粒径/最大粒径（单位：毫米）。

**格式：** [最小]/[最大]

**常见值：**
- **0/16** - 0至16毫米（密级配，常用于面层）
- **0/11** - 0至11毫米（中等级配）
- **0/8** - 0至8毫米（细级配）
- **4/8** - 4至8毫米（单一级配）
- **2/6** - 2至6毫米（细骨料）
- **0/22** - 0至22毫米（粗级配，常用于基层）

**含义说明：**
- **第一个数字（最小粒径）：**
  - 0 = 包含细料（砂、矿粉）
  - >0 = 不含细料，骨架结构

- **第二个数字（最大粒径）：**
  - 决定混合料的最大颗粒尺寸
  - 与层厚度相关（最大粒径 ≈ 层厚的1/2至1/3）

---

### 17. DEKLAAGSOORT (bijv. ZOAB, SMA, tweelaags ZOAB, duurzaam ZOAB, etc.)
**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 面层类型
**英文名称：** Surface Layer Type / Wearing Course Type
**数据类型：** 文本
**必填：** 是

**含义：**
路面面层（最上层）的材料类型。

#### 常见面层类型：

##### ZOAB (Zeer Open Asfaltbeton)
**英文：** Porous Asphalt / Very Open Asphalt Concrete
**中文：** 多孔沥青/排水性沥青
**特点：** 高孔隙率（>15%），排水降噪

##### DZOAB (Dicht ZOAB)
**英文：** Dense Open Asphalt
**中文：** 密级配开级配沥青
**特点：** 相对密实，但仍有排水功能

##### SMA (Steen Mastiek Asfalt)
**英文：** Stone Mastic Asphalt
**中文：** 沥青玛蹄脂碎石
**特点：** 高粘结性，耐磨耐久

##### Tweelaags ZOAB
**英文：** Two-layer Porous Asphalt
**中文：** 双层多孔沥青
**特点：** 上下两层不同孔隙率的ZOAB

##### Duurzaam ZOAB
**英文：** Durable Porous Asphalt
**中文：** 耐久性多孔沥青
**特点：** 增强的长期性能

##### DAB (Dicht Asfaltbeton)
**英文：** Dense Asphalt Concrete
**中文：** 密级配沥青混凝土
**特点：** 低孔隙率，传统面层

##### PA (Poreus Asfalt)
**英文：** Porous Asphalt
**中文：** 多孔沥青（与ZOAB类似）

##### Dunne deklagen
**英文：** Thin Surface Layers
**中文：** 薄层罩面
**特点：** 厚度较薄的养护层（通常<30mm）

**英文对照：**
参考 Documents/Vertaallijst_EN-Nl_def2 (1).xlsx

---

### 18. DIKTE VERHARDING
**字段分类：** 🔵 非关键字段 (Non-Critical)
**中文名称：** 路面厚度/面层厚度
**英文名称：** Pavement Thickness / Surface Layer Thickness
**数据类型：** 数值
**必填：** 是
**单位：** 毫米 (mm)

**含义：**
新铺设或更换的面层（DEKLAAG）的厚度。

**典型值：**
- **薄层罩面：** 20-30 mm
- **标准面层：** 40-50 mm
- **厚面层：** 60-80 mm
- **重载路面：** 80-100+ mm

**注意：**
- 厚度与骨料最大粒径相关
- 一般规则：厚度 ≥ 2.5 × 最大骨料粒径

---

### 19. TUSSENLAAG
**字段分类：** 🔵 非关键字段 (Non-Critical)
**中文名称：** 中间层/结合层
**英文名称：** Binder Course / Intermediate Layer
**数据类型：** 文本（是/否 或 材料类型）
**必填：** 视情况而定

**含义：**
是否有中间层（位于面层和基层之间的结构层），或中间层的类型。

**可能的值：**
- **Ja** (是) - 有中间层
- **Nee** (否) - 无中间层
- **具体材料名称** - 如"Bindlaag", "AC 22 bind"等

**作用：**
- 承上启下，连接面层和基层
- 提供结构强度
- 防止反射裂缝

---

### 20. Mengselcode TUSSENLAAG
**字段分类：** 🔵 非关键字段 (Non-Critical)
**中文名称：** 中间层混合料代码
**英文名称：** Binder Course Mixture Code
**数据类型：** 文本
**必填：** 当TUSSENLAAG存在时必填

**含义：**
中间层所用沥青混合料的标准代码。

**示例值：**
- AC 22 bind
- AC 16 bind
- STAB (Steenasfalt Bindlaag)

**注意：**
- 仅当第19列"TUSSENLAAG"不为空/不为"Nee"时填写
- 命名规则与MENGSELCODE类似

---

### 21. DIKTE TUSSENLAAG (indien van toepassing)
**字段分类：** 🔵 非关键字段 (Non-Critical)
**中文名称：** 中间层厚度（如适用）
**英文名称：** Binder Course Thickness (if applicable)
**数据类型：** 数值
**必填：** 当TUSSENLAAG存在时必填
**单位：** 毫米 (mm)

**含义：**
中间层的厚度。

**典型值：**
- 50 mm
- 60 mm
- 70 mm
- 80 mm

**注意：**
- 仅当有TUSSENLAAG时填写
- 通常比面层厚

---

### 22. AANLEGDATUM
**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 施工日期/铺设日期
**英文名称：** Construction Date / Laying Date
**数据类型：** 日期
**必填：** 是

**含义：**
沥青混合料实际铺设的日期。

**格式：**
- 常见：DD-MM-YYYY (荷兰格式)
- 或：YYYY-MM-DD (ISO格式)

**示例值：**
- 15-06-2022
- 2022-06-15

**重要性：**
- 用于养护历史追溯
- 质量保修期计算
- 性能评估基准

---

### 23. ASFALTCENTRALE
**字段分类：** 🔵 非关键字段 (Non-Critical)
**中文名称：** 沥青拌合站
**英文名称：** Asphalt Plant / Asphalt Mixing Plant
**数据类型：** 文本
**必填：** 是

**含义：**
生产沥青混合料的拌合站名称或位置标识。

**用途：**
- 质量追溯
- 材料来源记录
- 温度和运输距离监控

**示例值：**
- Asfaltcentrale Utrecht
- Plant XYZ - Amsterdam
- [公司名称] - [城市]

---

### 24. TONNEN
**字段分类：** 🔵 非关键字段 (Non-Critical)
**中文名称：** 吨数
**英文名称：** Tonnes / Weight
**数据类型：** 数值
**必填：** 是
**单位：** 吨 (ton)

**含义：**
实际使用的沥青混合料总重量。

**格式：**
- 数值（使用欧洲格式）
- 可精确到小数

**示例值：**
- 123,5 吨
- 1.234,75 吨

**用途：**
- 工程量统计
- 成本核算
- 与理论计算量对比（质量控制）

**理论计算：**
理论吨数 = 长度(m) × 宽度(m) × 厚度(m) × 密度(ton/m³)
（密度通常为2.3-2.5 ton/m³）

---

### 25. evt. indien beschikbaar temperatuur (Productie)
**字段分类：** 🔵 非关键字段 (Non-Critical)
**中文名称：** 生产温度（如有）
**英文名称：** Production Temperature (if available)
**数据类型：** 数值
**必填：** 否（可选）
**单位：** 摄氏度 (°C)

**含义：**
沥青混合料在拌合站生产时的温度。

**典型温度范围：**
- **传统热拌沥青：** 150-180°C
- **改性沥青：** 160-190°C
- **温拌沥青：** 100-140°C

**重要性：**
- 影响施工质量
- 影响压实效果
- 质量控制参数

**注意：**
此列为可选字段，如承包商有数据则提供。

---

### 26. OPMERKINGENVELD
**字段分类：** 🔵 非关键字段 (Non-Critical)
**中文名称：** 备注字段
**英文名称：** Remarks / Comments Field
**数据类型：** 文本（自由格式）
**必填：** 否

**含义：**
记录任何额外信息、特殊情况、异常说明等。

**典型用途：**
- 施工条件特殊说明
- 材料变更记录
- 质量问题记录
- 坐标或位置补充说明
- 与其他项目的关联

**示例内容：**
- "因天气原因延期施工"
- "与项目XXX同期进行"
- "包含交叉口区域"
- "使用再生材料"

---

## 数据格式规范

### 数值格式
- **欧洲格式（必须遵守）：**
  - 小数分隔符：**逗号 (,)**
  - 千位分隔符：**点 (.)**
  - ✅ 正确：`1.234,56`
  - ❌ 错误：`1,234.56`

### 日期格式
- **推荐格式：** DD-MM-YYYY 或 YYYY-MM-DD
- 示例：`15-06-2022` 或 `2022-06-15`

### 文本格式
- 使用荷兰语术语（保持与RWS标准一致）
- 代码使用大写（如ZOAB, SMA）
- 车道编号遵循标准格式（如1R-L, 2W-R）

---

## 字段关联关系

### 位置相关字段组
```
Weg + BAAN + WEGLET + VAN + TOT → 唯一定位工程段
KM_Van, KM_Tot ← 与VAN, TOT对应（单位换算）
Lengte ← 由VAN和TOT计算得出
```

### 车道相关字段组
```
BAAN + STROOK → 确定具体车道
如果 STROOK = "ALL" → 参考"Aantal rijstroken"
```

### 材料相关字段组
```
MENGSELCODE + GRANULAIR MENGSEL + DEKLAAGSOORT → 面层材料完整描述
DIKTE VERHARDING → 面层厚度

TUSSENLAAG + Mengselcode TUSSENLAAG + DIKTE TUSSENLAAG → 中间层完整描述（可选）
```

### 工程量相关字段组
```
Lengte × Breedte × DIKTE VERHARDING → 体积
体积 × 密度 ≈ TONNEN (验证用)
```

### 追溯相关字段组
```
NAAM OPDRACHTNEMER + AANLEGDATUM + ASFALTCENTRALE + temperatuur → 质量追溯链
```

---

## 验证规则建议

### 必填字段验证
字段1-5, 7-8, 11-15, 17-18, 22-24必须非空。

### 逻辑一致性验证
1. TOT ≥ VAN
2. KM_Tot ≥ KM_Van
3. KM_Van ≈ VAN / 10 (允许小误差)
4. KM_Tot ≈ TOT / 10
5. Lengte ≈ (TOT - VAN) × 100
6. 如果STROOK = "ALL"，则"Aantal rijstroken"必填且 > 1
7. 如果TUSSENLAAG存在，则字段20和21必填

### 数据范围验证
1. Breedte：通常在 3.0 - 20.0 米之间
2. DIKTE VERHARDING：通常在 20 - 150 mm之间
3. DIKTE TUSSENLAAG：通常在 40 - 100 mm之间
4. temperatuur：如有值，应在 80 - 200°C之间

### 格式验证
1. Weg：应以"RW"或"A"开头
2. STROOK：应匹配正则表达式 `^\d+[RWUIQB]-[LR]$` 或等于"ALL"
3. 数值字段使用欧洲格式（逗号小数点）

### 参照数据验证
1. BAAN + WEGLET组合应存在于 `Documents/Validator - rijstroken.xlsx`
2. DEKLAAGSOORT应在已知类型列表中（ZOAB, SMA, DAB, PA等）

---

## 术语速查表

| 荷兰语 | 英文 | 中文 |
|--------|------|------|
| Rijksweg | National road | 国家公路 |
| Hoofdrijbaan | Main carriageway | 主车道 |
| Verbindingsweg | Connecting road / Ramp | 连接道/匝道 |
| Rijstrook | Lane | 车道 |
| Weefstrook | Weaving lane | 交织车道 |
| Invoegstrook | Acceleration lane | 加速车道 |
| Uitvoegstrook | Deceleration lane | 减速车道 |
| Spitsstrook | Rush hour lane | 高峰车道 |
| Deklaag | Wearing course | 面层 |
| Tussenlaag | Binder course | 中间层/结合层 |
| Bindlaag | Base course | 基层 |
| ZOAB | Porous asphalt | 多孔沥青 |
| SMA | Stone mastic asphalt | 沥青玛蹄脂碎石 |
| Mengsel | Mixture | 混合料 |
| Granulair | Aggregate / Grain | 骨料/级配 |
| Verharding | Pavement | 路面 |
| Dikte | Thickness | 厚度 |
| Breedte | Width | 宽度 |
| Lengte | Length | 长度 |
| Aanlegdatum | Construction date | 施工日期 |
| Asfaltcentrale | Asphalt plant | 沥青拌合站 |
| Opdrachtnemer | Contractor | 承包商 |

---

## 附录：Leon的车道类型说明（原文摘要）

根据 `Documents/Hallo Peng Luuk.txt`：

**Weefstroken (W)：**
> "lanes on which vehicles merge onto the highway at the end of a loop immediately before other vehicles leave to go around another loop, creating conflict known as weaving"

**Invoegstroken (I)：**
> "These lanes are identical to acceleration lanes that allow traffic entering a highway to accelerate to the speed of through traffic before merging with it"

**Uitvoegstroken (U)：**
> "These lanes are identical to deceleration lanes. A deceleration lane is a lane adjacent to the primary road or street used to improve traffic safety by allowing drivers to pull out of the through lane and decelerate"

**Spitsstroken (Q)：**
> "These lanes are only available to the traffic during rush hours. They are always on the right side of the carriage way"

---

## 文档维护

**下一步工作：**
1. 与Leon确认每个字段的理解是否正确
2. 补充实际数据示例
3. 完善验证规则
4. 建立标准枚举值列表（DEKLAAGSOORT, MENGSELCODE等）

**反馈联系：**
如发现错误或需要补充，请联系项目团队。

---

**文档结束**
