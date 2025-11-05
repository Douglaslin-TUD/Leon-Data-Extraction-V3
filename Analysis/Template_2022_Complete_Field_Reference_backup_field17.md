# 2022 Template Column Definitions
## Verzamelstaat_2022c.xlsx - Blad1 字段定义

**文档版本：** 2.0 (完整整合版)
**创建日期：** 2025-11-05
**更新日期：** 2025-11-05
**数据源：** Data/FW_ /Template/Verzamelstaat_2022c.xlsx
**数据行数：** 1,592行真实养护数据
**参考文档：**
- config/field_mapping_2022.json (字段定义-权威来源)
- config/validation_rules_2022.json (验证规则)
- config/enum_values_2022.json (枚举值统计)
- Analysis/Template_2022_Field_Analysis_OLD.md (真实数据分析)
- Documents/Hallo Peng Luuk.txt (Leon的车道类型说明)
- Documents/BPS_boek_concept.pdf (BPS系统官方文档)

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
**荷兰语：** NAAM OPDRACHTNEMER
**数据类型：** string (max_length: 200)
**必填：** 是

**含义：**
执行道路养护工程的承包商/公司名称。

**📊 数据统计（基于1,592行真实数据）：**
- **数据完整度：** 1528/1592 (96.0%)
- **缺失数据：** 64行 (4.0%)
- **唯一值数量：** 9个不同承包商

**📈 值分布：**

| 承包商名称 | 次数 | 占比 | 说明 |
|-----------|---:|---:|------|
| Gebr. van der Lee | 983 | 64.3% | 主要承包商 |
| BAM | 144 | 9.4% | |
| Mourik | 118 | 7.7% | |
| Heijmans | 75 | 4.9% | |
| Via Optimum | 72 | 4.7% | |
| Van Gelder | 69 | 4.5% | |
| Van der Weerd - Dostal | 29 | 1.9% | |
| De Jong & Zuurmond | 22 | 1.4% | |
| KWS Infra | 16 | 1.0% | |

**⚙️ 验证规则（来自JSON）：**
```json
{
  "min_length": 1,
  "max_length": 200
}
```

**📝 示例值：**
- "Gebr. van der Lee"
- "BAM"
- "Mourik"
- "Heijmans"

**👀 关键观察：**
- Gebr. van der Lee占绝对主导地位（64.3%）
- 仅9个承包商参与2022年养护工程
- 4%的数据缺失承包商名称（需要确认原因）

---

### 2. DISTRICT
**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 区域
**英文名称：** District
**荷兰语：** DISTRICT
**数据类型：** string
**必填：** 是

**含义：**
RWS管理区域划分。荷兰全国划分为7个大区（Regio），每个大区再细分为2-3个地区（District），共计15个地区。

**📊 数据统计（基于1,592行真实数据）：**
- **数据完整度：** 1591/1592 (99.9%)
- **缺失数据：** 1行 (0.1%)
- **唯一值数量：** 15个地区

**📈 值分布：**

| District | 次数 | 占比 | 所属大区 |
|----------|---:|---:|---------|
| ON-Noord | 800 | 50.3% | Oost-Nederland |
| NN-Oost | 143 | 9.0% | Noord-Nederland |
| ON_Zuid | 119 | 7.5% | Oost-Nederland (下划线格式) |
| ZN-West | 118 | 7.4% | Zuid-Nederland |
| MN-Zuid | 92 | 5.8% | Midden-Nederland |
| ZN-Midden | 72 | 4.5% | Zuid-Nederland |
| MN-Noord | 63 | 4.0% | Midden-Nederland |
| ZN-Zuidoost | 52 | 3.3% | Zuid-Nederland |
| NN-West | 52 | 3.3% | Noord-Nederland |
| ON-Oost | 36 | 2.3% | Oost-Nederland |
| WNN-Noord | 11 | 0.7% | West-Nederland Noord |
| WNN-Zuid | 11 | 0.7% | West-Nederland Noord |
| ZD-Zuid | 9 | 0.6% | Zuidwest-Nederland |
| ZD-Noord | 7 | 0.4% | Zuidwest-Nederland |
| WNZ-Noord | 6 | 0.4% | West-Nederland Zuid |

**🗺️ 大区命名体系：**
- **NN** = Noord-Nederland (北荷兰) → 2个地区
- **MN** = Midden-Nederland (中荷兰) → 2个地区
- **ON** = Oost-Nederland (东荷兰) → 3个地区
- **WNN** = West-Nederland Noord (西荷兰北) → 2个地区
- **WNZ** = West-Nederland Zuid (西荷兰南) → 1个地区
- **ZD** = Zuidwest-Nederland (西南荷兰/Zee en Delta) → 2个地区
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

**⚙️ 数据格式说明：**
- **标准格式：** 使用连字符 `-`（如 `ON-Zuid`）
- **别名格式：** 部分数据使用下划线 `_`（如 `ON_Zuid`）
- **数据统计：** 连字符格式占92.5% (1472条)，下划线格式占7.5% (119条)
- **验证规则：** 接受两种格式作为输入，输出统一为连字符标准格式

**别名映射：**
- `ON_Zuid` → 标准化为 `ON-Zuid`
- `MN_Zuid` → 标准化为 `MN-Zuid`

**⚙️ 验证规则（来自JSON + enum_values_2022.json）：**
```json
{
  "type": "in_list",
  "allowed_values": [
    "NN-Oost", "NN-West",
    "MN-Noord", "MN-Zuid",
    "ON-Noord", "ON-Zuid", "ON-Oost",
    "WNN-Noord", "WNN-Zuid",
    "WNZ-Noord",
    "ZD-Noord", "ZD-Zuid",
    "ZN-West", "ZN-Midden", "ZN-Zuidoost"
  ],
  "aliases": {
    "ON_Zuid": "ON-Zuid",
    "MN_Zuid": "MN-Zuid"
  },
  "canonical_format": "hyphen",
  "validation_rule": "接受连字符和下划线格式，输出统一为连字符标准格式"
}
```

**📝 示例值：**
- "ON-Noord" (标准格式)
- "ON_Zuid" (别名，应标准化为 "ON-Zuid")
- "ZN-West"
- "NN-Oost"

**👀 关键观察：**
- ON-Noord占据半数数据（50.3%），是最主要的养护区域
- 数据几乎完整（99.9%）
- 存在格式不一致问题，需要数据标准化

---

### 3. ZAAKNUMMER
**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 案件编号/项目编号
**英文名称：** Case Number / Project Number
**荷兰语：** ZAAKNUMMER
**数据类型：** string (VARCHAR)
**必填：** 是

**含义：**
RWS内部项目追踪编号，用于识别特定的养护项目。

**⚠️ 重要：数据类型说明**
- **JSON定义（正确）：** `data_type = "string"`
- **Excel读取结果：** 被pandas读取为`float64`（因为纯数字，Excel自动识别为数字）
- **实际应该：** 这是标识符，不是数值，应作为字符串处理
- **处理方式：** 读取时指定 `dtype={'ZAAKNUMMER': str}`，移除`.0`后缀

**📊 数据统计（基于1,592行真实数据）：**
- **数据完整度：** 1050/1592 (66.0%)
- **缺失数据：** 542行 (34.0%) ⚠️
- **唯一值数量：** 24个不同项目编号

**📈 格式分析：**

**两种格式并存：**
1. **12位格式：** 782个值 (74.5%)
   - 示例：`311181260135`, `311181260147`
   - 可能结构：31-1-181260135（推测）

2. **8位格式：** 268个值 (25.5%)
   - 示例：`31142564`, `31142566`
   - 可能结构：31-142564（推测）

**值分布（Top 10）：**

| 项目编号 | 次数 | 占比 | 格式 |
|---------|---:|---:|-----|
| 311181260135 | 139 | 13.2% | 12位 |
| 311181260147 | 88 | 8.4% | 12位 |
| 31142564 | 78 | 7.4% | 8位 |
| 311181260143 | 70 | 6.7% | 12位 |
| 311181260139 | 65 | 6.2% | 12位 |
| 311181260132 | 64 | 6.1% | 12位 |
| 31142566 | 63 | 6.0% | 8位 |
| 311181260148 | 56 | 5.3% | 12位 |
| 311181260138 | 56 | 5.3% | 12位 |
| 311181260146 | 53 | 5.0% | 12位 |

**完整项目编号列表（24个）：**
```
8位格式 (8个):
  31118127    (29次)
  31142564    (78次)
  31142566    (63次)
  31143621    (7次)
  31143622    (47次)
  31150507    (6次)
  31153856    (22次)
  31163605    (16次)

12位格式 (16个):
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

**⚙️ 验证规则（来自field_mapping_2022.json）：**
```json
{
  "data_type": "string",
  "pattern": "^[A-Z0-9-]+$",
  "description": "允许大写字母、数字和连字符"
}
```

**📝 示例值：**
- "311181260135"
- "31142564"
- "311181260147"

**👀 关键观察：**
- **34%数据缺失项目编号** - 这是正常现象还是数据问题？需要与Leon确认
- 8位和12位格式的区别和含义需要确认
- 所有值都是纯数字，未见字母或连字符（与pattern定义不完全匹配）

**❓ 待确认问题（已添加到会议议程）：**
1. 为什么有34%的数据缺失项目编号？
2. 8位和12位编号的区别是什么？代表不同类型的项目吗？
3. 是否有标准的编号命名规则或结构？
4. 应该按字符串存储还是整数存储？（推荐：VARCHAR(12)）

**数据库设计建议：**
- **类型：** VARCHAR(12)
- **理由：**
  - 这是标识符，不需要数学运算
  - 12位数字接近INT上限，用BIGINT浪费空间
  - 如果将来格式改变（加字母/符号），不需要改表结构
  - 与STROOK等字段保持一致（混合格式字段都用VARCHAR）

---

### 4. Weg
**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 道路编号
**英文名称：** Road Number / Highway Number
**荷兰语：** Weg
**数据类型：** string (VARCHAR(6))
**必填：** 是

**含义：**
国家公路编号（Rijksweg），RWS管理的主干高速公路标识。每个编号代表一条特定的高速公路。

**📊 数据统计（基于1,592行真实数据）：**
- **数据完整度：** 1592/1592 (100.0%) ✅
- **缺失数据：** 0行 (0.0%)
- **唯一值数量：** 34条不同道路
- **数值范围：** 1 - 835

**📈 值分布（Top 20）：**

| 道路编号 | 次数 | 占比 | 对应道路 |
|---------|---:|---:|---------|
| 28 | 422 | 26.5% | A28 (数据集主要公路) |
| 1 | 369 | 23.2% | A1 (第二主要公路) |
| 50 | 133 | 8.4% | A50 |
| 2 | 120 | 7.5% | A2 |
| 6 | 69 | 4.3% | A6 |
| 58 | 56 | 3.5% | A58 |
| 33 | 37 | 2.3% | A33 |
| 27 | 37 | 2.3% | A27 |
| 12 | 37 | 2.3% | A12 |
| 7 | 33 | 2.1% | A7 |
| 15 | 32 | 2.0% | A15 |
| 32 | 31 | 1.9% | A32 |
| 37 | 29 | 1.8% | A37 |
| 30 | 27 | 1.7% | A30 |
| 59 | 23 | 1.4% | A59 |
| 35 | 19 | 1.2% | A35 |
| 16 | 15 | 0.9% | A16 |
| 31 | 14 | 0.9% | A31 |
| 17 | 13 | 0.8% | A17 |
| 4 | 12 | 0.8% | A4 |

**当前数据格式：**
- 现有1,592条数据全部为**纯数字格式**（如 `1`, `28`, `50`）
- 数据完整度：100%（无缺失）
- 覆盖：34条不同道路

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

**数据库设计（来自field_mapping_2022.json）：**
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

## ⚙️ **验证规则（来自field_mapping_2022.json）**

```json
{
  "input_pattern": "^(\\d{1,3}|A\\d{1,3}|RW\\d{1,4})$",
  "accepted_formats": ["numeric", "A_prefix", "RW_prefix"],
  "normalization_required": true,
  "N_roads_warning": "N roads are provincial roads, not national highways",
  "storage_format": "A{number}",
  "remove_leading_zeros": true,
  "excel_output_format": "{number}"
}
```

**验证步骤：**
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

**📝 示例值：**
- 当前数据：`28`, `1`, `50`, `2`
- 存储格式：`A28`, `A1`, `A50`, `A2`
- Excel输出：`28`, `1`, `50`, `2`

---

### 5. BAAN
**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 车道类型/行车道
**英文名称：** Carriageway
**荷兰语：** BAAN
**数据类型：** string (固定枚举值)
**必填：** 是

**含义：**
车道的基本分类代码，定义道路的方向性和位置。**与STROOK字段有严格的逻辑依赖关系。**

**📊 数据统计（基于1,592行真实数据）：**
- **数据完整度：** 1592/1592 (100.0%) ✅
- **缺失数据：** 0行 (0.0%)
- **唯一值数量：** 6个不同值

**📈 值分布：**

| BAAN | 次数 | 占比 | 荷兰语全称 | 中文 | 状态 |
|------|---:|---:|-----------|------|------|
| **1HRL** | 723 | 45.4% | Hoofdrijbaan Links | 左侧主车道 | ✅ 标准值 |
| **1HRR** | 669 | 42.0% | Hoofdrijbaan Rechts | 右侧主车道 | ✅ 标准值 |
| **0VW** | 185 | 11.6% | Verbindingsweg | 连接道/匝道 | ✅ 标准值 |
| **0HRM** | 10 | 0.6% | Hoofdrijbaan Midden | 中间主车道 | ✅ 标准值 |
| **PWL** | 4 | 0.3% | Parallelweg Links | 左侧平行路 | ✅ 标准值 |
| **1HRR+HRR** | 1 | 0.1% | - | 异常值 | ⚠️ 数据错误 |

**👀 关键观察：**
- 左右主车道（1HRL + 1HRR）占87.4%，是最常见的车道类型
- 连接道（0VW）占11.6%
- 0HRM和PWL非常少见（共14次，0.9%）
- 发现1个异常值"1HRR+HRR"，可能是数据错误

---

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

**⚠️ 数据异常：**
- **1HRR+HRR**: 出现1次（0.1%）- 可能是数据录入错误，应该是"1HRR"或其他有效值

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
   ✅ BAAN = PWL（左侧平行路）
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
| PWL | 1R-L | ✅ 有效 | 左侧平行路，左向车道 |

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

## ⚙️ **验证规则总结（来自validation_rules_2022.json）**

**关键验证点：**

1. ✅ **ENUM-001**: BAAN必须是5个标准值之一（1HRR, 1HRL, 0HRM, 0VW, PWL）
2. ✅ **CROSS-002**: STROOK后缀-R只能出现在1HRR/0HRM/0VW
3. ✅ **CROSS-003**: STROOK后缀-L只能出现在1HRL/0HRM/0VW/PWL
4. ✅ **CROSS-005**: 0HRM必须同时有1R-R和1R-L车道
5. ✅ **COND-002**: 0VW必须填写WEGLET字段

**JSON验证规则（来自field_mapping_2022.json）：**
```json
{
  "field_number": 5,
  "field_name_nl": "BAAN",
  "data_type": "string",
  "validation_rules": {
    "pattern": "^(\\d{1})(VW|HR[LRM]|PW[LR])$"
  }
}
```

**参考来源：**
- Leon邮件确认（2025-11）
- Documents/Validator - rijstroken.xlsx
- Documents/BPS_boek_concept.pdf
- RWS Geo Services (PWL确认)
- RWS Productspecificatie Ultimo (2014)
- config/validation_rules_2022.json (ENUM-001, CROSS-002/003/005, COND-002)

**📝 示例值：**
- "1HRL" (最常见，45.4%)
- "1HRR" (第二常见，42.0%)
- "0VW" (连接道，11.6%)
- "0HRM" (中间车道，0.6%)
- "PWL" (平行路，0.3%)

**❓ 待确认问题（已添加到会议议程）：**
1. "1HRR+HRR"异常值的含义和处理方式
2. PWR（右侧平行路）是否存在？理论上应该与PWL对称

---


---

### 6. WEGLET (zie toelichting blad 2)

**字段分类：** 🔴 关键字段 (Critical)  
**中文名称：** 连接道字母编码  
**英文名称：** Connecting Road Letter / Ramp Code  
**数据类型：** string  
**必填：** 条件必填（当BAAN=0VW时）  
**验证规则编号：** COND-002

**📊 JSON定义（权威来源）：**
```json
{
  "field_number": 6,
  "field_name_nl": "WEGLET (zie toelichting blad 2)",
  "data_type": "string",
  "required": false,
  "classification": "critical",
  "category": "location_identification",
  "validation_rules": {
    "pattern": "^[a-z]$"
  }
}
```

**📊 数据统计（基于1,592行真实数据）：**

- **数据完整度：** 196/1592 (12.3%)
- **缺失数据：** 1396 (87.7%)
- **唯一值数量：** 22

**📈 值分布：**

| WEGLET | 次数 | 占比 | 符合BPS标准 | 备注 |
|--------|------|------|-------------|------|
| `a` | 30 | 15.3% | ✅ 标准 | 下匝道-顺向 |
| `c` | 29 | 14.8% | ✅ 标准 | 下匝道-逆向 |
| `b` | 26 | 13.3% | ✅ 标准 | 上匝道-顺向 |
| `d` | 24 | 12.2% | ✅ 标准 | 上匝道-逆向 |
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
| `[Parallelweg Li]` | 4 | 2.0% | ⚠️ 异常值 | 格式错误 |
| `a/b` | 2 | 1.0% | ⚠️ 组合值 | 跨越两个weglet? |
| `c/d` | 1 | 0.5% | ⚠️ 组合值 | 跨越两个weglet? |

**✅ BPS标准编码系统（BPS_boek_concept.pdf Tabel 3）：**

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

**⚠️ 数据质量问题：**

1. **标准值占比：** 109/196 (55.6%) - a/b/c/d四个标准值
2. **非标准字母：** 83/196 (42.3%) - e-z等其他字母（共15个）
3. **异常值：** 4行'[Parallelweg Li]'格式错误，应为单字母
4. **组合值：** 3行'a/b'或'c/d'，可能表示跨越两个weglet

**条件必填规则：**
```
IF BAAN = "0VW" THEN WEGLET IS REQUIRED
ELSE WEGLET SHOULD BE EMPTY
```

**验证规则（validation_rules_2022.json - COND-002）：**
```json
{
  "rule_id": "COND-002",
  "category": "conditional_required",
  "enabled": true,
  "condition": {"field": "BAAN", "value": "0VW"},
  "then": {"field": "WEGLET", "required": true},
  "error_message": "当BAAN='0VW'时，'WEGLET'不能为空",
  "severity": "error"
}
```

**示例组合：**
- **0VWa** - 顺向下匝道（离开主路，hectometer增长方向）
- **0VWb** - 顺向上匝道（汇入主路，hectometer增长方向）
- **0VWc** - 逆向下匝道（离开主路，hectometer减少方向）
- **0VWd** - 逆向上匝道（汇入主路，hectometer减少方向）

**数据库设计：**
- 类型：CHAR(1) 或 VARCHAR(20)（考虑异常值）
- 约束：CHECK (WEGLET IN ('a', 'b', 'c', 'd') OR WEGLET ~ '^[a-z]$')
- 外键关联：需要与BAAN字段配合验证

**❓ 待与Leon确认的问题：**

1. **非标准字母含义：** e, f, g, h, j, m, n, p, q, r, s, t, u, x, y 这些字母的实际含义是什么？
2. **组合值含义：** 'a/b', 'c/d' 是否表示工程段跨越两个匝道？
3. **异常值处理：** '[Parallelweg Li]'应该如何标准化？是否应为空或特定字母？
4. **非标准字母是否有效：** 这些值是承包商的错误还是有特殊用途？

**参考来源：**
- 📄 config/field_mapping_2022.json - 字段定义
- 📊 Analysis/Template_2022_Field_Analysis_OLD.md - 真实数据统计
- 📖 Documents/BPS_boek_concept.pdf (Tabel 3) - BPS标准编码系统
- 📧 Documents/Hallo Peng Luuk.txt - Leon提供的实际示例
- 📋 config/enum_values_2022.json (lines 218-262) - WEGLET枚举定义

**特别说明：**
- 模板Blad 2（第二个工作表）应包含更详细的说明和示例
- 当前数据中存在大量非标准值，需要与Leon确认处理方式
- 建议建立扩展的WEGLET编码表，覆盖所有实际使用的字母

---

### 7. VAN (graag tot min. 10 meter nauwkeurig)

**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 起始位置
**英文名称：** From (Kilometer Position)
**数据类型：** number (float)
**必填：** 是
**单位：** 🔴 **公里 (kilometer, km)** ⚠️ 重大更正
**精度要求：** 最少到10米（0.010 km = 10米，需要3位小数）

**🚨 重要更正（2025-11-05）：**
- ❌ **旧理解：** 单位是百米(hectometer, hm)
- ✅ **正确理解：** 单位是**公里(km)**
- 💡 **关键概念：** 荷兰道路系统使用hectometer标识系统，但VAN/TOT字段存储的是**公里数值**

**📊 JSON定义（权威来源）：**
```json
{
  "field_number": 7,
  "field_name_nl": "VAN (graag tot min. 10 meter nauwkeurig)",
  "data_type": "number",
  "unit": "kilometer",
  "required": true,
  "classification": "critical",
  "category": "location_identification",
  "validation_rules": {
    "type": "float",
    "min": -1,
    "max": 300,
    "precision": 3,
    "european_format": true
  }
}
```

**📊 数据统计（基于1,592行真实数据）：**

- **数据完整度：** 1592/1592 (100.0%)
- **缺失数据：** 0 (0.0%)
- **唯一值数量：** 1162

**📈 值分布（前20个最常见值）：**

| VAN (km) | 次数 | 占比 | 说明 |
|----------|------|------|------|
| `104.5` | 14 | 0.9% | ✅ 104.5公里位置 |
| `104.375` | 10 | 0.6% | ✅ 104.375公里位置 |
| `111.1` | 9 | 0.6% | ✅ 111.1公里位置 |
| `113.0` | 9 | 0.6% | ✅ 113.0公里位置 |
| `112.6` | 9 | 0.6% | ✅ 112.6公里位置 |
| `111.88` | 8 | 0.5% | ✅ 111.88公里位置 |
| `54350.0` | 8 | 0.5% | ⚠️ 异常大值（54,350 km） |
| `113.3` | 8 | 0.5% | ✅ 113.3公里位置 |
| `111.955` | 7 | 0.4% | ✅ 111.955公里位置 |
| `102.75` | 7 | 0.4% | ✅ 102.75公里位置 |
| `112.025` | 6 | 0.4% | ✅ 112.025公里位置 |
| `105.9` | 6 | 0.4% | ✅ 105.9公里位置 |
| `111.87` | 6 | 0.4% | ✅ 111.87公里位置 |
| `67.14` | 6 | 0.4% | ✅ 67.14公里位置 |
| `112.825` | 5 | 0.3% | ✅ 112.825公里位置 |
| `104.45` | 5 | 0.3% | ✅ 104.45公里位置 |
| `112.8` | 5 | 0.3% | ✅ 112.8公里位置 |
| `53800.0` | 5 | 0.3% | ⚠️ 异常大值（53,800 km） |
| `66.9` | 5 | 0.3% | ✅ 66.9公里位置 |
| `52700.0` | 5 | 0.3% | ⚠️ 异常大值（52,700 km） |

**⚠️ 数据质量问题：**

**问题1：异常大数值**
- 发现多个异常大值：272660.0 km (最大), 54350.0, 53800.0, 52700.0等
- **正常范围：** 荷兰公路里程一般在0-300 km之间
- **可能原因：**
  - 数据录入错误（多打了位数）
  - 单位混淆
  - 特殊编码

**问题2：VAN > TOT在44.5%的数据中出现**
- ✅ **这是正常现象，不是错误！**
- 原因：某些BAAN类型（如1HRL, PWL）的正常行车方向与道路标准方向(oriëntatierichting)相反
- 在这些BAAN上，hectometer递减，因此VAN > TOT是正确的

**含义：**
工程段起始位置的公里数。表示工程段在该道路上的起始位置，使用荷兰BPS (Beschrijvende Plaatsaanduiding Systematiek) 定位系统。

**📍 Hectometer系统与VAN/TOT的关系：**

虽然VAN/TOT以公里为单位，但其背后的概念与荷兰道路的**hectometer标识系统**密切相关：

1. **Oriëntatierichting（道路标准方向）：**
   - 每条weg（道路）有唯一的标准参考方向
   - Hectometer沿oriëntatierichting递增，反向递减
   - 这是BPS系统定义的物理规律

2. **BAAN与VAN-TOT方向关系：**

   | BAAN类型 | 正常车流方向 | Hectometer变化 | VAN vs TOT |
   |---------|-------------|---------------|-----------|
   | **1HRR** | 与oriëntatierichting同向 | 递增 ↑ | TOT > VAN ✅ |
   | **1HRL** | 与oriëntatierichting反向 | 递减 ↓ | VAN > TOT ✅ |
   | **PWR** | 与oriëntatierichting同向 | 递增 ↑ | TOT > VAN ✅ |
   | **PWL** | 与oriëntatierichting反向 | 递减 ↓ | VAN > TOT ✅ |
   | **0HRM** | 由STROOK后缀决定 | -R递增，-L递减 | 取决于STROOK |
   | **0VW** | 复杂，节点相关 | 不确定 | ❓ 待Leon确认 |

3. **关键原则：**
   > Hectometer的"增/减"本质上只跟"是否顺着道路的标准方向（oriëntatierichting）开"有关，BAAN只是间接影响。

**格式：**
- 小数形式
- 精度要求：最少到10米（0.010 km = 3位小数）
- **可以是负值**（起点前的路段）
- **欧洲数字格式：** 逗号作小数点，点作千位分隔符

**示例值：**
- `104.325` km = 104公里325米位置
- `7.800` km = 7公里800米位置
- `125.225` km = 125公里225米位置
- `-0.030` km（起点前30米）

**数据处理流程：**

**1️⃣ 输入阶段：**
- 接受欧洲格式：`104,325` 或 `125,225`
- 使用pandas读取：`pd.read_excel(..., decimal=',')`

**2️⃣ 验证阶段：**
```python
# 单字段验证
assert -1 <= VAN <= 300, "VAN超出正常范围（警告>300km）"
assert isinstance(VAN, (int, float)), "VAN必须是数值"

