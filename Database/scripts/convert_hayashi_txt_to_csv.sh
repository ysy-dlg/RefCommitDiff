#!/bin/bash

# 检查命令行参数是否正确
if [ "$#" -ne 2 ]; then
    echo "使用方法: $0 <输入目录> <输出目录>"
    exit 1
fi

# 指定输入目录和输出目录
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

# 检查输入目录中是否存在 .txt 文件
shopt -s nullglob
TXT_FILES=("$INPUT_DIR"/*.txt)
if [ "${#TXT_FILES[@]}" -eq 0 ]; then
    echo "输入目录中没有 .txt 文件：$INPUT_DIR"
    exit 1
fi

# 遍历目录中的每个 .txt 文件
for INPUT_FILE in "${TXT_FILES[@]}"; do
    # 提取文件名（不带路径和后缀）
    FILENAME=$(basename -- "$INPUT_FILE")
    FILENAME_NO_EXT="${FILENAME%.*}"

    # 设置输出文件路径
    OUTPUT_FILE="$OUTPUT_DIR/${FILENAME_NO_EXT}_commits_finergit_hayashi.csv"

    # 写入CSV文件头
    echo "repository_name,commit_id,file_similarity_score,change_type,change_type_info,old_file_path,new_file_path" > "$OUTPUT_FILE"

    # 逐行解析输入文件
    while IFS=$'\t' read -r _ commit_id similarity_score change_details old_path new_path; do
        # 提取 change_type 和 change_type_info
        change_type=$(echo "$change_details" | cut -d':' -f1)
        change_type_info=$(echo "$change_details" | cut -d':' -f2- | sed "s/^ //")

        # 提取 repository_name
        repository_name="$FILENAME_NO_EXT"

        # 转换为CSV格式并追加到输出文件
        echo "$repository_name,$commit_id,$similarity_score,\"$change_type\",\"$change_type_info\",\"$old_path\",\"$new_path\"" >> "$OUTPUT_FILE"
    done < "$INPUT_FILE"

    echo "转换完成: $OUTPUT_FILE"
done

echo "所有文件转换完成！"

