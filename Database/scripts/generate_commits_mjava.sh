#!/bin/bash

# 检查命令行参数
if [ "$#" -ne 2 ]; then
    echo "用法: $0 <FinerGit目录> <输出目录>"
    exit 1
fi

# 获取命令行参数
finergit_dir="$1"    # FinerGit 处理后的仓库目录
output_dir="$2"      # 输出结果的根目录

# 确保输出目录存在，仅清空最后一级子目录
if [ -d "$output_dir" ]; then
    echo "清空目录：$output_dir"
    rm -rf "$output_dir"/*
else
    echo "创建目录：$output_dir"
    mkdir -p "$output_dir"
fi

# 遍历 FinerGit 处理的仓库
for repo_name in $(ls "$finergit_dir"); do
    mjava_dir="$finergit_dir/$repo_name"  # FinerGit 处理后的仓库路径
    output_repo_dir="$output_dir/$repo_name"  # 输出目录的子目录

    # 检查 FinerGit 处理后的仓库是否存在
    if [ ! -d "$mjava_dir" ]; then
        echo "FinerGit repository not found: $mjava_dir"
        continue
    fi

    # 创建输出目录
    mkdir -p "$output_repo_dir"

    # 遍历该仓库的所有 .mjava 文件
    find "$mjava_dir" -type f -name "*.mjava" | while read mjava_file; do
        # 提取 .mjava 文件名和相对路径
        file_name_mjava=$(basename "$mjava_file")  # .mjava 文件名
        relative_path=${mjava_file#"$mjava_dir/"}  # 相对路径
        file_path=$(dirname "$relative_path")      # 仅保留目录部分

        # 输出文件路径
        output_file="$output_repo_dir/${file_name_mjava%.mjava}.log"

        echo "Processing $relative_path -> $output_file"

        # 获取提交历史并保存（移除 commit_message 字段）
        git -C "$mjava_dir" log --all --follow \
            --pretty=format:"----------------------------------------%ncommit_id: %H%ncommit_author: %an%ncommit_date: %cd%nfile_name_mjava: $file_name_mjava%nfile_path: $file_path%n" \
            -p -- "$relative_path" |
        awk '
            /^--- / { print ""; print; print ""; next }   # 在 --- 前后添加空行
            /^\+\+\+ / { print; print ""; next }         # 在 +++ 后添加空行
            /^@@/ { print ""; print; next }              # 在每个 @@ 块前添加空行，但 @@ 和内容之间无空行
            { print }
        ' > "$output_file"
    done

done