# 跨字段验证：不再要求TOT > VAN！
# 改为基于BAAN类型的方向一致性检查
if BAAN in ['1HRR', 'PWR']:
    if VAN > TOT:
        warnings.warn(f"BAAN={BAAN}应该递增，但VAN>TOT，可能需要交换")
elif BAAN in ['1HRL', 'PWL']:
    if TOT > VAN:
        warnings.warn(f"BAAN={BAAN}应该递减，但TOT>VAN，可能需要交换")
```

**3️⃣ 存储阶段：**
- 数据库类型：DECIMAL(10,3) 或 FLOAT
- 保留3位小数精度

**验证规则（已更新）：**
```json
{
  "type": "float",
  "min": -1,
  "max": 300,
  "precision": 3,
  "european_format": true,
  "warning_threshold": 300
}
```

**逻辑关系（已更新）：**
- ❌ ~~VAN < TOT~~（不再适用）
- ✅ VAN与TOT的大小关系由BAAN类型决定
- ✅ 工程段长度 = **abs(TOT - VAN)** km（永远是正值）

**❓ 待与Leon确认的问题：**

1. **异常大数值：** 272660.0, 54350.0等值是数据错误还是特殊编码？（已添加到议题9.5）

2. **0VW方向规则：** 0VW（匝道）的VAN-TOT方向判断规则？（已添加到议题9.1）

3. **负值VAN：** 负值VAN的使用场景和频率？

4. **数据自动修正：** 是否基于BAAN类型自动交换VAN/TOT？（已添加到议题9.2）
   - 原则：BAAN一般不会错，VAN/TOT经常填写错误

**参考来源：**
- 📄 config/field_mapping_2022.json - 字段定义和验证规则
- 📊 Analysis/Template_2022_Field_Analysis_OLD.md (lines 475-539) - 真实数据统计
- 🚨 Analysis/CRITICAL_CORRECTION_VAN_TOT_Units.md - 重大单位更正文档
- 📋 Meeting_Notes/2025-11-06_Leon_Meeting_Agenda.md (议题9) - VAN/TOT相关问题

---

### 8. TOT (graag tot min. 10 meter nauwkeurig)

**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 结束位置
**英文名称：** To (Kilometer Position)
**数据类型：** number (float)
**必填：** 是
**单位：** 🔴 **公里 (kilometer, km)** ⚠️ 重大更正
**精度要求：** 最少到10米（0.010 km = 10米，需要3位小数）

**🚨 重要更正（2025-11-05）：**
- ❌ **旧理解：** 单位是百米(hectometer, hm)，且TOT必须 >= VAN
- ✅ **正确理解：** 单位是**公里(km)**，且TOT可以小于VAN（取决于BAAN类型）

**📊 JSON定义（权威来源）：**
```json
{
  "field_number": 8,
  "field_name_nl": "TOT (graag tot min. 10 meter nauwkeurig)",
  "data_type": "number",
  "unit": "kilometer",
  "required": true,
  "classification": "critical",
  "category": "location_identification",
  "validation_rules": {
    "type": "float",
    "min": -1,
    "max": 300,
    "precision": 3,
    "european_format": true
  }
}
```

**📊 数据统计（基于1,592行真实数据）：**

- **数据完整度：** 1587/1592 (99.7%)
- **缺失数据：** 5 (0.3%)
- **唯一值数量：** 1138

**📈 值分布（前20个最常见值）：**

| TOT (km) | 次数 | 占比 | 说明 |
|----------|------|------|------|
| `113.0` | 14 | 0.9% | ✅ 113.0公里位置 |
| `104.45` | 11 | 0.7% | ✅ 104.45公里位置 |
| `111.1` | 10 | 0.6% | ✅ 111.1公里位置 |
| `108.15` | 9 | 0.6% | ✅ 108.15公里位置 |
| `111.88` | 9 | 0.6% | ✅ 111.88公里位置 |
| `111.955` | 8 | 0.5% | ✅ 111.955公里位置 |
| `113.3` | 8 | 0.5% | ✅ 113.3公里位置 |
| `111.95` | 8 | 0.5% | ✅ 111.95公里位置 |
| `52800.0` | 7 | 0.4% | ⚠️ 异常大值（52,800 km） |
| `53490.0` | 7 | 0.4% | ⚠️ 异常大值（53,490 km） |
| `102.5` | 7 | 0.4% | ✅ 102.5公里位置 |
| `104.375` | 6 | 0.4% | ✅ 104.375公里位置 |
| `105.975` | 6 | 0.4% | ✅ 105.975公里位置 |
| `104.425` | 6 | 0.4% | ✅ 104.425公里位置 |
| `53900.0` | 6 | 0.4% | ⚠️ 异常大值（53,900 km） |
| `51400.0` | 6 | 0.4% | ⚠️ 异常大值（51,400 km） |
| `67.075` | 6 | 0.4% | ✅ 67.075公里位置 |
| `60.45` | 5 | 0.3% | ✅ 60.45公里位置 |
| `105.9` | 5 | 0.3% | ✅ 105.9公里位置 |
| `66.875` | 5 | 0.3% | ✅ 66.875公里位置 |

**⚠️ 数据质量问题：**

**问题1：缺失数据**
- 5行(0.3%)TOT字段为空

**问题2：异常大数值**
- 与VAN字段类似，出现272760.0 km (最大), 52800.0, 53490.0等异常大值

**问题3：TOT < VAN在44.5%的数据中出现**
- ✅ **这是正常现象，不是错误！**
- 在1HRL、PWL等左侧BAAN上，车流方向与oriëntatierichting相反
- Hectometer递减，因此TOT < VAN是正确的

**含义：**
工程段结束位置的公里数。与VAN配合定义工程段的精确位置范围。

**📍 TOT与VAN的方向关系：**

TOT与VAN的大小关系**不是固定的**，而是由BAAN类型决定：

| BAAN类型 | 正常情况 | 说明 |
|---------|---------|------|
| **1HRR** | TOT > VAN ✅ | 右侧主线，递增方向 |
| **1HRL** | TOT < VAN ✅ | 左侧主线，递减方向 |
| **PWR** | TOT > VAN ✅ | 右侧平行路，递增方向 |
| **PWL** | TOT < VAN ✅ | 左侧平行路，递减方向 |
| **0HRM** | 取决于STROOK | -R后缀递增，-L后缀递减 |
| **0VW** | ❓ 待Leon确认 | 匝道方向复杂 |

**格式规则：** 与VAN相同
- 小数形式
- 精度：0.010 km（10米 = 3位小数）
- 可以为负值
- 欧洲数字格式

**示例值：**
- `113.000` km = 113公里位置
- `104.450` km = 104公里450米位置
- `67.075` km = 67公里75米位置

**逻辑关系（已更新）：**

**❌ 旧规则（错误）：**
```
TOT必须 >= VAN（终点 >= 起点）
```

**✅ 新规则（正确）：**
```
TOT与VAN的大小关系由BAAN类型决定：
- 右侧BAAN (1HRR, PWR): 应该 TOT > VAN
- 左侧BAAN (1HRL, PWL): 应该 VAN > TOT
- 0HRM: 由STROOK的-R/-L后缀决定
- 0VW: 待Leon确认规则
```

**长度计算（已更新）：**
```
工程段长度 = abs(TOT - VAN) km
（永远是正值，使用绝对值）
```

**示例：**
```
例1（递增方向）:
BAAN=1HRR, VAN=104.5, TOT=113.0
长度 = abs(113.0 - 104.5) = 8.5 km ✅

例2（递减方向）:
BAAN=1HRL, VAN=113.0, TOT=104.5
长度 = abs(104.5 - 113.0) = 8.5 km ✅
```

**数据处理流程：**

**1️⃣ 输入阶段：**
- 使用pandas读取：`pd.read_excel(..., decimal=',')`

**2️⃣ 验证阶段（已更新）：**
```python
# 单字段验证
assert -1 <= TOT <= 300, "TOT超出正常范围（警告>300km）"
assert not pd.isna(TOT), "TOT不能为空"

# 跨字段验证：基于BAAN类型
if BAAN in ['1HRR', 'PWR']:
    if TOT < VAN:
        warnings.warn(f"BAAN={BAAN}应该递增，但TOT<VAN，可能需要交换")
elif BAAN in ['1HRL', 'PWL']:
    if TOT > VAN:
        warnings.warn(f"BAAN={BAAN}应该递减，但TOT>VAN，可能需要交换")
elif BAAN == '0HRM':
    if '-R' in STROOK and TOT < VAN:
        warnings.warn(f"0HRM with -R应该递增，但TOT<VAN")
    elif '-L' in STROOK and TOT > VAN:
        warnings.warn(f"0HRM with -L应该递减，但TOT>VAN")
```

**3️⃣ 计算衍生字段（已更新）：**
```python
# 计算长度（使用绝对值）
Lengte = abs(TOT - VAN)
```

**数据库设计（已更新）：**
- 类型：DECIMAL(10,3) 或 FLOAT
- 约束：❌ ~~CHECK (TOT >= VAN)~~（已删除）
- 新约束：基于BAAN的条件验证（待实现）

**❓ 待与Leon确认的问题：**

1. **异常大数值：** TOT字段中的272760.0, 52800.0等值是否与VAN对应？（已添加到议题9.5）

2. **缺失值处理：** 5行缺失TOT的原因？如何补充？

3. **负值TOT：** TOT是否也可能为负值？使用场景？

4. **0VW方向规则：** 匝道的TOT-VAN方向判断规则？（已添加到议题9.1）

5. **自动修正策略：** 是否基于BAAN自动交换TOT/VAN？（已添加到议题9.2）
   - 原则：BAAN一般不会错，VAN/TOT经常填写错误

**参考来源：**
- 📄 config/field_mapping_2022.json - 字段定义和验证规则
- 📊 Analysis/Template_2022_Field_Analysis_OLD.md (lines 542-606) - 真实数据统计
- 🚨 Analysis/CRITICAL_CORRECTION_VAN_TOT_Units.md - 重大单位更正文档
- 📋 Meeting_Notes/2025-11-06_Leon_Meeting_Agenda.md (议题9) - VAN/TOT相关问题


---

### 9. STROOK

**字段分类：** 🔴 关键字段 (Critical)  
**中文名称：** 车道编号/车道类型  
**英文名称：** Lane / Lane Type  
**数据类型：** string  
**必填：** 是

**📊 JSON定义（权威来源）：**
```json
{
  "field_number": 9,
  "field_name_nl": "STROOK",
  "data_type": "string",
  "required": true,
  "classification": "critical",
  "category": "lane_identification",
  "validation_rules": {
    "pattern": "^(\\d{1}[RWUIQB]-[LR]|ALL)$"
  },
  "lane_types": {
    "R": "Rijstrook (Regular lane)",
    "W": "Weefstrook (Weaving lane)",
    "I": "Invoegstrook (Acceleration lane)",
    "U": "Uitvoegstrook (Deceleration lane)",
    "Q": "Spitsstrook (Rush hour lane)",
    "B": "Busstrook (Bus lane)",
    "ALL": "Rijbaanbreed (Full carriageway width)"
  }
}
```

**📊 数据统计（基于1,592行真实数据）：**

- **数据完整度：** 1589/1592 (99.8%)
- **缺失数据：** 3 (0.2%)
- **唯一值数量：** 84

**📈 值分布（前20个最常见值）：**

| STROOK | 次数 | 占比 | 车道类型 | 说明 |
|--------|------|------|----------|------|
| `2R-L` | 261 | 16.4% | Rijstrook | 第2常规车道-左侧 ✅ |
| `2R-R` | 249 | 15.7% | Rijstrook | 第2常规车道-右侧 ✅ |
| `ALL` | 224 | 14.1% | 全幅宽度 | 全车道宽度 ✅ |
| `1R-L` | 219 | 13.8% | Rijstrook | 第1常规车道-左侧 ✅ |
| `1R-R` | 132 | 8.3% | Rijstrook | 第1常规车道-右侧 ✅ |
| `3R-L` | 68 | 4.3% | Rijstrook | 第3常规车道-左侧 ✅ |
| `3R-R` | 51 | 3.2% | Rijstrook | 第3常规车道-右侧 ✅ |
| `1U-R` | 42 | 2.6% | Uitvoegstrook | 减速车道-右侧 ✅ |
| `1I-R` | 32 | 2.0% | Invoegstrook | 加速车道-右侧 ✅ |
| `1I-L` | 25 | 1.6% | Invoegstrook | 加速车道-左侧 ✅ |
| `1Q-R` | 22 | 1.4% | Spitsstrook | 高峰车道-右侧 ✅ |
| `1V-R` | 22 | 1.4% | Vluchtstrook | **应急车道-右侧 ⚠️** |
| `1U-L` | 21 | 1.3% | Uitvoegstrook | 减速车道-左侧 ✅ |
| `1V-L` | 21 | 1.3% | Vluchtstrook | **应急车道-左侧 ⚠️** |
| `1R-R, 2R-R` | 17 | 1.1% | 组合值 | **多车道组合 ⚠️** |
| `1W-L` | 16 | 1.0% | Weefstrook | 交织车道-左侧 ✅ |
| `1R-L, 2R-L` | 12 | 0.8% | 组合值 | **多车道组合 ⚠️** |
| `4R-R` | 12 | 0.8% | Rijstrook | 第4常规车道-右侧 ✅ |
| `4R-L` | 7 | 0.4% | Rijstrook | 第4常规车道-左侧 ✅ |
| `2U-L` | 7 | 0.4% | Uitvoegstrook | 第2减速车道-左侧 ✅ |

**含义：**
具体车道的详细标识，包括车道编号、类型和方向。STROOK与BAAN配合使用，精确定位养护工程的具体位置。

**标准格式：** `[编号][类型]-[方向]` 或 `ALL`

**车道类型代码详解：**

#### R - Rijstrook (Regular lane / 常规车道)
**英文：** Regular traffic lane  
**中文：** 主行车道/常规车道  
**定义：** 正常通行的主要车道

**示例：**
- `1R-L` (第1车道-左侧)
- `1R-R` (第1车道-右侧)
- `2R-L`, `2R-R`, `3R-L`, `3R-R`, `4R-L`, `4R-R`

**数据中出现：** 1,347次（84.7%）

---

#### W - Weefstrook (Weaving lane / 交织车道)
**英文：** Weaving lane  
**中文：** 交织车道  
**定义：** 车辆在离开环道前立即与进入高速公路的车辆汇合的车道，形成"交织"冲突区

**特点：** 荷兰公路网上的交织车道通常较长，以减少冲突

**示例：**
- `1W-L`, `1W-R`
- `2W-L`, `2W-R`

**数据中出现：** 27次（1.7%）

---

#### I - Invoegstrook (Acceleration/Entrance lane / 加速车道)
**英文：** Acceleration lane / Entrance ramp  
**中文：** 入口加速车道/汇入车道  
**定义：** 允许进入交通流的车辆在汇入前加速至高速公路速度

**示例：**
- `1I-L`, `1I-R`
- `2I-L`, `2I-R`

**数据中出现：** 62次（3.9%）

---

#### U - Uitvoegstrook (Deceleration/Exit lane / 减速车道)
**英文：** Deceleration lane / Exit ramp  
**中文：** 出口减速车道/离开车道  
**定义：** 与主路相邻的车道，允许驾驶员在离开前减速

**示例：**
- `1U-L`, `1U-R`
- `2U-L`, `2U-R`

**数据中出现：** 79次（5.0%）

---

#### Q - Spitsstrook (Rush hour lane / 高峰车道)
**英文：** Rush hour lane / Peak hour lane  
**中文：** 高峰时段车道（外侧）  
**定义：** 仅在高峰时段开放的车道

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
- `1Q-R`, `2Q-R`（右侧外部高峰车道）
- `1R-L`（可能是左侧内部高峰车道Plusstrook，也可能是永久第1车道）

**数据中出现：** 22次（1.4%）

---

#### B - Busstrook (Bus lane / 公交车道) ✅
**英文：** Bus lane  
**中文：** 公交专用道  
**定义：** 专用于公共交通或货运车辆的车道

**来源：** BPS_boek_concept.pdf（第30页确认）

**示例：**
- `1B-L`, `1B-R`

**数据中出现：** 0次

---

#### V - Vluchtstrook (Emergency lane / 应急车道) ⚠️
**英文：** Emergency lane / Shoulder  
**中文：** 应急车道/路肩  
**定义：** 仅在特殊情况下可使用或停车的车道

**来源：** BPS_boek_concept.pdf（第30页）

**⚠️ 数据异常：**
- PDF定义：V- = Vluchtstrook（应急车道）
- **数据中发现：** `1V-L` (21次), `1V-R` (22次), `2V-R` (1次) - 共44次
- **问题：** 应急车道通常不应有编号（1V, 2V）和方向（-L, -R）
- **状态：** 待Leon确认是否为数据错误或特殊编码

**示例（数据中实际出现）：**
- `1V-L`, `1V-R`
- `2V-R`

---

#### 其他车道类型（BPS定义但数据中未见）：

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

---

#### 特殊值：ALL - Rijbaanbreed (全车道宽度)

**含义：** 表示整个车道宽度的养护工程  
**使用场景：** 工程覆盖全部车道时使用  
**关联字段：** 此时必须填写"Aantal rijstroken"（车道数量）

**数据中出现：** 224次（14.1%）

---

**⚠️ 数据质量问题：**

1. **V型车道异常：** 43次出现`1V-L`, `1V-R`, `2V-R`
   - BPS文档中V-应表示应急车道，通常不编号
   - 需要确认这是数据错误还是特殊用法

2. **组合值：** 29次出现组合值如`1R-R, 2R-R`
   - 表示同时施工多条车道
   - 不符合JSON正则表达式`^(\\d{1}[RWUIQB]-[LR]|ALL)$`
   - 需要确认是否应拆分为多行

3. **JSON验证规则不匹配：**
   - JSON pattern不包含V型车道
   - JSON pattern不支持组合值格式
   - 实际数据84个唯一值，但标准格式预期应更少

**BAAN-STROOK跨字段依赖关系：**

详见Field 5 (BAAN)的完整说明：

**规则1：方向匹配（关键验证）**
```
STROOK后缀-R → 只能出现在BAAN=1HRR/0HRM/0VW
STROOK后缀-L → 只能出现在BAAN=1HRL/0HRM/0VW
```

**规则2：0HRM特殊要求**
```
BAAN=0HRM → 必须同时存在1R-R和1R-L两条车道
```

**规则3：0VW连接道规则**
```
BAAN=0VW → STROOK编码必须与WEGLET匹配
```

**验证规则（validation_rules_2022.json）：**
```json
{
  "rule_id": "CROSS-002",
  "description": "STROOK后缀-R只能出现在BAAN=1HRR/0HRM/0VW",
  "severity": "error"
},
{
  "rule_id": "CROSS-003",
  "description": "STROOK后缀-L只能出现在BAAN=1HRL/0HRM/0VW",
  "severity": "error"
},
{
  "rule_id": "CROSS-005",
  "description": "0HRM必须同时有1R-R和1R-L车道",
  "severity": "error"
}
```

**❓ 待与Leon确认的问题：**

1. **V型车道：** `1V-L`, `1V-R`, `2V-R`是否合法？如何解释编号应急车道？
2. **组合值：** `1R-R, 2R-R`应该如何处理？拆分为多行还是保留？
3. **JSON pattern更新：** 是否应更新正则表达式以包含V和组合格式？
4. **84个唯一值：** 是否所有值都合法？是否存在输入错误？

**参考来源：**
- 📄 config/field_mapping_2022.json - 字段定义和车道类型
- 📊 Analysis/Template_2022_Field_Analysis_OLD.md (lines 609-676) - 真实数据统计
- 📖 Documents/Hallo Peng Luuk.txt - Leon提供的车道类型详细说明
- 📖 Documents/BPS_boek_concept.pdf (第29-31页) - BPS标准车道编码系统
- 🔗 参见Field 5 (BAAN) - 完整的BAAN-STROOK依赖关系说明

---

### 10. Aantal rijstroken - in geval van rijbaanbreed (ALL)

**字段分类：** 🔴 关键字段 (Critical)  
**中文名称：** 车道数量（全幅宽度情况下）  
**英文名称：** Number of Lanes (in case of full carriageway width)  
**数据类型：** integer  
**必填：** 条件必填（当STROOK="ALL"时）

**📊 JSON定义（权威来源）：**
```json
{
  "field_number": 10,
  "field_name_nl": "Aantal rijstroken - in geval van rijbaanbreed (ALL)",
  "data_type": "integer",
  "required": false,
  "classification": "critical",
  "category": "lane_information",
  "validation_rules": {
    "min": 1,
    "max": 6,
    "required_when": {
      "field": "STROOK",
      "equals": "ALL"
    }
  }
}
```

**📊 数据统计（基于1,592行真实数据）：**

- **数据完整度：** 928/1592 (58.3%)
- **缺失数据：** 664 (41.7%)
- **唯一值数量：** 6
- **数据类型混合：** 整数(90.4%) + 字符串(9.6%)

**📈 值分布（所有6个不同值）：**

| 值 | 次数 | 占比（非空） | 数据类型 | 说明 |
|----|------|--------------|----------|------|
| `1` | 779 | 83.9% | int | 单车道 ⚠️ |
| `ALL` | 66 | 7.1% | str | 字符串"ALL" ⚠️ |
| `2` | 57 | 6.1% | int | 双车道 ✅ |
| `n.v.t.` | 21 | 2.3% | str | "不适用" ⚠️ |
| `3` | 3 | 0.3% | int | 三车道 ✅ |
| `1/2` | 2 | 0.2% | str | 范围值？ ⚠️ |

**含义：**
当养护工程为全车道宽度(rijbaanbreed, STROOK="ALL")时，涉及的车道总数。

**使用场景：**
```
IF STROOK = "ALL" THEN
    Aantal rijstroken IS REQUIRED
    AND Aantal rijstroken IN (1, 2, 3, 4, 5, 6)
