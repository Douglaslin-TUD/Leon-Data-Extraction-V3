# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Project Name:** Leon Data Extraction - 养护数据标准化系统
**Project Code:** RWS-Leon-002
**Status:** Early Stage - 术语体系建立阶段
**Domain:** RWS Road Maintenance Data Standardization
**Last Updated:** 2025-11-05

### 核心目标

Leon是ICO（信息中心维护部门）的数据专家。本项目旨在开发一个**数据标准化软件**，用于处理RWS每年从多个承包商收集的道路养护数据。

**核心问题：**
- 承包商提交的Excel文件格式混乱、不统一
- 需要自动提取、验证、转换为标准格式
- 减少人工处理，提高数据质量

**技术方案：**
原始Excel → 数据提取 → 数据库存储 → 验证 → 按标准模板生成新Excel

## Directory Structure

```
Leon_Data_Extraction/
├── Documents/                          # 文档资料
│   ├── Domain_Knowledge_Dictionary.md  # 术语词典（待创建）
│   ├── Data_Format_Standards.md        # 数据格式规范（待创建）
│   ├── Hallo Peng Luuk.txt             # Leon提供的背景信息
│   ├── Validator - rijstroken.xlsx     # 车道验证参照数据
│   └── Vertaallijst_EN-Nl_def2 (1).xlsx # 英荷翻译对照表
│
├── Data/                               # ⚠️ 核心数据文件夹
│   └── FW_ /
│       ├── Template/                   # 标准模板（目标格式）
│       │   ├── Verzamelformulier_2021_v2.xlsx    # 2021年标准模板
│       │   └── Verzamelstaat_2022c.xlsx          # 2022年标准模板
│       │
│       └── Validator/                  # 原始数据（⚠️ 不要修改）
│           ├── 2021/Origineel/         # 2021年12个原始Excel文件
│           └── 2022/Origineel/         # 2022年10个原始Excel文件
│
├── Analysis/                           # 分析文档（待创建）
│   ├── Template_2021_Fields_Inventory.xlsx
│   ├── Template_2021_Complete_Analysis.md
│   ├── Field_Definitions_2021.md
│   └── Sample_Files_2021_Deep_Dive.md
│
├── Reference_Data/                     # 参照数据（待创建）
│   ├── Rijksweg_List.csv
│   ├── Material_Types.csv
│   └── Work_Types.csv
│
├── Validation/                         # 验证规则（待创建）
│   ├── Field_Validation_Rules.xlsx
│   ├── Cross_Field_Logic_Rules.md
│   └── Business_Rules.md
│
├── code/                               # 软件代码（待开发）
│   ├── extractors/
│   ├── validators/
│   ├── generators/
│   └── ui/
│
├── Project_Background.md               # ✅ 项目背景介绍
├── Implementation_Plan.md              # ✅ 详细执行计划
├── Project_Brief.md                    # 项目简报（中文）
├── README.md                          # 项目概述
└── CLAUDE.md                          # 本文件
```

## 关键文档导航

在开始工作前，务必先阅读：

1. **📖 Project_Background.md** - 完整的项目背景和业务介绍
   - Leon的角色和ICO部门
   - 承包商数据问题
   - 技术方案概述
   - 数据文件结构说明

2. **📋 Implementation_Plan.md** - 详细的执行计划
   - 4个阶段的任务分解
   - 系统架构设计
   - 数据库Schema
   - UI设计

3. **本文件 (CLAUDE.md)** - 快速参考指南

## 当前项目阶段

### 阶段0：行业名词理解与定义 🔤 ← 当前阶段

**任务：**
- [ ] 从2021模板提取所有字段名
- [ ] 逐字段理解业务含义（与人类协作）
- [ ] 建立术语词典（荷兰语-英语-中文）
- [ ] 识别枚举值和代码系统
- [ ] 定义数据格式规范

**为什么这个阶段最重要：**
在没有数据字典的情况下，必须先建立共同的术语体系，否则AI无法理解数据的业务含义。

**下一步行动：**
开始分析 `Data/FW_ /Template/Verzamelformulier_2021_v2.xlsx`

## Domain Knowledge - RWS Road Maintenance（养护领域知识）

### 核心业务术语（待完善）

以下术语需要在阶段0中详细定义：

#### 路段标识类
- **Rijksweg** - 国家公路编号（如RW200）
- **Rijbaan** - 车道/行车道
- **Km_Van / Km_Tot** - 起止公里数

#### 养护类型类
- **Groot Onderhoud** - 大修
- **Klein Onderhoud** - 小修
- **Preventief Onderhoud** - 预防性养护
- **Reconstructie** - 重建

#### 路面结构类
- **Deklaag** - 面层
- **Bindlaag** - 基层
- **Onderlaag** - 底层

#### 材料类型类
- **DZOAB** - 密级配沥青混凝土（Dichte Zeer Open Asfalt Beton）
- **ZOAB** - 开级配沥青混凝土（Zeer Open Asfalt Beton）
- **SMA** - 沥青玛蹄脂碎石
- **PA** - 多孔沥青

#### 工程量类
- **Oppervlak** - 面积（m²）
- **Dikte** - 厚度（mm）
- **Gewicht** - 重量（ton）
- **Lengte** - 长度（m）

### Dutch Lane Type Terminology（补充：车道类型）

以下是从之前文档中获得的车道类型知识：

**Weefstroken (W)** - Weaving lanes
- Example codes: `1W-L`, `1W-R`, `2W-L`, `2W-R`
- Lanes where vehicles merge onto highway immediately before others exit
- Creates conflict zones requiring careful traffic analysis
- Typically long on Dutch network to reduce weaving conflicts

