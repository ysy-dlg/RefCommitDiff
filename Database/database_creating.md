# sqlite
在进入 SQLite 命令行后，输入以下命令可以显示列名，并且以表格形式呈现：

```
.mode column
.headers on
```
在 SQLite 中导入 CSV 文件时，可以通过以下方式忽略标题行并指定字段进行插入：

---

### **1. 使用 `.import` 忽略标题行**
SQLite 的 `.import` 命令不能直接忽略标题行。解决方法是 **手动去掉 CSV 文件的标题行** 或者通过预处理生成无标题的新 CSV 文件。

#### 示例命令
```
sqlite3 your_database_name.db
```

进入 SQLite 后：
```
.mode csv
.import /path/to/your_file.csv your_table_name
```

如果你的 CSV 文件有标题行，需要先去掉标题行。

---

### **2. 使用 SQL 插入并忽略标题行**
SQLite 支持使用 SQL 脚本从 CSV 文件中导入数据，同时可以忽略标题行。

#### 步骤：
1. **准备目标表**
   确保目标表已存在，例如：

   ```
   CREATE TABLE commits_original (
       commit_id VARCHAR(40),
       repository_name VARCHAR(255),
       commit_message_subject TEXT,
       is_file_modified TINYINT(1),
       is_code_file_modified TINYINT(1),
       commit_date TIMESTAMP
   );
   ```

2. **导入 CSV 忽略标题行**
   使用以下 SQL 语句忽略标题行并指定字段：

   ```
   .mode csv
   .headers on
   .import /path/to/your_file.csv temp_table
   ```

3. **将数据插入指定字段**
   假设导入的数据在临时表 `temp_table` 中，你可以执行以下语句将数据插入到目标表：

   ```
   INSERT INTO commits_original (commit_id, repository_name, commit_date)
   SELECT commit_id, repository_name, commit_date
   FROM temp_table
   WHERE commit_id IS NOT NULL; -- 这里是为了排除无效数据
   ```

---
```
git clone https://github.com/square/javapoet.git
git clone https://github.com/bennidi/mbassador.git
git clone https://github.com/nutzam/nutz.git
```

# commit_diff.db
数据库管理工具: sqlite3

git log - -all

## 创建数据库相关命令

创建一个名为 commit_diff.db 的数据库：
```
sqlite3 commit_diff.db
```
删除数据库
```shell-session
rm commit_diff.db
```
## 数据表

The tables in commit_diff_db:
```
sqlite> .tables
commit_diff_lines_finergit    commits_original            
commit_file_changes_finergit  finergit_original_mapping   
commit_file_changes_original  refactor_keywords           
commits_finergit_hayashi      repository  
```

---
### Table `repository`


| 字段名            | 数据类型     | 是否为空 | 主键/外键 | 描述                               |
|--------------------|--------------|----------|-----------|------------------------------------|
| id                | INTEGER          | 否       | 主键      | 仓库的唯一标识符，自增主键。       |
| repository_url    | TEXT         | 否       |           | 仓库地址（如 GitHub、GitLab 等）。 |
| repository_name   | VARCHAR(255) | 是       |           | 仓库的名称，用于标识或描述仓库。   |
| language          | VARCHAR(50)  | 否       |           | 仓库的主要编程语言（如 Java、Python）。 |

**创建数据表命令**
```
CREATE TABLE repository (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    repository_url TEXT NOT NULL,
    repository_name VARCHAR(255),
    language VARCHAR(50) NOT NULL
);
```


**获取所需信息导入数据表方法**

利用chatgpt获取RefactoringMiner研究中利用的data.json里抽取repos的url，存入unique_github_repository_urls.csv

利用chatgpt获取insert_repository_data.sql，根据repos的url获得repo name，然后language填java

**导入数据**
```
sqlite3 /path/to/commit_diff.db < /path/to/insert_repository_data.sql
```
---
### Table `refactor_keywords`

| 字段名           | 数据类型     | 是否为空 | 主键/外键 | 描述                     |
|-------------------|--------------|----------|-----------|--------------------------|
| id               | INTEGER      | 否       | 自增主键  | 关键词组 ID              |
| base_keyword     | VARCHAR(50)  | 否       |           | 基础关键词（例如 extend）|
| variant_keyword  | VARCHAR(50)  | 否       |           | 变体关键词（例如 extend, extended） |

**创建数据表命令**
```
CREATE TABLE refactor_keywords (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    base_keyword VARCHAR(50) NOT NULL,
    variant_keyword VARCHAR(50) NOT NULL
);
```

---
### Table `commits_original`

| 字段名                  | 数据类型     | 是否为空 | 主键/外键 | 描述                                           |
|-------------------------|--------------|----------|-----------|------------------------------------------------|
| commit_id              | VARCHAR(40)  | 否       | 主键      | 原始提交 ID (SHA1 哈希值)。                   |
| repository_id          | INTEGER      | 是       |           | 仓库的唯一标识符，用于标识或描述仓库。              |
| commit_message_subject | TEXT         | 是       |           | 提交信息标题。                                |
| is_file_modified       | TINYINT(1)   | 否       |           | With/Without File Modification               |
| is_code_file_modified  | TINYINT(1)   | 否       |           | With/Without code File Modification          |
| commit_date            | TIMESTAMP    | 否       |           | 提交时的完整日期格式（统一UTC）。             |