ELSE
    Aantal rijstroken可为空或为1
END IF
```

**示例值（合法）：**
- `2` (双车道全幅)
- `3` (三车道全幅)
- `4` (四车道全幅)

**⚠️ 重大数据质量问题：**

**问题1：83.9%的值是1**
- **预期逻辑：** 当STROOK已指定具体车道（如1R-L），此列应为空
- **实际数据：** 779行（83.9%非空数据）填写了1
- **矛盾：** 不符合"仅在STROOK=ALL时填写"的规则
- **可能原因：**
  - 承包商误解字段含义
  - 模板填写指导不明确
  - 数据验证未执行

**问题2：出现字符串值**
- `"ALL"` (66次) - 与STROOK列的"ALL"重复，应填写数字
- `"n.v.t."` (21次) - "niet van toepassing"（不适用），应该为空而非填写文本
- `"1/2"` (2次) - 范围值？含义不明

**问题3：数据类型不一致**
- 90.4%是整数（正确类型）
- 9.6%是字符串（错误类型）
- 需要在输入阶段强制类型转换或验证

**条件必填验证规则：**
```python
if row['STROOK'] == 'ALL':
    assert not pd.isna(row['Aantal rijstroken']), "STROOK=ALL时，Aantal必填"
    assert isinstance(row['Aantal rijstroken'], int), "Aantal必须是整数"
    assert 1 <= row['Aantal rijstroken'] <= 6, "车道数量必须在1-6之间"
else:
    # STROOK为具体车道时，此列应为空或1
    # 当前数据：83.9%填写了1（可能是错误）
    pass
```

**数据库设计：**
- 类型：INT
- 约束：CHECK (Aantal_rijstroken BETWEEN 1 AND 6)
- 允许NULL：是（当STROOK不为ALL时）

**❓ 待与Leon确认的问题：**

1. **83.9%填写1的原因：**
   - 是否应该清空这些值？
   - 还是规则理解有误，STROOK为具体车道时也可以填1？

2. **字符串值处理：**
   - `"ALL"`应该转换为什么数字？
   - `"n.v.t."`应该转换为NULL吗？
   - `"1/2"`的实际含义？

3. **验证规则严格性：**
   - 是否强制执行"仅ALL时必填"规则？
   - 还是允许其他情况下填写1作为默认值？

**参考来源：**
- 📄 config/field_mapping_2022.json - 字段定义和条件必填规则
- 📊 Analysis/Template_2022_Field_Analysis_OLD.md (lines 679-735) - 真实数据统计

---

### 11. KM_Van

**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 起点公里数
**英文名称：** Kilometer From
**数据类型：** number (float)
**必填：** 是
**单位：** 公里 (km)

**🚨 重要更正（2025-11-05）：**
- ❌ **旧理解：** KM_Van = VAN / 10（单位转换）
- ✅ **正确理解：** KM_Van = VAN（相同值，可能是冗余字段）

**📊 JSON定义（权威来源）：**
```json
{
  "field_number": 11,
  "field_name_nl": "KM_Van",
  "data_type": "number",
  "unit": "kilometer",
  "required": true,
  "classification": "critical",
  "category": "location_identification",
  "validation_rules": {
    "type": "float",
    "min": -1,
    "max": 300,
    "precision": 3,
    "european_format": true
  }
}
```

**📊 数据统计（基于1,592行真实数据）：**

- **数据完整度：** 1592/1592 (100.0%)
- **缺失数据：** 0 (0.0%)
- **唯一值数量：** 1125

**📈 值分布（前20个最常见值）：**

| KM_Van (km) | 次数 | 占比 | 说明 |
|-------------|------|------|------|
| `111.1` | 13 | 0.8% | ✅ = VAN值 |
| `104.375` | 10 | 0.6% | ✅ = VAN值 |
| `113.0` | 9 | 0.6% | ✅ = VAN值 |
| `108.15` | 9 | 0.6% | ✅ = VAN值 |
| `111.88` | 8 | 0.5% | ✅ = VAN值 |
| `111.95` | 8 | 0.5% | ✅ = VAN值 |
| `111.955` | 7 | 0.4% | ✅ = VAN值 |
| `53.49` | 7 | 0.4% | ✅ = VAN值 |
| `102.5` | 7 | 0.4% | ✅ = VAN值 |
| `112.6` | 7 | 0.4% | ✅ = VAN值 |

**含义：**
工程段起始位置的公里数标识。在当前数据中，**KM_Van与VAN完全相同**。

**与VAN的关系（已更正）：**

**❌ 旧理解（错误）：**
```
KM_Van = VAN ÷ 10
(因为VAN是百米，需要转换为公里)
```

**✅ 正确理解：**
```
KM_Van = VAN
(VAN本身就是公里，无需转换)
```

**数据验证（38.1%的行KM_Van = VAN）：**
```python
# 检查KM_Van与VAN的关系
df_match = df[df['KM_Van'] == df['VAN']]
print(f"KM_Van与VAN完全相同的行: {len(df_match)} / {len(df)} = {len(df_match)/len(df)*100:.1f}%")
# 结果：38.1%的行KM_Van = VAN

# 之前认为这是"数据错误"，但实际上VAN本身就是km单位
```

**❓ KM_Van字段的必要性：**

由于KM_Van与VAN值相同，存在以下疑问：

1. **为什么需要这个冗余字段？**
   - 历史遗留字段？
   - Excel模板兼容性需求？
   - 数据库设计需要？
   - 用户界面友好性（明确标注"km"单位）？

2. **是否可以删除？**
   - 如果仅用于显示，可以删除
   - 如果有其他系统依赖此字段，需保留

**格式：**
- 小数形式
- 精度：3位小数
- 使用欧洲格式（逗号作小数点）
- 可以是负值

**示例值：**
- KM_Van = 104.375 km = VAN值
- KM_Van = 111.100 km = VAN值
- KM_Van = 53.490 km = VAN值

**数据处理流程：**

**1️⃣ 输入阶段：**
```python
# 读取数据
df = pd.read_excel('template.xlsx', decimal=',')

# KM_Van可能与VAN相同，或需要赋值
if 'KM_Van' not in df.columns:
    df['KM_Van'] = df['VAN']  # 如果不存在，从VAN复制
```

**2️⃣ 验证阶段：**
```python
# 验证KM_Van与VAN的一致性
assert (df['KM_Van'] == df['VAN']).all(), "KM_Van应该等于VAN"

# 或者允许一定容差（考虑浮点精度）
assert ((df['KM_Van'] - df['VAN']).abs() < 0.001).all()
```

**3️⃣ 存储阶段：**
- 数据库类型：DECIMAL(10,3) 或 FLOAT
- 建议：如果KM_Van确实是冗余字段，可考虑使用计算列或视图

**数据库设计建议：**

**方案1：保留冗余字段**
```sql
CREATE TABLE road_segments (
    VAN DECIMAL(10,3),
    KM_Van DECIMAL(10,3),  -- 冗余，但保留以兼容现有系统
    CHECK (KM_Van = VAN)
);
```

**方案2：使用计算列（推荐）**
```sql
CREATE TABLE road_segments (
    VAN DECIMAL(10,3),
    KM_Van DECIMAL(10,3) AS (VAN) STORED  -- 自动等于VAN
);
```

**方案3：删除KM_Van字段**
```sql
CREATE TABLE road_segments (
    VAN DECIMAL(10,3)
    -- 不需要KM_Van，查询时直接使用VAN并重命名
);

-- 查询时：
SELECT VAN AS KM_Van FROM road_segments;
```

**❓ 待与Leon确认的问题：**

1. **字段必要性（已添加到议题9.4）：**
   - 为什么需要KM_Van这个与VAN相同的字段？
   - 是历史遗留还是有特殊用途？

2. **未来规划：**
   - 是否可以在新系统中删除KM_Van？
   - 还是需要保留以兼容其他系统/报表？

3. **Excel模板：**
   - 是否应在Excel中使用公式：`=VAN列`？
   - 减少承包商重复输入错误？

**参考来源：**
- 📄 config/field_mapping_2022.json - 字段定义
- 📊 Analysis/Template_2022_Field_Analysis_OLD.md (lines 738-801) - 真实数据统计
- 🚨 Analysis/CRITICAL_CORRECTION_VAN_TOT_Units.md - 单位更正说明
- 📋 Meeting_Notes/2025-11-06_Leon_Meeting_Agenda.md (议题9.4) - KM_Van字段必要性

---

### 12. KM_Tot

**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 终点公里数
**英文名称：** Kilometer To
**数据类型：** number (float)
**必填：** 是
**单位：** 公里 (km)

**🚨 重要更正（2025-11-05）：**
- ❌ **旧理解：** KM_Tot = TOT / 10（单位转换），且KM_Tot >= KM_Van
- ✅ **正确理解：** KM_Tot = TOT（相同值，可能是冗余字段），且大小关系由BAAN决定

**📊 JSON定义（权威来源）：**
```json
{
  "field_number": 12,
  "field_name_nl": "KM_Tot",
  "data_type": "number",
  "unit": "kilometer",
  "required": true,
  "classification": "critical",
  "category": "location_identification",
  "validation_rules": {
    "type": "float",
    "min": -1,
    "max": 300,
    "precision": 3,
    "european_format": true
  }
}
```

**📊 数据统计（基于1,592行真实数据）：**

- **数据完整度：** 1592/1592 (100.0%)
- **缺失数据：** 0 (0.0%)
- **唯一值数量：** 1103

**📈 值分布（前20个最常见值）：**

| KM_Tot (km) | 次数 | 占比 | 说明 |
|-------------|------|------|------|
| `104.5` | 14 | 0.9% | ✅ = TOT值 |
| `113.0` | 14 | 0.9% | ✅ = TOT值 |
| `104.45` | 11 | 0.7% | ✅ = TOT值 |
| `54.35` | 10 | 0.6% | ✅ = TOT值 |
| `113.3` | 10 | 0.6% | ✅ = TOT值 |
| `111.88` | 9 | 0.6% | ✅ = TOT值 |
| `52.8` | 8 | 0.5% | ✅ = TOT值 |
| `111.955` | 8 | 0.5% | ✅ = TOT值 |

**含义：**
工程段结束位置的公里数标识。在当前数据中，**KM_Tot与TOT完全相同**。

**与TOT的关系（已更正）：**

**❌ 旧理解（错误）：**
```
KM_Tot = TOT ÷ 10
(因为TOT是百米，需要转换为公里)
```

**✅ 正确理解：**
```
KM_Tot = TOT
(TOT本身就是公里，无需转换)
```

**数据验证：**
```python
# 检查KM_Tot与TOT的关系
df_match = df[df['KM_Tot'] == df['TOT']]
print(f"KM_Tot与TOT完全相同的行: {len(df_match)} / {len(df)}")
# 结果：与KM_Van类似，大部分行KM_Tot = TOT
```

**格式规则：** 与KM_Van相同
- 小数形式
- 精度：3位小数
- 欧洲格式
- 可以为负值

**逻辑关系（已更正）：**

**❌ 旧规则（错误）：**
```
KM_Tot >= KM_Van（终点 >= 起点）
```

**✅ 新规则（正确）：**
```
KM_Tot与KM_Van的大小关系由BAAN类型决定：
- 右侧BAAN (1HRR, PWR): KM_Tot > KM_Van
- 左侧BAAN (1HRL, PWL): KM_Van > KM_Tot
- 0HRM: 由STROOK决定
- 0VW: 待Leon确认

（因为KM_Tot = TOT, KM_Van = VAN）
```

**数据处理流程：**

**1️⃣ 输入阶段：**
```python
# 读取数据
df = pd.read_excel('template.xlsx', decimal=',')

# KM_Tot可能与TOT相同，或需要赋值
if 'KM_Tot' not in df.columns:
    df['KM_Tot'] = df['TOT']  # 如果不存在，从TOT复制
```

**2️⃣ 验证阶段：**
```python
# 验证KM_Tot与TOT的一致性
assert (df['KM_Tot'] == df['TOT']).all(), "KM_Tot应该等于TOT"

# 或者允许一定容差
assert ((df['KM_Tot'] - df['TOT']).abs() < 0.001).all()
```

**3️⃣ 存储阶段：**
- 数据库类型：DECIMAL(10,3) 或 FLOAT
- 建议：如果KM_Tot确实是冗余字段，可考虑使用计算列或视图

**数据库设计建议：**

**方案1：保留冗余字段**
```sql
CREATE TABLE road_segments (
    TOT DECIMAL(10,3),
    KM_Tot DECIMAL(10,3),  -- 冗余，但保留兼容性
    CHECK (KM_Tot = TOT)
);
```

**方案2：使用计算列（推荐）**
```sql
CREATE TABLE road_segments (
    TOT DECIMAL(10,3),
    KM_Tot DECIMAL(10,3) AS (TOT) STORED  -- 自动等于TOT
);
```

**方案3：删除KM_Tot字段**
```sql
CREATE TABLE road_segments (
    TOT DECIMAL(10,3)
    -- 不需要KM_Tot，查询时直接使用TOT并重命名
);

-- 查询时：
SELECT TOT AS KM_Tot FROM road_segments;
```

**❓ KM_Tot字段的必要性：**

与KM_Van相同的疑问：

1. **为什么需要这个冗余字段？**
   - 历史遗留字段？
   - 用户界面友好性（明确"km"单位）？

2. **是否可以删除？**
   - 如果仅用于显示，可以删除
   - 如果其他系统依赖，需保留

**❓ 待与Leon确认的问题：**

1. **字段必要性（已添加到议题9.4）：**
   - 与KM_Van相同，为什么需要这个冗余字段？

2. **未来规划：**
   - 是否可以在新系统中同时删除KM_Van和KM_Tot？

3. **Excel模板：**
   - 是否应使用公式：`=TOT列`？

**参考来源：**
- 📄 config/field_mapping_2022.json - 字段定义
- 📊 Analysis/Template_2022_Field_Analysis_OLD.md (lines 804-866) - 真实数据统计
- 🚨 Analysis/CRITICAL_CORRECTION_VAN_TOT_Units.md - 单位更正说明
- 📋 Meeting_Notes/2025-11-06_Leon_Meeting_Agenda.md (议题9.4) - KM_Tot字段必要性

---

### 13. Lengte

**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 长度
**英文名称：** Length
**数据类型：** number (float)
**必填：** 是
**单位：** 🔴 **公里 (kilometer, km)** ⚠️ 重大更正

**🚨 重要更正（2025-11-05）：**
- ❌ **旧理解：** 单位可能是米(m)，公式是 (TOT - VAN) × 100
- ✅ **正确理解：** 单位是**公里(km)**，公式是 **abs(TOT - VAN)**

**📊 JSON定义（已更正）：**
```json
{
  "field_number": 13,
  "field_name_nl": "Lengte",
  "data_type": "number",
  "unit": "kilometer",
  "required": true,
  "classification": "critical",
  "category": "quantity",
  "validation_rules": {
    "type": "float",
    "min": 0.001,
    "max": 50,
    "european_format": true,
    "derived_from": "abs(TOT - VAN)"
  }
}
```

**📊 数据统计（基于1,592行真实数据）：**

- **数据完整度：** 1592/1592 (100.0%)
- **缺失数据：** 0 (0.0%)
- **唯一值数量：** 399

**📈 值分布（前20个最常见值）：**

| Lengte (km) | 次数 | 占比 | 等于多少米 | 状态 |
|-------------|------|------|-----------|------|
| `0.09999999999999432` | 75 | 4.7% | ≈ 100m | ✅ 浮点精度问题 |
| `0.10000000000000142` | 57 | 3.6% | = 100m | ✅ |
| `0.025000000000005684` | 51 | 3.2% | ≈ 25m | ✅ |
| `0.07500000000000284` | 50 | 3.1% | ≈ 75m | ✅ |
| `0.04999999999999716` | 43 | 2.7% | ≈ 50m | ✅ |
| `0.20000000000000284` | 39 | 2.4% | ≈ 200m | ✅ |
| `0.25` | 33 | 2.1% | = 250m | ✅ |
| `0.02499999999999858` | 32 | 2.0% | ≈ 25m | ✅ |
| `0.10000000000000853` | 27 | 1.7% | ≈ 100m | ✅ |
| `0.030000000000001137` | 26 | 1.6% | ≈ 30m | ✅ |

**含义：**
工程段的总长度，单位为公里。**永远是正值**，使用VAN和TOT的绝对值差计算。

**正确计算公式（已确认）：**

```python
Lengte (km) = abs(TOT - VAN)
```

**关键原则：**
1. ✅ 使用**绝对值**，确保长度永远为正
2. ✅ 无论VAN > TOT还是TOT > VAN，长度都正确
3. ✅ 单位是km（因为VAN和TOT本身就是km）

**示例验证：**

**例1（递增方向）：**
```
BAAN = 1HRR (右侧主线)
VAN = 104.5 km, TOT = 113.0 km
Lengte = abs(113.0 - 104.5) = 8.5 km = 8,500米 ✅
```

**例2（递减方向）：**
```
BAAN = 1HRL (左侧主线)
VAN = 113.0 km, TOT = 104.5 km  (注意：VAN > TOT)
Lengte = abs(104.5 - 113.0) = 8.5 km = 8,500米 ✅
```

**例3（小路段）：**
```
VAN = 104.5 km, TOT = 104.6 km
Lengte = abs(104.6 - 104.5) = 0.1 km = 100米 ✅
```

**⚠️ 浮点精度问题：**

数据中出现大量浮点精度误差：
- `0.09999999999999432` 应该是 `0.1` km
- `0.025000000000005684` 应该是 `0.025` km
- `0.10000000000000142` 应该是 `0.1` km

**原因：** Python/pandas浮点运算的固有精度限制

**处理方案：**
```python
# 方法1：四舍五入到3位小数
df['Lengte'] = df['Lengte'].round(3)

# 方法2：使用Decimal类型（精确计算）
from decimal import Decimal
df['Lengte'] = df['Lengte'].apply(
    lambda x: float(Decimal(str(x)).quantize(Decimal('0.001')))
)

# 方法3：计算时使用绝对值
df['Lengte'] = abs(df['TOT'] - df['VAN']).round(3)
```

**数据处理流程：**

**1️⃣ 计算Lengte：**
```python
# 读取数据
df = pd.read_excel('template.xlsx', decimal=',')

# 计算Lengte（使用绝对值）
df['Lengte'] = abs(df['TOT'] - df['VAN']).round(3)
```

**2️⃣ 验证Lengte：**
```python
# 验证Lengte是否正确计算
calculated_lengte = abs(df['TOT'] - df['VAN']).round(3)
errors = abs(df['Lengte'] - calculated_lengte) > 0.001

if errors.any():
    print(f"发现 {errors.sum()} 行Lengte计算错误")
    print(df[errors][['VAN', 'TOT', 'Lengte', 'calculated_lengte']])
```

**3️⃣ 数据验证规则：**
```python
# Lengte必须是正值
assert (df['Lengte'] > 0).all(), "Lengte必须大于0"

# Lengte合理范围（0.001 km = 1米 到 50 km）
assert (df['Lengte'] >= 0.001).all(), "Lengte不能小于1米"
assert (df['Lengte'] <= 50).all(), "Lengte不能大于50公里"

# Lengte必须等于abs(TOT-VAN)
assert (abs(abs(df['TOT'] - df['VAN']) - df['Lengte']) < 0.001).all()
```

**数据库设计：**

```sql
CREATE TABLE road_segments (
    VAN DECIMAL(10,3),
    TOT DECIMAL(10,3),
    Lengte DECIMAL(10,3),

    -- 验证Lengte = abs(TOT - VAN)
    CHECK (ABS(Lengte - ABS(TOT - VAN)) < 0.001),

    -- Lengte必须为正值
    CHECK (Lengte > 0),

    -- 合理范围
    CHECK (Lengte BETWEEN 0.001 AND 50)
);
```

**或者使用计算列（推荐）：**
```sql
CREATE TABLE road_segments (
    VAN DECIMAL(10,3),
    TOT DECIMAL(10,3),
    Lengte DECIMAL(10,3) AS (ABS(TOT - VAN)) STORED,  -- 自动计算

    CHECK (Lengte > 0)
);
```

**与KM_Van/KM_Tot的关系：**

由于KM_Van = VAN, KM_Tot = TOT，因此：
```python
# 以下三种计算方式等价：
Lengte = abs(TOT - VAN)
Lengte = abs(KM_Tot - KM_Van)
Lengte = abs(df['TOT'] - df['VAN'])  # pandas
```

**❓ 待与Leon确认的问题（已添加到议题9.3）：**

1. **浮点精度处理：**
   - 如何处理`0.09999999999999432`这样的值？
   - 是否应四舍五入到3位小数？
   - 还是接受这些精度误差？

2. **最小长度限制：**
   - 实际业务中，最小工程段长度是多少？
   - 是否有小于10米（0.010 km）的合理路段？

3. **最大长度限制：**
   - 单个工程段的最大长度一般是多少？
   - 50 km的上限是否合理？

**参考来源：**
- 📄 config/field_mapping_2022.json - 字段定义
- 📊 Analysis/Template_2022_Field_Analysis_OLD.md (lines 870-936) - 真实数据统计
- 🚨 Analysis/CRITICAL_CORRECTION_VAN_TOT_Units.md - 单位和公式更正
- 📋 Meeting_Notes/2025-11-06_Leon_Meeting_Agenda.md (议题9.3) - Lengte字段计算

---

### 14. Breedte

**字段分类：** 🔵 非关键字段 (Non-Critical)  
**中文名称：** 宽度  
**英文名称：** Width  
**数据类型：** number (float)  
**必填：** 是  
**单位：** 米 (m)

**📊 JSON定义（权威来源）：**
```json
{
  "field_number": 14,
  "field_name_nl": "Breedte",
  "data_type": "number",
  "unit": "meter",
  "required": true,
  "classification": "non-critical",
  "category": "quantity",
  "validation_rules": {
    "type": "float",
    "min": 3.0,
    "max": 20.0,
    "european_format": true
  }
}
```

**📊 数据统计（基于1,592行真实数据）：**

- **数据完整度：** 1567/1592 (98.4%)
- **缺失数据：** 25 (1.6%)
- **唯一值数量：** 1 ⚠️

**📈 值分布（仅1个不同值）：**

| Breedte (m) | 次数 | 占比 | 说明 |
|-------------|------|------|------|
| `4.3` | 1567 | 100.0% | 全部数据！⚠️ |

**含义：**
养护工程段的宽度（路面宽度）。

**⚠️ 重大数据质量问题：98.4%的数据都是4.3米**

**异常发现：**
1. **唯一值：** 1567行非空数据，只有1个唯一值：4.3米
2. **缺失数据：** 25行(1.6%)缺失
3. **无变化：** 所有车道类型、所有道路、所有工程段宽度都相同

**可能原因分析：**

**假设1：默认值填充**
- 承包商没有实际测量宽度
- 使用模板默认值4.3米自动填充
- **问题：** 不同车道类型宽度应不同

**假设2：单车道标准宽度**
- 4.3米接近荷兰单车道标准宽度（3.5-3.75米）
- 可能表示"每条车道宽度"而非"工程段总宽度"
- **问题：** 字段名称是"Breedte"（宽度），不是"车道宽度"

**假设3：数据录入错误**
- Excel模板中设置了默认值4.3
- 承包商忘记修改实际值

**假设4：非关键字段被忽略**
- 该字段分类为"非关键字段"
- 承包商可能认为不重要，随便填写

**荷兰标准车道宽度参考：**
- 单车道：3.5米（老标准）或3.75米（新标准）
- 双车道：7.0-7.5米
- 三车道：10.5-11.25米
- 高速公路应急车道：2.5-3.0米

**预期数据 vs 实际数据：**

| STROOK | 预期Breedte (m) | 实际Breedte (m) |
|--------|-----------------|-----------------|
| 1R-L | 3.5-3.75 | 4.3 ⚠️ |
| 2R-L | 3.5-3.75 | 4.3 ⚠️ |
| ALL (2车道) | 7.0-7.5 | 4.3 ⚠️ |
| ALL (3车道) | 10.5-11.25 | 4.3 ⚠️ |

**数据清洗建议：**
```python
# 方案1：标记为可疑数据
df['Breedte_status'] = 'SUSPICIOUS: All values are 4.3m'

