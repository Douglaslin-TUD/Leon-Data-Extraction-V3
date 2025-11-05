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
RWS管理区域划分，荷兰全国分为多个管理区。

**可能的值：**
- NN-Oost (Noord-Nederland Oost)
- Zee en Delta
- 其他RWS管理区

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
**英文名称：** Road Number
**数据类型：** 文本
**必填：** 是

**含义：**
国家公路编号（Rijksweg），RWS管理的主干道路标识。

**格式：** RWxxx 或 Axxx
**示例值：**
- RW200 (即 A200)
- RW57 (即 A57)
- RW61, RW65, RW835

**注意：**
- "RW" = Rijksweg (国家公路)
- 通常与高速公路A编号对应

---

### 5. BAAN
**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 车道类型/行车道
**英文名称：** Carriageway
**数据类型：** 文本
**必填：** 是

**含义：**
车道的基本分类代码，与HM-LETTER结合使用标识具体车道位置。

**常见值：**
- **0VW** - Verbindingsweg (连接道路/匝道)
- **1HRL** - Hoofdrijbaan Links (主车道左侧)
- **1HRR** - Hoofdrijbaan Rechts (主车道右侧)
- **0HRM** - Hoofdrijbaan Midden (主车道中间)

**代码结构：**
- **数字部分：** 车道序号
  - 0 = 连接道/特殊道
  - 1 = 第一主车道
  - 2 = 第二主车道

- **字母部分：**
  - **VW** = Verbindingsweg (连接道)
  - **HR** = Hoofdrijbaan (主车道)
  - **L** = Links (左侧)
  - **R** = Rechts (右侧)
  - **M** = Midden (中间)

**参考：** Documents/Validator - rijstroken.xlsx 提供BAAN与HM-LETTER的对应关系。

---

### 6. WEGLET (zie toelichting blad 2)
**字段分类：** 🔴 关键字段 (Critical)
**中文名称：** 道路字母标识
**英文名称：** Road Letter / Carriageway Letter
**数据类型：** 字母 (单个字符)
**必填：** 视情况而定

**含义：**
道路的细分标识字母，与BAAN结合使用精确定位道路段。对于0VW类型特别重要。

**常见值：** a, b, c, d, e, f, g, h, j, k, m, n, p, q, r, s, t, u, v, w

**示例组合：**
- 0VWa, 0VWb, 0VWc, ...
- 这些字母标识不同的连接道/匝道

**特别说明：**
模板Blad 2（第二个工作表）应包含详细说明。

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
- 总是在车道右侧
- 包括以前称为"plusstroken"的左侧车道（通常为1号车道：1R-L或1R-R）

**示例：**
- 1Q-L, 1Q-R
- 2Q-L, 2Q-R

##### B - Busstrook (Bus lane / 公交车道)
**英文：** Bus lane
**中文：** 公交专用道

**示例：**
- 1B-L

##### 特殊值：
- **ALL** - Rijbaanbreed (全车道宽度)
  - 表示整个车道宽度的养护工程
  - 此时参考第10列"Aantal rijstroken"

**参考来源：** Documents/Hallo Peng Luuk.txt (Leon提供的详细说明)

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
