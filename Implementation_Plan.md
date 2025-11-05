# 项目执行计划 - Leon Data Extraction

**创建日期：** 2025-11-05
**项目编号：** RWS-Leon-002
**计划版本：** v1.1（根据2025-11-05讨论更新）
**最后更新：** 2025-11-05

---

## 📋 执行策略总览

根据讨论确定的执行步骤：

| 阶段 | 名称 | 核心目标 | 状态 |
|------|------|---------|------|
| **阶段0** | 🔤 行业名词理解与定义 | 建立共同的术语体系 | 📝 准备开始 |
| **阶段1** | 📖 读懂数据结构 | 从模板开始，理解每个字段含义 | ⏳ 待开始 |
| **阶段2** | 🔍 理清数据关系 | 掌握数据合理范围和逻辑关系 | ⏳ 待开始 |
| **阶段3** | 🚀 构建交互系统 | 开发数据处理软件 | ⏳ 待开始 |

**系统定位：**
- **初期：** 本地运行（单机桌面应用）
- **后期：** 可扩展为多用户Web应用

**开发方法：**
- 迭代式开发（边分析边开发边验证）
- 先2021年后2022年
- 先简单格式后复杂格式
- 配置驱动，规则可调整

---

## 阶段0：行业名词理解与定义 ⭐

**核心理念：** "磨刀不误砍柴工" - 在没有现成数据字典的情况下，必须先建立术语体系

### 0.1 为什么这个阶段最关键？

在开发任何自动化工具之前，我们需要回答：

❓ **Rijksweg** 是什么？（国家公路编号）
❓ **Deklaag** 和 **Bindlaag** 有什么区别？（面层 vs 基层）
❓ **DZOAB** 和 **ZOAB** 是什么材料？（密级配 vs 开级配沥青）
❓ **Oppervlak** 的单位是什么？（m²）
❓ **Dikte** 通常是多少范围？（20-100mm）

**如果不理解这些术语：**
- ❌ 无法设计正确的数据库字段
- ❌ 无法编写合理的验证规则
- ❌ 无法识别数据异常
- ❌ AI和人类会"鸡同鸭讲"

### 0.2 任务清单

#### 📋 任务0.1：从2021模板提取所有字段名

**输入文件：** `Template/Verzamelformulier_2021_v2.xlsx`

**工作内容：**
1. 打开模板文件，识别所有sheet
2. 列出每个sheet中的所有列名（字段名）
3. 记录字段的数据格式（文本、数字、日期、下拉列表）
4. 观察是否有示例数据
5. 识别公式字段（自动计算）

**输出：** `Analysis/Template_2021_Fields_Inventory.xlsx`

字段清单格式：
```
| Sheet名称 | 列号 | 字段名（荷兰语） | 数据类型 | 必填 | 示例值 | 备注 |
|----------|------|----------------|---------|------|--------|------|
| Sheet1   | A    | Rijksweg       | 文本     | 是   | RW200  | 下拉列表 |
| Sheet1   | B    | Rijbaan        | 文本     | 是   | 1HRL   | 车道编码 |
| Sheet1   | C    | Km_Van         | 数值     | 是   | 23,456 | 欧洲格式 |
```

#### 📖 任务0.2：逐字段理解业务含义（人工标注）

**工作方式：** 你和我一起，逐个字段讨论

**讨论内容：**
- **字段的中文含义**（如：Rijksweg = 国家公路）
- **业务用途**（这个字段在道路养护中用来干什么？）
- **取值规则**（允许的值、格式、范围）
- **实际案例**（举1-2个真实例子）

**输出：** `Analysis/Field_Definitions_2021.md`