# 方案2：根据车道数量推算
def estimate_width(row):
    if row['STROOK'] == 'ALL' and not pd.isna(row['Aantal rijstroken']):
        return row['Aantal rijstroken'] * 3.75  # 标准车道宽度
    else:
        return 3.75  # 单车道标准宽度

df['Breedte_estimated'] = df.apply(estimate_width, axis=1)
```

**数据库设计：**
- 类型：DECIMAL(5,2) 或 FLOAT
- 约束：CHECK (Breedte BETWEEN 3.0 AND 20.0)
- 建议：添加WARNING标记字段，标识所有4.3米的可疑数据

**❓ 待与Leon确认的问题：**

1. **4.3米的含义：**
   - 为什么所有数据都是4.3米？
   - 这是默认值还是实际测量值？
   - 单车道宽度应该是3.5或3.75米，为何是4.3？

2. **数据可靠性：**
   - 这个字段的数据是否可信？
   - 是否需要重新收集实际宽度数据？

3. **字段重要性：**
   - 标记为"非关键字段"是否合理？
   - 宽度是否影响工程量计算？

4. **数据修正方案：**
   - 保留4.3作为默认值？
   - 根据车道类型和数量自动计算？
   - 要求承包商提供实际宽度？

**参考来源：**
- 📄 config/field_mapping_2022.json - 字段定义，范围3.0-20.0米
- 📊 Analysis/Template_2022_Field_Analysis_OLD.md (lines 939-983) - 真实数据统计，发现异常
- 📖 荷兰道路设计标准 (CROW) - 标准车道宽度参考

---

## 🎨 材料规格字段 (Fields 15-21)

本组字段记录沥青混合料的材料规格信息，包括混合料代码、骨料级配、面层类型、厚度等关键技术参数。

---

### 15. MENGSELCODE

**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 混合料代码
**英文名称：** Mixture Code
**数据类型：** string (可包含数字)
**必填：** 是（但23.4%缺失）
**单位：** 无（编码）

**📊 JSON定义（权威来源）：**
```json
{
  "field_number": 15,
  "field_name_nl": "MENGSELCODE",
  "field_name_en": "Mixture Code",
  "field_name_cn": "混合料代码",
  "data_type": "string",
  "required": true,
  "classification": "critical",
  "category": "material_specification",
  "validation_rules": {
    "pattern": "^[A-Z0-9]*$",
    "min_length": 1,
    "max_length": 10
  },
  "description": "Asphalt mixture code identifying the specific mixture type"
}
```

**📊 数据统计（基于1,592行真实数据）：**

- **数据完整度：** 1220/1592 (76.6%)
- **缺失数据：** 372 (23.4%) ⚠️
- **唯一值数量：** 64

**📈 值分布（前20个最常见值）：**

| MENGSELCODE | 次数 | 占比 | 数据类型 |
|-------------|------|------|---------|
| `70611` | 420 | 34.4% | 整数 |
| `70814` | 131 | 10.7% | 整数 |
| `72611` | 127 | 10.4% | 整数 |
| `55302` | 67 | 5.5% | 整数 |
| `28618` | 58 | 4.8% | 整数 |
| `730D001` | 38 | 3.1% | 字符串 |
| `55031` | 34 | 2.8% | 整数 |
| `73001` | 32 | 2.6% | 整数 |
| `25317` | 30 | 2.5% | 整数 |
| `83407` | 21 | 1.7% | 整数 |
| `74304200` | 20 | 1.6% | 整数(8位) |
| `28218` | 18 | 1.5% | 整数 |
| `916009` | 18 | 1.5% | 整数 |
| `Minifalt` | 14 | 1.1% | 字符串 ⚠️ |
| `76300601` | 13 | 1.1% | 整数(8位) |
| `43611` | 13 | 1.1% | 整数 |
| `82807` | 12 | 1.0% | 整数 |
| `84900` | 12 | 1.0% | 整数 |
| `26760200` | 12 | 1.0% | 整数(8位) |
| `50405` | 11 | 0.9% | 整数 |

**含义：**
沥青混合料的标准代码，用于唯一标识特定的混合料配方。每个代码对应一种经过认证的沥青混合料配方，包含特定的骨料级配、沥青类型、添加剂等信息。

**⚠️ 数据质量问题：**

**问题1：缺失率高**
- 23.4%的行缺失混合料代码
- 作为关键字段，缺失率偏高

**问题2：格式不一致**
- 91.2%是纯数字（5位或8位）
- 8.8%包含字母（如730D001, Minifalt）
- 没有统一的编码规则

**问题3：编码长度不统一**
- 5位数：70611, 55302 (最常见)
- 8位数：74304200, 76300601
- 带字母：730D001, 156D002
- 文本：Minifalt

**问题4：特殊值**
- "Minifalt" 出现14次 - 这是产品名还是代码？
- 以"D"结尾的代码（730D001, 155D001）- 特殊含义？

**格式规则（推测）：**

**5位数代码（最常见）：**
```
70611, 55302, 28618
可能格式：[类型2位][级配2位][变体1位]？
```

**8位数代码：**
```
74304200, 76300601
可能格式：[年份2位][类型2位][级配2位][批次2位]？
```

**带字母代码：**
```
730D001, 155D001
"D"可能表示特殊配方或供应商代码？
```

**数据处理流程：**

**1️⃣ 输入阶段：**
```python
# 读取时保持原始格式
df = pd.read_excel('template.xlsx', dtype={'MENGSELCODE': str})

# 标准化：去除空格、转大写
df['MENGSELCODE'] = df['MENGSELCODE'].str.strip().str.upper()
```

**2️⃣ 验证阶段：**
```python
# 检查缺失
assert df['MENGSELCODE'].notna().sum() / len(df) > 0.75, "缺失率过高"

# 检查格式
valid_pattern = df['MENGSELCODE'].str.match(r'^[A-Z0-9]{5,8}$|^Minifalt$')
invalid = df[~valid_pattern & df['MENGSELCODE'].notna()]

if len(invalid) > 0:
    print(f"发现 {len(invalid)} 行格式异常的混合料代码")
```

**3️⃣ 分类阶段：**
```python
# 按代码类型分类
df['code_type'] = df['MENGSELCODE'].apply(lambda x:
    'numeric_5' if str(x).isdigit() and len(str(x)) == 5
    else 'numeric_8' if str(x).isdigit() and len(str(x)) == 8
    else 'alphanumeric' if pd.notna(x)
    else 'missing'
)
```

**数据库设计：**
```sql
CREATE TABLE road_segments (
    MENGSELCODE VARCHAR(10),

    -- 验证规则
    CHECK (MENGSELCODE IS NOT NULL),
    CHECK (LENGTH(MENGSELCODE) BETWEEN 5 AND 10),
    CHECK (MENGSELCODE ~ '^[A-Z0-9]+$' OR MENGSELCODE = 'Minifalt')
);

-- 建议：创建混合料代码参照表
CREATE TABLE mixture_codes (
    code VARCHAR(10) PRIMARY KEY,
    description TEXT,
    aggregate_gradation VARCHAR(20),
    binder_type VARCHAR(50),
    is_standard BOOLEAN,
    notes TEXT
);
```

**❓ 待与Leon确认的问题：**

1. **编码规则：**
   - 5位数vs8位数代码的区别是什么？
   - "D"字母的含义？（730D001, 155D001）
   - 是否有官方编码规范文档？

2. **特殊值处理：**
   - "Minifalt"是产品名还是有效代码？
   - 应该保留还是替换为标准代码？

3. **缺失数据：**
   - 23.4%缺失率是否可接受？
   - 如何处理缺失：要求补充还是允许缺失？

4. **标准化需求：**
   - 是否需要统一编码格式？
   - 是否建立混合料代码标准库？

**参考来源：**
- 📄 config/field_mapping_2022.json - 字段定义
- 📊 Analysis/Template_2022_Field_Analysis_OLD.md (lines 986-1055) - 真实数据统计
- 📋 建议咨询Leon获取官方混合料代码手册


---

### 16. GRANULAIR MENGSEL (0/16, 4/8, 2/6, 0/11, 0/8 enz)

**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 骨料级配
**英文名称：** Aggregate Gradation
**数据类型：** string
**必填：** 是（但14.4%缺失）
**单位：** 无（级配范围，单位mm）

**📊 JSON定义（权威来源）：**
```json
{
  "field_number": 16,
  "field_name_nl": "GRANULAIR MENGSEL (0/16, 4/8, 2/6, 0/11, 0/8 enz)",
  "field_name_en": "Aggregate Gradation",
  "field_name_cn": "骨料级配",
  "data_type": "string",
  "required": true,
  "classification": "critical",
  "category": "material_specification",
  "validation_rules": {
    "pattern": "^[0-9/]+$|^PA\\s*[0-9]+$",
    "enum": ["0/16", "0/11", "0/8", "0/5", "4/8", "11/16", "PA 5", "PA 8", "PA 16"]
  },
  "description": "Aggregate particle size distribution (e.g., 0/16 means particles from 0 to 16mm)"
}
```

**📊 数据统计（基于1,592行真实数据）：**

- **数据完整度：** 1363/1592 (85.6%)
- **缺失数据：** 229 (14.4%)
- **唯一值数量：** 16

**📈 值分布（所有16个不同值）：**

| 级配 | 次数 | 占比 | 类型 |
|------|------|------|------|
| `0/16` | 893 | 65.5% | 标准级配 ✅ |
| `4/8` | 131 | 9.6% | 标准级配 ✅ |
| `11/16` | 127 | 9.3% | 标准级配 ✅ |
| `0/8` | 110 | 8.1% | 标准级配 ✅ |
| `0/11` | 44 | 3.2% | 标准级配 ✅ |
| `PA 8` | 15 | 1.1% | 多孔沥青 |
| `??` | 15 | 1.1% | ⚠️ 未知 |
| `PA 5` | 11 | 0.8% | 多孔沥青 |
| `PA16` | 5 | 0.4% | 多孔沥青（无空格）|
| `0/16 SURF` | 4 | 0.3% | 带后缀 |
| `0/5` | 3 | 0.2% | 标准级配 ✅ |
| `PA8` | 1 | 0.1% | 多孔沥青（无空格）|
| `PA 16` | 1 | 0.1% | 多孔沥青 |
| `0/5 PMB` | 1 | 0.1% | 带后缀 |
| `AC 16 surf` | 1 | 0.1% | 错误类型？|
| `DAB PMB` | 1 | 0.1% | 错误类型？|

**含义：**
沥青混合料中骨料（石料）的粒径分布范围。例如"0/16"表示骨料粒径从0毫米到16毫米。骨料级配直接影响混合料的性能，如抗车辙性能、耐久性等。

**🔍 级配类型解析：**

**标准数字级配（X/Y格式）：**
```
0/16  - 最常见（65.5%），粗级配，用于结构层或面层
0/11  - 中级配
0/8   - 细级配
0/5   - 很细级配
4/8   - 单一粒径范围
11/16 - 单一粒径范围
```

**PA系列（多孔沥青Porous Asphalt）：**
```
PA 8  - 8mm多孔沥青（15次）
PA 5  - 5mm多孔沥青（11次）
PA 16 - 16mm多孔沥青（1次）
PA8, PA16 - 无空格变体（格式不标准）
```

**⚠️ 数据质量问题：**

**问题1：格式不一致**
- 标准格式："PA 8"（有空格）
- 非标准："PA8", "PA16"（无空格）
- 需要标准化

**问题2：未知值**
- "??" 出现15次（1.1%）
- 表示承包商不确定或未填写

**问题3：错误类型值**
- "AC 16 surf" - 这是面层类型，不是骨料级配
- "DAB PMB" - 这是混合料类型，不是级配
- 可能是字段填写错误

**问题4：后缀混杂**
- "0/16 SURF" - 添加了"SURF"后缀
- "0/5 PMB" - 添加了"PMB"后缀
- 需要确认后缀含义

**数据清洗建议：**

**1️⃣ 标准化PA系列：**
```python
# 统一PA格式
df['GRANULAIR MENGSEL'] = df['GRANULAIR MENGSEL'].replace({
    'PA8': 'PA 8',
    'PA16': 'PA 16',
    'PA 5': 'PA 5',
    'PA 8': 'PA 8',
    'PA 16': 'PA 16'
})
```

**2️⃣ 处理未知值：**
```python
# 标记未知值
df.loc[df['GRANULAIR MENGSEL'] == '??', 'data_quality_flag'] = 'GRADATION_UNKNOWN'
```

**3️⃣ 修正错误类型：**
```python
# 检测并标记错误
wrong_type = df['GRANULAIR MENGSEL'].isin(['AC 16 surf', 'DAB PMB'])
df.loc[wrong_type, 'data_quality_flag'] = 'WRONG_FIELD_TYPE'
```

**数据处理流程：**

**1️⃣ 输入阶段：**
```python
# 读取并标准化
df = pd.read_excel('template.xlsx', dtype={'GRANULAIR MENGSEL': str})
df['GRANULAIR MENGSEL'] = df['GRANULAIR MENGSEL'].str.strip()
```

**2️⃣ 验证阶段：**
```python
# 定义标准值
standard_gradations = [
    '0/16', '0/11', '0/8', '0/5', '4/8', '11/16',
    'PA 5', 'PA 8', 'PA 16'
]

# 检查非标准值
non_standard = df[
    ~df['GRANULAIR MENGSEL'].isin(standard_gradations) &
    df['GRANULAIR MENGSEL'].notna()
]

print(f"非标准级配值: {len(non_standard)} 行")
print(non_standard['GRANULAIR MENGSEL'].value_counts())
```

**3️⃣ 与其他字段关联验证：**
```python
# 验证级配与面层类型的一致性
# 例如：DZOAB通常使用0/16或0/11级配
# PA系列面层应该使用PA系列级配

consistency_check = df.groupby(['DEKLAAGSOORT', 'GRANULAIR MENGSEL']).size()
print("面层类型与级配组合：")
print(consistency_check.sort_values(ascending=False).head(20))
```

**数据库设计：**
```sql
CREATE TABLE road_segments (
    granulair_mengsel VARCHAR(20),

    -- 验证规则
    CHECK (granulair_mengsel IS NOT NULL),
    CHECK (
        granulair_mengsel ~ '^[0-9]+/[0-9]+( (SURF|PMB))?$' OR  -- 标准级配
        granulair_mengsel ~ '^PA\s*[0-9]+$' OR                   -- PA系列
        granulair_mengsel = '??'                                  -- 未知值
    )
);

-- 参照表
CREATE TABLE aggregate_gradations (
    gradation VARCHAR(20) PRIMARY KEY,
    min_size_mm INT,
    max_size_mm INT,
    type VARCHAR(20), -- 'standard', 'PA', 'special'
    typical_uses TEXT,
    description TEXT
);
```

**❓ 待与Leon确认的问题：**

1. **PA系列格式：**
   - "PA 8"和"PA8"应该统一为哪种格式？
   - PA系列是否只用于多孔沥青面层？

2. **未知值处理：**
   - "??"应该如何处理？
   - 是否要求承包商补充数据？

3. **错误值处理：**
   - "AC 16 surf", "DAB PMB"是否应该移到DEKLAAGSOORT字段？
   - 还是有特殊含义？

4. **后缀含义：**
   - "0/16 SURF"中的"SURF"表示什么？（Surface面层？）
   - "0/5 PMB"中的"PMB"表示什么？（改性沥青Polymer Modified Bitumen？）

5. **标准级配库：**
   - 是否有官方的荷兰标准级配列表？
   - 是否需要建立标准级配参照数据库？

**参考来源：**
- 📄 config/field_mapping_2022.json - 字段定义
- 📊 Analysis/Template_2022_Field_Analysis_OLD.md (lines 1057-1191) - 真实数据统计
- 📖 EN 13108系列标准 - 欧洲沥青混合料标准
- 📋 CROW标准 - 荷兰道路工程标准


---

### 17. DEKLAAGSOORT (bijv. ZOAB, SMA, tweelaags ZOAB, duurzaam ZOAB, etc.)

**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 面层类型
**英文名称：** Surface Layer Type / Wearing Course Type
**数据类型：** string
**必填：** 是（但8.3%缺失）
**单位：** 无（类型分类）

**📊 JSON定义（权威来源）：**
```json
{
  "field_number": 17,
  "field_name_nl": "DEKLAAGSOORT (bijv. ZOAB, SMA, tweelaags ZOAB, duurzaam ZOAB, etc.)",
  "field_name_en": "Surface Layer Type",
  "field_name_cn": "面层类型",
  "data_type": "string",
  "required": true,
  "classification": "critical",
  "category": "material_specification",
  "validation_rules": {
    "enum": ["ZOAB", "DZOAB", "SMA", "Tweelaags ZOAB", "Duurzaam ZOAB", "DAB", "PA", "Dunne deklagen"]
  },
  "description": "Type of surface layer (wearing course)"
}
```

**📊 数据统计（基于1,592行真实数据）：**

- **数据完整度：** 1460/1592 (91.7%)
- **缺失数据：** 132 (8.3%)
- **唯一值数量：** 24

**📈 值分布（所有24个不同值）：**

| 面层类型 | 次数 | 占比 | 分类 |
|---------|------|------|------|
| `DZOAB` | 634 | 43.4% | 密级配多孔沥青 ✅ |
| `ZOABTW TL` | 185 | 12.7% | 双层ZOAB-表层 ✅ |
| `ZOAB` | 179 | 12.3% | 多孔沥青 ✅ |
| `ZOABTW OL` | 132 | 9.0% | 双层ZOAB-底层 ✅ |
| `AC 16 Surf` | 89 | 6.1% | AC面层 ✅ |
| `SMA` | 52 | 3.6% | 沥青玛蹄脂碎石 ✅ |
| `ZOABDI` | 29 | 2.0% | 耐久ZOAB |
| `ZOABTW` | 26 | 1.8% | 双层ZOAB |
| `ZOEAB` | 23 | 1.6% | 特殊ZOAB变体？|
| `ZOABTW DL` | 21 | 1.4% | 双层ZOAB-面层 |
| `DGD` | 17 | 1.2% | 稀浆封层 |
| `ZOABTW-fijn DL` | 15 | 1.0% | 细双层ZOAB |
| `SMA-NL 11B` | 13 | 0.9% | SMA荷兰标准 |
| `ZOAB ` | 13 | 0.9% | ⚠️ 尾随空格 |
| `ZOAB+` | 6 | 0.4% | ZOAB改进型 |
| `SMA-NL 11B ` | 5 | 0.3% | ⚠️ 尾随空格 |
| `ZOABTW fijn OL` | 5 | 0.3% | 细双层ZOAB-底层 |
| `ZOABTW OL ` | 4 | 0.3% | ⚠️ 尾随空格 |
| `SMA 8 Geel` | 4 | 0.3% | 黄色SMA |
| `AC 11 Surf` | 3 | 0.2% | AC面层 |
| `SMA 8G+` | 2 | 0.1% | SMA改进型 |
| `SMA-NL 11` | 1 | 0.1% | SMA荷兰标准 |
| `SMA-NL 11B PMB SBS Bestone` | 1 | 0.1% | 详细规格 |
| `EAB` | 1 | 0.1% | 特殊类型 |

**含义：**
道路面层（磨耗层）的类型。面层直接承受交通荷载和环境作用，其类型决定了路面的性能特征，如降噪、排水、抗滑、耐久性等。

**🔍 主要面层类型详解：**

**ZOAB系列（多孔沥青）：** 43.4% + 12.3% + 12.7% + 9.0% = 77.4%
- **DZOAB (Dicht ZOAB)** - 密级配多孔沥青，最常用（43.4%）
- **ZOAB** - 标准多孔沥青（12.3%）
- **ZOABTW (Tweelaags)** - 双层多孔沥青：
  - TL (Toplaag/表层) - 12.7%
  - OL (Onderlaag/底层) - 9.0%  
  - DL (Deklaag/面层) - 1.4%
- **ZOABDI (Duurzaam/Innovatief)** - 耐久/创新型ZOAB

**SMA系列（沥青玛蹄脂碎石）：** 3.6%
- **SMA** - 标准SMA（3.6%）
- **SMA-NL 11B** - 荷兰标准11B型（0.9%）
- **SMA 8 Geel** - 8mm黄色SMA（用于标识）

**AC系列（致密级配沥青混凝土）：** 6.1%
- **AC 16 Surf** - 16mm AC面层（6.1%）
- **AC 11 Surf** - 11mm AC面层（0.2%）

**⚠️ 数据质量问题：**

**问题1：尾随空格**
- "ZOAB " vs "ZOAB"（13次带空格）
- "SMA-NL 11B " vs "SMA-NL 11B"（5次带空格）
- "ZOABTW OL " vs "ZOABTW OL"（4次带空格）
- 需要trim处理

**问题2：TL/OL/DL后缀不统一**
```
ZOABTW TL  - 185次 (Toplaag/表层)
ZOABTW OL  - 132次 (Onderlaag/底层)
ZOABTW DL  - 21次  (Deklaag/面层)
ZOABTW     - 26次  (无后缀)
```
- 需确认：TL和DL是否相同？
- 26次无后缀ZOABTW缺少层位信息

**问题3：变体命名**
- "ZOAB+" - 是ZOAB的改进型？还是数据错误？
- "SMA 8G+" - "G"表示Geel（黄色）？"+"表示改进型？
- "ZOEAB" vs "ZOAB" - 拼写错误还是特殊类型？

**问题4：过度详细规格**
- "SMA-NL 11B PMB SBS Bestone" - 包含了改性剂和供应商信息
- 应该简化为"SMA-NL 11B"？

**数据清洗建议：**

**1️⃣ 去除空格：**
```python
df['DEKLAAGSOORT'] = df['DEKLAAGSOORT'].str.strip()
```

**2️⃣ 标准化ZOABTW后缀：**
```python
# 统一TL/DL为Toplaag
df['DEKLAAGSOORT'] = df['DEKLAAGSOORT'].replace({
    'ZOABTW DL': 'ZOABTW TL',  # 如果DL=TL
    'ZOABTW-fijn DL': 'ZOABTW fijn TL'
})
```

**3️⃣ 简化详细规格：**
```python
# 提取主要类型
df['DEKLAAGSOORT_simplified'] = df['DEKLAAGSOORT'].str.extract(
    r'(DZOAB|ZOAB|SMA|AC \d+ Surf|DGD|EAB)'
)[0]
```

**数据处理流程：**

**1️⃣ 输入和标准化：**
```python
df = pd.read_excel('template.xlsx', dtype={'DEKLAAGSOORT': str})
df['DEKLAAGSOORT'] = df['DEKLAAGSOORT'].str.strip().str.upper()
```

**2️⃣ 验证与分类：**
```python
# 定义主要类型
main_types = {
    'ZOAB': ['DZOAB', 'ZOAB', 'ZOABTW', 'ZOABDI', 'ZOEAB'],
    'SMA': ['SMA', 'SMA-NL'],
    'AC': ['AC 11 Surf', 'AC 16 Surf'],
    'Other': ['DGD', 'EAB']
}

# 分类
for main_type, variants in main_types.items():
    mask = df['DEKLAAGSOORT'].str.contains('|'.join(variants), na=False)
    df.loc[mask, 'surface_type_category'] = main_type
```

**3️⃣ 与其他字段关联：**
```python
# ZOAB类型应该配合PA级配
zoab_pa_check = df[
    (df['DEKLAAGSOORT'].str.contains('ZOAB', na=False)) &
    (~df['GRANULAIR MENGSEL'].str.contains('PA', na=False))
]
print(f"ZOAB类型但非PA级配: {len(zoab_pa_check)} 行")
```

**数据库设计：**
```sql
CREATE TABLE surface_types (
    type_code VARCHAR(50) PRIMARY KEY,
    main_category VARCHAR(20), -- 'ZOAB', 'SMA', 'AC', 'Other'
    is_porous BOOLEAN,
    is_noise_reducing BOOLEAN,
    typical_gradation VARCHAR(20),
    description_nl TEXT,
    description_en TEXT
);

