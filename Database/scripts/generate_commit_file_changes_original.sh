#!/bin/bash

# 检查输入参数是否正确
if [[ $# -lt 2 ]]; then
    echo "Usage: $0 <repo_directory> <output_directory> [file_extension]"
    exit 1
fi

# 获取输入和输出目录
REPO_DIR=$1
OUTPUT_DIR=$2
FILE_EXTENSION=${3:-""}  # 可选参数，默认为空

# 确保仅删除输出目录的最后一级子目录
if [ -d "$OUTPUT_DIR" ]; then
    echo "清空目录：$OUTPUT_DIR"
    rm -rf "$OUTPUT_DIR"/*
else
    echo "创建目录：$OUTPUT_DIR"
    mkdir -p "$OUTPUT_DIR"
fi

# 遍历输入目录中的所有 Git 仓库
for repo in "$REPO_DIR"/*; do
    if [[ -d "$repo/.git" ]]; then
        repo_name=$(basename "$repo")
        output_file="$OUTPUT_DIR/${repo_name}_commit_file_changes_original.csv"

        echo "Processing repository: $repo_name"

        # 初始化 CSV 文件，写入表头
        echo "commit_id,file_status,source_dir,source_file,target_dir,target_file,repository_name" > "$output_file"

        # 解析日志并处理文件变更
        git -C "$repo" log --all --name-status --format="%H" | awk -v ext="$FILE_EXTENSION" '
        BEGIN {
            OFS = ","
            commit_id = ""
        }
        /^[a-f0-9]{40}$/ {
            # 处理 commit_id
            commit_id = $1
            next
        }
        /^[A-Z]/ {
            # 提取文件状态和路径
            file_status = $1
            source_dir = ""
            source_file = ""
            target_dir = ""
            target_file = ""

            # 根据状态决定路径分配
            if (file_status == "A") {
                # 新增 (A): 使用 target_file_path
                target_file_path = $2
                split(target_file_path, arr, "/")
                target_file = arr[length(arr)]
                target_dir = substr(target_file_path, 1, length(target_file_path) - length(target_file))
            } else if (file_status == "M" || file_status == "D" || file_status == "T" || file_status == "U") {
                # 修改/删除/类型修改/冲突: 使用 source_file_path
                source_file_path = $2
                split(source_file_path, arr, "/")
                source_file = arr[length(arr)]
                source_dir = substr(source_file_path, 1, length(source_file_path) - length(source_file))
            } else if (file_status ~ /^R|C/) {
                # 重命名 (Rxx) 和复制 (Cxx): 使用 source_file_path 和 target_file_path
                source_file_path = $2
                target_file_path = $3
                split(source_file_path, arr, "/")
                source_file = arr[length(arr)]
                source_dir = substr(source_file_path, 1, length(source_file_path) - length(source_file))
                split(target_file_path, arr, "/")
                target_file = arr[length(arr)]
                target_dir = substr(target_file_path, 1, length(target_file_path) - length(target_file))
            }

            # 如果指定了扩展名且文件不匹配，跳过
            if (ext != "" && target_file !~ "\\." ext "$" && source_file !~ "\\." ext "$") {
                next
            }

            # 输出一行记录
            print commit_id, file_status, source_dir, source_file, target_dir, target_file, "'$repo_name'"
        }
        ' >> "$output_file"

        # 删除无有效数据的文件（仅有表头）
        if [[ $(wc -l < "$output_file") -eq 1 ]]; then
            rm "$output_file"
        fi
    fi

done

echo "Processing completed. CSV files are saved in $OUTPUT_DIR."