**创建数据表命令**
```
CREATE TABLE commits_original (
    commit_id VARCHAR(40) NOT NULL PRIMARY KEY,
    repository_id INTEGER,
    commit_message_subject TEXT,
    is_file_modified TINYINT(1) NOT NULL,
    is_code_file_modified TINYINT(1) NOT NULL,
    commit_date TIMESTAMP NOT NULL
);
```


**获取所需信息导入数据表方法**

**1.`original_commits`数据表信息获取**

脚本`generate_commits_original.sh`

对`is_code_file_modified`的判定依据，可以在执行的时候指定代码文件扩展名


```

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

```


- **运行方式**：
  - 给脚本赋予执行权限：
   
   ```
   chmod +x generate_commits_original.sh
   ```
  - 假设要检测 .java 文件：
   
   ```
   ./generate_commits_original.sh /path/to/repos /path/to/output/commits_original java
   ```
  - 假设要检测 .py 文件：
   ```
   ./generate_commits_original.sh /path/to/repos /path/to/output/commits_original py
   ```
    
   - `/path/to/repos`：Git 仓库目录。
   - `/path/to/output/commits_original`：CSV 文件存放目录。



**2. 导入数据**

导入1中获得的csv

```
sqlite3 your_database_name.db
```

进入 SQLite 后，依次执行以下命令：

**导入 CSV 忽略标题行 使用以下 SQL 语句忽略标题行并指定字段：**
```
.mode csv
.headers on
.import /path/to/output/commits_original/[repo_name]_commits_original.csv temp_table
```

**将数据插入指定字段 假设导入的数据在临时表 temp_table 中，你可以执行以下语句将数据插入到目标表：**
```
INSERT INTO commits_original (commit_id, repository_id, commit_date, commit_message_subject, is_file_modified, is_code_file_modified)
SELECT 
    tt.commit_id,
    r.id AS repository_id,
    tt.commit_date,
    tt.commit_message_subject,
    tt.is_file_modified,
    tt.is_code_file_modified
FROM temp_table AS tt
LEFT JOIN repository AS r
ON tt.repository_name = r.repository_name
WHERE tt.commit_id IS NOT NULL AND r.id IS NOT NULL;
```
**删除临时表**

```
drop table temp_table;
```

---
### Table `commit_file_changes_original`

| 字段名         | 数据类型    | 是否为空 | 主键/外键 | 描述                                                         |
|----------------|-------------|----------|-----------|--------------------------------------------------------------|
| id             | INTEGER     | 否       | 主键      | 自增                                                         |
| commit_id      | VARCHAR(40) | 否       |           | 原始提交 ID (SHA1 哈希值)                                   |
| repository_id  | INTEGER     | 否       |           | 仓库的 ID                                                   |
| file_status    | VARCHAR(10) | 否       |           | 文件状态：A（新增）、M（修改）、D（删除）、Rxx（重命名）、Cxx（复制）等 |
| source_dir     | VARCHAR(255)| 否       |           | `source_file_path` 的路径部分，去掉文件名后的内容            |
| source_file    | VARCHAR(255)| 否       |           | `source_file_path` 的文件名部分                              |
| target_dir     | VARCHAR(255)| 否       |           | `target_file_path` 的路径部分，去掉文件名后的内容（适用于 R 和 C 状态） |
| target_file    | VARCHAR(255)| 否       |           | `target_file_path` 的文件名部分                              |


**创建数据表命令**
```
CREATE TABLE commit_file_changes_original (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    commit_id VARCHAR(40) NOT NULL,
    repository_id INTEGER NOT NULL,
    file_status VARCHAR(10) NOT NULL,
    source_dir VARCHAR(255) NOT NULL,
    source_file VARCHAR(255) NOT NULL,
    target_dir VARCHAR(255) NOT NULL,
    target_file VARCHAR(255) NOT NULL
);
```

**获取所需信息导入数据表方法**

**1.`commit_file_changes_original`数据表信息获取**

脚本`generate_commit_file_changes_original.sh`

可以在执行的时候指定代码文件扩展名，比如`java`或`py`。只输出代码文件的变更信息

```
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


```

- **脚本说明**

| 文件状态 | source_dir                 | source_file       | target_dir                   | target_file         |
|----------|----------------------------|-------------------|------------------------------|--------------------|
| A        | 空                        | 空                | 新文件路径的目录部分         | 新文件名部分       |
| M        | 原文件路径的目录部分       | 原文件名部分      | 空                           | 空                 | 
| D        | 被删除文件路径的目录部分   | 被删除文件名部分  | 空                           | 空                 | 
| Rxx      | 原文件路径的目录部分       | 原文件名部分      | 重命名后路径的目录部分       | 重命名后文件名部分 | 
| Cxx      | 原文件路径的目录部分       | 原文件名部分      | 复制后路径的目录部分         | 复制后文件名部分   | 
| T        | 文件路径的目录部分         | 文件名部分        | 空                           | 空                 | 
| U        | 冲突文件路径的目录部分     | 冲突文件名部分    | 空                           | 空                 | 