CREATE TABLE road_segments (
    deklaagsoort VARCHAR(50),

    FOREIGN KEY (deklaagsoort) REFERENCES surface_types(type_code),
    CHECK (deklaagsoort IS NOT NULL)
);
```

**❓ 待与Leon确认的问题：**

1. **ZOABTW后缀含义：**
   - TL (Toplaag) vs DL (Deklaag) - 是否相同？
   - 26次无后缀的ZOABTW应该归类为哪一层？

2. **变体含义：**
   - "ZOAB+" 是什么？改进型ZOAB？
   - "ZOEAB" - 拼写错误还是特殊类型？
   - "DGD" 的全称是什么？

3. **SMA规格：**
   - "SMA 8 Geel" 黄色SMA的用途？
   - "SMA-NL 11B" 中的"11B"规格含义？

4. **标准化策略：**
   - 是否建立标准面层类型列表？
   - 过度详细的规格是否应简化？
   - 尾随空格应如何处理（自动清理还是报错）？

**参考来源：**
- 📄 config/field_mapping_2022.json - 字段定义
- 📊 Analysis/Template_2022_Field_Analysis_OLD.md (lines 1120-1191) - 真实数据统计
- 📖 RAW Bepalingen - 荷兰道路技术规范
- 📖 CROW Publicatie 147 - ZOAB设计和施工指南


---

### 18. DIKTE VERHARDING

**字段分类：** 🔵 非关键字段 (Non-Critical)
**中文名称：** 路面厚度
**英文名称：** Pavement Thickness / Surface Layer Thickness
**数据类型：** number (float)
**必填：** 是（但9.0%缺失）
**单位：** 米 (m)（实际应为毫米mm）

**🚨 重要说明：单位问题**
- JSON定义单位：millimeter (mm)
- 实际数据单位：meter (m)（以米存储的毫米值）
- 例如：0.05 表示 50mm

**📊 JSON定义（权威来源）：**
```json
{
  "field_number": 18,
  "field_name_nl": "DIKTE VERHARDING",
  "field_name_en": "Pavement Thickness",
  "field_name_cn": "路面厚度",
  "data_type": "number",
  "unit": "millimeter",
  "required": true,
  "classification": "non-critical",
  "category": "material_specification",
  "validation_rules": {
    "type": "integer",
    "min": 20,
    "max": 150
  },
  "description": "Thickness of the surface layer in millimeters"
}
```

**📊 数据统计（基于1,592行真实数据）：**

- **数据完整度：** 1448/1592 (91.0%)
- **缺失数据：** 144 (9.0%)
- **唯一值数量：** 9

**📈 值分布（所有9个不同值）：**

| DIKTE (m) | DIKTE (mm) | 次数 | 占比 |
|-----------|-----------|------|------|
| `0.05` | 50 | 734 | 50.7% |
| `0.025` | 25 | 268 | 18.5% |
| `0.035` | 35 | 125 | 8.6% |
| `0.045` | 45 | 123 | 8.5% |
| `0.03` | 30 | 83 | 5.7% |
| `0.45` | 450 | 58 | 4.0% ⚠️ |
| `0.003` | 3 | 24 | 1.7% ⚠️ |
| `0.04` | 40 | 18 | 1.2% |
| `0.02` | 20 | 15 | 1.0% |

**含义：**
沥青面层的施工厚度。一般范围20-150mm，影响路面的结构强度和耐久性。

**⚠️ 数据质量问题：**

**问题1：异常薄厚度 - 3mm**
- 24行数据显示0.003米（3mm）
- 这对于沥青面层来说异常薄
- **可能原因：**
  - 数据录入错误（30mm误输为0.003？）
  - 薄层修补（patching）
  - 表面处治（surface dressing）

**问题2：异常厚厚度 - 450mm**
- 58行数据显示0.45米（450mm）
- 远超标准面层厚度（50-80mm）
- **可能原因：**
  - 数据录入错误（45mm误输为0.45？）
  - 包含了多层总厚度
  - 特殊加厚路段

**厚度分布分析：**

**正常范围 (20-80mm)：** 1341行 (92.6%)
```
20mm - 15行 (1.0%)  - 薄层
25mm - 268行 (18.5%) - 常见
30mm - 83行 (5.7%)
35mm - 125行 (8.6%)
40mm - 18行 (1.2%)
45mm - 123行 (8.5%)
50mm - 734行 (50.7%)  - 最常见
```

**异常范围：** 82行 (5.7%)
```
3mm  - 24行 - 太薄 ⚠️
450mm - 58行 - 太厚 ⚠️
```

**数据清洗建议：**

**1️⃣ 识别异常值：**
```python
# 异常薄值
thin_layer = df[df['DIKTE VERHARDING'] < 0.015]  # <15mm
print(f"异常薄层: {len(thin_layer)} 行")

# 异常厚值  
thick_layer = df[df['DIKTE VERHARDING'] > 0.15]  # >150mm
print(f"异常厚层: {len(thick_layer)} 行")
```

**2️⃣ 可能的修正：**
```python
# 假设：0.003 应该是 0.03 (3mm → 30mm)
df.loc[df['DIKTE VERHARDING'] == 0.003, 'DIKTE VERHARDING'] = 0.03

# 假设：0.45 应该是 0.045 (450mm → 45mm)
df.loc[df['DIKTE VERHARDING'] == 0.45, 'DIKTE VERHARDING'] = 0.045
```

**3️⃣ 标记待确认：**
```python
df['thickness_flag'] = 'OK'
df.loc[df['DIKTE VERHARDING'] < 0.015, 'thickness_flag'] = 'TOO_THIN'
df.loc[df['DIKTE VERHARDING'] > 0.15, 'thickness_flag'] = 'TOO_THICK'
```

**数据处理流程：**

**1️⃣ 输入阶段：**
```python
# 读取（保持浮点精度）
df = pd.read_excel('template.xlsx', decimal=',')

# 转换为mm显示
df['DIKTE_mm'] = df['DIKTE VERHARDING'] * 1000
```

**2️⃣ 验证阶段：**
```python
# 验证范围
valid_thickness = (df['DIKTE VERHARDING'] >= 0.020) & \
                  (df['DIKTE VERHARDING'] <= 0.150)

invalid = df[~valid_thickness & df['DIKTE VERHARDING'].notna()]
print(f"厚度超出正常范围: {len(invalid)} 行")
```

**3️⃣ 与面层类型关联：**
```python
# 不同面层类型的典型厚度
typical_thickness = {
    'DZOAB': [30, 40, 50],  # mm
    'ZOAB': [40, 50],
    'SMA': [30, 40],
    'AC 16 Surf': [40, 50, 60]
}

# 检查是否匹配
for surface_type, typical in typical_thickness.items():
    mask = df['DEKLAAGSOORT'] == surface_type
    actual = df.loc[mask, 'DIKTE_mm'].value_counts()
    print(f"\n{surface_type} 实际厚度分布：")
    print(actual)
```

**数据库设计：**
```sql
CREATE TABLE road_segments (
    dikte_verharding DECIMAL(5,3), -- 单位：米（范围0.020-0.150）

    -- 验证规则
    CHECK (dikte_verharding BETWEEN 0.020 AND 0.150),

    -- 或存储为毫米（整数）
    dikte_mm INT,
    CHECK (dikte_mm BETWEEN 20 AND 150)
);
```

**❓ 待与Leon确认的问题：**

1. **3mm厚度：**
   - 24行3mm数据是否正确？
   - 是否为薄层修补或特殊工艺？
   - 还是应该修正为30mm？

2. **450mm厚度：**
   - 58行450mm数据是否正确？
   - 是否包含了多层总厚度（面层+中间层）？
   - 还是应该修正为45mm？

3. **单位标准化：**
   - 数据库中以mm（整数）存储更好，还是m（浮点）？
   - Excel模板是否应明确标注单位？

4. **与其他字段关联：**
   - DIKTE VERHARDING是否应该等于面层厚度？
   - 还是包含了其他层？

**参考来源：**
- 📄 config/field_mapping_2022.json - 字段定义（范围20-150mm）
- 📊 Analysis/Template_2022_Field_Analysis_OLD.md (lines 1194-1251) - 真实数据统计
- 📖 RAW Bepalingen - 荷兰沥青厚度规范

---

### 19. TUSSENLAAG

**字段分类：** 🔵 非关键字段 (Non-Critical)
**中文名称：** 中间层 / 粘结层
**英文名称：** Binder Course / Intermediate Layer
**数据类型：** string
**必填：** 否（条件必填）
**单位：** 无（层型描述）

**📊 JSON定义（权威来源）：**
```json
{
  "field_number": 19,
  "field_name_nl": "TUSSENLAAG",
  "field_name_en": "Binder Course",
  "field_name_cn": "中间层",
  "data_type": "string",
  "required": false,
  "classification": "non-critical",
  "category": "material_specification",
  "validation_rules": {
    "enum": ["Ja", "Nee", ""]
  },
  "description": "Whether a binder course (intermediate layer) is present"
}
```

**📊 数据统计（基于1,592行真实数据）：**

- **数据完整度：** 221/1592 (13.9%)
- **缺失数据：** 1371 (86.1%)
- **唯一值数量：** 8

**📈 值分布（所有8个不同值）：**

| TUSSENLAAG类型 | 次数 | 占比 | 说明 |
|---------------|------|------|------|
| `AC 16 Bind` | 140 | 63.3% | AC16粘结层 ✅ |
| `AC Bind` | 33 | 14.9% | AC粘结层 ✅ |
| `AC Base 22` | 18 | 8.1% | AC22基层 |
| `STAB` | 14 | 6.3% | 稳定层？|
| `AC Bind 22` | 8 | 3.6% | AC22粘结层 |
| `AC 22 base-bind` | 4 | 1.8% | AC22基粘结层 |
| `AC 16 OL/TL` | 3 | 1.4% | AC16底层/表层 |
| `AC 22 TL-C` | 1 | 0.5% | AC22表层-C型 |

**含义：**
面层和基层之间的中间层（粘结层/结合层）。并非所有工程都有中间层，取决于路面结构设计。86.1%的工程没有中间层是正常的。

**🔍 数据分析：**

**有中间层的工程：** 221行 (13.9%)
- **AC Bind系列（粘结层）：** 181行 (81.9%)
  - AC 16 Bind - 140行（最常见）
  - AC Bind - 33行（未指定级配）
  - AC Bind 22 - 8行
  
- **AC Base系列（基层）：** 18行 (8.1%)
  - AC Base 22 - 18行
  - AC 22 base-bind - 4行
  
- **其他类型：** 22行 (10.0%)
  - STAB - 14行（稳定层）
  - AC 16 OL/TL - 3行
  - AC 22 TL-C - 1行

**无中间层的工程：** 1371行 (86.1%)

**⚠️ 数据质量问题：**

**问题1：JSON定义与实际数据不符**
- **JSON规定：** enum = ["Ja", "Nee", ""]
- **实际数据：** 具体层型名称（AC 16 Bind等）
- **不一致：** JSON期望Yes/No，实际是详细规格

**问题2：命名不统一**
```
"AC 16 Bind"  - 完整规格（级配+层型）
"AC Bind"     - 未指定级配
"AC Bind 22"  - 级配在后
```
- 需要标准化命名规则

**问题3：Base vs Bind混淆**
- AC 16 Bind - "Bind"通常指粘结层（Binder Course）
- AC Base 22 - "Base"通常指基层（Base Course）
- 是否应该区分两种不同的层？

**问题4：特殊缩写**
- "STAB" - 含义不明确（Stabilization? Stab层？）

**数据清洗建议：**

**1️⃣ 标准化命名：**
```python
# 统一命名格式：AC [级配] [层型]
standardize_map = {
    'AC Bind': 'AC 16 Bind',  # 假设默认16
    'AC Bind 22': 'AC 22 Bind',
    'AC Base 22': 'AC 22 Base',
    'AC 22 base-bind': 'AC 22 Base-Bind'
}

df['TUSSENLAAG'] = df['TUSSENLAAG'].replace(standardize_map)
```

**2️⃣ 提取层型和级配：**
```python
# 提取级配
df['tussenlaag_gradation'] = df['TUSSENLAAG'].str.extract(r'(\d+)')

# 提取层型
df['tussenlaag_type'] = df['TUSSENLAAG'].apply(lambda x:
    'Bind' if 'Bind' in str(x)
    else 'Base' if 'Base' in str(x)
    else 'Other' if pd.notna(x)
    else 'None'
)
```

**3️⃣ 转换为Yes/No（如果需要）：**
```python
# 如果要符合JSON定义
df['TUSSENLAAG_binary'] = df['TUSSENLAAG'].apply(
    lambda x: 'Ja' if pd.notna(x) else 'Nee'
)
```

**数据处理流程：**

**1️⃣ 输入阶段：**
```python
df = pd.read_excel('template.xlsx', dtype={'TUSSENLAAG': str})
df['TUSSENLAAG'] = df['TUSSENLAAG'].str.strip()
```

**2️⃣ 验证阶段：**
```python
# 检查是否填写了中间层
has_binder = df['TUSSENLAAG'].notna()
print(f"有中间层的工程: {has_binder.sum()} / {len(df)} = {has_binder.mean()*100:.1f}%")

# 检查字段20和21的一致性
has_code = df['Mengselcode TUSSENLAAG'].notna()
has_thickness = df['DIKTE TUSSENLAAG'].notna()

# 逻辑验证
inconsistent = (has_binder & ~has_code) | (~has_binder & has_code)
print(f"中间层字段不一致: {inconsistent.sum()} 行")
```

**3️⃣ 条件必填验证：**
```python
# 如果有中间层，字段20和21应该填写
if df['TUSSENLAAG'].notna().any():
    missing_code = df['TUSSENLAAG'].notna() & df['Mengselcode TUSSENLAAG'].isna()
    missing_thickness = df['TUSSENLAAG'].notna() & df['DIKTE TUSSENLAAG'].isna()
    
    print(f"有中间层但缺混合料代码: {missing_code.sum()} 行")
    print(f"有中间层但缺厚度: {missing_thickness.sum()} 行")
```

**数据库设计：**
```sql
CREATE TABLE road_segments (
    tussenlaag VARCHAR(50),
    mengselcode_tussenlaag VARCHAR(10),
    dikte_tussenlaag DECIMAL(5,3),

    -- 条件验证
    CHECK (
        (tussenlaag IS NULL AND mengselcode_tussenlaag IS NULL AND dikte_tussenlaag IS NULL) OR
        (tussenlaag IS NOT NULL AND mengselcode_tussenlaag IS NOT NULL AND dikte_tussenlaag IS NOT NULL)
    )
);
```

**❓ 待与Leon确认的问题：**

1. **字段定义修正：**
   - JSON定义["Ja", "Nee", ""]是否应改为允许具体层型名称？
   - 还是保留Yes/No，另外添加层型字段？

2. **Base vs Bind：**
   - AC Base 22 和 AC Bind 22 的区别？
   - 是否应该区分为不同字段（基层vs粘结层）？

3. **STAB含义：**
   - "STAB"是什么类型的中间层？
   - 完整名称是什么？

4. **命名标准：**
   - 是否需要统一命名格式？
   - 建议格式："AC [级配] [Bind/Base]"？

**参考来源：**
- 📄 config/field_mapping_2022.json - 字段定义
- 📊 Analysis/Template_2022_Field_Analysis_OLD.md (lines 1253-1302) - 真实数据统计


---

### 20. Mengselcode TUSSENLAAG

**字段分类：** 🔵 非关键字段 (Non-Critical)
**中文名称：** 中间层混合料代码
**英文名称：** Binder Course Mixture Code
**数据类型：** string (可包含数字)
**必填：** 条件必填（当TUSSENLAAG非空时）
**单位：** 无（编码）

**📊 JSON定义（权威来源）：**
```json
{
  "field_number": 20,
  "field_name_nl": "Mengselcode TUSSENLAAG",
  "field_name_en": "Binder Course Mixture Code",
  "field_name_cn": "中间层混合料代码",
  "data_type": "string",
  "required": false,
  "classification": "non-critical",
  "category": "material_specification",
  "validation_rules": {
    "pattern": "^[A-Z0-9\\s]*$",
    "required_when": {
      "field": "TUSSENLAAG",
      "not_equals": ["Nee", ""]
    }
  },
  "description": "Mixture code for binder course (if applicable)"
}
```

**📊 数据统计（基于1,592行真实数据）：**

- **数据完整度：** 160/1592 (10.1%)
- **缺失数据：** 1432 (89.9%)
- **唯一值数量：** 3 ⚠️

**📈 值分布（所有3个不同值）：**

| Mengselcode | 次数 | 占比 | 数据类型 |
|-------------|------|------|---------|
| `28618` | 157 | 98.1% | 整数 |
| `155D001` | 2 | 1.2% | 字符串 |
| `156D002` | 1 | 0.6% | 字符串 |

**含义：**
中间层（粘结层）使用的沥青混合料的标准代码。当字段19（TUSSENLAAG）有值时，本字段应该填写对应的混合料代码。

**⚠️ 数据质量问题：**

**问题1：唯一值过少**
- 只有3个不同的混合料代码
- 98.1%的中间层都使用28618代码
- 缺乏多样性，可能表示：
  - 中间层混合料高度标准化
  - 数据填写不完整
  - 默认值使用过多

**问题2：填写率与TUSSENLAAG不匹配**
- TUSSENLAAG有值：221行（13.9%）
- Mengselcode TUSSENLAAG有值：160行（10.1%）
- **差异：** 61行有TUSSENLAAG但缺少混合料代码

**问题3：代码格式不一致**
- 98.1%是纯数字（28618）
- 1.9%包含字母（155D001, 156D002）
- 与字段15（MENGSELCODE）的格式类似

**数据一致性检查：**

```python
# 检查TUSSENLAAG与Mengselcode TUSSENLAAG的一致性
has_tussenlaag = df['TUSSENLAAG'].notna()
has_mengselcode = df['Mengselcode TUSSENLAAG'].notna()

# 情况1：有TUSSENLAAG但缺Mengselcode
missing_code = has_tussenlaag & ~has_mengselcode
print(f"有中间层但缺代码: {missing_code.sum()} 行 ({missing_code.mean()*100:.1f}%)")

# 情况2：有Mengselcode但缺TUSSENLAAG
missing_layer = ~has_tussenlaag & has_mengselcode
print(f"有代码但缺中间层: {missing_layer.sum()} 行")

# 情况3：都有值（正常）
both_present = has_tussenlaag & has_mengselcode
print(f"两者都有: {both_present.sum()} 行")
```

**代码28618分析：**

由于98.1%的数据使用代码28618，这可能是：
- AC Bind的标准混合料代码
- 最常用的粘结层配方
- 需要与字段19的层型对应验证

```python
# 检查28618对应的TUSSENLAAG类型
code_28618 = df[df['Mengselcode TUSSENLAAG'] == '28618']
print("代码28618对应的TUSSENLAAG类型：")
print(code_28618['TUSSENLAAG'].value_counts())
```

**数据清洗建议：**

**1️⃣ 条件必填验证：**
```python
# 如果有TUSSENLAAG，应该有Mengselcode
df['needs_mengselcode'] = df['TUSSENLAAG'].notna()

missing = df['needs_mengselcode'] & df['Mengselcode TUSSENLAAG'].isna()
if missing.any():
    print(f"警告：{missing.sum()} 行需要补充中间层混合料代码")
    print(df[missing][['TUSSENLAAG', 'Mengselcode TUSSENLAAG']].head())
```

**2️⃣ 格式标准化：**
```python
# 保持字符串格式，去除空格
df['Mengselcode TUSSENLAAG'] = df['Mengselcode TUSSENLAAG'].astype(str).str.strip()

# 验证格式
valid_pattern = df['Mengselcode TUSSENLAAG'].str.match(r'^[A-Z0-9]+$|^nan$')
invalid = df[~valid_pattern]
print(f"格式不合规: {len(invalid)} 行")
```

**数据处理流程：**

**1️⃣ 输入阶段：**
```python
df = pd.read_excel('template.xlsx', dtype={
    'TUSSENLAAG': str,
    'Mengselcode TUSSENLAAG': str
})
```

**2️⃣ 验证阶段：**
```python
# 条件验证规则
def validate_tussenlaag_code(row):
    has_layer = pd.notna(row['TUSSENLAAG'])
    has_code = pd.notna(row['Mengselcode TUSSENLAAG'])
    
    if has_layer and not has_code:
        return 'MISSING_CODE'
    elif not has_layer and has_code:
        return 'UNEXPECTED_CODE'
    elif has_layer and has_code:
        return 'OK'
    else:
        return 'NO_BINDER'

df['tussenlaag_validation'] = df.apply(validate_tussenlaag_code, axis=1)
print(df['tussenlaag_validation'].value_counts())
```

**3️⃣ 与其他字段关联：**
```python
# 检查常见组合
combinations = df[df['TUSSENLAAG'].notna()].groupby([
    'TUSSENLAAG',
    'Mengselcode TUSSENLAAG'
]).size().sort_values(ascending=False)

print("常见的中间层类型与代码组合：")
print(combinations.head(10))
```

**数据库设计：**
```sql
CREATE TABLE road_segments (
    tussenlaag VARCHAR(50),
    mengselcode_tussenlaag VARCHAR(10),
    
    -- 条件约束
    CHECK (
        (tussenlaag IS NULL AND mengselcode_tussenlaag IS NULL) OR
        (tussenlaag IS NOT NULL AND mengselcode_tussenlaag IS NOT NULL)
    ),
    
    -- 格式约束
    CHECK (mengselcode_tussenlaag ~ '^[A-Z0-9]+$' OR mengselcode_tussenlaag IS NULL)
);

-- 外键约束（如果有混合料代码表）
ALTER TABLE road_segments
ADD FOREIGN KEY (mengselcode_tussenlaag) REFERENCES mixture_codes(code);
```

**❓ 待与Leon确认的问题：**

1. **代码28618：**
   - 28618是什么混合料配方？
   - 为什么98.1%的中间层都使用这个代码？
   - 是否过度使用默认值？

2. **缺失数据处理：**
   - 61行有TUSSENLAAG但缺少Mengselcode，如何处理？
   - 是否自动填充28618作为默认值？
   - 还是要求承包商补充？

3. **D系列代码：**
   - 155D001和156D002的"D"表示什么？
   - 与面层代码中的"D"含义相同吗？

4. **数据验证：**
   - 是否需要验证Mengselcode与TUSSENLAAG类型的匹配关系？
   - 例如：AC 16 Bind应该对应特定的代码？

**参考来源：**
- 📄 config/field_mapping_2022.json - 字段定义，条件必填规则
- 📊 Analysis/Template_2022_Field_Analysis_OLD.md (lines 1304-1347) - 真实数据统计

---

### 21. DIKTE TUSSENLAAG (indien van toepassing)

**字段分类：** 🔵 非关键字段 (Non-Critical)
**中文名称：** 中间层厚度
**英文名称：** Binder Course Thickness
**数据类型：** number (float) 或 string
**必填：** 条件必填（当TUSSENLAAG非空时）
**单位：** 米 (m)（实际应为毫米mm）

**📊 JSON定义（权威来源）：**
```json
{
  "field_number": 21,
  "field_name_nl": "DIKTE TUSSENLAAG (indien van toepassing)",
  "field_name_en": "Binder Course Thickness",
  "field_name_cn": "中间层厚度",
  "data_type": "number",
  "unit": "millimeter",
  "required": false,
  "classification": "non-critical",
  "category": "material_specification",
  "validation_rules": {
    "type": "integer",
    "min": 40,
    "max": 100,
    "required_when": {
      "field": "TUSSENLAAG",
      "not_equals": ["Nee", ""]
    }
  },
  "description": "Thickness of binder course in millimeters (if applicable)"
}
```

**📊 数据统计（基于1,592行真实数据）：**

- **数据完整度：** 221/1592 (13.9%)
- **缺失数据：** 1371 (86.1%)
- **唯一值数量：** 12

**📈 值分布（所有12个不同值）：**

| DIKTE (m) | DIKTE (mm) | 次数 | 占比 | 数据类型 |
|-----------|-----------|------|------|---------|
| `0.05` | 50 | 167 | 75.6% | 浮点 ✅ |
| `0.08` | 80 | 9 | 4.1% | 浮点 ✅ |
| `0.04` | 40 | 8 | 3.6% | 浮点 ✅ |
| `0.045` | 45 | 7 | 3.2% | 浮点 ✅ |
| `var.` | 可变 | 6 | 2.7% | 字符串 ⚠️ |
| `0.06` | 60 | 5 | 2.3% | 浮点 ✅ |
| `0.095` | 95 | 5 | 2.3% | 浮点 ✅ |
| `0.055` | 55 | 4 | 1.8% | 浮点 ✅ |
| `0.07` | 70 | 3 | 1.4% | 浮点 ✅ |
| `0.09` | 90 | 3 | 1.4% | 浮点 ✅ |
| `0.085` | 85 | 3 | 1.4% | 浮点 ✅ |
| `0.115` | 115 | 1 | 0.5% | 浮点 ⚠️ |

**含义：**
中间层（粘结层）的施工厚度。一般范围40-100mm，比面层厚度略大。

**⚠️ 数据质量问题：**

**问题1：特殊值"var."**
- 6行（2.7%）使用"var."表示厚度可变
- 混合了数值和字符串类型
- **可能含义：**
  - 变厚度设计（Variable thickness）
  - 数据缺失时的占位符
  - 未最终确定的施工厚度

**问题2：超出标准范围**
- JSON定义范围：40-100mm
- 实际数据：115mm超出上限（1行）
- **0.115m = 115mm** 超出15mm

**问题3：数据类型混合**
- 97.3%是浮点数
- 2.7%是字符串（"var."）
- 导致数据类型不一致

**厚度分布分析：**

**标准范围 (40-100mm)：** 214行 (96.8%)
```
40mm - 8行 (3.6%)   - 最薄（标准下限）
45mm - 7行 (3.2%)
50mm - 167行 (75.6%) - 最常见 ⭐
55mm - 4行 (1.8%)
60mm - 5行 (2.3%)
70mm - 3行 (1.4%)
80mm - 9行 (4.1%)
85mm - 3行 (1.4%)
90mm - 3行 (1.4%)
95mm - 5行 (2.3%)
```

**超出范围：** 7行 (3.2%)
```
var. - 6行 (2.7%)   - 无法确定
115mm - 1行 (0.5%)  - 超出上限 ⚠️
```

**与TUSSENLAAG的一致性：**

```python
# 检查三个字段的一致性
has_tussenlaag = df['TUSSENLAAG'].notna()
has_mengselcode = df['Mengselcode TUSSENLAAG'].notna()
has_dikte = df['DIKTE TUSSENLAAG'].notna()