**Invoegstroken (I)** - Acceleration/Entrance lanes
- Example codes: `1I-L`, `1I-R`, `2I-L`, `2I-R`
- Identical to acceleration lanes
- Allow entering traffic to accelerate to highway speed before merging

**Uitvoegstroken (U)** - Deceleration/Exit lanes
- Example codes: `1U-L`, `1U-R`, `2U-L`, `2U-R`
- Deceleration lanes adjacent to primary road
- Allow drivers to slow down before exiting

**Spitsstroken (Q)** - Rush hour lanes / Peak lanes
- Example codes: `1Q-L`, `1Q-R`, `2Q-L`, `2Q-R`
- Only available during rush hours
- Always on right side of carriageway
- Includes "plusstroken" (left-side lanes, usually lane 1: `1R-L` or `1R-R`)

### 数据格式要求 ⚠️

**欧洲数字格式（非常重要）：**
- ✅ 正确：`1.234,56`（千位分隔符用点，小数分隔符用逗号）
- ❌ 错误：`1,234.56`（美式格式）
- 示例：`23,456`、`1.234,56`

**日期格式：**
- 常见：`DD-MM-YYYY` 或 `YYYY-MM-DD`
- 时区：欧洲中部时间（CET）

**公里数特点：**
- 可以是负值（高速公路起点前的路段）
- 精度：通常1-3位小数
- 示例：`-0,3`、`23,456`、`199,875`

## 系统架构（待开发）

**技术栈：**
```
Frontend:  Streamlit（Web界面）
Backend:   Python 3.8+
Database:  SQLite（本地数据库）
Libraries: pandas, openpyxl, sqlalchemy, pydantic, streamlit
```

**核心模块：**
- **Extractors** - 从各种Excel格式提取数据
- **Validators** - 多层数据验证
- **Transformers** - 数据清洗和转换
- **Generators** - 按模板生成标准Excel
- **UI** - Streamlit多页面应用

详见 `Implementation_Plan.md` 阶段3的完整设计。

## Related Projects

**PDF to Excel - Harco** (`../PDF_to_Excel-Harco/code/`)
- 姊妹项目：类似的RWS数据提取项目
- 可复用组件：
  - 欧洲数字格式处理工具
  - 数据验证框架
  - Excel输出工具
  - 错误报告生成器

## 重要约束

### ⚠️ 数据安全
1. **不要修改原始数据**
   - `Data/FW_ /Validator/2021/Origineel/` ← 只读
   - `Data/FW_ /Validator/2022/Origineel/` ← 只读
   - 所有处理结果保存到其他目录

2. **保持欧洲数字格式**
   - 读取和写入都使用欧洲格式
   - 不要转换为美式格式

3. **保留荷兰语术语**
   - 输出文件的字段名使用荷兰语（如模板所示）
   - 代码和注释使用英文

## 工作方式

### 迭代式开发
1. 先2021年，后2022年
2. 先简单格式，后复杂格式
3. 先核心功能，后辅助功能
4. 边分析边开发边验证

### 人机协作
- **AI负责：** 数据分析、模式识别、代码开发
- **人类负责：** 业务解释、规则确认、异常判断
- **共同完成：** 术语定义、验证规则、质量标准

### 配置驱动
- 字段映射用JSON配置
- 验证规则用YAML配置
- 不硬编码业务规则
- 易于调整和扩展

## 数据质量标准

### 准确性（Accuracy）
- 必须符合RWS工程标准
- 数值精度匹配工程要求

### 完整性（Completeness）
- 所有必填字段完整
- 与原始文档交叉验证
- 标记可疑或不完整数据

### 一致性（Consistency）
- 统一的数据格式（欧洲数字格式）
- 标准化公路编码（RW前缀）
- 一致的术语使用

## 开发指南（当代码开发开始时）

### 常用命令
```bash
# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 初始化数据库
python code/database/init_db.py

# 启动Streamlit应用
streamlit run code/ui/app.py

# 运行测试
pytest code/tests/
```

### 开发原则

1. **利用姊妹项目**
   - 复用 `../PDF_to_Excel-Harco/code/` 中的验证工具
   - 参考欧洲数字格式处理方法

2. **保持欧洲格式**
   - 使用pandas时注意decimal参数
   - openpyxl读写时保持格式

3. **配置驱动**
   - 字段映射：`config/field_mapping_2021.json`
   - 验证规则：`config/validation_rules.yaml`
   - 不要硬编码业务逻辑

4. **详细日志**
   - 记录所有转换步骤
   - 保持数据审计追踪
   - 生成详细错误报告

5. **测试覆盖**
   - 单元测试（提取器、验证器）
   - 集成测试（端到端流程）
   - 真实数据测试

## 关键联系人

**项目负责人：** Leon（ICO数据专家）
**用户群体：** Leon团队，RWS数据分析团队

## 下一步行动 🚀

**立即开始（阶段0）：**

1. **读取2021模板文件**
   ```
   我（AI）：打开 Data/FW_ /Template/Verzamelformulier_2021_v2.xlsx
           列出所有sheet和字段
           生成字段清单

   你（人类）：解释每个字段的业务含义
              确认必填字段和验证规则
   ```

2. **建立术语词典**
   ```
   协作产出：Documents/Domain_Knowledge_Dictionary.md
            荷兰语-英语-中文三语对照
            业务含义详细说明
   ```

3. **定义验证规则**
   ```
   产出：Analysis/Field_Definitions_2021.md
        每个字段的类型、格式、范围、规则
   ```

**准备好开始分析模板文件了吗？** 📊