示例格式：
```markdown
### Rijksweg（国家公路编号）

**荷兰语：** Rijksweg
**英语：** National Highway / State Road
**中文：** 国家公路编号

**业务含义：**
RWS管理的国家级公路系统的编号，用于唯一标识一条高速公路或主干道。

**数据格式：**
- 类型：文本
- 模式：RW + 1-4位数字
- 正则：^RW\d{1,4}$
- 示例：RW200（A200高速公路）、RW57（A57）

**取值来源：**
- 有限枚举值（约500+条公路）
- 需要维护标准公路清单

**常见错误：**
- 缺少RW前缀（只写200）
- 拼写错误（RW200A）
- 不存在的公路编号

**验证规则：**
1. 必填字段
2. 必须匹配正则表达式
3. 必须在标准公路清单中

---
```

#### 🔤 任务0.3：建立术语词典

**输出：** `Documents/Domain_Knowledge_Dictionary.md`

分类组织术语：

**A. 路段标识类**
- Rijksweg（国家公路）
- Rijbaan（车道）
- Km_Van / Km_Tot（起止公里）
- Hectometerpaal（百米桩）

**B. 养护类型类**
- Groot Onderhoud（大修）
- Klein Onderhoud（小修）
- Preventief Onderhoud（预防性养护）
- Reconstructie（重建）

**C. 路面结构类**
- Deklaag（面层）
- Bindlaag（基层）
- Onderlaag（底层）

**D. 材料类型类**
- DZOAB（密级配沥青混凝土）
- ZOAB（开级配沥青混凝土）
- SMA（沥青玛蹄脂）
- PA（多孔沥青）

**E. 工程量类**
- Oppervlak（面积，m²）
- Dikte（厚度，mm）
- Gewicht（重量，ton）
- Lengte（长度，m）

**F. 时间类**
- Start Datum（开始日期）
- Eind Datum（结束日期）
- Jaar（年份）
- Week（周数）

**G. 组织机构类**
- Aannemer（承包商）
- Contractor（施工单位）
- Regio（区域）
- District（分区）

#### 🔢 任务0.4：识别枚举值和代码系统

某些字段有固定的取值范围，需要建立参照表：

**输出：** `Reference_Data/` 文件夹

需要建立的参照表：
- [ ] `Rijksweg_List.csv` - 公路清单（RW200, RW57...）
- [ ] `Rijbaan_Codes.csv` - 车道代码（1HRL, 1HRR, 0HRM...）
- [ ] `Material_Types.csv` - 材料类型清单
- [ ] `Work_Types.csv` - 养护类型清单
- [ ] `Contractor_Regions.csv` - 承包商和区域对照

参照表格式：
```csv
Code,Name_NL,Name_EN,Name_CN,Description,Active
RW200,Rijksweg 200,State Road 200,200号国家公路,Amsterdam Ring Road,Yes
RW57,Rijksweg 57,State Road 57,57号国家公路,Connects to Belgium,Yes
```

#### 📊 任务0.5：数据类型和格式规范

**输出：** `Documents/Data_Format_Standards.md`

定义每种数据类型的标准格式：

**数值格式：**
- 欧洲格式：`1.234,56`（千位点，小数逗号）
- 小数位数：根据字段类型（面积2位，厚度1位）
- 负值：允许还是禁止？

**日期格式：**
- 标准格式：`DD-MM-YYYY` 或 `YYYY-MM-DD`
- 时区：欧洲中部时间（CET）

**文本格式：**
- 大小写规则
- 特殊字符处理
- 最大长度

---

## 阶段1：读懂数据结构（从模板开始）📖

**目标：** 深入理解模板和原始数据的每个字段、每一行的含义

### 1.1 模板结构深度分析

#### 📝 任务1.1：分析2021年模板（逐Sheet详解）

**输入文件：** `Template/Verzamelformulier_2021_v2.xlsx`

**分析维度：**

**A. Sheet结构**
- [ ] 有多少个sheet？各叫什么名字？
- [ ] 每个sheet的业务用途？
- [ ] Sheet之间的关联关系？（主表、明细表）

**B. 字段详解（每个sheet）**
- [ ] 列顺序和分组
- [ ] 必填字段标记
- [ ] 数据验证规则（下拉列表、公式）
- [ ] 条件格式（颜色标注）
- [ ] 保护字段（只读、公式）

