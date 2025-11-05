#!/usr/bin/env python3
"""
AI Mapping Engine - Phase 2: Intelligent Mapping
使用规则+AI推理建立contractor数据到标准字段的映射关系

只处理15个关键字段
"""

import json
from pathlib import Path
from collections import defaultdict
from difflib import SequenceMatcher
import re

# 15个关键字段的标准枚举值（从enum_values_2022.json和分析中提取）
STANDARD_ENUM_VALUES = {
    "DISTRICT": ["NN-Oost", "Zee en Delta", "Noord", "Oost", "Zuid", "West"],
    "BAAN": ["1HRR", "1HRL", "0HRM", "0VW", "PWL"],
    "STROOK": [
        # 常规车道
        "1R-L", "2R-L", "3R-L", "4R-L", "1R-R", "2R-R", "3R-R", "4R-R",
        # 交织车道
        "1W-L", "2W-L", "1W-R", "2W-R",
        # 加速车道
        "1I-L", "1I-R",
        # 减速车道
        "1U-L", "1U-R",
        # 高峰车道
        "1Q-L", "1Q-R",
        # 应急车道
        "1V-L", "1V-R",
        # 全部车道
        "ALL"
    ],
    "DEKLAAGSOORT": [
        "DZOAB", "ZOAB", "ZOAB+", "ZOABTW TL", "ZOABTW DL", "ZOABTW OL",
        "ZOABTW", "ZOABTW fijn", "ZOABDI", "ZOEAB",
        "SMA", "SMA-NL 11B", "SMA-NL 11", "SMA 8G+", "SMA 8 Geel",
        "AC 16 Surf", "AC 11 Surf", "DGD", "EAB"
    ]
}


