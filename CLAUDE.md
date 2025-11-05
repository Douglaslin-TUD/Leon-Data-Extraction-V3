# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Project Name:** Leon Data Extraction - 养护数据标准化系统
**Project Code:** RWS-Leon-002
**Status:** Phase 0 - 框架搭建完成，规则填充中
**Domain:** RWS Road Maintenance Data Standardization
**Last Updated:** 2025-11-05

### 核心目标

Leon是ICO（信息中心维护部门）的数据专家。本项目旨在开发一个**数据标准化软件**，用于处理RWS每年从多个承包商收集的道路养护数据。

**核心问题：**
- 承包商提交的Excel文件格式混乱、不统一
- 需要自动提取、验证、转换为标准格式
- 减少人工处理，提高数据质量

**技术方案：**
原始Excel → 数据提取 → **规则引擎验证** → 数据库存储 → 按标准模板生成新Excel

**架构设计：** 配置驱动的规则引擎
- ✅ 规则与代码分离
- ✅ JSON配置文件定义所有验证规则
- ✅ 模块化、可扩展
- ✅ AI友好的开发方式

---

## Directory Structure

```
Leon_Data_Extraction/
├── Documents/                               # 📄 文档资料
│   ├── Template_2022_Column_Definitions.md  # ✅ 2022模板字段定义（荷/英/中）
│   ├── Hallo Peng Luuk.txt                  # Leon提供的车道类型说明
│   ├── Validator - rijstroken.xlsx          # 车道验证参照数据
│   └── Vertaallijst_EN-Nl_def2 (1).xlsx    # 英荷翻译对照表
│
├── Data/                                    # 💾 核心数据文件夹
│   └── FW_ /
│       ├── Template/                        # 标准模板（目标格式）
│       │   ├── Verzamelformulier_2021_v2.xlsx    # 2021年标准模板
│       │   └── Verzamelstaat_2022c.xlsx          # 2022年标准模板（1,592行真实数据）
│       │
│       └── Validator/                       # 原始数据（⚠️ 只读，不要修改）
│           ├── 2021/Origineel/              # 2021年12个原始Excel文件
│           └── 2022/Origineel/              # 2022年10个原始Excel文件
│
├── Analysis/                                # 📊 数据分析结果
│   └── Template_2022_Field_Analysis.md     # ✅ 2022模板完整字段分析
│                                            #    - 26个字段详细profiling
│                                            #    - 1,592行数据统计
│                                            #    - 32个待确认问题
│
├── config/                                  # ⚙️ 规则配置（重要！）
│   ├── field_mapping_2022.json             # ✅ 字段映射配置
│   ├── validation_rules_2022.json          # ✅ 验证规则定义（7条示例）
│   └── enum_values_2022.json               # ✅ 枚举值定义（从实际数据提取）
│
├── code/                                    # 💻 软件代码
│   ├── validators/
│   │   └── rule_engine.py                  # ✅ 规则引擎核心（360行）
│   │                                        #    - 7种验证器实现
│   │                                        #    - 配置驱动设计
│   ├── tests/
│   │   └── test_rule_engine.py            # ✅ 单元测试（全部通过）
│   └── README.md                           # ✅ 规则引擎使用指南
│
├── Project_Background.md                   # 项目背景介绍
├── Implementation_Plan.md                  # 详细执行计划
├── Project_Brief.md                        # 项目简报（中文）
├── README.md                               # 项目概述
└── CLAUDE.md                               # 本文件
```

---

## 关键文档导航

### 📖 必读文档

1. **Project_Background.md** - 项目背景
   - Leon的角色和ICO部门
   - 承包商数据问题
   - 技术方案概述

2. **Implementation_Plan.md** - 执行计划
   - 4个阶段的任务分解
   - 系统架构设计

3. **code/README.md** - 规则引擎使用指南
   - 架构设计说明
   - 7种规则类型详解
   - 如何添加新规则
   - 协作流程

### 📊 数据分析文档

4. **Documents/Template_2022_Column_Definitions.md** (v1.1)
   - 26个字段完整定义
   - 荷兰语-英语-中文三语
   - 字段分类（16关键 + 10非关键）
   - 数据格式规范
   - 字段关联关系

5. **Analysis/Template_2022_Field_Analysis.md**
   - 1,592行真实数据分析
   - 每个字段的值分布统计
   - 数据质量问题识别
   - 32个待确认问题

### ⚙️ 配置文件

6. **config/validation_rules_2022.json**
   - 验证规则定义（JSON格式）
   - 当前7条示例规则
   - 易于扩展

7. **config/enum_values_2022.json**
   - 从实际数据提取的枚举值
   - 6个主要字段的完整值列表

---

## 当前项目阶段

### ✅ 阶段0：框架搭建完成

