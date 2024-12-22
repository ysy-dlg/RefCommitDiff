#!/bin/bash

# 确保传入参数合法
if [ "$#" -ne 2 ]; then
    echo "用法: $0 <输入目录> <输出目录>"
    exit 1
fi

# 输入和输出目录
INPUT_DIR="$1"
OUTPUT_DIR="$2"

# 检查并处理输出目录
if [ -d "$OUTPUT_DIR" ]; then
    echo "清空输出目录最后一级子目录内容：$OUTPUT_DIR"
    find "$OUTPUT_DIR" -mindepth 1 -maxdepth 1 -exec rm -rf {} \;
else
    echo "创建输出目录：$OUTPUT_DIR"
    mkdir -p "$OUTPUT_DIR"
fi

# 遍历每个 repo_name 目录（排除 INPUT_DIR 自身）
find "$INPUT_DIR" -mindepth 1 -type d | while read -r repo_dir; do
    # 获取相对于 INPUT_DIR 的子目录路径
    sub_dir="${repo_dir#$INPUT_DIR/}"
    
    # 创建对应的输出子目录
    mkdir -p "$OUTPUT_DIR/$sub_dir"

    # 遍历每个 .log 文件
    find "$repo_dir" -type f -name "*.log" | while read -r log_file; do
        # 提取文件名，不带路径
        base_name=$(basename "$log_file" .log)

        # 按分隔符分割提交并保存
        awk -v base="$base_name" -v out_dir="$OUTPUT_DIR/$sub_dir" '
        BEGIN { RS = "----------------------------------------\n"; ORS = ""; count = 0; }
        {
            if (NR > 1) {
                output_file = out_dir "/" base "_" count ".log";
                print > output_file;
                close(output_file);
                count++;
            }
        }
        ' "$log_file"
    done
done

echo "日志文件分割完成，输出保存在 $OUTPUT_DIR 目录中。"