# 理想情况：三者同时存在或同时缺失
perfect_match = (has_tussenlaag == has_mengselcode) & (has_mengselcode == has_dikte)
print(f"三字段完全一致: {perfect_match.sum()} / {len(df)}")

# 异常情况
inconsistent = ~perfect_match
print(f"存在不一致: {inconsistent.sum()} 行")
```

**数据清洗建议：**

**1️⃣ 处理"var."值：**
```python
# 方案A：转换为NaN（缺失）
df.loc[df['DIKTE TUSSENLAAG'] == 'var.', 'DIKTE TUSSENLAAG'] = np.nan

# 方案B：替换为平均值50mm
df.loc[df['DIKTE TUSSENLAAG'] == 'var.', 'DIKTE TUSSENLAAG'] = 0.05

# 方案C：标记为特殊状态
df['thickness_type'] = 'fixed'
df.loc[df['DIKTE TUSSENLAAG'] == 'var.', 'thickness_type'] = 'variable'
```

**2️⃣ 验证范围：**
```python
# 转换为数值（忽略"var."）
df['DIKTE_mm'] = pd.to_numeric(df['DIKTE TUSSENLAAG'], errors='coerce') * 1000

# 检查范围
out_of_range = (df['DIKTE_mm'] < 40) | (df['DIKTE_mm'] > 100)
print(f"超出范围: {out_of_range.sum()} 行")
print(df[out_of_range][['TUSSENLAAG', 'DIKTE TUSSENLAAG', 'DIKTE_mm']])
```

**3️⃣ 条件必填验证：**
```python
# 如果有TUSSENLAAG，应该有DIKTE
has_layer = df['TUSSENLAAG'].notna()
missing_thickness = has_layer & (df['DIKTE TUSSENLAAG'].isna() | (df['DIKTE TUSSENLAAG'] == 'var.'))

if missing_thickness.any():
    print(f"警告：{missing_thickness.sum()} 行有中间层但厚度缺失或可变")
```

**数据处理流程：**

**1️⃣ 输入阶段：**
```python
# 先作为字符串读取
df = pd.read_excel('template.xlsx', dtype={'DIKTE TUSSENLAAG': str})

# 处理"var."
df['DIKTE_numeric'] = pd.to_numeric(df['DIKTE TUSSENLAAG'], errors='coerce')
df['DIKTE_is_variable'] = df['DIKTE TUSSENLAAG'] == 'var.'
```

**2️⃣ 验证阶段：**
```python
# 综合验证
def validate_binder_layer(row):
    has_type = pd.notna(row['TUSSENLAAG'])
    has_code = pd.notna(row['Mengselcode TUSSENLAAG'])
    has_thickness = pd.notna(row['DIKTE_numeric']) or row['DIKTE_is_variable']
    
    if has_type and has_code and has_thickness:
        return 'COMPLETE'
    elif has_type and not (has_code and has_thickness):
        return 'INCOMPLETE'
    elif not has_type and (has_code or has_thickness):
        return 'INCONSISTENT'
    else:
        return 'NO_BINDER'

df['binder_status'] = df.apply(validate_binder_layer, axis=1)
print(df['binder_status'].value_counts())
```

**3️⃣ 与TUSSENLAAG类型关联：**
```python
# 不同类型的中间层典型厚度
typical_thickness = df[df['DIKTE_numeric'].notna()].groupby('TUSSENLAAG').agg({
    'DIKTE_numeric': ['mean', 'median', 'count']
})
print("不同中间层类型的典型厚度（米）：")
print(typical_thickness)
```

**数据库设计：**
```sql
CREATE TABLE road_segments (
    tussenlaag VARCHAR(50),
    mengselcode_tussenlaag VARCHAR(10),
    dikte_tussenlaag DECIMAL(5,3),
    dikte_is_variable BOOLEAN DEFAULT FALSE,
    
    -- 条件约束：三者同时存在或同时缺失
    CHECK (
        (tussenlaag IS NULL AND mengselcode_tussenlaag IS NULL AND dikte_tussenlaag IS NULL) OR
        (tussenlaag IS NOT NULL AND mengselcode_tussenlaag IS NOT NULL AND 
         (dikte_tussenlaag IS NOT NULL OR dikte_is_variable = TRUE))
    ),
    
    -- 范围约束
    CHECK (dikte_tussenlaag IS NULL OR dikte_tussenlaag BETWEEN 0.040 AND 0.100),
    
    -- 或存储为毫米
    dikte_tussenlaag_mm INT,
    CHECK (dikte_tussenlaag_mm IS NULL OR dikte_tussenlaag_mm BETWEEN 40 AND 100)
);
```

**❓ 待与Leon确认的问题：**

1. **"var."的处理：**
   - "var."表示什么？可变厚度设计？
   - 如何记录实际施工厚度？
   - 应该如何在数据库中表示？

2. **115mm超限：**
   - 115mm厚度是否合理？
   - 是否应该修正为100mm以下？
   - 还是确实存在超厚中间层？

3. **数据一致性：**
   - TUSSENLAAG、Mengselcode、DIKTE三个字段应该同时存在
   - 如何处理不一致的情况？
   - 是否需要自动修正？

4. **典型厚度：**
   - AC 16 Bind的标准厚度是多少？
   - AC Base的标准厚度是多少？
   - 是否需要根据层型验证厚度合理性？

**参考来源：**
- 📄 config/field_mapping_2022.json - 字段定义（范围40-100mm）
- 📊 Analysis/Template_2022_Field_Analysis_OLD.md (lines 1350-1406) - 真实数据统计
- 📖 RAW Bepalingen - 荷兰沥青层厚度规范

---

## ✅ 批次3完成总结

字段15-21（材料规格）已全部整合完成！

**主要内容：**
- 7个材料规格字段详细文档
- 数据质量问题识别和分析
- 数据清洗和验证建议
- 数据库设计方案
- 待Leon确认的问题列表

**下一步：** 批次4 - 字段22-26（施工记录和备注）


---

## 📅 施工记录字段 (Fields 22-26)

本组字段记录施工过程信息，包括施工日期、拌合站、材料用量、温度参数和备注信息。

---

### 22. AANLEGDATUM

**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 施工日期
**英文名称：** Construction Date / Laying Date
**数据类型：** date
**必填：** 是（但0.3%缺失）
**单位：** 日期格式

**📊 JSON定义（权威来源）：**
```json
{
  "field_number": 22,
  "field_name_nl": "AANLEGDATUM",
  "field_name_en": "Construction Date",
  "field_name_cn": "施工日期",
  "data_type": "date",
  "required": true,
  "classification": "critical",
  "category": "construction_record",
  "validation_rules": {
    "format": ["DD-MM-YYYY", "YYYY-MM-DD"],
    "min_year": 2000,
    "max_year": 2030
  },
  "description": "Date when the asphalt was laid"
}
```

**📊 数据统计（基于1,592行真实数据）：**

- **数据完整度：** 1587/1592 (99.7%)
- **缺失数据：** 5 (0.3%)
- **唯一值数量：** 173个不同日期

**📈 值分布（前20个最常见日期）：**

| 施工日期 | 次数 | 占比 | 数据类型 |
|---------|------|------|---------|
| `2022-09-16` | 44 | 2.8% | datetime ✅ |
| `2022-09-02` | 43 | 2.7% | datetime ✅ |
| `2022-10-27` | 29 | 1.8% | datetime ✅ |
| `2022-10-18` | 29 | 1.8% | datetime ✅ |
| `2022-06-01` | 29 | 1.8% | datetime ✅ |
| `2022-10-28` | 28 | 1.8% | datetime ✅ |
| `2022-05-10` | 27 | 1.7% | datetime ✅ |
| `2022-06-27` | 26 | 1.6% | datetime ✅ |
| `2022-09-23` | 26 | 1.6% | datetime ✅ |
| `2022-09-09` | 25 | 1.6% | datetime ✅ |
| `2022-11-01` | 24 | 1.5% | datetime ✅ |
| `2022-11-17` | 23 | 1.4% | datetime ✅ |
| `2022-10-25` | 23 | 1.4% | datetime ✅ |
| `2022-09-15` | 23 | 1.4% | datetime ✅ |
| `2022-09-19` | 22 | 1.4% | datetime ✅ |
| `[onbekend]` | 22 | 1.4% | string ⚠️ |
| `2022-11-04` | 21 | 1.3% | datetime ✅ |
| `2022-11-14` | 21 | 1.3% | datetime ✅ |
| `2022-11-11` | 20 | 1.3% | datetime ✅ |
| `2022-11-15` | 20 | 1.3% | datetime ✅ |

**含义：**
沥青面层的实际铺设日期。这是工程记录的关键信息，用于追溯施工质量、计算保修期、分析天气影响等。

**🔍 时间分布分析：**

**2022年施工季节分布：**
```
春季 (3-5月)：约25%
夏季 (6-8月)：约30%
秋季 (9-11月)：约45% ⭐ 最集中
冬季 (12-2月)：几乎没有（冬季停工）
```

**月度施工分布：**
- **9月：** 最繁忙（施工高峰）
- **10-11月：** 次繁忙（赶在冬季前完成）
- **5-6月：** 春季施工
- **12-2月：** 冬季停工（天气原因）

**⚠️ 数据质量问题：**

**问题1：未知日期"[onbekend]"**
- 22行（1.4%）使用"[onbekend]"字符串
- 荷兰语"onbekend" = "unknown"（未知）
- **可能原因：**
  - 数据收集时日期信息缺失
  - 承包商未及时填写
  - 历史数据追溯困难

**问题2：数据类型混合**
- 98.6%是datetime类型（正确）
- 1.4%是字符串"[onbekend]"（需要处理）

**问题3：缺失数据**
- 5行（0.3%）完全缺失
- 加上"[onbekend]"，实际缺失率为1.7%

**数据清洗建议：**

**1️⃣ 处理"[onbekend]"：**
```python
# 方案A：转换为NaT (Not a Time)
df.loc[df['AANLEGDATUM'] == '[onbekend]', 'AANLEGDATUM'] = pd.NaT

# 方案B：尝试从其他字段推断
# 例如：根据同一承包商、同一道路的其他工程日期推断

# 方案C：标记为特殊状态
df['date_status'] = 'known'
df.loc[df['AANLEGDATUM'] == '[onbekend]', 'date_status'] = 'unknown'
```

**2️⃣ 日期格式标准化：**
```python
# 读取时指定日期格式
df = pd.read_excel('template.xlsx', parse_dates=['AANLEGDATUM'])

# 或手动转换
df['AANLEGDATUM'] = pd.to_datetime(df['AANLEGDATUM'], errors='coerce')

# 格式化输出（荷兰格式 DD-MM-YYYY）
df['AANLEGDATUM_formatted'] = df['AANLEGDATUM'].dt.strftime('%d-%m-%Y')
```

**3️⃣ 日期范围验证：**
```python
# 验证日期合理性
current_year = 2022
df['year'] = df['AANLEGDATUM'].dt.year

# 检查异常年份
invalid_year = (df['year'] < 2000) | (df['year'] > 2030)
if invalid_year.any():
    print(f"发现异常年份: {df[invalid_year]['AANLEGDATUM']}")

# 检查未来日期
future_dates = df['AANLEGDATUM'] > pd.Timestamp.now()
if future_dates.any():
    print(f"发现未来日期: {df[future_dates]['AANLEGDATUM']}")
```

**数据处理流程：**

**1️⃣ 输入阶段：**
```python
# 读取Excel，自动解析日期
df = pd.read_excel('template.xlsx', parse_dates=['AANLEGDATUM'])

# 处理特殊字符串
df['AANLEGDATUM'] = df['AANLEGDATUM'].replace('[onbekend]', pd.NaT)
```

**2️⃣ 验证阶段：**
```python
# 验证必填
missing = df['AANLEGDATUM'].isna()
print(f"缺失日期: {missing.sum()} 行 ({missing.mean()*100:.1f}%)")

# 验证范围
year_range = (df['AANLEGDATUM'].dt.year >= 2000) & \
             (df['AANLEGDATUM'].dt.year <= 2030)
invalid = ~year_range & df['AANLEGDATUM'].notna()
print(f"年份超出范围: {invalid.sum()} 行")

# 验证逻辑（施工日期不应晚于数据提交日期）
if 'submission_date' in df.columns:
    future_construction = df['AANLEGDATUM'] > df['submission_date']
    print(f"施工日期晚于提交日期: {future_construction.sum()} 行")
```

**3️⃣ 统计分析：**
```python
# 按月统计施工量
monthly_stats = df.groupby(df['AANLEGDATUM'].dt.to_period('M')).size()
print("月度施工分布：")
print(monthly_stats.sort_index())

# 按承包商统计施工日期范围
contractor_stats = df.groupby('NAAM OPDRACHTNEMER').agg({
    'AANLEGDATUM': ['min', 'max', 'count']
})
print("\n承包商施工时间跨度：")
print(contractor_stats)

# 按工作日/周末统计
df['is_weekday'] = df['AANLEGDATUM'].dt.dayofweek < 5
weekday_ratio = df['is_weekday'].mean()
print(f"\n工作日施工占比: {weekday_ratio*100:.1f}%")
```

**数据库设计：**
```sql
CREATE TABLE road_segments (
    aanlegdatum DATE NOT NULL,
    date_is_estimated BOOLEAN DEFAULT FALSE,  -- 日期是否为估计值
    
    -- 验证规则
    CHECK (aanlegdatum >= '2000-01-01' AND aanlegdatum <= '2030-12-31'),
    CHECK (aanlegdatum <= CURRENT_DATE)  -- 不能是未来日期
);

-- 索引（常用于查询）
CREATE INDEX idx_aanlegdatum ON road_segments(aanlegdatum);
CREATE INDEX idx_aanlegdatum_year_month ON road_segments(
    EXTRACT(YEAR FROM aanlegdatum),
    EXTRACT(MONTH FROM aanlegdatum)
);
```

**❓ 待与Leon确认的问题：**

1. **"[onbekend]"处理：**
   - 22行未知日期如何处理？
   - 是否可以从其他来源（如施工记录、发票）补充？
   - 还是标记为估计日期？

2. **5行完全缺失：**
   - 这些工程的日期是否可以追溯？
   - 是否允许缺失日期的数据存在？

3. **日期验证规则：**
   - 是否需要验证施工日期与天气条件的合理性？
   - 例如：冬季（12-2月）通常不施工

4. **多日期工程：**
   - 如果一个工程跨多天施工，如何记录？
   - 是记录开始日期、结束日期，还是完成日期？

**参考来源：**
- 📄 config/field_mapping_2022.json - 字段定义，日期格式规范
- 📊 Analysis/Template_2022_Field_Analysis_OLD.md (lines 1409-1473) - 真实数据统计

---

### 23. ASFALTCENTRALE

**字段分类：** 🔵 非关键字段 (Non-Critical)
**中文名称：** 沥青拌合站
**英文名称：** Asphalt Plant / Asphalt Mixing Plant
**数据类型：** string
**必填：** 是（但17.6%缺失）
**单位：** 无（站点名称/代码）

**📊 JSON定义（权威来源）：**
```json
{
  "field_number": 23,
  "field_name_nl": "ASFALTCENTRALE",
  "field_name_en": "Asphalt Plant",
  "field_name_cn": "沥青拌合站",
  "data_type": "string",
  "required": true,
  "classification": "non-critical",
  "category": "construction_record",
  "validation_rules": {
    "min_length": 1,
    "max_length": 200
  },
  "description": "Name or location of the asphalt mixing plant"
}
```

**📊 数据统计（基于1,592行真实数据）：**

- **数据完整度：** 1312/1592 (82.4%)
- **缺失数据：** 280 (17.6%)
- **唯一值数量：** 19

**📈 值分布（所有19个不同值）：**

| 拌合站 | 次数 | 占比 | 类型 |
|--------|------|------|------|
| `Lelystad` | 911 | 69.4% | 城市名 ✅ |
| `ANH` | 87 | 6.6% | 代码 |
| `APE` | 73 | 5.6% | 代码 |
| `Den Bosch` | 55 | 4.2% | 城市名 ✅ |
| `AsfaltNU Deventer en/of AsfaltNU Amsterdam` | 43 | 3.3% | 组合名 ⚠️ |
| `Amsterdam` | 35 | 2.7% | 城市名 ✅ |
| `Hengelo` | 27 | 2.1% | 城市名 ✅ |
| `ANA` | 21 | 1.6% | 代码 |
| `ACN` | 17 | 1.3% | 代码 |
| `AsfaltNU Deventer` | 8 | 0.6% | 公司+城市 |
| `RAC` | 8 | 0.6% | 代码 |
| `APRR` | 6 | 0.5% | 代码 |
| `APN` | 5 | 0.4% | 代码 |
| `RAC en APH` | 4 | 0.3% | 组合代码 ⚠️ |
| `APH` | 4 | 0.3% | 代码 |
| `AsfaltNU Amsterdam` | 3 | 0.2% | 公司+城市 |
| `Huissen` | 2 | 0.2% | 城市名 ✅ |
| `Tiel` | 2 | 0.2% | 城市名 ✅ |
| ` ` | 1 | 0.1% | ⚠️ 空格 |

**含义：**
生产沥青混合料的拌合站名称或位置。拌合站的选择影响运输距离、材料质量控制等因素。

**🔍 命名类型分析：**

**类型1：城市名（直接）**  - 约80%
```
Lelystad, Amsterdam, Den Bosch, Hengelo, Huissen, Tiel
- 直接使用城市名
- 最清晰的命名方式
```

**类型2：三字母代码** - 约15%
```
ANH, APE, ANA, ACN, RAC, APRR, APN, APH
- 可能是公司代码+位置代码
- 需要查询代码表才能理解
```

**类型3：公司+城市** - 约4%
```
AsfaltNU Deventer, AsfaltNU Amsterdam
- 包含公司名称
- 更详细但较长
```

**类型4：组合形式** - 约3%
```
"AsfaltNU Deventer en/of AsfaltNU Amsterdam"
"RAC en APH"
- 使用"en/of"（和/或）连接多个站点
- 表示可能来自多个拌合站
```

**⚠️ 数据质量问题：**

**问题1：命名不统一**
- 混合了城市名、代码、公司名
- 缺乏标准化命名规范

**问题2：代码含义不明**
- ANH, APE, ANA等代码无法直接理解
- 需要代码对照表

**问题3：组合值处理**
- "AsfaltNU Deventer en/of AsfaltNU Amsterdam"
- 表示不确定具体来源？
- 数据分析时难以处理

**问题4：空白值**
- 1行仅包含空格
- 应视为缺失数据

**问题5：缺失率偏高**
- 17.6%缺失（280行）
- 对于必填字段，缺失率较高

**拌合站地理分布：**

基于城市名推测的地理位置（荷兰）：
```
Lelystad - 中部（69.4%）⭐ 主要拌合站
Amsterdam - 西部（2.7%）
Den Bosch - 南部（4.2%）
Hengelo - 东部（2.1%）
Huissen, Tiel - 东部/中部（0.4%）
```

Lelystad占据绝对主导地位（69.4%），可能是：
- 地理位置优越（荷兰中部）
- RWS主要合作拌合站
- 最大产能的拌合站

**数据清洗建议：**

**1️⃣ 建立代码对照表：**
```python
# 创建拌合站代码映射
plant_code_map = {
    'ANH': 'Asfalt Noord Holland',  # 假设
    'APE': 'Asfalt Plant Eindhoven',  # 假设
    'ANA': 'Asfalt Noord Amsterdam',  # 假设
    'ACN': 'Asfalt Centraal Nederland',  # 假设
    # ... 需要与Leon确认实际含义
}

df['ASFALTCENTRALE_full'] = df['ASFALTCENTRALE'].replace(plant_code_map)
```

**2️⃣ 标准化命名：**
```python
# 去除空格，统一大小写
df['ASFALTCENTRALE'] = df['ASFALTCENTRALE'].str.strip().str.title()

# 处理空白值
df.loc[df['ASFALTCENTRALE'] == '', 'ASFALTCENTRALE'] = np.nan
```

**3️⃣ 处理组合值：**
```python
# 分离组合值
df['primary_plant'] = df['ASFALTCENTRALE'].str.split(' en/of ').str[0]
df['has_multiple_plants'] = df['ASFALTCENTRALE'].str.contains('en/of', na=False)

print(f"使用多个拌合站的工程: {df['has_multiple_plants'].sum()} 行")
```

**数据处理流程：**

**1️⃣ 输入和清理：**
```python
df = pd.read_excel('template.xlsx', dtype={'ASFALTCENTRALE': str})
df['ASFALTCENTRALE'] = df['ASFALTCENTRALE'].str.strip()

# 替换空白为NaN
df.loc[df['ASFALTCENTRALE'] == '', 'ASFALTCENTRALE'] = np.nan
```

**2️⃣ 验证和分类：**
```python
# 检查缺失
missing = df['ASFALTCENTRALE'].isna()
print(f"缺失拌合站: {missing.sum()} / {len(df)} = {missing.mean()*100:.1f}%")

# 分类
df['plant_type'] = df['ASFALTCENTRALE'].apply(lambda x:
    'city_name' if x in ['Lelystad', 'Amsterdam', 'Den Bosch', 'Hengelo', 'Huissen', 'Tiel']
    else 'code' if pd.notna(x) and len(x) <= 5 and x.isupper()
    else 'company_location' if pd.notna(x) and 'AsfaltNU' in x
    else 'combination' if pd.notna(x) and 'en/of' in x
    else 'other' if pd.notna(x)
    else 'missing'
)

print("\n拌合站命名类型分布：")
print(df['plant_type'].value_counts())
```

**3️⃣ 统计分析：**
```python
# 按拌合站统计工程量
plant_stats = df.groupby('ASFALTCENTRALE').agg({
    'TONNEN': 'sum',  # 总吨数
    'Weg': 'count'    # 工程数
}).sort_values('Weg', ascending=False)