**C. 数据关系**
- [ ] 主键字段（唯一标识一条记录）
- [ ] 外键关系（跨sheet引用）
- [ ] 计算字段（公式依赖）

**D. 隐藏规则**
- [ ] 隐藏列或隐藏sheet
- [ ] VBA宏（如果有）
- [ ] 命名范围（Named Ranges）

**输出：** `Analysis/Template_2021_Complete_Analysis.md`

#### 📝 任务1.2：分析2022年模板

**输入文件：** `Template/Verzamelstaat_2022c.xlsx`

**分析内容：** 同上

**输出：** `Analysis/Template_2022_Complete_Analysis.md`

#### 🔄 任务1.3：对比2021与2022模板差异

**输出：** `Analysis/Template_Changes_2021_to_2022.md`

对比内容：
- [ ] 新增字段
- [ ] 删除字段
- [ ] 重命名字段
- [ ] 数据类型变化
- [ ] 验证规则变化
- [ ] Sheet结构调整

### 1.2 原始数据探索

#### 🔍 任务1.4：样本文件深度解剖（2021年）

**选择3个代表性样本：**

**样本1：标准格式**
- 文件：`Formulier_2021 - uitvraag AB7 MNZ.xlsx`
- 特点：可能是最接近标准模板的格式

**样本2：变体格式**
- 文件：`Lijst werkzaamheden WNN A Wegen 2021.xlsx`
- 特点：文件名不同，可能格式差异较大

**样本3：承包商自定义格式**
- 文件：`Mourik WNZZ Template_deklagen_2021.xlsx`
- 特点：承包商自己的模板

**每个样本的分析内容：**
1. **结构对比**
   - 与标准模板的相似度
   - Sheet数量和名称
   - 字段顺序

2. **字段映射**
   - 原始字段名 → 标准模板字段名
   - 缺失字段
   - 额外字段

3. **数据质量**
   - 缺失值统计
   - 异常值标记
   - 格式不一致

4. **提取难度评估**
   - 容易（直接对应）
   - 中等（需要转换）
   - 困难（需要推断或人工）

**输出：** `Analysis/Sample_Files_2021_Deep_Dive.md`

#### 🔍 任务1.5：样本文件深度解剖（2022年）

**选择3个代表性样本：**
- `Formulier_2022 - uitvraag AB7 - productiedashboard ON-Noord.xlsx`
- `Asfalt 2022 Zuid Nederland.xlsx`
- `asfalt productiedashboard 2022 (WNN).xlsx`

**输出：** `Analysis/Sample_Files_2022_Deep_Dive.md`

#### 📊 任务1.6：全量文件扫描

**目标：** 快速扫描所有22个文件（2021: 12个 + 2022: 10个）

**收集信息：**
- 文件名
- 文件大小
- Sheet数量
- 数据行数
- 格式类型（与哪个样本最相似）
- 特殊情况标记（损坏、空白、加密）

**输出：** `Analysis/All_Files_Inventory.xlsx`

格式：
```
| 年份 | 文件名 | 大小(KB) | Sheet数 | 数据行数 | 格式类型 | 状态 | 备注 |
|------|--------|---------|---------|---------|---------|------|------|
| 2021 | Formulier_2021_AB7_MNZ.xlsx | 53 | 3 | 45 | Type-A | OK | 标准格式 |
| 2021 | Lijst_werkzaamheden_WNN.xlsx | 111 | 5 | 120 | Type-B | OK | 多sheet |
```

---

## 阶段2：理清数据关系与验证规则 🔍

**目标：** 建立完整的数据验证体系，确保数据质量

### 2.1 字段级验证规则

#### ✅ 任务2.1：建立字段验证规则表

**输出：** `Validation/Field_Validation_Rules.xlsx`

为每个标准模板字段定义：