**已完成任务：**
- ✅ 2022模板字段分析（26个字段）
- ✅ 数据Profiling（1,592行真实数据）
- ✅ 字段分类（关键/非关键）
- ✅ 术语词典建立（Documents/Template_2022_Column_Definitions.md）
- ✅ 规则引擎框架开发完成
- ✅ 7种验证器实现
- ✅ 配置文件结构建立
- ✅ 单元测试通过

**当前任务：** 🔄 规则库填充中

与用户协作，逐步添加业务规则到 `config/validation_rules_2022.json`

**工作流程：**
1. 用户描述业务规则（自然语言）
2. AI转换为JSON配置
3. 用户确认规则正确性
4. 运行测试验证
5. 在真实数据上验证

**下一步计划：**
- [ ] 完善验证规则（目标：50-100条规则）
- [ ] 在1,592行数据上运行完整验证
- [ ] 分析2021模板
- [ ] 对比2021/2022差异
- [ ] 扩展到原始contractor文件

---

## 规则引擎架构 🏗️

### 设计原则

**配置驱动 (Configuration-Driven):**
- 所有业务规则在JSON配置中定义
- 无需修改代码即可添加/修改规则
- AI只需理解框架，不需要记住所有业务逻辑

**模块化 (Modular):**
- 每种规则类型一个独立验证器
- 验证器可独立开发、测试
- 易于扩展新的规则类型

**测试友好 (Test-Friendly):**
- 每个验证器有独立测试用例
- 规则修改后立即可测试
- 避免逻辑丢失

### 支持的规则类型

| 类型 | 用途 | 示例 |
|------|------|------|
| `required_field` | 必填字段 | Weg不能为空 |
| `enum` | 枚举值验证 | BAAN必须在[1HRL, 1HRR, 0VW]中 |
| `range` | 数值范围 | DIKTE在20-150mm之间 |
| `conditional_required` | 条件必填 | STROOK=ALL → Aantal必填 |
| `cross_field_logic` | 跨字段逻辑 | TOT >= VAN |
| `calculated_field` | 计算字段验证 | Lengte = (TOT-VAN)*100 |
| `format` | 格式验证 | STROOK匹配正则表达式 |

详见 `code/README.md`

---

## 域知识 - RWS Road Maintenance

### 核心术语（荷兰语-英语-中文）

| 荷兰语 | 英文 | 中文 | 说明 |
|--------|------|------|------|
| Rijksweg | National road | 国家公路 | RWxxx或Axxx |
| Hoofdrijbaan (HR) | Main carriageway | 主车道 | 1HRL/1HRR/0HRM |
| Verbindingsweg (VW) | Connecting road | 连接道/匝道 | 0VW |
| Rijstrook (R) | Regular lane | 常规车道 | 1R-L, 2R-R |
| Weefstrook (W) | Weaving lane | 交织车道 | 1W-L, 2W-R |
| Invoegstrook (I) | Acceleration lane | 加速车道 | 1I-L, 1I-R |
| Uitvoegstrook (U) | Deceleration lane | 减速车道 | 1U-L, 1U-R |
| Spitsstrook (Q) | Rush hour lane | 高峰车道 | 1Q-L, 1Q-R |
| ZOAB | Porous asphalt | 多孔沥青 | 常见面层类型 |
| DZOAB | Dense porous asphalt | 密级配多孔沥青 | 最常见(43.4%) |
| SMA | Stone mastic asphalt | 沥青玛蹄脂碎石 | - |

**详细说明：** 见 `Documents/Template_2022_Column_Definitions.md`

### 数据格式要求 ⚠️

**欧洲数字格式（必须遵守）：**
- ✅ 正确：`1.234,56`（点=千位分隔符，逗号=小数点）
- ❌ 错误：`1,234.56`（美式格式）

**位置系统：**
- VAN/TOT单位：百米 (hectometer, hm)
- 1 hm = 100米
- 可以是负值（起点前的路段）

**字段关联关系：**
```
唯一标识：Weg + BAAN + WEGLET + VAN + TOT + STROOK
位置计算：KM_Van = VAN / 10, KM_Tot = TOT / 10
长度计算：Lengte = (TOT - VAN) × 100 (米)
条件依赖：STROOK=ALL → Aantal rijstroken必填
         BAAN=0VW → WEGLET必填
         TUSSENLAAG存在 → Mengselcode TUSSENLAAG必填
```

---

## 工作方式

### 当前开发模式：快速迭代 + 人机协作

**协作流程：**

```
用户（业务专家）          AI（技术实现）
     │                        │
     ├─ 描述规则 ──────────→  │
     │  （自然语言）           │
     │                        ├─ 转换为JSON配置
     │                        │
     │  ← 确认配置 ───────────┤
     │                        │
     ├─ 确认/修改 ──────────→  │
     │                        │
     │                        ├─ 运行测试
     │                        │
     │  ← 测试结果 ───────────┤
     │                        │
     ├─ 批准 ─────────────→   │
     │                        │
     │                        ├─ 提交到代码库
     └────────────────────────┘
```