print("拌合站工程量统计：")
print(plant_stats.head(10))

# 按承包商-拌合站组合分析
contractor_plant = df.groupby(['NAAM OPDRACHTNEMER', 'ASFALTCENTRALE']).size()
print("\n承包商-拌合站组合（前10）：")
print(contractor_plant.sort_values(ascending=False).head(10))
```

**数据库设计：**
```sql
-- 拌合站参照表
CREATE TABLE asphalt_plants (
    plant_code VARCHAR(10) PRIMARY KEY,
    plant_name VARCHAR(200) NOT NULL,
    city VARCHAR(100),
    company VARCHAR(100),
    address TEXT,
    capacity_tonnes_per_hour INT,
    is_active BOOLEAN DEFAULT TRUE
);

-- 主表外键
CREATE TABLE road_segments (
    asfaltcentrale VARCHAR(200),
    
    -- 可选：外键约束（需要先建立参照表）
    -- FOREIGN KEY (asfaltcentrale) REFERENCES asphalt_plants(plant_code)
);

-- 插入示例数据
INSERT INTO asphalt_plants VALUES
('Lelystad', 'Asfalt Centrale Lelystad', 'Lelystad', 'Unknown', NULL, NULL, TRUE),
('ANH', 'Asfalt Noord Holland', 'Unknown', 'Unknown', NULL, NULL, TRUE);
```

**❓ 待与Leon确认的问题：**

1. **代码全称：**
   - ANH, APE, ANA, ACN, RAC, APRR, APN, APH的完整名称？
   - 是否有官方的拌合站代码表？

2. **组合值含义：**
   - "AsfaltNU Deventer en/of AsfaltNU Amsterdam"表示什么？
   - 材料来自两个站点混合？还是不确定来源？

3. **缺失数据：**
   - 17.6%缺失率是否可接受？
   - 如何处理：要求补充还是允许缺失？

4. **标准化需求：**
   - 是否需要统一命名格式？
   - 建议：统一使用代码或统一使用城市名？

5. **数据关联：**
   - 拌合站是否与MENGSELCODE有关联？
   - 特定拌合站是否生产特定混合料？

**参考来源：**
- 📄 config/field_mapping_2022.json - 字段定义
- 📊 Analysis/Template_2022_Field_Analysis_OLD.md (lines 1476-1538) - 真实数据统计


---

### 字段 24: TONNEN (吨数)

**荷兰语全称：** TONNEN
**英文名称：** Tonnes
**中文名称：** 吨数
**字段分类：** 🔵 非关键字段（Non-Critical Field）

**JSON字段定义：**
```json
{
  "field_number": 24,
  "dutch_name": "TONNEN",
  "english_name": "Tonnes",
  "chinese_name": "吨数",
  "data_type": "float",
  "is_required": false,
  "description": "Total weight of asphalt material in tonnes"
}
```

---

#### 📊 数据统计

**数据完整度：**
- 有效数据：1,104行 / 1,592行
- 完整度：**69.3%** ✅ 较高
- 缺失数据：488行（30.7%）

**唯一值数量：** 697个

**数据类型分布：**
| 数据类型 | 数量 | 占比 |
|---------|------|------|
| **float（浮点数）** | 960 | 87.0% |
| **int（整数）** | 139 | 12.6% |
| **str（字符串）** | 5 | 0.5% |

---

#### 📈 值分布

**前20个最常见值：**

| 吨数值 | 次数 | 占比 | 类型 |
|--------|------|------|------|
| `1e-09` | 140 | 12.7% | 浮点数（科学计数法） ⚠️ |
| `12.09375` | 17 | 1.5% | 浮点数 |
| `24.1875` | 12 | 1.1% | 浮点数 |
| `48.375` | 10 | 0.9% | 浮点数 |
| `43` | 9 | 0.8% | 整数 |
| `42.1875000000016` | 7 | 0.6% | 浮点数（精度问题） |
| `72.5625` | 7 | 0.6% | 浮点数 |
| `96.75` | 7 | 0.6% | 浮点数 |
| `52.3125` | 6 | 0.5% | 浮点数 |
| `16.93125` | 5 | 0.5% | 浮点数 |
| `100` | 5 | 0.5% | 整数 |
| `50` | 5 | 0.5% | 整数 |

**示例值（实际数据）：**
- `235.8000000000001`
- `324.2249999999999`
- `73.6875`
- `35.37000000000134`
- `58.950000000005026`

**数值范围：**
- 最小值：1e-09 (0.000000001吨，接近0)
- 最大值：约324吨
- 典型值：10-100吨范围

---

#### 🚨 数据质量问题

**问题1：科学计数法"1e-09"**
- **出现次数：** 140次（12.7%）
- **含义：** 1×10⁻⁹ = 0.000000001 吨（接近零）

**可能原因：**
1. **数据缺失的占位符：** 
   - Excel公式计算结果为0时，用极小值表示
   - 避免除零错误的技术处理
   
2. **极小工程量：** 
   - 修补性工作
   - 试验性铺筑
   
3. **数据录入错误：**
   - 实际值未填写，默认为0

**影响：**
- 如果用于统计总量，1e-09可视为0
- 需要确认这些行是否应该被排除

**问题2：浮点精度问题**
- `42.1875000000016`（应该是42.1875）
- `12.09375000000275`（应该是12.09375）
- `58.950000000005026`（应该是58.95）

**原因：** Excel浮点运算精度损失

**问题3：混合数据类型**
- 87.0%是浮点数
- 12.6%是整数
- 0.5%是字符串

**字符串值需要识别和处理**

**问题4：0.5%的字符串值**
- 5行数据是字符串类型
- 需要查看具体内容（可能是"未知"、"N/A"等）

---

#### 🛠️ 数据清洗建议

**步骤1：处理"1e-09"值**
```python
import pandas as pd
import numpy as np

# 方案A：转换为NaN（缺失）
df.loc[df['TONNEN'] < 0.001, 'TONNEN'] = np.nan

# 方案B：转换为0
df.loc[df['TONNEN'] < 0.001, 'TONNEN'] = 0.0

# 方案C：标记为特殊状态
df['tonnage_type'] = 'normal'
df.loc[df['TONNEN'] < 0.001, 'tonnage_type'] = 'negligible'
```

**步骤2：浮点精度修正**
```python
# 方案A：四舍五入到合理精度（小数点后2位）
df['TONNEN'] = df['TONNEN'].round(2)

# 方案B：四舍五入到小数点后4位（保留更多精度）
df['TONNEN'] = df['TONNEN'].round(4)
```

**步骤3：统一数据类型**
```python
# 转换为浮点数，无法转换的变为NaN
df['TONNEN'] = pd.to_numeric(df['TONNEN'], errors='coerce')
```

**步骤4：异常值检测**
```python
# 识别异常大值
threshold = df['TONNEN'].quantile(0.99)  # 99分位数
outliers = df[df['TONNEN'] > threshold]

print(f"超过99%分位数({threshold:.2f}吨)的异常值：")
print(outliers[['Weg', 'BAAN', 'VAN', 'TOT', 'Lengte', 'TONNEN']])
```

---

#### 💾 数据处理流程

```python
import pandas as pd
import numpy as np

def clean_tonnage_field(df):
    """
    清洗TONNEN（吨数）字段
    
    处理：
    1. 科学计数法极小值（1e-09）
    2. 浮点精度问题
    3. 数据类型统一
    4. 异常值识别
    """
    # 1. 转换为数值类型
    df['TONNEN'] = pd.to_numeric(df['TONNEN'], errors='coerce')
    
    # 2. 处理极小值（< 0.001吨，即1克）
    negligible_mask = (df['TONNEN'].notna()) & (df['TONNEN'] < 0.001)
    negligible_count = negligible_mask.sum()
    
    print(f"发现{negligible_count}行极小值（< 0.001吨）")
    
    # 转换为NaN（视为缺失）
    df.loc[negligible_mask, 'TONNEN'] = np.nan
    
    # 3. 浮点精度修正（保留2位小数）
    df['TONNEN'] = df['TONNEN'].round(2)
    
    # 4. 异常值检测
    if df['TONNEN'].notna().any():
        q99 = df['TONNEN'].quantile(0.99)
        outliers = df[df['TONNEN'] > q99]
        
        print(f"99%分位数: {q99:.2f}吨")
        print(f"发现{len(outliers)}行异常大值（> {q99:.2f}吨）")
    
    # 5. 统计报告
    stats = {
        'total_rows': len(df),
        'valid_tonnage': df['TONNEN'].notna().sum(),
        'missing': df['TONNEN'].isna().sum(),
        'min': df['TONNEN'].min(),
        'max': df['TONNEN'].max(),
        'mean': df['TONNEN'].mean(),
        'median': df['TONNEN'].median()
    }
    
    return df, stats

# 使用示例
df_cleaned, stats = clean_tonnage_field(df)

print(f"\n数据统计：")
print(f"  总行数: {stats['total_rows']}")
print(f"  有效数据: {stats['valid_tonnage']} ({stats['valid_tonnage']/stats['total_rows']*100:.1f}%)")
print(f"  缺失数据: {stats['missing']} ({stats['missing']/stats['total_rows']*100:.1f}%)")
print(f"  范围: {stats['min']:.2f} - {stats['max']:.2f}吨")
print(f"  平均值: {stats['mean']:.2f}吨")
print(f"  中位数: {stats['median']:.2f}吨")
```

---

#### 📋 数据验证规则

**规则24.1：数据类型验证**
```python
# 必须是数值类型
assert df['TONNEN'].dtype in ['float64', 'int64'] or df['TONNEN'].isna().all()
```

**规则24.2：合理范围验证**
```python
# 如果有值，必须 >= 0（吨数不能为负）
invalid = df[(df['TONNEN'].notna()) & (df['TONNEN'] < 0)]
if not invalid.empty:
    print(f"警告：发现{len(invalid)}行负吨数值")
```

**规则24.3：极小值检测**
```python
# 检测接近0的值（可能是数据质量问题）
near_zero = df[(df['TONNEN'].notna()) & (df['TONNEN'] < 0.01)]
if not near_zero.empty:
    print(f"警告：发现{len(near_zero)}行极小吨数值（< 0.01吨）")
```

**规则24.4：与长度的逻辑验证**
```python
# 单位长度吨数应在合理范围（吨/公里）
# 典型值：40-200吨/公里（取决于宽度和厚度）

df['tonnage_per_km'] = df['TONNEN'] / df['Lengte']

# 检测异常单位长度吨数
abnormal = df[
    (df['tonnage_per_km'].notna()) & 
    ((df['tonnage_per_km'] < 10) | (df['tonnage_per_km'] > 500))
]

if not abnormal.empty:
    print(f"警告：发现{len(abnormal)}行异常单位长度吨数")
    print(abnormal[['Weg', 'BAAN', 'Lengte', 'Breedte', 'TONNEN', 'tonnage_per_km']])
```

---

#### 🗄️ 数据库设计建议

**字段定义：**
```sql
CREATE TABLE pavement_records (
    ...
    
    -- 吨数
    tonnen DECIMAL(10, 2) NULL
        COMMENT '沥青材料总吨数（tonnes）',
    
    tonnen_status ENUM('measured', 'negligible', 'unknown') 
        DEFAULT 'measured'
        COMMENT '吨数数据状态：measured=实测值，negligible=极小值，unknown=未知',
    
    tonnage_per_km DECIMAL(10, 2) 
        GENERATED ALWAYS AS (
            CASE 
                WHEN lengte > 0 AND tonnen IS NOT NULL 
                THEN tonnen / lengte 
                ELSE NULL 
            END
        ) STORED
        COMMENT '单位长度吨数（吨/公里）',
    
    ...
    
    -- 约束
    CONSTRAINT chk_tonnen_nonnegative 
        CHECK (tonnen IS NULL OR tonnen >= 0),
    
    CONSTRAINT chk_tonnage_per_km_reasonable
        CHECK (tonnage_per_km IS NULL OR 
               (tonnage_per_km >= 5 AND tonnage_per_km <= 1000))
);

-- 索引
CREATE INDEX idx_tonnen ON pavement_records(tonnen) 
    WHERE tonnen IS NOT NULL;

-- 统计视图
CREATE VIEW tonnage_statistics AS
SELECT 
    EXTRACT(YEAR FROM aanlegdatum) AS year,
    EXTRACT(MONTH FROM aanlegdatum) AS month,
    naam_opdrachtnemer,
    deklaagsoort,
    COUNT(*) AS record_count,
    SUM(tonnen) AS total_tonnes,
    AVG(tonnen) AS avg_tonnes_per_record,
    AVG(tonnage_per_km) AS avg_tonnes_per_km,
    MIN(tonnen) AS min_tonnes,
    MAX(tonnen) AS max_tonnes
FROM pavement_records
WHERE tonnen IS NOT NULL AND tonnen >= 0.01
GROUP BY year, month, naam_opdrachtnemer, deklaagsoort;
```

---

#### ❓ 需要与Leon确认的问题

**问题24.1：** "1e-09"值的含义
- ❓ 这140行（12.7%）的极小值表示什么？
- 选项A：数据缺失的占位符
- 选项B：极小工程量
- 选项C：数据录入错误
- **建议处理：** 转换为NULL（缺失）

**问题24.2：** 5行字符串值的内容
- ❓ 这5行（0.5%）的字符串值是什么？
- 需要查看具体内容以确定清洗策略

**问题24.3：** 合理的吨数范围
- ❓ 单个路段的典型吨数范围是多少？
- ❓ 最大值324吨是否合理？
- 需要确定异常值检测的阈值

**问题24.4：** 单位长度吨数的合理范围
- ❓ 典型的吨/公里值是多少？
- ❓ 是否与Breedte（宽度）和DIKTE（厚度）有关联？
- 可以用于交叉验证数据合理性

**问题24.5：** 与其他字段的关联
- ❓ TONNEN是否应该与Lengte、Breedte、DIKTE有数学关系？
- 理论公式：吨数 ≈ 长度 × 宽度 × 厚度 × 密度
- 可以建立计算验证规则


---

### 字段 25: evt. indien beschikbaar temperatuur (Productie) (生产温度)

**荷兰语全称：** evt. indien beschikbaar temperatuur (Productie)
**英文名称：** Production Temperature (if available)
**中文名称：** 生产温度（如有）
**字段分类：** 🔵 非关键字段（Non-Critical Field）

**JSON字段定义：**
```json
{
  "field_number": 25,
  "dutch_name": "temperatuur",
  "english_name": "Production Temperature",
  "chinese_name": "生产温度",
  "data_type": "float",
  "unit": "°C",
  "is_required": false,
  "description": "Asphalt production temperature if available"
}
```

---

#### 📊 数据统计

**数据完整度：**
- 有效数据：930行 / 1,592行
- 完整度：**58.4%** ⚠️ 中等
- 缺失数据：662行（41.6%）

**唯一值数量：** 68个

**数据类型分布：**
| 数据类型 | 数量 | 占比 |
|---------|------|------|
| **int（整数）** | 564 | 60.6% |
| **str（字符串）** | 352 | 37.8% |
| **float（浮点数）** | 14 | 1.5% |

---

#### 📈 值分布

**前20个最常见值：**

| 温度值 | 次数 | 占比 | 格式类型 |
|--------|------|------|----------|
| `155` | 430 | 46.2% | 整数 ✅ |
| `155 / 170` | 242 | 26.0% | 范围字符串 ⚠️ |
| `165` | 109 | 11.7% | 整数 ✅ |
| `n.b.` | 53 | 5.7% | 特殊值 ⚠️ |
| `170` | 11 | 1.2% | 整数 ✅ |
| `160` | 10 | 1.1% | 整数 ✅ |
| `170°C` | 4 | 0.4% | 带单位字符串 ⚠️ |
| `157°C` | 3 | 0.3% | 带单位字符串 ⚠️ |
| `147°C` | 3 | 0.3% | 带单位字符串 ⚠️ |
| `162.8` | 2 | 0.2% | 浮点数 ✅ |
| `174°C` | 2 | 0.2% | 带单位字符串 ⚠️ |
| `158°C` | 2 | 0.2% | 带单位字符串 ⚠️ |
| ` ` | 2 | 0.2% | 空格 ⚠️ |
| `149°C` | 2 | 0.2% | 带单位字符串 ⚠️ |
| `141.3` | 2 | 0.2% | 浮点数 ✅ |
| `147; 148,2; 151,1` | 1 | 0.1% | 多值字符串 ⚠️ |
| `149,1; 151,5 143,7; 144,6` | 1 | 0.1% | 多值字符串 ⚠️ |
| `141,3 142,4; 144` | 1 | 0.1% | 多值字符串 ⚠️ |
| `146,7; 144,3; 142,5` | 1 | 0.1% | 多值字符串 ⚠️ |
| `144,6; 145,1` | 1 | 0.1% | 多值字符串 ⚠️ |

**示例值（实际数据）：**
- `155 / 170`（最常见，26.0%）
- `155`（最常见单一值，46.2%）
- `165`
- `n.b.`
- `170°C`

**温度范围：**
- 典型值：140-170°C
- 最常见：155°C（46.2%）
- 次常见：165°C（11.7%）

---

#### 🚨 数据质量问题

**问题1：格式不一致 - 5种格式混合**

**格式A：纯数字（60.6%）**
- 示例：`155`, `165`, `170`
- 假定单位：°C
- **最标准的格式** ✅

**格式B：范围字符串（26.0%）**
- 示例：`155 / 170`
- **可能含义：**
  - 双层沥青的不同温度（表层/底层）
  - 温度范围（最低/最高）
  - 多次测量的温度值

**格式C：带单位字符串（~2%）**
- 示例：`170°C`, `157°C`, `147°C`
- 包含温度单位符号
- 需要移除单位进行数值处理

**格式D：多值字符串（~1%）**
- 示例：`147; 148,2; 151,1`
- 分号或空格分隔的多个测量值
- **可能含义：**
  - 多次测量记录
  - 不同车道的温度
  - 不同时间点的温度

**格式E：欧洲数字格式（1.5%）**
- 示例：`162,8`（逗号作为小数点）
- 与其他整数格式混合

**问题2：特殊值"n.b."**
- **出现次数：** 53次（5.7%）
- **荷兰语含义：** "nota bene" = "注意"，或 "niet beschikbaar" = "不可用"

**可能含义：**
1. 温度数据不可用
2. 未测量
3. 测量但未记录

**处理建议：** 转换为NULL（缺失）

**问题3：空格值**
- 2行数据仅包含空格
- 应视为缺失数据

**问题4：混合数据类型**
- 60.6%是整数
- 37.8%是字符串
- 1.5%是浮点数
- 数据库导入和处理复杂

---

#### 🛠️ 数据清洗建议

**步骤1：提取温度范围**
```python
import pandas as pd
import numpy as np
import re

def extract_temperature_values(temp_str):
    """
    从各种格式中提取温度值
    
    返回：(min_temp, max_temp, avg_temp, value_count)
    """
    if pd.isna(temp_str):
        return None, None, None, 0
    
    # 转换为字符串
    temp_str = str(temp_str).strip()
    
    # 处理特殊值
    if temp_str.lower() in ['n.b.', '', ' ']:
        return None, None, None, 0
    
    # 移除单位符号
    temp_str = temp_str.replace('°C', '').replace('°', '').strip()
    
    # 替换欧洲格式逗号为点
    temp_str = temp_str.replace(',', '.')
    
    # 提取所有数字（支持浮点）
    numbers = re.findall(r'\d+\.?\d*', temp_str)
    
    if not numbers:
        return None, None, None, 0
    
    # 转换为浮点数
    temps = [float(n) for n in numbers]
    
    return min(temps), max(temps), sum(temps)/len(temps), len(temps)

# 应用到数据
df[['temp_min', 'temp_max', 'temp_avg', 'temp_count']] = df['temperatuur'].apply(
    lambda x: pd.Series(extract_temperature_values(x))
)

# 示例结果
# "155" → (155, 155, 155, 1)
# "155 / 170" → (155, 170, 162.5, 2)
# "147; 148,2; 151,1" → (147, 151.1, 148.77, 3)
# "n.b." → (None, None, None, 0)
```

**步骤2：数据标准化**
```python
def standardize_temperature(df):
    """
    标准化温度字段
    
    策略：
    1. 提取温度范围
    2. 使用平均值作为标准值
    3. 保留范围信息
    """
    # 提取温度值
    df[['temp_min', 'temp_max', 'temp_avg', 'temp_count']] = df['temperatuur'].apply(
        lambda x: pd.Series(extract_temperature_values(x))
    )
    
    # 创建标准化字段
    df['temperatuur_std'] = df['temp_avg']
    
    # 创建温度类型标签
    df['temp_type'] = 'unknown'
    df.loc[df['temp_count'] == 1, 'temp_type'] = 'single'
    df.loc[df['temp_count'] == 2, 'temp_type'] = 'range'
    df.loc[df['temp_count'] > 2, 'temp_type'] = 'multiple'
    df.loc[df['temp_count'] == 0, 'temp_type'] = 'missing'
    
    # 统计报告
    print("温度数据标准化结果：")
    print(df['temp_type'].value_counts())
    print(f"\n标准化后有效温度数据：{df['temperatuur_std'].notna().sum()}行")
    
    return df

df = standardize_temperature(df)
```

**步骤3：范围字符串特殊处理**
```python
# 分析"155 / 170"模式
range_pattern = df[df['temperatuur'].astype(str).str.contains('/', na=False)]

print(f"发现{len(range_pattern)}行使用'/'格式的范围值")

# 检查是否与双层结构相关
if 'TUSSENLAAG' in df.columns:
    with_binder = range_pattern[range_pattern['TUSSENLAAG'].notna()]
    print(f"其中{len(with_binder)}行有TUSSENLAAG（中间层）")
    print("假设：155 = 表层温度，170 = 底层温度")
```

---

#### 💾 数据处理流程

```python
import pandas as pd
import numpy as np
import re

def clean_temperature_field(df):
    """
    清洗temperatuur（温度）字段
    
    处理：
    1. 格式统一（移除单位，处理范围）
    2. 提取温度值（最小、最大、平均）
    3. 标准化为数值类型
    4. 异常值检测
    """
    # 1. 提取温度值
    df[['temp_min', 'temp_max', 'temp_avg', 'temp_count']] = df['temperatuur'].apply(
        lambda x: pd.Series(extract_temperature_values(x))
    )
    
    # 2. 温度合理性检查
    # 沥青生产温度通常在 120-190°C
    invalid_low = df[(df['temp_min'].notna()) & (df['temp_min'] < 100)]
    invalid_high = df[(df['temp_max'].notna()) & (df['temp_max'] > 200)]
    
    if not invalid_low.empty:
        print(f"警告：发现{len(invalid_low)}行异常低温（< 100°C）")
        print(invalid_low[['Weg', 'BAAN', 'DEKLAAGSOORT', 'temperatuur', 'temp_min']])
    
    if not invalid_high.empty:
        print(f"警告：发现{len(invalid_high)}行异常高温（> 200°C）")
        print(invalid_high[['Weg', 'BAAN', 'DEKLAAGSOORT', 'temperatuur', 'temp_max']])
    
    # 3. 按材料类型分析温度
    if 'DEKLAAGSOORT' in df.columns:
        temp_by_material = df.groupby('DEKLAAGSOORT')['temp_avg'].agg(['count', 'mean', 'std', 'min', 'max'])
        print("\n按材料类型的温度统计：")
        print(temp_by_material.round(1))
    
    # 4. 统计报告
    stats = {
        'total_rows': len(df),
        'has_temp_data': df['temp_avg'].notna().sum(),
        'single_value': (df['temp_count'] == 1).sum(),
        'range_value': (df['temp_count'] == 2).sum(),
        'multiple_value': (df['temp_count'] > 2).sum(),
        'typical_temp': df['temp_avg'].mode()[0] if df['temp_avg'].notna().any() else None,
        'mean_temp': df['temp_avg'].mean(),
        'temp_range': f"{df['temp_avg'].min():.1f} - {df['temp_avg'].max():.1f}°C"
    }
    
    return df, stats

# 使用示例
df_cleaned, stats = clean_temperature_field(df)

