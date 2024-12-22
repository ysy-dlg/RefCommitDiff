#!/bin/bash

# 设置 UTF-8 编码
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

# 检查是否提供了正确的参数
if [ "$#" -ne 3 ]; then
  echo "用法: $0 <源目录> <输出目录> <文件扩展名>"
  exit 1
fi

# 获取源目录、输出目录和文件扩展名
REPO_ROOT=$1
OUTPUT_DIR=$2
FILE_EXTENSION=$3

# 确保仅删除输出目录的最后一级子目录
if [ -d "$OUTPUT_DIR" ]; then
  echo "清空目录：$OUTPUT_DIR"
  rm -rf "$OUTPUT_DIR"/*
else
  echo "创建目录：$OUTPUT_DIR"
  mkdir -p "$OUTPUT_DIR"
fi

# 遍历每个仓库
for repo_path in "$REPO_ROOT"/*; do
  # 确保路径是一个目录
  if [ -d "$repo_path" ]; then
    # 获取仓库的名称
    repo_name=$(basename "$repo_path")

    # 定义输出文件名
    output_file="$OUTPUT_DIR/${repo_name}_commits_original.csv"

    # 在输出文件中写入表头
    echo "commit_id,repository_name,commit_date,commit_message_subject,is_file_modified,is_code_file_modified" > "$output_file"

    # 提取日志，以unix时间戳形式输出，然后在bash中转UTC格式化
    (
      cd "$repo_path" || exit
      git log --all --pretty=format:"%H,$repo_name,%ct,%s" --date=unix |
      while IFS=',' read -r commit_id repo_name commit_unix_ts commit_subject; do
        # 使用macOS下BSD版date的-r选项从unix时间戳获取UTC时间
        commit_date=$(date -u -r "$commit_unix_ts" +"%Y-%m-%d %H:%M:%S")

        # 转义提交消息中的双引号并处理编码问题
        commit_subject=$(echo "$commit_subject" | iconv -f UTF-8 -t UTF-8//IGNORE | sed 's/"/""/g')

        # 初始化标志
        is_file_modified=0
        is_code_file_modified=0

        # 获取当前提交的所有修改文件列表
        modified_files=$(git diff-tree --no-commit-id --name-only -r "$commit_id")

        # 检测是否有文件修改
        if [ -n "$modified_files" ]; then
          is_file_modified=1
          # 检测是否包含指定扩展名的文件
          if echo "$modified_files" | grep -qE "\.${FILE_EXTENSION}$"; then
            is_code_file_modified=1
          fi
        fi

        # 写入输出文件
        echo "$commit_id,$repo_name,$commit_date,\"$commit_subject\",$is_file_modified,$is_code_file_modified" >> "$output_file"
      done
    )

    # 确保输出文件为 UTF-8 格式
    mv "$output_file" "$output_file.bak"
    iconv -f UTF-8 -t UTF-8 "$output_file.bak" > "$output_file"
    rm "$output_file.bak"

    echo "日志已保存到 $output_file"
  fi
done

echo "所有仓库日志提取完成，CSV 文件存储在 $OUTPUT_DIR 目录下。"