！！！！！！！！！！！！！！！这里的重命名包括路径名改变，有时候文件名一致但路径变了


- **运行方式**：
  - 给脚本赋予执行权限：
   
   ```
   chmod +x generate_commit_file_changes_original.sh
   ```
  - 运行脚本：
    
    假设要检测 .java 文件：
   ```
   ./generate_commit_file_changes_original.sh /path/to/repos /path/to/output/commit_file_changes_original java
   ```
    
   - `/path/to/repos`：Git 仓库目录。
   - `/path/to/output/commit_file_changes_original`：CSV 文件存放目录。

**2. 导入数据**

导入1中获得的csv

```
sqlite3 your_database_name.db
```

进入 SQLite 后，依次执行以下命令：

**导入 CSV 忽略标题行 使用以下 SQL 语句忽略标题行并指定字段：**
```
.mode csv
.headers on
.import /path/to/output/commit_file_changes_original/[repo_name]_commit_file_changes_original.csv temp_table
```

**将数据插入指定字段 假设导入的数据在临时表 temp_table 中，你可以执行以下语句将数据插入到目标表：**
```
INSERT INTO commit_file_changes_original (commit_id, repository_id, file_status, source_dir, source_file, target_dir, target_file)
SELECT 
    tt.commit_id,
    r.id AS repository_id,
    tt.file_status,
    tt.source_dir,
    tt.source_file,
    tt.target_dir,
    tt.target_file
FROM temp_table AS tt
LEFT JOIN repository AS r
ON tt.repository_name = r.repository_name
WHERE tt.commit_id IS NOT NULL AND r.id IS NOT NULL;
```
**删除临时表**

```
drop table temp_table;
```

---
### Table `finergit_original_mapping`

| 字段名             | 数据类型    | 是否为空 | 主键/外键 | 描述             |
|--------------------|-------------|----------|-----------|------------------|
| commit_id          | VARCHAR(40) | 否       | 主键      | FinerGit 提交 ID |
| original_commit_id | VARCHAR(7)  | 否       |           |                  |
| repository_id      | INTEGER     | 否       |           | 仓库的 ID        |
| commit_date        | TIMESTAMP   | 是       |           |                  |




**创建数据表命令**
```
CREATE TABLE finergit_original_mapping (
    commit_id VARCHAR(40) NOT NULL PRIMARY KEY,
    original_commit_id VARCHAR(7) NOT NULL,
    repository_id INTEGER NOT NULL,
    commit_date TIMESTAMP
);

```

**获取所需信息导入数据表方法**

**1.finergit化repos**

使用`--token-type-included <true|false>` 使其包含token type.

finergit选项：
```
Options:
--access-modifier-included         	: include access modifiers in Java <true|false>) method files
--check-commit <true|false>)       	: check whether each rebuilt commit is fine state or not
--class-file-generated <true|false>)   : generate files for classes
--field-file-generated <true|false>)   : generate files for fields
--hash-length N                    	: length of hash value attached to too long name files
--head <commitId>                  	: commitId for HEAD of finer repository
--max-file-name-length N           	: max file name length for Java method files [13, 255]
--method-file-generated <true|false>)  : generate files for methods
--method-token-included <true|false>)  : include method tokens
--method-type-erasure-included     	: include method type erasure in Java <true|false>) method files
--nthreads <num>                   	: number of threads used for --parallel
--peripheral-file-generated <true|false>) : generate files for peripheral (outer) tokens
--return-type-included <true|false>)   : include return types in Java method files
--token-type-included <true|false>)	: include token types
-d (--des) <path>                  	: path to output repository
-j (--java-version) <version>      	: java version of target source files
-l (--log-level) <level>           	: log level (trace, debug, info, warn, error)
-o (--original-javafiles) <true|false>) : finer repository includes whether original Java files or not
-p (--otherfiles) <true|false>)    	: finer repository includes whether other files or not
-s (--src) <path>                  	: path to input repository
-t (--tokenize) <true|false>)      	: do tokenize Java method files
```

本次使用的finergit命令：
```
java -jar /path/to/FinerGit/build/libs/FinerGit-all.jar create --src /path/to/repos/mbassador --des /path/to/repos_finergit/mbassador --token-type-included true  ---如果设置了finergit快捷引用可以用下面的命令

finergit create --src /path/to/repos/mbassador --des /path/to/repos_finergit/mbassador --token-type-included true 
finergit create --src /path/to/repos/javapoet --des /path/to/repos_finergit/javapoet --token-type-included true
finergit create --src /path/to/repos/nutz --des /path/to/repos_finergit/nutz --token-type-included true
```