**示例对话：**

```
用户: "当BAAN是0VW时，WEGLET必须填写"

AI: 好的，我将其转换为规则配置：
{
  "rule_id": "COND-002",
  "category": "conditional_required",
  "condition": {"field": "BAAN", "value": "0VW"},
  "then": {"field": "WEGLET", "required": true},
  "error_message": "当BAAN='0VW'时，'WEGLET'不能为空"
}

用户: 确认，添加

AI: ✅ 已添加并测试通过
```

### 迭代单位：30分钟

- 每次添加5-10条规则
- 立即测试验证
- 确认后git commit
- 小步快跑，降低风险

---

## 开发指南

### 如何添加新验证规则

**方法1：使用现有规则类型（推荐）**

直接编辑 `config/validation_rules_2022.json`：

```json
{
  "rule_id": "NEW-001",
  "category": "enum",
  "enabled": true,
  "field": "DEKLAAGSOORT",
  "validation": {
    "type": "in_list",
    "allowed_values": ["DZOAB", "ZOAB", "SMA"]
  },
  "error_message": "字段'DEKLAAGSOORT'值'{value}'不在标准列表中",
  "severity": "warning"
}
```

**方法2：创建新规则类型（需要编程）**

1. 在 `code/validators/rule_engine.py` 中继承 `BaseValidator`
2. 实现 `validate()` 方法
3. 在 `RuleEngine` 中注册
4. 添加测试用例

详见 `code/README.md`

### 测试

```bash
# 运行所有单元测试
python3 code/tests/test_rule_engine.py

# 在真实数据上验证（开发中）
python3 code/validate_template.py
```

---

## 数据质量发现 🔍

### 通过分析发现的问题

**严重问题（需要确认）：**
1. VAN/TOT字段出现异常大值（54350.0） - 正常应在0-1000
2. KM_Van/KM_Tot数据与VAN/TOT相同，不是除以10
3. Breedte字段98.4%是4.3米，只有1个值
4. DIKTE VERHARDING出现3mm（太薄）和450mm（太厚）

**格式不一致：**
5. BAAN出现未定义类型：PWL, 1HRR+HRR
6. STROOK出现未文档化类型：1V-L/R（V型车道？）
7. Aantal rijstroken：83.9%是1，不符合"仅ALL时填写"逻辑
8. DEKLAAGSOORT存在空格变体：'ZOAB' vs 'ZOAB '
9. temperatuur格式混乱：155 vs 155/170 vs 155°C

**32个详细问题** - 见 `Analysis/Template_2022_Field_Analysis.md`

---

## 重要约束

### ⚠️ 数据安全
1. **不要修改原始数据**
   - `Data/FW_ /Validator/2021/Origineel/` ← 只读
   - `Data/FW_ /Validator/2022/Origineel/` ← 只读
   - 所有处理结果保存到其他目录

2. **保持欧洲数字格式**
   - 读取和写入都使用欧洲格式
   - 不要转换为美式格式

3. **Git管理**
   - 大数据文件已在 `.gitignore` 中排除
   - 只提交代码、配置、文档

---

## 下一步行动 🚀

### 立即任务

1. **完善验证规则库**
   - 与用户协作，逐条添加业务规则
   - 目标：50-100条规则
   - 覆盖所有字段和依赖关系

2. **在真实数据上验证**
   - 运行规则引擎处理1,592行数据
   - 生成验证报告
   - 根据结果调整规则

3. **分析2021模板**
   - 提取字段定义
   - 对比2021/2022差异
   - 建立年份差异规则

### 中期任务

4. **扩展到原始contractor文件**
   - 分析22个原始文件的格式
   - 建立映射规则
   - 开发extractors

5. **开发数据标准化流程**
   - 实现数据库Schema
   - 开发生成器
   - 构建UI

---

## 版本历史

**v0.3 (2025-11-05)** - 框架搭建完成
- ✅ 规则引擎框架实现
- ✅ 7种验证器
- ✅ 配置文件结构
- ✅ 完整数据分析

**v0.2 (2025-11-05)** - 字段分析
- ✅ 2022模板字段定义
- ✅ 字段分类
- ✅ JSON映射配置

**v0.1 (2025-11-05)** - 项目初始化
- ✅ 项目结构
- ✅ 文档框架
- ✅ Git仓库建立

---

## 联系信息

**项目负责人：** Leon（ICO数据专家）
**用户群体：** Leon团队，RWS数据分析团队
**技术支持：** Claude Code

---

**最后更新：** 2025-11-05
**文档版本：** v0.3
