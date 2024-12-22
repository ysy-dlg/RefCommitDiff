import os
import csv
import sys
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
                writer.writerow(['commit_id', 'commit_date', 'file_name_mjava', 'file_path', 'repository_name'])  # 写入表头
                
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
        
        if commit_id and commit_date and file_name_mjava and file_path:
            writer.writerow([commit_id, commit_date, file_name_mjava, file_path, repository_name])

def convert_to_utc(raw_date):
    # 将日期字符串转换为UTC格式并去掉时区信息
    date_obj = datetime.strptime(raw_date, "%a %b %d %H:%M:%S %Y %z")
    utc_date = date_obj.astimezone(timezone.utc).replace(tzinfo=None)
    return utc_date.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("使用方法: python3 extract_commit_diff_lines_finergit.py <输入目录> <输出目录>")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    if not os.path.isdir(input_dir):
        print(f"输入目录不存在或不是有效目录: {input_dir}")
        sys.exit(1)

    process_logs(input_dir, output_dir)

