#!/usr/bin/env python3
"""
Contractor Data Scanner - Phase 1: Discovery
扫描contractor原始Excel文件，提取字段结构和唯一值

只关注15个关键字段的映射
"""

import pandas as pd
import openpyxl
from pathlib import Path
import json
from datetime import datetime
from collections import defaultdict
import re

# 15个关键字段（从field_mapping_2022.json提取）
CRITICAL_FIELDS = {
    2: {"nl": "DISTRICT", "en": "District", "cn": "区域"},
    3: {"nl": "ZAAKNUMMER", "en": "Case Number", "cn": "案件编号"},
    4: {"nl": "Weg", "en": "Road Number", "cn": "道路编号"},
    5: {"nl": "BAAN", "en": "Carriageway", "cn": "车道类型"},
    6: {"nl": "WEGLET", "en": "Road Letter", "cn": "道路字母标识"},
    7: {"nl": "VAN", "en": "From Position", "cn": "起始位置"},
    8: {"nl": "TOT", "en": "To Position", "cn": "结束位置"},
    9: {"nl": "STROOK", "en": "Lane Number", "cn": "车道编号"},
    10: {"nl": "Aantal rijstroken", "en": "Number of Lanes", "cn": "车道数量"},
    11: {"nl": "KM_Van", "en": "Kilometer From", "cn": "起点公里数"},
    12: {"nl": "KM_Tot", "en": "Kilometer To", "cn": "终点公里数"},
    13: {"nl": "Lengte", "en": "Length", "cn": "长度"},
    15: {"nl": "MENGSELCODE", "en": "Mixture Code", "cn": "混合料代码"},
    17: {"nl": "DEKLAAGSOORT", "en": "Surface Layer Type", "cn": "面层类型"},
    22: {"nl": "AANLEGDATUM", "en": "Construction Date", "cn": "施工日期"}
}