class AIMapper:
    """AI辅助映射引擎"""

    def __init__(self, discovery_file, value_file):
        """初始化"""
        self.discovery_file = Path(discovery_file)
        self.value_file = Path(value_file)

        # 加载发现数据
        with open(self.discovery_file, 'r', encoding='utf-8') as f:
            self.discovery_data = json.load(f)

        with open(self.value_file, 'r', encoding='utf-8') as f:
            self.value_data = json.load(f)

        # 映射结果
        self.field_name_mappings = {}
        self.value_mappings = {}

    def calculate_string_similarity(self, s1, s2):
        """计算字符串相似度"""
        return SequenceMatcher(None, s1.lower(), s2.lower()).ratio()

    def map_field_names(self):
        """
        建立字段名映射关系
        已经在contractor_scanner.py中完成，这里只需要整理和验证
        """
        print("\n" + "="*80)
        print("Phase 2.1: 字段名映射整理")
        print("="*80)

        field_mappings = defaultdict(lambda: {
            "contractors": {},
            "total_matched": 0,
            "match_rate": 0.0
        })

        total_contractors = len(self.discovery_data["contractors"])

        # 从发现数据中提取已匹配的字段
        for contractor_id, contractor_data in self.discovery_data["contractors"].items():
            for field in contractor_data["discovered_fields"]:
                std_field_num = field["standard_field_number"]
                std_field_name_nl = field["standard_field_name_nl"]

                if std_field_name_nl not in field_mappings:
                    field_mappings[std_field_name_nl]["standard_field_number"] = std_field_num
                    field_mappings[std_field_name_nl]["standard_field_name_cn"] = field["standard_field_name_cn"]

                field_mappings[std_field_name_nl]["contractors"][contractor_id] = {
                    "original_field_name": field["original_field_name"],
                    "column_index": field["column_index"],
                    "confidence": field["mapping_confidence"],
                    "mapping_method": field["mapping_method"],
                    "verified": field["mapping_confidence"] >= 95  # 自动验证高置信度映射
                }

                field_mappings[std_field_name_nl]["total_matched"] += 1

        # 计算匹配率
        for field_name in field_mappings:
            matched = field_mappings[field_name]["total_matched"]
            field_mappings[field_name]["match_rate"] = round(matched / total_contractors * 100, 1)

        self.field_name_mappings = dict(field_mappings)

        # 打印统计
        print(f"\n字段名映射统计:")
        for field_name in sorted(self.field_name_mappings.keys(),
                                  key=lambda x: self.field_name_mappings[x]["standard_field_number"]):
            info = self.field_name_mappings[field_name]
            print(f"  {info['standard_field_number']:2d}. {field_name:20s} ({info['standard_field_name_cn']:10s}): "
                  f"{info['total_matched']:2d}/{total_contractors:2d} ({info['match_rate']:5.1f}%)")

        return self.field_name_mappings

    def map_field_values(self):
        """
        建立字段值映射关系
        使用规则 + AI推理
        """
        print("\n" + "="*80)
        print("Phase 2.2: 字段值映射推理")
        print("="*80)

        value_mappings = {}

        # 只处理有标准枚举值的字段
        enum_fields = ["DISTRICT", "BAAN", "STROOK", "DEKLAAGSOORT"]

        for field_name in enum_fields:
            if field_name not in self.value_data:
                continue

            print(f"\n处理字段: {field_name}")

            field_data = self.value_data[field_name]
            standard_values = STANDARD_ENUM_VALUES.get(field_name, [])

            # 收集所有原始值
            all_original_values = set()
            for contractor_id, contractor_info in field_data["contractors"].items():
                for val in contractor_info["sample_values"]:
                    all_original_values.add(val)

            print(f"  标准值数量: {len(standard_values)}")
            print(f"  原始唯一值数量: {len(all_original_values)}")

            # 建立映射
            mappings = {}
            for original_value in sorted(all_original_values):
                mapped_value, confidence, method, reasoning = self.infer_value_mapping(
                    field_name, original_value, standard_values
                )

                if mapped_value:
                    mappings[original_value] = {
                        "standard_value": mapped_value,
                        "confidence": confidence,
                        "mapping_method": method,
                        "reasoning": reasoning,
                        "verified": confidence >= 0.95,  # 自动验证高置信度
                        "needs_review": confidence < 0.85  # 低置信度需要审核
                    }

            value_mappings[field_name] = {
                "standard_field_name": field_name,
                "standard_field_number": field_data["standard_field_number"],
                "standard_field_name_cn": field_data["standard_field_name_cn"],
                "standard_values": standard_values,
                "total_original_values": len(all_original_values),
                "total_mapped": len(mappings),
                "mapping_rate": round(len(mappings) / len(all_original_values) * 100, 1) if all_original_values else 0,
                "value_mappings": mappings
            }

            # 统计
            high_conf = sum(1 for m in mappings.values() if m["confidence"] >= 0.9)
            med_conf = sum(1 for m in mappings.values() if 0.7 <= m["confidence"] < 0.9)
            low_conf = sum(1 for m in mappings.values() if m["confidence"] < 0.7)

            print(f"  映射完成: {len(mappings)}/{len(all_original_values)}")
            print(f"    高置信度 (≥0.9): {high_conf}")
            print(f"    中置信度 (0.7-0.9): {med_conf}")
            print(f"    低置信度 (<0.7): {low_conf}")

        self.value_mappings = value_mappings
        return self.value_mappings

    def infer_value_mapping(self, field_name, original_value, standard_values):
        """
        推断值映射关系
        返回: (mapped_value, confidence, method, reasoning)
        """
        original_clean = str(original_value).strip()

        # 1. 精确匹配
        if original_clean in standard_values:
            return original_clean, 1.0, "exact_match", "精确匹配标准值"

        # 2. 大小写不敏感匹配
        for std_val in standard_values:
            if original_clean.lower() == std_val.lower():
                return std_val, 0.98, "case_insensitive_match", f"大小写不同: '{original_clean}' → '{std_val}'"

        # 3. 去除空格匹配
        original_no_space = original_clean.replace(" ", "").replace("\n", "").replace("\t", "")
        for std_val in standard_values:
            std_no_space = std_val.replace(" ", "")
            if original_no_space.lower() == std_no_space.lower():
                return std_val, 0.95, "whitespace_normalized", f"去除空格后匹配: '{original_clean}' → '{std_val}'"

        # 4. 字段特定规则
        if field_name == "BAAN":
            return self.infer_baan_mapping(original_clean, standard_values)
        elif field_name == "DEKLAAGSOORT":
            return self.infer_deklaagsoort_mapping(original_clean, standard_values)
        elif field_name == "STROOK":
            return self.infer_strook_mapping(original_clean, standard_values)
        elif field_name == "DISTRICT":
            return self.infer_district_mapping(original_clean, standard_values)

        # 5. 模糊匹配（最后手段）
        best_match = None
        best_score = 0
        for std_val in standard_values:
            score = self.calculate_string_similarity(original_clean, std_val)
            if score > best_score:
                best_score = score
                best_match = std_val

        if best_score >= 0.75:
            return best_match, best_score, "fuzzy_match", f"模糊匹配 (相似度: {best_score:.2f})"

        # 无法映射
        return None, 0.0, "no_match", "无法找到匹配的标准值"

    def infer_baan_mapping(self, original_value, standard_values):
        """BAAN字段特定推理"""
        # VW → 0VW
        if original_value.upper() == "VW":
            return "0VW", 0.90, "semantic_inference", "VW是Verbindingsweg缩写，标准写法0VW"

        # 1HRM → 0HRM (可能是输入错误)
        if original_value == "1HRM":
            return "0HRM", 0.70, "error_correction", "1HRM可能是0HRM的输入错误（主干道中间车道）"

        # PWL已经是标准值
        if original_value == "PWL":
            return "PWL", 1.0, "exact_match", "PWL是标准值（平行车道）"

        return None, 0.0, "no_match", f"未知BAAN值: {original_value}"

    def infer_deklaagsoort_mapping(self, original_value, standard_values):
        """DEKLAAGSOORT字段特定推理"""
        original_clean = original_value.strip()

        # 处理常见变体
        mappings = {
            "Duurzaam ZOAB": ("DZOAB", 0.95, "semantic_equivalence", "Duurzaam ZOAB = DZOAB"),
            "duurzaam ZOAB": ("DZOAB", 0.95, "semantic_equivalence", "duurzaam ZOAB = DZOAB (大小写)"),
            "D ZOAB": ("DZOAB", 0.90, "abbreviation", "D ZOAB = DZOAB (缩写)"),
            "Tweelaags ZOAB": ("ZOABTW", 0.90, "semantic_equivalence", "Tweelaags ZOAB = ZOABTW"),
            "2-laags ZOAB": ("ZOABTW", 0.90, "semantic_equivalence", "2-laags ZOAB = ZOABTW"),
        }

        if original_clean in mappings:
            std_val, conf, method, reason = mappings[original_clean]
            return std_val, conf, method, reason

        # 检查是否包含ZOAB关键字
        if "ZOAB" in original_value.upper():
            for std_val in standard_values:
                if "ZOAB" in std_val and self.calculate_string_similarity(original_clean, std_val) > 0.75:
                    return std_val, 0.80, "fuzzy_match_zoab", f"ZOAB系列模糊匹配: '{original_value}' → '{std_val}'"

        # 检查是否包含SMA关键字
        if "SMA" in original_value.upper():
            for std_val in standard_values:
                if "SMA" in std_val and self.calculate_string_similarity(original_clean, std_val) > 0.75:
                    return std_val, 0.80, "fuzzy_match_sma", f"SMA系列模糊匹配: '{original_value}' → '{std_val}'"

        return None, 0.0, "no_match", f"未知DEKLAAGSOORT值: {original_value}"

    def infer_strook_mapping(self, original_value, standard_values):
        """STROOK字段特定推理"""
        # STROOK可能包含多个车道（逗号分隔）
        if "," in original_value:
            return original_value, 1.0, "multi_lane", "多车道值保持原样（提取时拆分）"

        # 检查是否是标准格式 (数字+字母-L/R)
        pattern = r'^\d+[RWIUQV]-[LR]$'
        if re.match(pattern, original_value):
            if original_value in standard_values:
                return original_value, 1.0, "exact_match", "标准STROOK格式"
            else:
                return original_value, 0.95, "valid_format", "符合STROOK格式但非标准枚举值"

        # ALL
        if original_value.upper() == "ALL":
            return "ALL", 1.0, "exact_match", "全部车道"

        return None, 0.0, "no_match", f"未知STROOK值: {original_value}"

    def infer_district_mapping(self, original_value, standard_values):
        """DISTRICT字段特定推理"""
        # 缩写映射
        abbreviations = {
            "ZED": "Zee en Delta",
            "Z&D": "Zee en Delta",
            "ZeD": "Zee en Delta",
            "NN-O": "NN-Oost",
            "NNO": "NN-Oost",
            "N": "Noord",
            "O": "Oost",
            "Z": "Zuid",
            "W": "West"
        }

        if original_value in abbreviations:
            std_val = abbreviations[original_value]
            return std_val, 0.90, "abbreviation_expansion", f"缩写扩展: '{original_value}' → '{std_val}'"

        return None, 0.0, "no_match", f"未知DISTRICT值: {original_value}"

    def save_mappings(self, output_dir):
        """保存映射结果"""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        # 1. 保存字段名映射
        field_mapping_file = output_path / "contractor_field_name_mapping.json"
        mapping_data = {
            "version": "1.0",
            "generated_date": self.discovery_data["scan_date"],
            "total_contractors": len(self.discovery_data["contractors"]),
            "field_mappings": self.field_name_mappings
        }
        with open(field_mapping_file, 'w', encoding='utf-8') as f:
            json.dump(mapping_data, f, ensure_ascii=False, indent=2)
        print(f"\n✅ 字段名映射已保存: {field_mapping_file}")

        # 2. 保存字段值映射
        value_mapping_file = output_path / "contractor_value_mapping.json"
        value_data = {
            "version": "1.0",
            "generated_date": self.discovery_data["scan_date"],
            "field_count": len(self.value_mappings),
            "value_mappings": self.value_mappings
        }
        with open(value_mapping_file, 'w', encoding='utf-8') as f:
            json.dump(value_data, f, ensure_ascii=False, indent=2)
        print(f"✅ 字段值映射已保存: {value_mapping_file}")

        # 3. 生成审核统计
        self.print_review_statistics()

    def print_review_statistics(self):
        """打印审核统计"""
        print("\n" + "="*80)
        print("审核统计")
        print("="*80)

        # 字段名映射统计
        total_fields = len(self.field_name_mappings)
        auto_verified_fields = sum(
            1 for field in self.field_name_mappings.values()
            if any(c["verified"] for c in field["contractors"].values())
        )

        print(f"\n字段名映射:")
        print(f"  总字段数: {total_fields}")
        print(f"  自动验证: {auto_verified_fields} (高置信度 ≥95%)")
        print(f"  需审核: {total_fields - auto_verified_fields}")

        # 字段值映射统计
        total_value_mappings = 0
        auto_verified_values = 0
        needs_review_values = 0

        for field_name, field_data in self.value_mappings.items():
            mappings = field_data["value_mappings"]
            total_value_mappings += len(mappings)
            auto_verified_values += sum(1 for m in mappings.values() if m["verified"])
            needs_review_values += sum(1 for m in mappings.values() if m["needs_review"])

        print(f"\n字段值映射:")
        print(f"  总映射数: {total_value_mappings}")
        print(f"  自动验证: {auto_verified_values} (置信度 ≥95%)")
        print(f"  需审核: {needs_review_values} (置信度 <85%)")


def main():
    """主函数"""
    print("=" * 80)
    print("AI映射引擎 - Phase 2: Intelligent Mapping")
    print("只处理15个关键字段")
    print("=" * 80)

    # 设置路径
    base_dir = Path("/data/AI Life/Work/RWS_Road_Engineer/01-Projects/Leon_Data_Extraction/Analysis/Contractor_Discovery")
    discovery_file = base_dir / "contractor_field_discovery.json"
    value_file = base_dir / "contractor_value_discovery.json"
    output_dir = base_dir

    # 创建映射器
    mapper = AIMapper(discovery_file, value_file)

    # 执行映射
    mapper.map_field_names()
    mapper.map_field_values()

    # 保存结果
    mapper.save_mappings(output_dir)

    print("\n✅ Phase 2 完成！")
    print(f"   输出目录: {output_dir}")
    print(f"   - contractor_field_name_mapping.json (字段名映射)")
    print(f"   - contractor_value_mapping.json (字段值映射)")
    print(f"\n下一步: Phase 3 生成Markdown审核文档")


if __name__ == "__main__":
    main()