| 字段名 | 数据类型 | 必填 | 格式规则 | 取值范围 | 默认值 | 错误级别 | 示例值 | 错误示例 |
|--------|---------|------|---------|---------|--------|---------|--------|---------|
| Rijksweg | 文本 | 是 | ^RW\d{1,4}$ | 参照表 | - | Error | RW200 | 200, RW |
| Km_Van | 数值 | 是 | 欧洲格式，3位小数 | -10.0~999.999 | - | Error | 23,456 | 23.456 |
| Oppervlak | 数值 | 是 | 欧洲格式，2位小数 | 1~100000 | - | Error | 1.234,56 | 0, -100 |
| Dikte | 数值 | 否 | 欧洲格式，1位小数 | 10~150 | - | Warning | 45,0 | 5, 200 |

**验证类型：**
- **Error（错误）：** 必须修正才能导入
- **Warning（警告）：** 可疑但允许导入
- **Info（信息）：** 仅提示，不影响导入

### 2.2 跨字段逻辑验证

#### 🔗 任务2.2：定义逻辑关系规则

**输出：** `Validation/Cross_Field_Logic_Rules.md`

**规则分类：**

**A. 顺序规则**
```
规则ID: R001
规则名称: 公里数顺序
描述: 结束公里数必须大于等于起始公里数
表达式: Km_Tot >= Km_Van
错误级别: Error
错误消息: "结束公里({Km_Tot})不能小于起始公里({Km_Van})"
```

**B. 计算规则**
```
规则ID: R002
规则名称: 长度计算
描述: 路段长度 = 结束公里 - 起始公里
表达式: Lengte = (Km_Tot - Km_Van) * 1000  # 转换为米
容差: ±5m（允许5米误差）
错误级别: Warning
```

**C. 一致性规则**
```
规则ID: R003
规则名称: 养护类型与材料匹配
描述: 某些养护类型只能用特定材料
表达式:
  IF WerkType = "Groot Onderhoud" THEN
    MaterialType IN ["DZOAB", "SMA", "PA"]
错误级别: Warning
```

**D. 参照完整性**
```
规则ID: R004
规则名称: 公路编号存在性
描述: Rijksweg必须在标准公路清单中
表达式: Rijksweg IN Rijksweg_List.Code
错误级别: Error
```

### 2.3 业务规则验证

#### 🏢 任务2.3：定义业务层面规则

**输出：** `Validation/Business_Rules.md`

**合理范围规则：**

| 字段 | 最小值 | 最大值 | 典型范围 | 异常阈值 | 说明 |
|------|--------|--------|---------|---------|------|
| Oppervlak | 1 m² | 100,000 m² | 100-10,000 m² | <50 或 >50,000 | 面积过小或过大可能是单位错误 |
| Dikte | 10 mm | 150 mm | 30-80 mm | <20 或 >100 | 厚度异常 |
| Lengte | 10 m | 50,000 m | 100-5,000 m | <50 或 >20,000 | 路段过短或过长 |

**时间合理性：**
- 施工日期不能是未来日期
- 结束日期 >= 开始日期
- 施工跨度通常不超过1年
- 避免冬季施工（12月-2月，可能但不常见）

**数据一致性：**
- 同一Rijksweg+Rijbaan的车道数应一致
- 同一项目的承包商应一致
- 同一区域的数据来源应匹配

### 2.4 验证规则配置化

#### ⚙️ 任务2.4：设计验证规则配置文件

**输出：** `config/validation_rules.yaml`

目标：验证规则可配置，易于调整，不需要修改代码

```yaml
# 字段验证规则配置
field_validations:
  Rijksweg:
    type: string
    required: true
    pattern: "^RW\\d{1,4}$"
    reference_table: "Rijksweg_List"
    error_level: error
    error_message: "Rijksweg格式错误或不在标准清单中"

  Km_Van:
    type: decimal
    required: true
    format: "european"  # 欧洲格式：1.234,56
    decimal_places: 3
    min_value: -10.0
    max_value: 999.999
    error_level: error

  Oppervlak:
    type: decimal
    required: true
    format: "european"
    decimal_places: 2
    min_value: 1
    max_value: 100000
    warning_min: 50
    warning_max: 50000
    error_level: error

# 跨字段逻辑规则
cross_field_rules:
  - rule_id: "R001"
    rule_name: "公里数顺序"
    expression: "Km_Tot >= Km_Van"
    error_level: error
    error_message: "结束公里({Km_Tot})不能小于起始公里({Km_Van})"

  - rule_id: "R002"
    rule_name: "长度合理性"
    expression: "(Km_Tot - Km_Van) * 1000 <= 50000"
    error_level: warning
    error_message: "路段长度超过50公里，请确认"

# 业务规则
business_rules:
  施工时间合理性:
    - rule: "Start_Datum <= End_Datum"
      error_level: error
    - rule: "Start_Datum <= TODAY()"
      error_level: warning
      message: "施工开始日期在未来，请确认"
    - rule: "MONTH(Start_Datum) NOT IN [12, 1, 2]"
      error_level: info
      message: "冬季施工，不常见"
```

