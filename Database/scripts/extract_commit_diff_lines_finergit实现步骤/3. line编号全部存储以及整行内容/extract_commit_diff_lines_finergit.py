import os
import csv
import sys
import re
from datetime import datetime, timezone

def process_logs(input_dir, output_dir):
    # 检查并处理输出目录
    if os.path.exists(output_dir):
        print(f"清空输出目录最后一级子目录内容：{output_dir}")
        for item in os.listdir(output_dir):
            item_path = os.path.join(output_dir, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                for sub_item in os.listdir(item_path):
                    os.remove(os.path.join(item_path, sub_item))
    else:
        print(f"创建输出目录：{output_dir}")
        os.makedirs(output_dir)

    # 遍历指定目录下的 [repo_name] 子目录
    for repo_name in os.listdir(input_dir):
        repo_path = os.path.join(input_dir, repo_name)
        if os.path.isdir(repo_path):
            csv_filename = os.path.join(output_dir, f"{repo_name}_commit_diff_lines_finergit.csv")
            
            with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['commit_id', 'commit_date', 'file_name_mjava', 'file_path', 'repository_name', 'hunk_id', 'hunk_header', 'line_id', 'line_content'])  # 写入表头
                
                for log_file in os.listdir(repo_path):
                    log_file_path = os.path.join(repo_path, log_file)
                    if log_file.endswith(".log") and os.path.isfile(log_file_path):
                        process_log_file(log_file_path, writer, repo_name)

def process_log_file(log_file_path, writer, repository_name):
    with open(log_file_path, 'r', encoding='utf-8') as log_file:
        lines = log_file.readlines()
        
        commit_id = None
        commit_date = None
        file_name_mjava = None
        file_path = None
        
        hunk_id = 0
        hunk_headers = []
        hunk_lines = []
        
        for line in lines:
            if line.startswith("commit_id:"):
                commit_id = line.split(":", 1)[1].strip()
            elif line.startswith("commit_date:"):
                raw_date = line.split(":", 1)[1].strip()
                commit_date = convert_to_utc(raw_date)
            elif line.startswith("file_name_mjava:"):
                file_name_mjava = line.split(":", 1)[1].strip()
            elif line.startswith("file_path:"):
                file_path = line.split(":", 1)[1].strip()
            elif line.startswith("@@"):
                if hunk_headers and hunk_lines:  # 写入上一个 hunk
                    write_hunk(writer, commit_id, commit_date, file_name_mjava, file_path, repository_name, hunk_id, hunk_headers[-1], hunk_lines)
                    hunk_id += 1
                hunk_headers.append(line.strip())
                hunk_lines = []  # 重置线集合
            elif hunk_headers:
                hunk_lines.append(line.strip())
        
        if hunk_headers and hunk_lines:  # 写入最后一个 hunk
            write_hunk(writer, commit_id, commit_date, file_name_mjava, file_path, repository_name, hunk_id, hunk_headers[-1], hunk_lines)

def write_hunk(writer, commit_id, commit_date, file_name_mjava, file_path, repository_name, hunk_id, hunk_header, hunk_lines):
    line_id = 0  # 重置 line_id，从 0 开始
    for line_content in hunk_lines:
        # 跳过空行
        if not line_content.strip():
            continue
        
        # 写入有效代码行
        writer.writerow([commit_id, commit_date, file_name_mjava, file_path, repository_name, hunk_id, hunk_header, line_id, line_content])
        line_id += 1

def convert_to_utc(raw_date):
    # 将日期字符串转换为UTC格式并去掉时区信息
    date_obj = datetime.strptime(raw_date, "%a %b %d %H:%M:%S %Y %z")
    utc_date = date_obj.astimezone(timezone.utc).replace(tzinfo=None)
    return utc_date.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("\u4f7f\u7528\u65b9\u6cd5: python3 extract_commit_diff_lines_finergit.py <\u8f93\u5165\u76ee\u5f55> <\u8f93\u51fa\u76ee\u5f55>")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    if not os.path.isdir(input_dir):
        print(f"\u8f93\u5165\u76ee\u5f55\u4e0d\u5b58\u5728\u6216\u4e0d\u662f\u6709\u6548\u76ee\u5f55: {input_dir}")
        sys.exit(1)

    process_logs(input_dir, output_dir)