**2.`finergit_original_mapping`数据表信息获取**

脚本`generate_finergit_original_mapping.sh`
```
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



```

- **运行方式**：
  - 给脚本赋予执行权限：
   
   ```
   chmod +x generate_finergit_original_mapping.sh
   ```
  - 运行脚本：
    
   ```
   ./generate_finergit_original_mapping.sh /path/to/repos_finergit /path/to/output/finergit_original_mapping
   ```
    
   - `/path/to/repos_finergit`：finergit处理，token化后的Git 仓库目录。
   - `/path/to/output/finergit_original_mapping`：CSV 文件存放目录。

**3. 导入数据**

导入2中获得的csv

```
sqlite3 your_database_name.db
```

进入 SQLite 后，依次执行以下命令：

**导入 CSV 忽略标题行 使用以下 SQL 语句忽略标题行并指定字段：**
```
.mode csv
.headers on
.import /path/to/output/finergit_original_mapping/[repo_name]_finergit_original_mapping.csv temp_table
```

**将数据插入指定字段 假设导入的数据在临时表 temp_table 中，你可以执行以下语句将数据插入到目标表：**
```
INSERT INTO finergit_original_mapping (commit_id, original_commit_id, repository_id, commit_date)
SELECT 
    tt.commit_id,
    tt.original_commit_id,
    r.id AS repository_id,
    tt.commit_date
FROM temp_table AS tt
LEFT JOIN repository AS r
ON tt.repository_name = r.repository_name
WHERE tt.commit_id IS NOT NULL AND r.id IS NOT NULL;

```
**删除临时表**

```
drop table temp_table;
```

---
### Table `commit_file_changes_finergit`

| 字段名         | 数据类型    | 是否为空 | 主键/外键 | 描述                                                         |
|----------------|-------------|----------|-----------|--------------------------------------------------------------|
| id             | INTEGER     | 否       | 主键      | 自增                                                         |
| commit_id      | VARCHAR(40) | 否       |           | 原始提交 ID (SHA1 哈希值)                                   |
| repository_id  | INTEGER     | 否       |           | 仓库的 ID                                                   |
| file_status    | VARCHAR(10) | 否       |           | 文件状态：A（新增）、M（修改）、D（删除）、Rxx（重命名）、Cxx（复制）等 |
| source_dir     | VARCHAR(255)| 否       |           | `source_file_path` 的路径部分，去掉文件名后的内容            |
| source_file    | VARCHAR(255)| 否       |           | `source_file_path` 的文件名部分                              |
| target_dir     | VARCHAR(255)| 否       |           | `target_file_path` 的路径部分，去掉文件名后的内容（适用于 R 和 C 状态） |
| target_file    | VARCHAR(255)| 否       |           | `target_file_path` 的文件名部分                              |



**创建数据表命令**
```
CREATE TABLE commit_file_changes_finergit (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    commit_id VARCHAR(40) NOT NULL,
    repository_id INTEGER NOT NULL,
    file_status VARCHAR(10) NOT NULL,
    source_dir VARCHAR(255) NOT NULL,
    source_file VARCHAR(255) NOT NULL,
    target_dir VARCHAR(255) NOT NULL,
    target_file VARCHAR(255) NOT NULL
);
```

**获取所需信息导入数据表方法**

**1.`commit_file_changes_finergit`数据表信息获取**

脚本`generate_commit_file_changes_finergit.py`

仅支持`mjava`