---

## 阶段3：构建交互系统 🚀

**目标：** 开发可用的数据处理软件

### 3.1 技术架构设计

#### 🏗️ 系统架构

**技术栈：**
```
Frontend:  Streamlit（Web界面，易于开发和使用）
Backend:   Python 3.8+
Database:  SQLite（本地数据库，无需安装服务器）
Libraries:
  - pandas（数据处理）
  - openpyxl（Excel读写，支持样式）
  - sqlalchemy（数据库ORM）
  - pydantic（数据验证）
  - streamlit（UI框架）
```

**项目结构：**
```
code/
├── config/
│   ├── config.yaml                  # 主配置文件
│   ├── validation_rules.yaml        # 验证规则配置
│   └── field_mapping_2021.json      # 2021字段映射
│   └── field_mapping_2022.json      # 2022字段映射
│
├── database/
│   ├── schema.py                    # SQLAlchemy模型
│   ├── init_db.py                   # 数据库初始化
│   └── leon_data.db                 # SQLite数据库文件
│
├── extractors/
│   ├── base_extractor.py            # 抽象基类
│   ├── excel_reader.py              # Excel读取工具
│   ├── format_detector.py           # 自动格式识别
│   └── template_extractors/
│       ├── extractor_2021_typeA.py  # 2021标准格式
│       ├── extractor_2021_typeB.py  # 2021变体格式
│       └── extractor_2022_typeA.py  # 2022标准格式
│
├── validators/
│   ├── field_validator.py           # 字段级验证
│   ├── logic_validator.py           # 逻辑验证
│   ├── business_validator.py        # 业务规则验证
│   └── validation_engine.py         # 验证引擎（协调器）
│
├── transformers/
│   ├── data_cleaner.py              # 数据清洗
│   ├── format_converter.py          # 格式转换（欧洲/美式）
│   └── field_mapper.py              # 字段映射
│
├── generators/
│   ├── template_filler.py           # 填充模板
│   ├── report_generator.py          # 生成报告
│   └── excel_exporter.py            # 导出Excel
│
├── ui/
│   ├── app.py                       # Streamlit主应用
│   ├── pages/
│   │   ├── 1_上传数据.py
│   │   ├── 2_查看数据.py
│   │   ├── 3_数据验证.py
│   │   ├── 4_生成模板.py
│   │   └── 5_系统设置.py
│   └── components/
│       ├── file_uploader.py
│       ├── data_viewer.py
│       └── validation_display.py
│
├── utils/
│   ├── excel_utils.py               # Excel工具函数
│   ├── number_formatter.py          # 数字格式处理
│   ├── logger.py                    # 日志系统
│   └── config_loader.py             # 配置加载器
│
├── tests/
│   ├── test_extractors.py
│   ├── test_validators.py
│   └── fixtures/                    # 测试数据
│
├── requirements.txt                 # Python依赖
├── README.md                        # 项目说明
└── run.py                           # 启动脚本
```

### 3.2 数据库设计

#### 💾 数据库Schema

**核心表：**

