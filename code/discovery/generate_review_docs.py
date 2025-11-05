#!/usr/bin/env python3
"""
Markdown Review Document Generator - Phase 3
生成人类友好的Markdown审核文档
"""

import json
from pathlib import Path
from datetime import datetime


class ReviewDocGenerator:
    """生成Markdown审核文档"""

    def __init__(self, field_mapping_file, value_mapping_file):
        # 加载映射数据
        with open(field_mapping_file, 'r', encoding='utf-8') as f:
            self.field_mappings = json.load(f)

        with open(value_mapping_file, 'r', encoding='utf-8') as f:
            self.value_mappings = json.load(f)

    def generate_main_review_doc(self, output_file):
        """生成主审核文档"""
        content = []

        # 标题
        content.append("# Contractor数据映射审核表")
        content.append(f"**生成日期：** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        content.append(f"**审核人：** Leon")
        content.append(f"**状态：** ⏸️ 待审核\n")
        content.append("---\n")

        # 审核说明
        content.append("## 📋 审核说明\n")
        content.append("### 审核标记：")
        content.append("- ✅ **正确** - 映射关系正确，通过")
        content.append("- ❌ **错误** - 映射关系错误，需要修改")
        content.append("- ⚠️ **需修改** - 基本正确但需要调整\n")

        content.append("### 审核方法：")
        content.append("1. 检查每个映射关系")
        content.append("2. 在\"审核\"列填写 ✅/❌/⚠️")
        content.append("3. 如有问题，在\"备注\"列填写说明")
        content.append("4. 完成后通知AI进行下一步处理\n")
        content.append("---\n")

        # 审核统计
        content.append("## 📊 审核统计\n")

        total_field_mappings = len(self.field_mappings["field_mappings"])
        auto_verified_fields = sum(
            1 for field in self.field_mappings["field_mappings"].values()
            if any(c.get("verified", False) for c in field.get("contractors", {}).values())
        )

        total_value_mappings = sum(
            len(field["value_mappings"])
            for field in self.value_mappings["value_mappings"].values()
        )
        auto_verified_values = sum(
            sum(1 for m in field["value_mappings"].values() if m.get("verified", False))
            for field in self.value_mappings["value_mappings"].values()
        )
        needs_review_values = sum(
            sum(1 for m in field["value_mappings"].values() if m.get("needs_review", False))
            for field in self.value_mappings["value_mappings"].values()
        )

        content.append(f"- **字段名映射总数：** {total_field_mappings}")
        content.append(f"  - 自动验证（置信度≥95%）：{auto_verified_fields}")
        content.append(f"  - 需人工审核：{total_field_mappings - auto_verified_fields}")
        content.append(f"- **字段值映射总数：** {total_value_mappings}")
        content.append(f"  - 自动验证（置信度≥95%）：{auto_verified_values}")
        content.append(f"  - 需人工审核（置信度<85%）：{needs_review_values}\n")
        content.append("---\n")

        # 字段名映射审核
        content.append("## Part 1: 字段名映射审核\n")
        content.append("检查每个contractor的字段名是否正确映射到标准字段。\n")

        for field_name in sorted(self.field_mappings["field_mappings"].keys(),
                                  key=lambda x: self.field_mappings["field_mappings"][x]["standard_field_number"]):
            field_info = self.field_mappings["field_mappings"][field_name]
            content.append(f"### 字段 {field_info['standard_field_number']}: {field_name} ({field_info['standard_field_name_cn']})\n")

            content.append("| Contractor | 原始字段名 | 列位置 | 置信度 | 方法 | 审核 | 备注 |")
            content.append("|------------|-----------|--------|--------|------|------|------|")

            for contractor_id in sorted(field_info.get("contractors", {}).keys()):
                contractor_info = field_info["contractors"][contractor_id]
                confidence = contractor_info.get("confidence", 0)
                method = contractor_info.get("mapping_method", "unknown")
                verified = "✅" if contractor_info.get("verified", False) else "⏸️"

                content.append(
                    f"| {contractor_id[:30]} | "
                    f"{contractor_info['original_field_name']} | "
                    f"{contractor_info.get('column_index', 'N/A')} | "
                    f"{confidence}% | "
                    f"{method} | "
                    f"{verified} | |"
                )

            content.append(f"\n**匹配率：** {field_info['total_matched']}/{self.field_mappings['total_contractors']} "
                           f"({field_info['match_rate']}%)\n")

        content.append("---\n")

        # 字段值映射审核
        content.append("## Part 2: 字段值映射审核\n")
        content.append("检查原始值到标准值的映射是否正确。重点关注 ⚠️ 标记的低置信度映射。\n")

        for field_name in sorted(self.value_mappings["value_mappings"].keys(),
                                  key=lambda x: self.value_mappings["value_mappings"][x]["standard_field_number"]):
            field_data = self.value_mappings["value_mappings"][field_name]

            content.append(f"### 字段 {field_data['standard_field_number']}: {field_name} ({field_data['standard_field_name_cn']})\n")

            content.append(f"**标准值列表：** {', '.join(field_data['standard_values'])}\n")
            content.append(f"**原始唯一值数量：** {field_data['total_original_values']}\n")
            content.append(f"**已映射数量：** {field_data['total_mapped']} ({field_data['mapping_rate']}%)\n")

            # 按置信度分组
            high_conf = []
            low_conf = []

            for orig_val, mapping_info in sorted(field_data["value_mappings"].items()):
                if mapping_info.get("needs_review", False):
                    low_conf.append((orig_val, mapping_info))
                else:
                    high_conf.append((orig_val, mapping_info))

            # 先显示需要审核的（低置信度）
            if low_conf:
                content.append(f"\n#### ⚠️ 需要审核的映射 ({len(low_conf)}个)\n")
                content.append("| 原始值 | 建议标准值 | 置信度 | 推理方法 | 推理说明 | 审核 | Leon备注 |")
                content.append("|--------|-----------|--------|---------|---------|------|----------|")

                for orig_val, mapping_info in low_conf:
                    content.append(
                        f"| `{orig_val}` | "
                        f"`{mapping_info['standard_value']}` | "
                        f"{mapping_info['confidence']:.2f} | "
                        f"{mapping_info['mapping_method']} | "
                        f"{mapping_info['reasoning']} | "
                        f"⏸️ | |"
                    )

            # 高置信度映射（折叠显示）
            if high_conf:
                content.append(f"\n<details>")
                content.append(f"<summary>✅ 高置信度映射 ({len(high_conf)}个) - 点击展开</summary>\n")
                content.append("| 原始值 | 标准值 | 置信度 | 方法 | 说明 |")
                content.append("|--------|--------|--------|------|------|")

                for orig_val, mapping_info in high_conf[:50]:  # 只显示前50个
                    content.append(
                        f"| `{orig_val}` | "
                        f"`{mapping_info['standard_value']}` | "
                        f"{mapping_info['confidence']:.2f} | "
                        f"{mapping_info['mapping_method']} | "
                        f"{mapping_info['reasoning']} |"
                    )

                if len(high_conf) > 50:
                    content.append(f"\n*（还有 {len(high_conf) - 50} 个高置信度映射未显示）*")

                content.append("</details>\n")

        content.append("---\n")

        # 审核完成确认
        content.append("## ✅ 审核完成确认\n")
        content.append("请在完成审核后填写：\n")
        content.append("- [ ] Part 1 字段名映射审核完成")
        content.append("- [ ] Part 2 字段值映射审核完成")
        content.append("- [ ] 所有问题已标记和说明\n")
        content.append(f"**审核完成日期：** ___________\n")
        content.append(f"**审核人签名：** ___________\n")

        # 写入文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(content))

        print(f"✅ 主审核文档已生成: {output_file}")
        return output_file

    def generate_field_specific_docs(self, output_dir):
        """为每个字段生成独立的审核文档"""
        field_dir = output_dir / "02_Value_Mappings"
        field_dir.mkdir(parents=True, exist_ok=True)

        generated_files = []

        for field_name, field_data in self.value_mappings["value_mappings"].items():
            content = []

            content.append(f"# {field_name} - 字段值映射审核\n")
            content.append(f"**标准字段编号：** {field_data['standard_field_number']}")
            content.append(f"**中文名称：** {field_data['standard_field_name_cn']}")
            content.append(f"**标准定义：** 见 [Template_2022_Complete_Field_Reference.md](../../Template_2022_Complete_Field_Reference.md)\n")
            content.append("---\n")

            content.append("## 标准值列表\n")
            for std_val in field_data["standard_values"]:
                content.append(f"- `{std_val}`")
            content.append("")

            content.append("## 原始值映射表\n")
            content.append("| 原始值 | → | 标准值 | 置信度 | 推理方法 | 推理说明 | 审核 | Leon备注 |")
            content.append("|--------|---|--------|--------|---------|---------|------|----------|")

            for orig_val in sorted(field_data["value_mappings"].keys()):
                mapping_info = field_data["value_mappings"][orig_val]
                verified_mark = "✅" if mapping_info.get("verified", False) else "⏸️"
                if mapping_info.get("needs_review", False):
                    verified_mark = "⚠️"

                content.append(
                    f"| `{orig_val}` | → | "
                    f"`{mapping_info['standard_value']}` | "
                    f"{mapping_info['confidence']:.2f} | "
                    f"{mapping_info['mapping_method']} | "
                    f"{mapping_info['reasoning']} | "
                    f"{verified_mark} | |"
                )

            # 写入文件
            filename = field_dir / f"{field_name}_value_mappings.md"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write('\n'.join(content))

            generated_files.append(filename)
            print(f"  ✅ 生成: {filename.name}")

        return generated_files

    def generate_overview_doc(self, output_dir):
        """生成映射概述文档"""
        content = []

        content.append("# Contractor数据映射概述\n")
        content.append(f"**生成日期：** {datetime.now().strftime('%Y-%m-%d')}")
        content.append(f"**项目：** Leon Data Extraction - Contractor数据标准化")
        content.append(f"**阶段：** Phase 1-2 完成，Phase 3 待审核\n")
        content.append("---\n")

        content.append("## 📊 总体统计\n")
        content.append(f"- **扫描文件数：** {self.field_mappings['total_contractors']}")
        content.append(f"- **关键字段数：** 15")
        content.append(f"- **已映射字段：** {len(self.field_mappings['field_mappings'])}")
        content.append(f"- **总值映射数：** {sum(len(f['value_mappings']) for f in self.value_mappings['value_mappings'].values())}\n")

        content.append("## 📁 文档结构\n")
        content.append("```")
        content.append("Contractor_Mapping_Documentation/")
        content.append("├── 00_Contractor_Mapping_Overview.md          # 本文档")
        content.append("├── 01_Contractor_Mapping_Review.md            # 主审核文档（⏸️ 待审核）")
        content.append("└── 02_Value_Mappings/                         # 字段值映射（按字段分文件）")
        for field_name in sorted(self.value_mappings["value_mappings"].keys()):
            content.append(f"    ├── {field_name}_value_mappings.md")
        content.append("```\n")

        content.append("## 🔍 字段映射概览\n")
        content.append("| # | 字段名 | 中文名 | 匹配率 | 状态 |")
        content.append("|---|--------|--------|--------|------|")

        for field_name in sorted(self.field_mappings["field_mappings"].keys(),
                                  key=lambda x: self.field_mappings["field_mappings"][x]["standard_field_number"]):
            field_info = self.field_mappings["field_mappings"][field_name]
            status = "✅" if field_info["match_rate"] >= 90 else "⚠️"

            content.append(
                f"| {field_info['standard_field_number']} | "
                f"{field_name} | "
                f"{field_info['standard_field_name_cn']} | "
                f"{field_info['match_rate']}% | "
                f"{status} |"
            )

        content.append("\n## 📝 下一步行动\n")
        content.append("1. ⏸️ Leon审核 `01_Contractor_Mapping_Review.md`")
        content.append("2. ⏸️ 标记所有映射关系（✅/❌/⚠️）")
        content.append("3. ⏸️ 填写备注说明")
        content.append("4. ⏸️ 通知AI进行Phase 4（配置保存）\n")

        # 写入文件
        filename = output_dir / "00_Contractor_Mapping_Overview.md"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(content))

        print(f"✅ 概述文档已生成: {filename}")
        return filename