```
import os
import re
import subprocess
import csv
import sys

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <repo_directory> <output_directory>")
        sys.exit(1)

    repo_dir = sys.argv[1]
    output_dir = sys.argv[2]

    # Ensure output directory exists
    if os.path.exists(output_dir):
        print(f"Clearing directory: {output_dir}")
        for file in os.listdir(output_dir):
            file_path = os.path.join(output_dir, file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                os.rmdir(file_path)
    else:
        print(f"Creating directory: {output_dir}")
        os.makedirs(output_dir)

    # Check if file has .mjava extension
    def is_mjava_file(file_path):
        return file_path.endswith(".mjava")

    for repo in os.listdir(repo_dir):
        repo_path = os.path.join(repo_dir, repo)
        if os.path.isdir(os.path.join(repo_path, ".git")):
            output_file = os.path.join(output_dir, f"{repo}_commit_file_changes_finergit.csv")
            print(f"Processing repository: {repo}")

            with open(output_file, mode="w", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["commit_id", "file_status", "source_dir", "source_file", "target_dir", "target_file", "repository_name"])

                git_log = subprocess.run(["git", "-C", repo_path, "log", "--all", "--name-status", "--format=%H"],
                                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                if git_log.returncode != 0:
                    print(f"Error processing {repo}: {git_log.stderr}")
                    continue

                commit_id = ""
                for line in git_log.stdout.splitlines():
                    if re.match(r"^[a-f0-9]{40}$", line):
                        commit_id = line
                    elif line and commit_id:
                        parts = line.split('\t')
                        if len(parts) < 2:
                            continue

                        file_status = parts[0]

                        if file_status.startswith("R") and len(parts) > 2:
                            # Handle renames with source and target files
                            source_file_path, target_file_path = parts[1], parts[2]
                            if is_mjava_file(source_file_path) or is_mjava_file(target_file_path):
                                writer.writerow([
                                    commit_id, file_status, os.path.dirname(source_file_path), os.path.basename(source_file_path), os.path.dirname(target_file_path), os.path.basename(target_file_path), repo
                                ])
                        elif file_status.startswith("C") and len(parts) > 2:
                            # Handle copies with source and target files
                            source_file_path, target_file_path = parts[1], parts[2]
                            if is_mjava_file(source_file_path) or is_mjava_file(target_file_path):
                                writer.writerow([
                                    commit_id, file_status, os.path.dirname(source_file_path), os.path.basename(source_file_path), os.path.dirname(target_file_path), os.path.basename(target_file_path), repo
                                ])
                        elif file_status in {"A"}:
                            # Handle additions
                            target_file_path = parts[1]
                            if is_mjava_file(target_file_path):
                                writer.writerow([
                                    commit_id, file_status, "", "", os.path.dirname(target_file_path), os.path.basename(target_file_path), repo
                                ])
                        elif file_status in {"M"}:
                            # Handle modifications
                            source_file_path = parts[1]
                            if is_mjava_file(source_file_path):
                                writer.writerow([
                                    commit_id, file_status, os.path.dirname(source_file_path), os.path.basename(source_file_path), "", "", repo
                                ])
                        elif file_status in {"D"}:
                            # Handle deletions
                            source_file_path = parts[1]
                            if is_mjava_file(source_file_path):
                                writer.writerow([
                                    commit_id, file_status, os.path.dirname(source_file_path), os.path.basename(source_file_path), "", "", repo
                                ])
                        elif file_status in {"T"}:
                            # Handle type changes
                            source_file_path = parts[1]
                            if is_mjava_file(source_file_path):
                                writer.writerow([
                                    commit_id, file_status, os.path.dirname(source_file_path), os.path.basename(source_file_path), "", "", repo
                                ])
                        elif file_status in {"U"}:
                            # Handle unresolved conflicts
                            source_file_path = parts[1]
                            if is_mjava_file(source_file_path):
                                writer.writerow([
                                    commit_id, file_status, os.path.dirname(source_file_path), os.path.basename(source_file_path), "", "", repo
                                ])

            # Remove file if only header exists
            if os.path.getsize(output_file) == 0:
                os.remove(output_file)

    print("Processing completed. CSV files are saved in", output_dir)

if __name__ == "__main__":
    main()



```

- **脚本说明**

  - **运行方式**：

   ```
   python3 generate_commit_file_changes_finergit.py /path/to/repos_finergit /path/to/output/commit_file_changes_finergit
   ```
 
  - `/path/to/repos_finergit`：被finergit处理token化的Git 仓库目录。
  - `/path/to/output/commit_file_changes_finergit`：CSV 文件存放目录。

**2. 导入数据**

导入1中获得的csv

```
sqlite3 your_database_name.db
```

进入 SQLite 后，依次执行以下命令：

**导入 CSV 忽略标题行 使用以下 SQL 语句忽略标题行并指定字段：**
```
.mode csv
.headers on
.import /path/to/output/commit_file_changes_finergit/[repo_name]_commit_file_changes_finergit.csv temp_table
```

**将数据插入指定字段 假设导入的数据在临时表 temp_table 中，你可以执行以下语句将数据插入到目标表：**
```
INSERT INTO commit_file_changes_finergit (commit_id, repository_id, file_status, source_dir, source_file, target_dir, target_file)
SELECT 
    tt.commit_id,
    r.id AS repository_id,
    tt.file_status,
    tt.source_dir,
    tt.source_file,
    tt.target_dir,
    tt.target_file
FROM temp_table AS tt
LEFT JOIN repository AS r
ON tt.repository_name = r.repository_name
WHERE tt.commit_id IS NOT NULL AND r.id IS NOT NULL;
```
**删除临时表**

```
drop table temp_table;
```
---
### Table `commit_diff_lines_finergit`

| 字段名         | 数据类型    | 是否为空 | 主键/外键 | 描述                                                         |
|----------------|-------------|----------|-----------|--------------------------------------------------------------|
| id             | INTEGER     | 否       | 主键      | 自增                                                         |
| commit_id      | VARCHAR(40) | 否       |           | FinerGit 提交 ID                                             |
| repository_id  | INTEGER     | 否       |           | 仓库的 ID                                                   |
| file_name      | VARCHAR(255)| 否       |           | `mjava` 文件名，不包含路径信息                               |
| file_path      | TEXT        | 否       |           | 文件路径                                                    |
| commit_date    | TIMESTAMP   | 否       |           | UTC 时间，无时区信息                                         |
| hunk_id        | INT         | 否       |           | `hunk` 的唯一标识符，从 0 开始计数                           |
| hunk_header    | TEXT        | 否       |           | `hunk` 的头部信息                                           |
| line_id        | INT         | 否       |           | 行的唯一标识符，从 0 开始计数                                |
| change_type    | ENUM('+', '-') | 否    |           | 变更类型 (`+` 表示添加, `-` 表示删除)                       |
| token_type     | VARCHAR(50) | 是       |           | 令牌类型，注释行的令牌类型为空或 `JAVADOCCOMMENT`                     |
| token_value    | TEXT        | 否       |           | 令牌值                                                      |