```sql
-- 原始文件管理表
CREATE TABLE source_files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    file_size_kb INTEGER,
    year INTEGER NOT NULL,
    contractor TEXT,
    region TEXT,
    format_type TEXT,  -- 'Type-A', 'Type-B', etc.
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT CHECK(status IN ('pending','processing','completed','failed')),
    total_rows INTEGER,
    valid_rows INTEGER,
    error_rows INTEGER,
    warning_rows INTEGER
);

-- 标准化养护数据表
CREATE TABLE maintenance_work (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_file_id INTEGER NOT NULL,
    source_row_number INTEGER,  -- 原始文件中的行号

    -- 路段信息
    rijksweg TEXT NOT NULL,
    rijbaan TEXT,
    km_van DECIMAL(10,3),
    km_tot DECIMAL(10,3),
    lengte DECIMAL(10,2),  -- 米

    -- 养护信息
    werk_type TEXT,         -- 养护类型
    deklaag_type TEXT,      -- 面层类型
    materiaal_type TEXT,    -- 材料类型

    -- 工程量
    oppervlak DECIMAL(12,2),  -- 面积 m²
    dikte DECIMAL(5,1),       -- 厚度 mm
    gewicht DECIMAL(12,2),    -- 重量 ton

    -- 时间信息
    jaar INTEGER,
    start_datum DATE,
    eind_datum DATE,

    -- 组织信息
    aannemer TEXT,          -- 承包商
    regio TEXT,             -- 区域

    -- 质量状态
    validation_status TEXT CHECK(validation_status IN ('valid','warning','error')),
    is_anomaly BOOLEAN DEFAULT 0,

    -- 审计字段
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (source_file_id) REFERENCES source_files(id)
);

-- 验证错误表
CREATE TABLE validation_errors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    work_id INTEGER,
    source_file_id INTEGER,
    error_type TEXT CHECK(error_type IN ('field','logic','business')),
    rule_id TEXT,
    field_name TEXT,
    severity TEXT CHECK(severity IN ('error','warning','info')),
    error_message TEXT,
    current_value TEXT,
    expected_value TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (work_id) REFERENCES maintenance_work(id),
    FOREIGN KEY (source_file_id) REFERENCES source_files(id)
);

-- 处理日志表
CREATE TABLE processing_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER,
    stage TEXT,  -- 'upload','extraction','validation','export'
    status TEXT,  -- 'started','completed','failed'
    message TEXT,
    details TEXT,  -- JSON格式详细信息
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (file_id) REFERENCES source_files(id)
);

-- 参照表：公路清单
CREATE TABLE reference_rijksweg (
    code TEXT PRIMARY KEY,
    name_nl TEXT,
    name_en TEXT,
    name_cn TEXT,
    description TEXT,
    active BOOLEAN DEFAULT 1
);

-- 参照表：材料类型
CREATE TABLE reference_materials (
    code TEXT PRIMARY KEY,
    name_nl TEXT,
    name_en TEXT,
    name_cn TEXT,
    category TEXT,
    active BOOLEAN DEFAULT 1
);

-- 参照表：养护类型
CREATE TABLE reference_work_types (
    code TEXT PRIMARY KEY,
    name_nl TEXT,
    name_en TEXT,
    name_cn TEXT,
    category TEXT,
    active BOOLEAN DEFAULT 1
);
```

### 3.3 核心功能开发

#### 📦 模块1：数据提取（Extractors）

**功能：** 从各种格式的Excel文件中提取数据

**关键类：**
```python
# extractors/base_extractor.py
class BaseExtractor(ABC):
    """抽象基类，所有提取器继承此类"""

    @abstractmethod
    def detect_format(self, file_path: str) -> bool:
        """检测文件是否符合此提取器格式"""
        pass

    @abstractmethod
    def extract(self, file_path: str) -> pd.DataFrame:
        """提取数据，返回标准化DataFrame"""
        pass

    def get_field_mapping(self) -> dict:
        """返回字段映射关系"""
        pass

# extractors/format_detector.py
class FormatDetector:
    """自动检测文件格式并选择合适的提取器"""

    def __init__(self):
        self.extractors = [
            Extractor2021TypeA(),
            Extractor2021TypeB(),
            Extractor2022TypeA(),
        ]

    def detect(self, file_path: str) -> BaseExtractor:
        """返回合适的提取器"""
        for extractor in self.extractors:
            if extractor.detect_format(file_path):
                return extractor
        return None  # 无法识别
```