def main():
    """主函数"""
    print("=" * 80)
    print("Markdown审核文档生成器 - Phase 3")
    print("=" * 80)

    # 设置路径
    base_dir = Path("/data/AI Life/Work/RWS_Road_Engineer/01-Projects/Leon_Data_Extraction/Analysis")
    input_dir = base_dir / "Contractor_Discovery"
    output_dir = base_dir / "Contractor_Mapping_Documentation"

    field_mapping_file = input_dir / "contractor_field_name_mapping.json"
    value_mapping_file = input_dir / "contractor_value_mapping.json"

    # 创建输出目录
    output_dir.mkdir(parents=True, exist_ok=True)

    # 创建生成器
    generator = ReviewDocGenerator(field_mapping_file, value_mapping_file)

    # 生成文档
    print("\n生成文档...")

    # 1. 概述文档
    generator.generate_overview_doc(output_dir)

    # 2. 主审核文档
    main_review_file = output_dir / "01_Contractor_Mapping_Review.md"
    generator.generate_main_review_doc(main_review_file)

    # 3. 字段特定文档
    print("\n生成字段特定文档:")
    generator.generate_field_specific_docs(output_dir)

    print("\n" + "=" * 80)
    print("✅ Phase 3 完成！")
    print("=" * 80)
    print(f"\n📁 输出目录: {output_dir}")
    print(f"\n📄 生成的文档:")
    print(f"   1. 00_Contractor_Mapping_Overview.md      - 映射概述")
    print(f"   2. 01_Contractor_Mapping_Review.md        - 主审核文档（⏸️ 待Leon审核）")
    print(f"   3. 02_Value_Mappings/                     - 字段值映射详情\n")

    print("🎯 下一步：Leon审核 01_Contractor_Mapping_Review.md")
    print("   填写审核标记: ✅正确 / ❌错误 / ⚠️需修改")


if __name__ == "__main__":
    main()