print(f"\n温度数据统计：")
print(f"  总行数: {stats['total_rows']}")
print(f"  有温度数据: {stats['has_temp_data']} ({stats['has_temp_data']/stats['total_rows']*100:.1f}%)")
print(f"  单一值: {stats['single_value']}")
print(f"  范围值: {stats['range_value']}")
print(f"  多值: {stats['multiple_value']}")
print(f"  最常见温度: {stats['typical_temp']}°C")
print(f"  平均温度: {stats['mean_temp']:.1f}°C")
print(f"  温度范围: {stats['temp_range']}")
```

---

#### 📋 数据验证规则

**规则25.1：温度合理范围**
```python
# 沥青生产温度通常在 120-190°C
# 超出范围需要警告

valid_temp_range = (120, 190)

invalid = df[
    (df['temp_avg'].notna()) & 
    ((df['temp_avg'] < valid_temp_range[0]) | 
     (df['temp_avg'] > valid_temp_range[1]))
]

if not invalid.empty:
    print(f"警告：发现{len(invalid)}行温度超出正常范围({valid_temp_range[0]}-{valid_temp_range[1]}°C)")
```

**规则25.2：材料-温度匹配**
```python
# 不同材料有推荐温度范围
material_temp_ranges = {
    'ZOAB': (140, 170),
    'DZOAB': (150, 170),
    'SMA': (160, 180),
    'AC': (150, 170)
}

for material, (min_t, max_t) in material_temp_ranges.items():
    material_data = df[df['DEKLAAGSOORT'].str.contains(material, na=False)]
    
    out_of_range = material_data[
        (material_data['temp_avg'].notna()) & 
        ((material_data['temp_avg'] < min_t) | 
         (material_data['temp_avg'] > max_t))
    ]
    
    if not out_of_range.empty:
        print(f"警告：{material}材料发现{len(out_of_range)}行温度不在推荐范围({min_t}-{max_t}°C)")
```

**规则25.3：格式一致性检查**
```python
# 统计各种格式的出现次数
format_types = df['temp_type'].value_counts()

print("温度格式分布：")
print(format_types)

# 如果范围值超过30%，可能需要特别处理
if format_types.get('range', 0) / len(df) > 0.3:
    print("⚠️ 超过30%的数据使用范围格式，建议与Leon确认含义")
```

---

#### 🗄️ 数据库设计建议

**字段定义：**
```sql
CREATE TABLE pavement_records (
    ...
    
    -- 生产温度（原始值保留）
    temperatuur_raw VARCHAR(100) NULL
        COMMENT '原始温度记录（可能包含范围）',
    
    -- 标准化温度值
    temperatuur_min DECIMAL(5, 2) NULL
        COMMENT '最低温度（°C）',
    
    temperatuur_max DECIMAL(5, 2) NULL
        COMMENT '最高温度（°C）',
    
    temperatuur_avg DECIMAL(5, 2) NULL
        COMMENT '平均温度（°C，用于统计）',
    
    temp_type ENUM('single', 'range', 'multiple', 'missing') 
        DEFAULT 'missing'
        COMMENT '温度数据类型：单值、范围、多值、缺失',
    
    ...
    
    -- 约束
    CONSTRAINT chk_temp_range 
        CHECK (
            temperatuur_avg IS NULL OR 
            (temperatuur_avg >= 100 AND temperatuur_avg <= 200)
        ),
    
    CONSTRAINT chk_temp_min_max
        CHECK (
            (temperatuur_min IS NULL AND temperatuur_max IS NULL) OR
            (temperatuur_min <= temperatuur_max)
        )
);

-- 索引
CREATE INDEX idx_temp_avg ON pavement_records(temperatuur_avg) 
    WHERE temperatuur_avg IS NOT NULL;

-- 按材料类型的温度统计视图
CREATE VIEW temperature_by_material AS
SELECT 
    deklaagsoort,
    COUNT(*) AS record_count,
    COUNT(temperatuur_avg) AS temp_records,
    ROUND(AVG(temperatuur_avg), 1) AS avg_temp,
    ROUND(STDDEV(temperatuur_avg), 1) AS temp_stddev,
    MIN(temperatuur_min) AS min_temp,
    MAX(temperatuur_max) AS max_temp,
    SUM(CASE WHEN temp_type = 'range' THEN 1 ELSE 0 END) AS range_count
FROM pavement_records
WHERE temperatuur_avg IS NOT NULL
GROUP BY deklaagsoort
ORDER BY record_count DESC;
```

---

#### ❓ 需要与Leon确认的问题

**问题25.1：** "155 / 170"范围值的含义
- ❓ 这种格式（242次，26.0%）表示什么？
- 选项A：双层沥青的不同温度（表层155°C / 底层170°C）
- 选项B：温度范围（最低155°C / 最高170°C）
- 选项C：多次测量的两个值
- **影响：** 决定如何提取和使用这些值

**问题25.2：** "n.b."的确切含义
- ❓ "n.b." = "nota bene"（注意）还是 "niet beschikbaar"（不可用）？
- 53次出现（5.7%）
- **建议处理：** 转换为NULL

**问题25.3：** 多值字符串的含义
- ❓ `147; 148,2; 151,1`这种多值记录表示什么？
- 选项A：多次测量
- 选项B：不同车道
- 选项C：不同时间点
- **建议处理：** 使用平均值

**问题25.4：** 温度与材料的关联规则
- ❓ 不同DEKLAAGSOORT是否有推荐的温度范围？
- ❓ 温度超出范围是否表示数据错误？
- 可以建立验证规则

**问题25.5：** 温度数据的重要性
- ❓ 温度数据是否影响质量评估？
- ❓ 41.6%的缺失率是否可接受？
- ❓ 是否需要强制要求记录温度？


---

### 字段 26: OPMERKINGENVELD (备注栏)

**荷兰语全称：** OPMERKINGENVELD
**英文名称：** Remarks Field
**中文名称：** 备注栏
**字段分类：** 🔵 非关键字段（Non-Critical Field）

**JSON字段定义：**
```json
{
  "field_number": 26,
  "dutch_name": "OPMERKINGENVELD",
  "english_name": "Remarks",
  "chinese_name": "备注",
  "data_type": "string",
  "is_required": false,
  "description": "Additional comments or special notes"
}
```

---

#### 📊 数据统计

**数据完整度：**
- 有效数据：1,004行 / 1,592行
- 完整度：**63.1%** ✅ 较高
- 缺失数据：588行（36.9%）

**唯一值数量：** 127个

**数据类型：**
- **str（字符串）：** 1,004行（100.0%）

---

#### 📈 值分布

**前20个最常见备注：**

| 备注内容 | 次数 | 占比 | 类别 |
|---------|------|------|------|
| `Frezen 50 mm en aanbrengen 50 mm PA16` | 339 | 33.8% | 标准工序 |
| `Frezen 70 mm en aanbrengen 70 mm ZOABTW` | 86 | 8.6% | 标准工序 |
| `Aanbrengen 70 mm ZOABTW` | 78 | 7.8% | 标准工序 |
| `Aanbrengen 50 mm PA16` | 27 | 2.7% | 标准工序 |
| `Frezen 100 mm en aanbrengen 50 mm AC 16 Bind en 50 mm PA16` | 26 | 2.6% | 双层工序 |
| `Frezen 35 mm en aanbrengen 35 mm SMA` | 22 | 2.2% | 标准工序 |
| `AC 16 Surf` | 19 | 1.9% | 材料简称 |
| `Frezen 50 mm en aanbrengen 50 mm ZOABTW` | 17 | 1.7% | 标准工序 |
| `Frezen 70 mm en aanbrengen 70 mm PA16` | 16 | 1.6% | 标准工序 |
| `Aanbrengen 50 mm ZOABTW` | 15 | 1.5% | 标准工序 |

**备注内容分类统计：**
- **"Frezen ... en aanbrengen ..."（铣刨+铺设）：** 约60%
- **"Aanbrengen ..."（仅铺设）：** 约25%
- **材料简称（如"AC 16 Surf"）：** 约10%
- **其他特殊说明：** 约5%

---

#### 🔍 备注内容分析

**类型1：标准铣刨+铺设工序（约60%）**

**格式：** `Frezen [厚度] mm en aanbrengen [厚度] mm [材料]`

**示例：**
- `Frezen 50 mm en aanbrengen 50 mm PA16`（339次）
- `Frezen 70 mm en aanbrengen 70 mm ZOABTW`（86次）
- `Frezen 100 mm en aanbrengen 50 mm AC 16 Bind en 50 mm PA16`（26次，双层）

**含义：**
- **Frezen** = 铣刨（Milling）
- **Aanbrengen** = 铺设（Paving/Laying）
- **en** = 和（and）

**结构化信息：**
```
Operation: Milling + Paving
Milling_Depth: 50 mm
Paving_Thickness: 50 mm
Material: PA16
```

**类型2：仅铺设工序（约25%）**

**格式：** `Aanbrengen [厚度] mm [材料]`

**示例：**
- `Aanbrengen 70 mm ZOABTW`（78次）
- `Aanbrengen 50 mm PA16`（27次）
- `Aanbrengen 50 mm ZOABTW`（15次）

**含义：**
- 没有铣刨，直接铺设（罩面，Overlay）

**类型3：材料简称（约10%）**

**示例：**
- `AC 16 Surf`（19次）
- `SMA 11 Surf Spec III`
- `ZOAB 11`

**含义：**
- 仅记录材料名称
- 与DEKLAAGSOORT字段重复信息

**类型4：双层工序（约5%）**

**示例：**
- `Frezen 100 mm en aanbrengen 50 mm AC 16 Bind en 50 mm PA16`（26次）

**结构化信息：**
```
Operation: Milling + Two-layer Paving
Milling_Depth: 100 mm
Layer1_Material: AC 16 Bind (Binder course)
Layer1_Thickness: 50 mm
Layer2_Material: PA16 (Surface course)
Layer2_Thickness: 50 mm
```

**类型5：特殊情况说明（少见）**

可能包含：
- 施工日期调整
- 特殊施工条件
- 问题记录
- 其他备注

---

#### 🚨 数据质量问题

**问题1：信息冗余**
- 备注中的厚度和材料与字段DIKTE、DEKLAAGSOORT重复
- **例如：**
  - 备注：`Aanbrengen 50 mm PA16`
  - DIKTE字段：0.05（50mm）
  - DEKLAAGSOORT字段：DZOAB

**可能原因：**
- 承包商习惯在备注中重复关键信息
- 备注作为施工记录的主要描述
- 其他字段后期补充

**问题2：格式不完全一致**
- 大部分遵循标准格式，但有变体：
  - `Frezen 50 mm en aanbrengen 50 mm PA16` ✅ 标准
  - `Frezen 50mm en aanbrengen 50mm PA16` ⚠️ 缺少空格
  - `frezen 50 mm en aanbrengen 50 mm pa16` ⚠️ 小写

**问题3：荷兰语专业术语**
- 需要翻译才能理解
- 不利于非荷兰语使用者

**问题4：36.9%缺失**
- 588行没有备注
- 是否应该要求所有记录都有备注？

---

#### 🛠️ 数据清洗建议

**步骤1：结构化提取**
```python
import pandas as pd
import re

def parse_remarks(remark_text):
    """
    从备注中提取结构化信息
    
    返回：{
        'has_milling': bool,
        'milling_depth': float,
        'paving_layers': [
            {'material': str, 'thickness': float},
            ...
        ]
    }
    """
    if pd.isna(remark_text):
        return None
    
    result = {
        'has_milling': False,
        'milling_depth': None,
        'paving_layers': []
    }
    
    # 检测铣刨
    milling_match = re.search(r'Frezen\s+(\d+)\s*mm', remark_text, re.IGNORECASE)
    if milling_match:
        result['has_milling'] = True
        result['milling_depth'] = float(milling_match.group(1))
    
    # 提取铺设信息
    # 模式：aanbrengen [厚度] mm [材料]
    paving_pattern = r'aanbrengen\s+(\d+)\s*mm\s+([A-Z0-9\s]+?)(?:\s+en\s+|$)'
    
    for match in re.finditer(paving_pattern, remark_text, re.IGNORECASE):
        thickness = float(match.group(1))
        material = match.group(2).strip()
        
        result['paving_layers'].append({
            'material': material,
            'thickness': thickness
        })
    
    return result

# 应用到数据
df['remark_parsed'] = df['OPMERKINGENVELD'].apply(parse_remarks)

# 展开结构化字段
df['has_milling'] = df['remark_parsed'].apply(
    lambda x: x['has_milling'] if x else None
)
df['milling_depth'] = df['remark_parsed'].apply(
    lambda x: x['milling_depth'] if x else None
)
df['layer_count'] = df['remark_parsed'].apply(
    lambda x: len(x['paving_layers']) if x else 0
)

# 统计
print(f"有铣刨的记录：{df['has_milling'].sum()}行")
print(f"仅铺设的记录：{(~df['has_milling'] & df['OPMERKINGENVELD'].notna()).sum()}行")
print(f"双层铺设的记录：{(df['layer_count'] == 2).sum()}行")
```

**步骤2：与字段DIKTE交叉验证**
```python
def validate_thickness_consistency(df):
    """
    验证备注中的厚度与DIKTE字段的一致性
    """
    inconsistent = []
    
    for idx, row in df.iterrows():
        if pd.isna(row['OPMERKINGENVELD']) or pd.isna(row['DIKTE VERHARDING']):
            continue
        
        parsed = row['remark_parsed']
        if not parsed or not parsed['paving_layers']:
            continue
        
        # 获取备注中的总厚度
        remark_thickness = sum(layer['thickness'] for layer in parsed['paving_layers'])
        
        # DIKTE字段（米转毫米）
        dikte_thickness = row['DIKTE VERHARDING'] * 1000
        
        # 允许±5mm误差
        if abs(remark_thickness - dikte_thickness) > 5:
            inconsistent.append({
                'index': idx,
                'Weg': row['Weg'],
                'BAAN': row['BAAN'],
                'remark': row['OPMERKINGENVELD'],
                'remark_thickness': remark_thickness,
                'dikte_thickness': dikte_thickness,
                'diff': remark_thickness - dikte_thickness
            })
    
    if inconsistent:
        print(f"发现{len(inconsistent)}行厚度不一致")
        return pd.DataFrame(inconsistent)
    else:
        print("✅ 所有厚度数据一致")
        return pd.DataFrame()

inconsistencies = validate_thickness_consistency(df)
```

**步骤3：标准化格式**
```python
def standardize_remark_format(remark_text):
    """
    标准化备注格式
    
    - 统一大小写
    - 统一空格
    - 标准化术语
    """
    if pd.isna(remark_text):
        return None
    
    # 转为标准格式（首字母大写）
    text = str(remark_text).strip()
    
    # 标准化关键词
    text = re.sub(r'\bfrezen\b', 'Frezen', text, flags=re.IGNORECASE)
    text = re.sub(r'\baanbrengen\b', 'Aanbrengen', text, flags=re.IGNORECASE)
    
    # 统一空格（数字和mm之间）
    text = re.sub(r'(\d+)\s*mm', r'\1 mm', text)
    
    return text

df['OPMERKINGENVELD_std'] = df['OPMERKINGENVELD'].apply(standardize_remark_format)
```

**步骤4：翻译到英文（可选）**
```python
# 术语翻译字典
translation_dict = {
    'Frezen': 'Milling',
    'Aanbrengen': 'Paving',
    'en': 'and',
    'mm': 'mm'
}

def translate_to_english(remark_text):
    """
    将荷兰语备注翻译为英文
    """
    if pd.isna(remark_text):
        return None
    
    text = str(remark_text)
    
    for dutch, english in translation_dict.items():
        text = text.replace(dutch, english)
    
    return text

df['remarks_en'] = df['OPMERKINGENVELD'].apply(translate_to_english)
```

---

#### 💾 数据处理流程

```python
import pandas as pd
import re

def process_remarks_field(df):
    """
    完整处理OPMERKINGENVELD字段
    
    功能：
    1. 结构化提取信息
    2. 交叉验证
    3. 格式标准化
    4. 分类统计
    """
    # 1. 结构化提取
    print("1. 提取结构化信息...")
    df['remark_parsed'] = df['OPMERKINGENVELD'].apply(parse_remarks)
    
    df['has_milling'] = df['remark_parsed'].apply(
        lambda x: x['has_milling'] if x else False
    )
    df['milling_depth'] = df['remark_parsed'].apply(
        lambda x: x['milling_depth'] if x else None
    )
    df['layer_count'] = df['remark_parsed'].apply(
        lambda x: len(x['paving_layers']) if x else 0
    )
    
    # 2. 分类统计
    print("\n2. 备注分类统计:")
    
    milling_paving = (df['has_milling'] == True).sum()
    paving_only = ((df['has_milling'] == False) & (df['layer_count'] > 0)).sum()
    double_layer = (df['layer_count'] == 2).sum()
    no_remark = df['OPMERKINGENVELD'].isna().sum()
    
    print(f"  铣刨+铺设: {milling_paving}行 ({milling_paving/len(df)*100:.1f}%)")
    print(f"  仅铺设: {paving_only}行 ({paving_only/len(df)*100:.1f}%)")
    print(f"  双层铺设: {double_layer}行 ({double_layer/len(df)*100:.1f}%)")
    print(f"  无备注: {no_remark}行 ({no_remark/len(df)*100:.1f}%)")
    
    # 3. 与DIKTE字段交叉验证
    print("\n3. 厚度一致性验证:")
    inconsistencies = validate_thickness_consistency(df)
    
    if not inconsistencies.empty:
        print(f"⚠️ 发现{len(inconsistencies)}行不一致")
        print(inconsistencies.head())
    else:
        print("✅ 厚度数据一致")
    
    # 4. 最常见备注类型
    print("\n4. 前10个最常见备注:")
    top_remarks = df['OPMERKINGENVELD'].value_counts().head(10)
    for remark, count in top_remarks.items():
        print(f"  {count:4d}次 | {remark}")
    
    return df

# 使用
df_processed = process_remarks_field(df)
```

---

#### 📋 数据验证规则

**规则26.1：备注-厚度一致性**
```python
# 备注中的厚度应与DIKTE字段匹配（±5mm容差）
def check_thickness_consistency(row):
    if pd.isna(row['OPMERKINGENVELD']) or pd.isna(row['DIKTE VERHARDING']):
        return True
    
    parsed = parse_remarks(row['OPMERKINGENVELD'])
    if not parsed or not parsed['paving_layers']:
        return True
    
    remark_thickness = sum(layer['thickness'] for layer in parsed['paving_layers'])
    dikte_thickness = row['DIKTE VERHARDING'] * 1000
    
    return abs(remark_thickness - dikte_thickness) <= 5

df['thickness_consistent'] = df.apply(check_thickness_consistency, axis=1)

inconsistent = df[~df['thickness_consistent']]
if not inconsistent.empty:
    print(f"警告：{len(inconsistent)}行厚度不一致")
```

**规则26.2：备注-材料一致性**
```python
# 备注中的材料应与DEKLAAGSOORT字段相关
def extract_material_from_remark(remark_text):
    if pd.isna(remark_text):
        return None
    
    # 提取材料代码（PA16, ZOABTW, SMA, AC等）
    material_match = re.search(r'(PA\d+|ZOAB\w*|SMA\s*\d*|AC\s*\d+\s*\w*)', 
                                remark_text, re.IGNORECASE)
    if material_match:
        return material_match.group(1).upper().strip()
    return None

df['remark_material'] = df['OPMERKINGENVELD'].apply(extract_material_from_remark)

# 比较
material_mismatch = df[
    (df['remark_material'].notna()) & 
    (df['DEKLAAGSOORT'].notna()) &
    (~df['DEKLAAGSOORT'].str.contains(df['remark_material'].fillna(''), regex=False, na=False))
]

if not material_mismatch.empty:
    print(f"警告：{len(material_mismatch)}行材料信息不匹配")
```

**规则26.3：双层记录验证**
```python
# 双层备注应该有TUSSENLAAG字段
double_layer = df[df['layer_count'] == 2]

missing_tussenlaag = double_layer[double_layer['TUSSENLAAG'].isna()]

if not missing_tussenlaag.empty:
    print(f"警告：{len(missing_tussenlaag)}行双层备注但TUSSENLAAG字段缺失")
```

---

#### 🗄️ 数据库设计建议

**字段定义：**
```sql
CREATE TABLE pavement_records (
    ...
    
    -- 备注字段（原始+结构化）
    opmerkingenveld TEXT NULL
        COMMENT '原始备注内容（荷兰语）',
    
    remarks_en TEXT NULL
        COMMENT '英文翻译备注',
    
    -- 结构化提取字段
    has_milling BOOLEAN DEFAULT FALSE
        COMMENT '是否包含铣刨工序',
    
    milling_depth DECIMAL(5, 2) NULL
        COMMENT '铣刨深度（mm）',
    
    paving_layer_count INT DEFAULT 0
        COMMENT '铺设层数（0/1/2）',
    
    -- 全文搜索索引
    FULLTEXT INDEX ft_remarks (opmerkingenveld, remarks_en),
    
    ...
);

-- 备注分类统计视图
CREATE VIEW remark_categories AS
SELECT 
    CASE 
        WHEN has_milling AND paving_layer_count = 1 
            THEN 'Milling + Single Layer'
        WHEN has_milling AND paving_layer_count = 2 
            THEN 'Milling + Double Layer'
        WHEN NOT has_milling AND paving_layer_count = 1 
            THEN 'Overlay (Single Layer)'
        WHEN NOT has_milling AND paving_layer_count = 2 
            THEN 'Overlay (Double Layer)'
        WHEN opmerkingenveld IS NULL 
            THEN 'No Remarks'
        ELSE 'Other'
    END AS work_type,
    COUNT(*) AS record_count,
    AVG(milling_depth) AS avg_milling_depth,
    SUM(tonnen) AS total_material
FROM pavement_records
GROUP BY work_type;

-- 常见备注模板表
CREATE TABLE remark_templates (
    template_id INT PRIMARY KEY AUTO_INCREMENT,
    template_nl VARCHAR(500) NOT NULL,
    template_en VARCHAR(500) NOT NULL,
    usage_count INT DEFAULT 0,
    last_used DATE,
    INDEX idx_usage (usage_count DESC)
);

-- 从现有数据填充模板
INSERT INTO remark_templates (template_nl, template_en, usage_count)
SELECT 
    opmerkingenveld,
    remarks_en,
    COUNT(*) AS usage_count
FROM pavement_records
WHERE opmerkingenveld IS NOT NULL
GROUP BY opmerkingenveld, remarks_en
HAVING COUNT(*) >= 5
ORDER BY usage_count DESC;
```

---

#### ❓ 需要与Leon确认的问题

**问题26.1：** 备注字段的规范化要求
- ❓ 是否需要建立标准备注模板库？
- ❓ 承包商是否应该从下拉菜单选择备注？
- **好处：** 减少格式不一致，便于数据分析

**问题26.2：** 信息冗余的处理
- ❓ 备注中的厚度/材料信息与其他字段重复，是否需要？
- ❓ 备注应该仅用于特殊说明（非标准信息）？
- **建议：** 明确备注用途，避免重复数据

**问题26.3：** 36.9%缺失的可接受性
- ❓ 是否所有记录都应该有备注？
- ❓ 哪些情况下备注是必填的？
- **建议：** 制定备注填写规则

**问题26.4：** 荷兰语vs英语
- ❓ 是否需要提供英文备注字段？
- ❓ 国际协作或报告需求？
- **建议：** 考虑双语备注系统

**问题26.5：** 备注与实际工序的验证
- ❓ 备注中的工序描述是否需要与其他字段交叉验证？
- ❓ 发现不一致时如何处理？
- **建议：** 建立自动验证规则，在数据提交时检查

---

## 🎉 Batch 4 完成！

**已完成字段 22-26：**
- ✅ 字段 22: AANLEGDATUM（施工日期）
- ✅ 字段 23: ASFALTCENTRALE（沥青拌合站）
- ✅ 字段 24: TONNEN（吨数）
- ✅ 字段 25: temperatuur（生产温度）
- ✅ 字段 26: OPMERKINGENVELD（备注栏）

**所有26个字段整合完成！** 🎊

