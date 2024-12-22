#!/bin/bash

# 检查是否提供了输入和输出目录
if [ $# -ne 2 ]; then
  echo "用法：$0 <输入目录> <输出目录>"
  exit 1
fi

# 从命令行参数获取输入和输出目录
root_dir="$1"
output_dir="$2"

# 确保输出目录只删除最后一级子目录
if [ -d "$output_dir" ]; then
  echo "清空目录：$output_dir"
  rm -rf "$output_dir"/*
else
  echo "创建目录：$output_dir"
  mkdir -p "$output_dir"
fi

# 遍历所有子目录
for repo_path in "$root_dir"/*; do
  # 检查是否为 Git 仓库
  if [ -d "$repo_path/.git" ]; then
    repo_name=$(basename "$repo_path")
    output_file="$output_dir/${repo_name}_finergit_original_mapping.csv"
    echo "正在处理仓库：$repo_name (路径：$repo_path)"

    # 添加列名到输出文件
    echo "commit_id,original_commit_id,commit_date,repository_name" > "$output_file"

    # 提取日志中包含 <OriginalCommitID:...> 的记录
    git -C "$repo_path" log --all --pretty=format:"%H|%ct|%B" --date=unix |
    while IFS='|' read -r commit_id commit_unix_ts commit_body; do
      # 提取 <OriginalCommitID:...> 中的 ID（去掉尖括号和标签部分，只保留 ID）
      original_commit_id=$(echo "$commit_body" | grep -o "<OriginalCommitID:[^>]*>" | sed -E 's/<OriginalCommitID:([^>]+)>/\1/')
      if [ -n "$original_commit_id" ]; then
        # 转换提交时间为 UTC 格式
        commit_date=$(date -u -r "$commit_unix_ts" +"%Y-%m-%d %H:%M:%S")
        # 写入到输出文件
        echo "$commit_id,$original_commit_id,$commit_date,$repo_name" >> "$output_file"
      fi
    done
    echo "日志生成完成：$output_file"
  fi
done

echo "所有仓库处理完成！输出目录：$output_dir"