**创建数据表命令**
```
CREATE TABLE commit_diff_lines_finergit (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    commit_id VARCHAR(40) NOT NULL,
    repository_id INTEGER NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    file_path TEXT NOT NULL,
    commit_date TIMESTAMP NOT NULL,
    hunk_id INT NOT NULL,
    hunk_header TEXT NOT NULL,
    line_id INT NOT NULL,
    change_type CHAR(1) NOT NULL CHECK (change_type IN ('+', '-')),
    token_type VARCHAR(50),
    token_value TEXT NOT NULL
);

```

**获取所需信息导入数据表方法**

**1.获取方法级别的提交信息**

脚本`generate_commits_mjava.sh`
该脚本输出diff --git 文件路径部分

```
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




```



- **脚本说明**
  - 该脚本仅输出每个xx.mjava文件（即一个method）的所有提交记录，存入与之同名的log文件里。一个提交的信息如下：
    - commit_id: 4d104d8d47143c6fc8e6ba3f08edb6157c38a17d
    - commit_date: Wed May 1 15:32:05 2019 -0400
    - file_name_mjava: ClassNameNoPackageTest#public_void_shouldSupportClassInDefaultPackage().mjava
    - file_path: src/test/java
    - hunks

 - 给脚本赋予执行权限：
   
   ```
   chmod +x generate_commits_mjava.sh
   ```
  - **运行方式**：

   ```
   ./generate_commits_mjava.sh /path/to/repos_finergit /path/to/output/commits_mjava
   ```
 
  - `/path/to/repos_finergit`：被finergit处理token化的Git 仓库目录。
  - `/path/to/output/commits_mjava`：log 文件存放目录。
 
**2. 分隔从1中获得的log，每个提交单独保存**

脚本`split_commits_mjava.sh`


```
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



```

- **脚本说明**
  - 给脚本赋予执行权限：
   
   ```
   chmod +x split_commits_mjava.sh
   ```
  - **运行方式**：

   ```
   ./split_commits_mjava.sh /path/to/output/commits_mjava /path/to/output/split_commits_mjava
   ```
 
  - `/path/to/output/commits_mjava`：log 文件存放目录。
  - `/path/to/output/split_commits_mjava`：被分割的单独提交的log 文件存放目录。

**3. `commit_file_changes_finergit`数据表信息获取**

从2中获得的log提取相关信息制作csv

脚本`extract_commit_diff_lines_finergit.py`
```
import os
import csv
import sys
import re
from datetime import datetime, timezone

def process_logs(input_dir, output_dir):
    # Check and handle output directory
    if os.path.exists(output_dir):
        print(f"Clearing contents of the last subdirectory in output: {output_dir}")
        for item in os.listdir(output_dir):
            item_path = os.path.join(output_dir, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                for sub_item in os.listdir(item_path):
                    os.remove(os.path.join(item_path, sub_item))
    else:
        print(f"Creating output directory: {output_dir}")
        os.makedirs(output_dir)

    # Iterate through [repo_name] subdirectories
    for repo_name in os.listdir(input_dir):
        repo_path = os.path.join(input_dir, repo_name)
        if os.path.isdir(repo_path):
            csv_filename = os.path.join(output_dir, f"{repo_name}_commit_diff_lines_finergit.csv")
            
            with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['commit_id', 'commit_date', 'file_name_mjava', 'file_path', 'repository_name', 'hunk_id', 'hunk_header', 'line_id', 'token_value', 'token_type', 'change_type'])  # Adjusted headers
                
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
                if hunk_headers and hunk_lines:  # Write the previous hunk
                    write_hunk(writer, commit_id, commit_date, file_name_mjava, file_path, repository_name, hunk_id, hunk_headers[-1], hunk_lines)
                    hunk_id += 1
                hunk_headers.append(line.strip())
                hunk_lines = []  # Reset line collection
            elif hunk_headers:
                hunk_lines.append(line.rstrip())
        
        if hunk_headers and hunk_lines:  # Write the last hunk
            write_hunk(writer, commit_id, commit_date, file_name_mjava, file_path, repository_name, hunk_id, hunk_headers[-1], hunk_lines)

def write_hunk(writer, commit_id, commit_date, file_name_mjava, file_path, repository_name, hunk_id, hunk_header, hunk_lines):
    line_id = 0  # Reset line_id, starting from 0
    in_comment_block = False  # Track whether inside a comment block
    for line_content in hunk_lines:
        # Skip empty lines
        if not line_content.strip():
            line_id += 1
            continue

        # Determine change_type and adjusted line_content
        if line_content.startswith('+'):
            change_type = '+'
            line_content = line_content[1:].strip()
        elif line_content.startswith('-'):
            change_type = '-'
            line_content = line_content[1:].strip()
        elif line_content.startswith(' '):
            change_type = ''
            line_content = line_content[1:].strip()
        else:
            change_type = ''
            line_content = line_content.strip()

        # Handle comment block logic
        if line_content.startswith("/**"):
            in_comment_block = True

        if in_comment_block:
            if line_content.startswith("*/") and "JAVADOCCOMMENT" in line_content:
                # Handle comment block ending
                token_value = "*/"
                token_type = "JAVADOCCOMMENT"
                in_comment_block = False
            elif line_content.startswith("*"):
                # Handle comment lines inside the block
                token_value = line_content
                token_type = ""
            else:
                # Any other line inside a comment block
                token_value = line_content
                token_type = ""
        else:
            # Split line_content into token_value and token_type outside comment blocks
            parts = line_content.rsplit(maxsplit=1)
            token_value = parts[0]
            token_type = parts[1] if len(parts) > 1 else ""

        # Write only if it's a change line (+ or -)
        if change_type in ('+', '-'):
            writer.writerow([commit_id, commit_date, file_name_mjava, file_path, repository_name, hunk_id, hunk_header, line_id, token_value, token_type, change_type])

        # Increment line_id regardless of writing
        line_id += 1

def convert_to_utc(raw_date):
    # Convert date string to UTC format and remove timezone info
    date_obj = datetime.strptime(raw_date, "%a %b %d %H:%M:%S %Y %z")
    utc_date = date_obj.astimezone(timezone.utc).replace(tzinfo=None)
    return utc_date.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 extract_commit_diff_lines_finergit.py <input_dir> <output_dir>")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    if not os.path.isdir(input_dir):
        print(f"Input directory does not exist or is not valid: {input_dir}")
        sys.exit(1)

    process_logs(input_dir, output_dir)


```