class ContractorScanner:
    """扫描contractor文件并提取数据"""

    def __init__(self, base_path):
        self.base_path = Path(base_path)
        self.results = {
            "scan_date": datetime.now().isoformat(),
            "total_files_scanned": 0,
            "contractors": {}
        }

    def find_contractor_files(self):
        """查找所有contractor原始文件"""
        files_2021 = list(self.base_path.glob("2021/Origineel/*.xlsx"))
        files_2022 = list(self.base_path.glob("2022/Origineel/*.xlsx"))

        # 过滤掉临时文件和隐藏文件
        all_files = [f for f in files_2021 + files_2022
                     if not f.name.startswith('~') and not f.name.startswith('.')]

        print(f"找到 {len(files_2021)} 个2021年文件")
        print(f"找到 {len(files_2022)} 个2022年文件")
        print(f"总计: {len(all_files)} 个contractor文件")

        return sorted(all_files)

    def identify_data_structure(self, file_path):
        """
        识别Excel文件的数据结构
        返回: (header_row_index, data_start_row, sheet_name)
        """
        try:
            # 读取前20行，寻找表头
            df_preview = pd.read_excel(file_path, nrows=20, header=None)

            # 寻找表头行（包含多个非空单元格的行）
            for idx, row in df_preview.iterrows():
                non_null_count = row.notna().sum()
                if non_null_count >= 10:  # 假设表头至少有10个字段
                    header_row = idx
                    data_start_row = idx + 1

                    # 获取sheet名称
                    xl_file = pd.ExcelFile(file_path)
                    sheet_name = xl_file.sheet_names[0]

                    return header_row, data_start_row, sheet_name

            # 如果没找到，默认第一行是表头
            return 0, 1, pd.ExcelFile(file_path).sheet_names[0]

        except Exception as e:
            print(f"  ⚠️  识别数据结构失败: {e}")
            return 0, 1, "Sheet1"

    def extract_field_names(self, file_path, header_row):
        """提取字段名"""
        try:
            df = pd.read_excel(file_path, header=header_row, nrows=0)
            return list(df.columns)
        except Exception as e:
            print(f"  ⚠️  提取字段名失败: {e}")
            return []

    def fuzzy_match_field(self, original_field_name, threshold=70):
        """
        模糊匹配字段名到15个关键字段
        返回: (field_number, confidence) 或 (None, 0)
        """
        original_lower = str(original_field_name).lower().strip()

        best_match = None
        best_score = 0

        for field_num, field_info in CRITICAL_FIELDS.items():
            # 检查荷兰语名称
            nl_name = field_info["nl"].lower()

            # 精确匹配
            if original_lower == nl_name:
                return field_num, 100

            # 包含匹配
            if nl_name in original_lower or original_lower in nl_name:
                score = 85
                if score > best_score:
                    best_score = score
                    best_match = field_num

            # 关键词匹配
            keywords = {
                2: ["district"],
                3: ["zaak", "nummer"],
                4: ["weg"],
                5: ["baan", "carriageway"],
                6: ["weglet", "letter"],
                7: ["van", "from", "start"],
                8: ["tot", "to", "end"],
                9: ["strook", "lane"],
                10: ["aantal", "rijstroken", "lanes"],
                11: ["km", "van", "from"],
                12: ["km", "tot", "to"],
                13: ["lengte", "length"],
                15: ["mengsel", "code", "mixture"],
                17: ["deklaag", "surface", "zoab", "sma"],
                22: ["datum", "date", "aanleg", "construction"]
            }

            if field_num in keywords:
                for keyword in keywords[field_num]:
                    if keyword in original_lower:
                        score = 75
                        if score > best_score:
                            best_score = score
                            best_match = field_num

        if best_score >= threshold:
            return best_match, best_score
        else:
            return None, 0

    def extract_unique_values(self, df, field_name, max_samples=100):
        """
        提取字段的唯一值和频率
        只保留前max_samples个最常见的值
        """
        try:
            if field_name not in df.columns:
                return {
                    "unique_count": 0,
                    "null_count": 0,
                    "sample_values": [],
                    "top_values": {}
                }

            series = df[field_name]

            # 统计
            unique_values = series.dropna().unique()
            value_counts = series.value_counts()

            # 取前max_samples个最常见的值
            top_values = value_counts.head(max_samples).to_dict()

            # 转换为可序列化的格式
            top_values_serializable = {
                str(k): int(v) for k, v in top_values.items()
            }

            sample_values = [str(v) for v in unique_values[:20]]  # 前20个样本

            return {
                "unique_count": len(unique_values),
                "null_count": int(series.isna().sum()),
                "null_percentage": float(series.isna().sum() / len(series) * 100),
                "sample_values": sample_values,
                "top_values": top_values_serializable
            }

        except Exception as e:
            print(f"  ⚠️  提取唯一值失败: {field_name}, {e}")
            return {
                "unique_count": 0,
                "null_count": 0,
                "sample_values": [],
                "top_values": {}
            }

    def scan_contractor_file(self, file_path):
        """扫描单个contractor文件"""
        contractor_name = file_path.stem
        year = "2021" if "2021" in str(file_path) else "2022"

        print(f"\n📂 扫描: {contractor_name} ({year})")
        print(f"   文件: {file_path.name}")

        try:
            # 1. 识别数据结构
            header_row, data_start_row, sheet_name = self.identify_data_structure(file_path)
            print(f"   表头行: {header_row + 1}, 数据起始行: {data_start_row + 1}, Sheet: {sheet_name}")

            # 2. 读取完整数据
            df = pd.read_excel(file_path, header=header_row)
            total_rows = len(df)
            print(f"   总行数: {total_rows}")

            # 3. 提取字段名
            original_fields = list(df.columns)
            print(f"   原始字段数: {len(original_fields)}")

            # 4. 匹配关键字段
            discovered_critical_fields = []
            matched_count = 0

            for col_idx, original_field in enumerate(original_fields):
                # 尝试匹配到15个关键字段
                field_num, confidence = self.fuzzy_match_field(original_field)

                if field_num is not None:
                    matched_count += 1

                    # 提取该字段的唯一值
                    value_stats = self.extract_unique_values(df, original_field)

                    field_info = {
                        "original_field_name": str(original_field),
                        "column_index": col_idx,
                        "standard_field_number": field_num,
                        "standard_field_name_nl": CRITICAL_FIELDS[field_num]["nl"],
                        "standard_field_name_cn": CRITICAL_FIELDS[field_num]["cn"],
                        "mapping_confidence": confidence,
                        "mapping_method": "exact_match" if confidence == 100 else "fuzzy_match",
                        "data_type": str(df[original_field].dtype),
                        "unique_count": value_stats["unique_count"],
                        "null_count": value_stats["null_count"],
                        "null_percentage": round(value_stats["null_percentage"], 2),
                        "sample_values": value_stats["sample_values"],
                        "top_values": value_stats["top_values"]
                    }

                    discovered_critical_fields.append(field_info)

            print(f"   ✅ 匹配到 {matched_count}/15 个关键字段")

            # 5. 保存结果
            contractor_id = f"{contractor_name}_{year}"
            self.results["contractors"][contractor_id] = {
                "contractor_name": contractor_name,
                "year": year,
                "file_path": str(file_path.relative_to(self.base_path.parent.parent)),
                "sheet_name": sheet_name,
                "header_row": header_row,
                "data_start_row": data_start_row,
                "total_rows": total_rows,
                "original_field_count": len(original_fields),
                "matched_critical_fields": matched_count,
                "discovered_fields": discovered_critical_fields
            }

            self.results["total_files_scanned"] += 1

            return True

        except Exception as e:
            print(f"   ❌ 扫描失败: {e}")
            return False

    def generate_value_aggregation(self):
        """
        聚合所有contractor的字段值，按标准字段分组
        生成 contractor_value_discovery.json
        """
        value_aggregation = {}

        # 按标准字段分组
        for field_num, field_info in CRITICAL_FIELDS.items():
            field_name = field_info["nl"]
            field_cn = field_info["cn"]

            value_aggregation[field_name] = {
                "standard_field_number": field_num,
                "standard_field_name_nl": field_name,
                "standard_field_name_cn": field_cn,
                "contractors": {},
                "all_unique_values": set(),
                "total_occurrences": 0
            }

        # 收集数据
        for contractor_id, contractor_data in self.results["contractors"].items():
            for field in contractor_data["discovered_fields"]:
                std_field_num = field["standard_field_number"]
                std_field_name = CRITICAL_FIELDS[std_field_num]["nl"]

                # 添加contractor数据
                value_aggregation[std_field_name]["contractors"][contractor_id] = {
                    "original_field_name": field["original_field_name"],
                    "unique_count": field["unique_count"],
                    "null_percentage": field["null_percentage"],
                    "top_values": field["top_values"],
                    "sample_values": field["sample_values"]
                }

                # 收集所有唯一值
                for val in field["sample_values"]:
                    value_aggregation[std_field_name]["all_unique_values"].add(val)

                # 统计总出现次数
                for count in field["top_values"].values():
                    value_aggregation[std_field_name]["total_occurrences"] += count

        # 转换set为list（JSON可序列化）
        for field_name in value_aggregation:
            value_aggregation[field_name]["all_unique_values"] = sorted(
                list(value_aggregation[field_name]["all_unique_values"])
            )
            value_aggregation[field_name]["unique_value_count"] = len(
                value_aggregation[field_name]["all_unique_values"]
            )

        return value_aggregation

    def save_results(self, output_dir):
        """保存扫描结果"""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        # 1. 保存字段发现结果
        discovery_file = output_path / "contractor_field_discovery.json"
        with open(discovery_file, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, ensure_ascii=False, indent=2)
        print(f"\n✅ 字段发现结果已保存: {discovery_file}")

        # 2. 生成并保存值聚合结果
        value_aggregation = self.generate_value_aggregation()
        value_file = output_path / "contractor_value_discovery.json"
        with open(value_file, 'w', encoding='utf-8') as f:
            json.dump(value_aggregation, f, ensure_ascii=False, indent=2)
        print(f"✅ 值聚合结果已保存: {value_file}")

        # 3. 生成汇总统计
        print(f"\n📊 扫描汇总:")
        print(f"   总文件数: {self.results['total_files_scanned']}")
        print(f"   总contractor数: {len(self.results['contractors'])}")

        # 统计每个关键字段的匹配率
        field_match_stats = defaultdict(int)
        for contractor_data in self.results["contractors"].values():
            for field in contractor_data["discovered_fields"]:
                field_num = field["standard_field_number"]
                field_match_stats[field_num] += 1

        print(f"\n   关键字段匹配统计:")
        for field_num in sorted(CRITICAL_FIELDS.keys()):
            field_name = CRITICAL_FIELDS[field_num]["cn"]
            match_count = field_match_stats.get(field_num, 0)
            total = self.results['total_files_scanned']
            percentage = (match_count / total * 100) if total > 0 else 0
            print(f"   {field_num:2d}. {field_name:15s}: {match_count:2d}/{total:2d} ({percentage:5.1f}%)")