**开发优先级：**
1. 先开发2021年Type-A（最标准的格式）
2. 测试验证通过后，再开发其他格式
3. 每个提取器配有单元测试

#### ✅ 模块2：数据验证（Validators）

**功能：** 多层验证，生成详细错误报告

**验证流程：**
```
输入数据
    ↓
字段验证（类型、格式、范围）
    ↓
逻辑验证（跨字段关系）
    ↓
业务规则验证
    ↓
输出：valid_data + error_report
```

**关键类：**
```python
# validators/validation_engine.py
class ValidationEngine:
    def __init__(self):
        self.field_validator = FieldValidator()
        self.logic_validator = LogicValidator()
        self.business_validator = BusinessValidator()

    def validate(self, df: pd.DataFrame) -> ValidationResult:
        """运行所有验证，返回结果"""
        results = ValidationResult()

        # 字段级验证
        field_errors = self.field_validator.validate(df)
        results.add_errors(field_errors)

        # 逻辑验证
        logic_errors = self.logic_validator.validate(df)
        results.add_errors(logic_errors)

        # 业务规则验证
        business_errors = self.business_validator.validate(df)
        results.add_errors(business_errors)

        return results
```

#### 📊 模块3：模板生成（Generators）

**功能：** 按照标准模板格式输出Excel文件

**关键功能：**
- 读取模板文件（保持样式）
- 填充数据
- 应用公式
- 应用条件格式
- 保持数据验证（下拉列表）

**关键类：**
```python
# generators/template_filler.py
class TemplateFiller:
    def __init__(self, template_path: str):
        self.template = openpyxl.load_workbook(template_path)

    def fill_data(self, df: pd.DataFrame, sheet_name: str):
        """填充数据到指定sheet"""
        ws = self.template[sheet_name]

        # 找到数据起始行（跳过表头）
        start_row = self._find_data_start_row(ws)

        # 逐行填充
        for idx, row in df.iterrows():
            for col_idx, field in enumerate(df.columns):
                cell = ws.cell(row=start_row + idx, column=col_idx + 1)
                cell.value = row[field]
                # 保持原有格式

    def save(self, output_path: str):
        self.template.save(output_path)
```

#### 📈 模块4：报告生成（Reports）

**报告类型：**

**1. 数据质量报告**
- 文件处理统计（成功/失败/警告）
- 数据完整性评分
- 错误分类汇总
- 趋势图表

**2. 错误详细报告**
- 按文件分组的错误列表
- 按严重程度分类（Error/Warning/Info）
- 每行数据的错误详情
- 修复建议

**3. 数据汇总报告**
- 按区域统计养护工作量
- 按材料类型统计
- 按时间分布统计
- 对比分析（年度、区域）

### 3.4 用户界面开发

#### 🖥️ Streamlit多页面应用

**页面1：首页（Dashboard）**
```python
# ui/app.py
st.set_page_config(page_title="Leon Data Extraction", layout="wide")

st.title("🛣️ RWS养护数据标准化系统")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("已处理文件", "8/22")
with col2:
    st.metric("有效数据行", "1,234")
with col3:
    st.metric("错误数", "45")

# 最近处理记录
st.subheader("最近处理记录")
# 显示表格...
```

**页面2：数据上传**
```python
# ui/pages/1_上传数据.py
uploaded_files = st.file_uploader(
    "拖拽或选择Excel文件",
    type=['xlsx', 'xls'],
    accept_multiple_files=True
)

year = st.selectbox("选择年份", [2021, 2022])

if st.button("开始处理"):
    for file in uploaded_files:
        # 处理逻辑
        progress_bar = st.progress(0)
        status_text = st.empty()
        # ...
```

**页面3：数据查看**
- 交互式数据表格（可筛选、排序）
- 字段统计信息
- 数据分布图表