- **脚本说明**
  - 给脚本赋予执行权限：
   
   ```
   chmod +x extract_commit_diff_lines_finergit.py
   ```
  - **运行方式**：

   ```
   python3 extract_commit_diff_lines_finergit.py /path/to/output/split_commits_mjava /path/to/output/commit_diff_lines_finergit
   ```
 
  - `/path/to/output/split_commits_mjava`：被分割的单独提交的log 文件存放目录。
  - `/path/to/output/commit_diff_lines_finergit`：CSV文件存放目录。






**4. 导入数据**

导入3中获得的csv

```
sqlite3 your_database_name.db
```

进入 SQLite 后，依次执行以下命令：

**导入 CSV 忽略标题行 使用以下 SQL 语句忽略标题行并指定字段：**
```
.mode csv
.headers on
.import /path/to/output/commit_diff_lines_finergit/[repo_name]_commit_diff_lines_finergit.csv temp_table
```

**将数据插入指定字段 假设导入的数据在临时表 temp_table 中，你可以执行以下语句将数据插入到目标表：**
```
INSERT INTO commit_diff_lines_finergit (commit_id, repository_id, file_name, file_path, commit_date, hunk_id, hunk_header, line_id, change_type, token_type, token_value)
SELECT 
    tt.commit_id,
    r.id AS repository_id,
    tt.file_name_mjava,
    tt.file_path,
    tt.commit_date,
    tt.hunk_id,
    tt.hunk_header,
    tt.line_id,
    tt.change_type,
    tt.token_type,
    tt.token_value
FROM temp_table AS tt
LEFT JOIN repository AS r
ON tt.repository_name = r.repository_name
WHERE tt.commit_id IS NOT NULL AND r.id IS NOT NULL;
```
**删除临时表**

```
drop table temp_table;
```

---
### Table `commits_finergit_hayashi`

再现林老师的根据文件名判断重构类型脚本`historage-refactoring-java.rb`

| 字段名                | 数据类型    | 是否为空 | 主键/外键 | 描述              |
|-----------------------|-------------|----------|-----------|-------------------|
| id                    | INTEGER     | 否       | 主键      | 自增              |
| commit_id             | VARCHAR(40) | 否       |           |                   |
| repository_id         | INTEGER     | 否       |           | 仓库的 ID         |
| file_similarity_score | INT         | 否       |           |                   |
| change_type           | VARCHAR(30) | 否       |           |                   |
| change_type_info      | TEXT        | 否       |           |                   |
| old_file_path      | VARCHAR(255)| 否       |           |                   |
| new_file_path      | VARCHAR(255)| 否       |           |                   |



**创建数据表命令**
```
CREATE TABLE commits_finergit_hayashi (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    commit_id VARCHAR(40) NOT NULL,
    repository_id INTEGER NOT NULL,
    file_similarity_score INT NOT NULL,
    change_type VARCHAR(30) NOT NULL,
    change_type_info TEXT NOT NULL,
    old_file_path VARCHAR(255) NOT NULL,
    new_file_path VARCHAR(255) NOT NULL
);

```