def main():
    """主函数"""
    print("=" * 80)
    print("Contractor数据扫描器 - Phase 1: Discovery")
    print("只扫描15个关键字段")
    print("=" * 80)

    # 设置路径
    base_path = Path("/data/AI Life/Work/RWS_Road_Engineer/01-Projects/Leon_Data_Extraction/Data/FW_ /Validator")
    output_dir = Path("/data/AI Life/Work/RWS_Road_Engineer/01-Projects/Leon_Data_Extraction/Analysis/Contractor_Discovery")

    # 创建扫描器
    scanner = ContractorScanner(base_path)

    # 查找所有文件
    contractor_files = scanner.find_contractor_files()

    if not contractor_files:
        print("❌ 未找到contractor文件！")
        return

    # 扫描所有文件
    print(f"\n开始扫描 {len(contractor_files)} 个contractor文件...")
    print("=" * 80)

    success_count = 0
    for file_path in contractor_files:
        if scanner.scan_contractor_file(file_path):
            success_count += 1

    print("\n" + "=" * 80)
    print(f"扫描完成: {success_count}/{len(contractor_files)} 个文件成功")
    print("=" * 80)

    # 保存结果
    scanner.save_results(output_dir)

    print("\n✅ Phase 1 完成！")
    print(f"   输出目录: {output_dir}")
    print(f"   - contractor_field_discovery.json (字段发现)")
    print(f"   - contractor_value_discovery.json (值聚合)")


if __name__ == "__main__":
    main()