**页面4：数据验证**
- 运行验证按钮
- 实时显示验证进度
- 错误列表展示（可展开详情）
- 人工修正界面（点击编辑）

**页面5：生成模板**
- 选择模板版本（2021/2022）
- 筛选条件（日期、区域、承包商）
- 生成并下载标准Excel

**页面6：系统设置**
- 配置验证规则
- 管理参照数据（公路清单、材料清单）
- 查看系统日志

### 3.5 开发和测试

#### 🧪 测试策略

**单元测试：**
- 每个提取器单独测试
- 每个验证器单独测试
- 工具函数测试

**集成测试：**
- 完整处理1个文件（2021）
- 完整处理1个文件（2022）
- 批量处理多个文件

**测试数据：**
- 使用真实样本文件
- 创建测试用例（边界情况、错误情况）

#### 🚀 部署方案

**本地运行（初期）：**
```bash
# 1. 安装Python 3.8+
# 2. 安装依赖
pip install -r requirements.txt

# 3. 初始化数据库
python database/init_db.py

# 4. 启动应用
streamlit run code/ui/app.py
```

**打包为可执行文件（可选）：**
- 使用PyInstaller打包为.exe
- Leon团队可以双击运行，无需安装Python

---

## 📅 项目里程碑

| 里程碑 | 关键产出 | 状态 |
|--------|---------|------|
| **M1: 术语体系建立** | 完整的术语词典和字段定义 | 📝 待开始 |
| **M2: 模板结构理解** | 2021和2022模板完整分析文档 | ⏳ 待开始 |
| **M3: 验证规则定义** | 完整的验证规则配置文件 | ⏳ 待开始 |
| **M4: MVP开发完成** | 能处理1种格式的基础功能 | ⏳ 待开始 |
| **M5: 2021年完整支持** | 能处理所有2021年文件 | ⏳ 待开始 |
| **M6: 2022年支持** | 扩展到2022年数据 | ⏳ 待开始 |
| **M7: UI和报告完成** | 完整的用户界面和报告功能 | ⏳ 待开始 |
| **M8: 测试和交付** | 测试通过，交付使用 | ⏳ 待开始 |

---

## 🎯 立即开始：第一步行动

### 本周任务（Week 1）

#### ✅ 已完成
1. ✅ 项目背景文档创建
2. ✅ 执行计划制定

#### 🔜 立即开始（优先级1）

**任务A：读取2021年模板**
```
我（AI）将执行：
1. 打开 Template/Verzamelformulier_2021_v2.xlsx
2. 列出所有sheet名称
3. 提取每个sheet的字段清单
4. 记录数据格式和示例值
5. 生成初步字段清单表格

你（人类）负责：
1. 解释每个字段的业务含义
2. 确认哪些字段是必填的
3. 说明字段之间的关系
4. 指出特殊规则和注意事项
```

**任务B：建立术语词典（协作）**
```
我们一起：
1. 我列出所有字段名（荷兰语）
2. 你解释含义和用途
3. 我记录并建立三语对照
4. 我们一起定义取值规则
5. 形成第一版术语词典
```

---

## 📞 沟通和协作

### 工作方式

**迭代循环：**
```
1. AI分析 → 2. 人类解释 → 3. 共同定义 → 4. 文档记录
                 ↑                              ↓
                 ←──────── 验证和调整 ──────────┘
```

**检查点：**
- 每完成一个阶段，review输出文档
- 发现问题及时调整
- 边做边学，持续改进

### 决策原则

- **有疑问就问**：不确定的地方不猜测，向你确认
- **记录一切**：所有决策和规则都记录在文档中
- **可配置优先**：规则写在配置文件里，不硬编码
- **小步快跑**：先做简单的，验证通过再做复杂的

---

## 🚀 准备好了！

**下一步：开始分析2021年模板文件**

我现在可以：
1. 打开模板文件，列出sheet和字段
2. 提取字段清单，等待你的业务解释
3. 一起建立第一版术语词典

**你准备好了吗？让我们从模板开始！** 📊