**获取所需信息导入数据表方法**

**1.利用林老师的脚本输出txt**

脚本`historage-refactoring-java.rb`

```
#!/usr/bin/env ruby

FNAME_RE = /^([^\#]+)\#([^\(]+)\(([^\)]+)\)\.mjava$/i

def parse_fname(fname)
  if FNAME_RE =~ fname
    [ $1, $2, $3 ]
  else
    nil
  end
end

def process_rename(old_fname, new_fname)
  o = parse_fname(old_fname)
  n = parse_fname(new_fname)
  return nil unless o && n

  if o[0] == n[0]
    if o[2] == n[2]
      "Rename Method: '#{o[1]}' to '#{n[1]}' at '#{o[0]}'"
    elsif o[1] == o[1]
      "Change Parameter: '#{o[1]}(#{o[2]})' to '#{n[1]}(#{n[2]})' at '#{o[0]}'"
    else
      "Rename Method+: '#{o[1]}(#{o[2]})' to '#{n[1]}(#{n[2]})' at '#{o[0]}'"
    end
  elsif o[1] == n[1]
    if o[2] == n[2]
      "Move Method: '#{o[1]}' from '#{o[0]}' to '#{n[0]}'"
    else
      "Move Method+: '#{o[1]}(#{o[2]})' to '#{n[1]}(#{n[2]})' at '#{o[0]}'"
    end
  elsif o[2] == n[2]
    "Move and Rename Method: '#{o[1]}' at '#{o[0]}' to '#{n[1]}' at '#{n[0]}'"
  else
    "Move and Rename Method+: '#{o[1]}(#{o[2]})' at '#{o[0]}' to '#{n[1]}(#{n[2]})' at '#{n[0]}'"
  end
end

open("| git --git-dir='#{ARGV[0]}' log --branches --tags --no-merges -M50 --name-status --pretty=tformat:'n:%N%h %s'") do |fin|
  fin.each_line do |line|
    line.chomp!
    case line
    when /^n:(.*)/
      $note = $1
    when /^([a-f0-9]+) (.*)/
      $cid, $log = $1, $2
    when /^R(\d+)\t(.*?)\t(.*?)$/
      score, old_fname, new_fname = $1.to_i, $2, $3
      type = process_rename(old_fname, new_fname)
      puts "#{$note[0,10]}\t#{$cid[0,10]}\t#{score}\t#{type}\t#{old_fname}\t#{new_fname}" if type
    end
  end
end

__END__

```

- **运行方式**：
  - 给脚本赋予执行权限：
   
   ```
   chmod +x historage-refactoring-java.rb
   ```
  - 运行脚本：
    
    假设要检测 .java 文件：
   ```
   ./historage-refactoring-java.rb /path/to/repos_finergit/[repo_name]/.git  > /path/to/output/commits_finergit_hayashi_txt/[repo_name].txt
   ```
    
  - `/path/to/repos_finergit/[repo_name]/.git`：被finergit处理token化的Git 仓库。
  - `/path/to/output/commits_finergit_hayashi_txt/[repo_name]_txt`：txt 文件路径。

**2. 生成csv**

脚本`convert_hayashi_txt_to_csv.sh`
```
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



```

- **运行方式**：
  - 给脚本赋予执行权限：
   
   ```
   chmod +x convert_hayashi_txt_to_csv.sh
   ```
  - 运行脚本：
    
    假设要检测 .java 文件：
   ```
   ./convert_hayashi_txt_to_csv.sh /path/to/output/commits_finergit_hayashi_txt /path/to/output/commits_finergit_hayashi_csv
   ```
    
  - `/path/to/output/commits_finergit_hayashi_txt`：txt 文件路径。
  - `/path/to/output/commits_finergit_hayashi_csv`：csv 文件路径。


**3. 导入csv**
导入1中获得的csv

```
sqlite3 your_database_name.db
```

进入 SQLite 后，依次执行以下命令：

**导入 CSV 忽略标题行 使用以下 SQL 语句忽略标题行并指定字段：**
```
.mode csv
.headers on
.import /path/to/output/commits_finergit_hayashi_csv/[repo_name]_commits_finergit_hayashi.csv temp_table
```

**将数据插入指定字段 假设导入的数据在临时表 temp_table 中，你可以执行以下语句将数据插入到目标表：**
```
INSERT INTO commits_finergit_hayashi (commit_id, repository_id, file_similarity_score, change_type, change_type_info, old_file_path, new_file_path)
SELECT 
    tt.commit_id,
    r.id AS repository_id,
    tt.file_similarity_score,
    tt.change_type,
    tt.change_type_info,
    tt.old_file_path,
    tt.new_file_path
FROM temp_table AS tt
LEFT JOIN repository AS r
ON tt.repository_name = r.repository_name
WHERE tt.commit_id IS NOT NULL AND r.id IS NOT NULL;
```
**删除临时表**

```
drop table temp_table;
```
