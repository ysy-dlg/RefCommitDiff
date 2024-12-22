# commit_diff_db
Testing Phase Version.

Considering the data volume in the later stages, I chose MySQL instead of SQLite.

Currently, I am using `git log --all`. In the future, I may consider adding options to exclude merge commits and other entries.

## Tables in commit_diff_db

There are 8 tables `commit_diff_lines_finergit`, `commits_original`, `commit_file_changes_finergit`,`finergit_original_mapping`,`commit_file_changes_original` ,`refactor_keywords`,`commits_finergit_hayashi`, 
 and `repository` in commit_diff_db.
```shell-session
sqlite> .tables
commit_diff_lines_finergit    commits_original            
commit_file_changes_finergit  finergit_original_mapping   
commit_file_changes_original  refactor_keywords           
commits_finergit_hayashi      repository  
```


<details>
<summary>Table <code>commit_diff_lines_finergit</code></summary>

- The schema of table `commit_diff_lines_finergit` is as follows.
  - To set the primary key, an auto-increment ID was added.

| Field Name     | Data Type      | Nullable | Primary/Foreign Key | Description                                                   |
|----------------|----------------|----------|----------------------|--------------------------------------------------------------|
| id             | INTEGER        | No       | Primary Key          | Auto-increment                                               |
| commit_id      | VARCHAR(40)    | No       |                      | FinerGit commit ID                                           |
| repository_id  | INTEGER        | No       |                      | Repository ID                                                |
| file_name      | VARCHAR(255)   | No       |                      | `mjava` file name, without path information                  |
| file_path      | TEXT           | No       |                      | File path                                                    |
| commit_date    | TIMESTAMP      | No       |                      | UTC time, without timezone information                       |
| hunk_id        | INT            | No       |                      | Unique identifier for `hunk`, starting from 0                |
| hunk_header    | TEXT           | No       |                      | Header information of the `hunk`                             |
| line_id        | INT            | No       |                      | Unique identifier for the line, starting from 0              |
| change_type    | ENUM('+', '-') | No       |                      | Change type (`+` for addition, `-` for deletion)             |
| token_type     | VARCHAR(50)    | Yes      |                      | Token type: For comment lines, non-terminal lines have a null token type, while terminal lines are `JAVADOCCOMMENT`  |
| token_value    | TEXT           | No       |                      | Token value                                                  |





- Displaying Data Stored in the Table
```shell-session
sqlite> .mode column
sqlite> .headers on
sqlite> sqlite> select * from commit_diff_lines_finergit limit 10;
id  commit_id                                 repository_id  file_name                                                     file_path                                 commit_date          hunk_id  hunk_header                               line_id  change_type  token_type    token_value                                                 
--  ----------------------------------------  -------------  ------------------------------------------------------------  ----------------------------------------  -------------------  -------  ----------------------------------------  -------  -----------  ------------  ------------------------------------------------------------
1   e2349134a2bc55891a5220c52ff7f3a0bbe1a378  183            PublicationError#public_PublicationError(Throwable,String,Me  src/main/java/net/engio/mbassy/bus/error  2016-10-02 21:01:46  0        @@ -1,10 +1,10 @@                         3        -                          * @param message         The message to send.               
                                                             thod,Object,IMessagePublication).mjava                                                                                                                                                                                                                                          

2   e2349134a2bc55891a5220c52ff7f3a0bbe1a378  183            PublicationError#public_PublicationError(Throwable,String,Me  src/main/java/net/engio/mbassy/bus/error  2016-10-02 21:01:46  0        @@ -1,10 +1,10 @@                         4        +                          * @param errorMsg         The message to send.              
                                                             thod,Object,IMessagePublication).mjava                                                                                                                                                                                                                                          

3   e2349134a2bc55891a5220c52ff7f3a0bbe1a378  183            PublicationError#public_PublicationError(Throwable,String,Me  src/main/java/net/engio/mbassy/bus/error  2016-10-02 21:01:46  0        @@ -1,10 +1,10 @@                         7        -                          * @param publishedObject The published object which gave ris
                                                             thod,Object,IMessagePublication).mjava                                                                                                                                                                              e to the error.                                             

4   e2349134a2bc55891a5220c52ff7f3a0bbe1a378  183            PublicationError#public_PublicationError(Throwable,String,Me  src/main/java/net/engio/mbassy/bus/error  2016-10-02 21:01:46  0        @@ -1,10 +1,10 @@                         8        +                          * @param publication The publication that errored           
                                                             thod,Object,IMessagePublication).mjava                                                                                                                                                                                                                                          

5   e2349134a2bc55891a5220c52ff7f3a0bbe1a378  183            PublicationError#public_PublicationError(Throwable,String,Me  src/main/java/net/engio/mbassy/bus/error  2016-10-02 21:01:46  1        @@ -15,7 +15,7 @@ cause VARIABLENAME      3        -            VARIABLENAME  message                                                     
                                                             thod,Object,IMessagePublication).mjava                                                                                                                                                                                                                                          

6   e2349134a2bc55891a5220c52ff7f3a0bbe1a378  183            PublicationError#public_PublicationError(Throwable,String,Me  src/main/java/net/engio/mbassy/bus/error  2016-10-02 21:01:46  1        @@ -15,7 +15,7 @@ cause VARIABLENAME      4        +            VARIABLENAME  errorMsg                                                    
                                                             thod,Object,IMessagePublication).mjava                                                                                                                                                                                                                                          

7   e2349134a2bc55891a5220c52ff7f3a0bbe1a378  183            PublicationError#public_PublicationError(Throwable,String,Me  src/main/java/net/engio/mbassy/bus/error  2016-10-02 21:01:46  2        @@ -26,8 +26,8 @@ Object        TYPENAME  3        -            TYPENAME      Object                                                      
                                                             thod,Object,IMessagePublication).mjava                                                                                                                                                                                                                                          

8   e2349134a2bc55891a5220c52ff7f3a0bbe1a378  183            PublicationError#public_PublicationError(Throwable,String,Me  src/main/java/net/engio/mbassy/bus/error  2016-10-02 21:01:46  2        @@ -26,8 +26,8 @@ Object        TYPENAME  4        -            VARIABLENAME  publishedObject                                             
                                                             thod,Object,IMessagePublication).mjava                                                                                                                                                                                                                                          

9   e2349134a2bc55891a5220c52ff7f3a0bbe1a378  183            PublicationError#public_PublicationError(Throwable,String,Me  src/main/java/net/engio/mbassy/bus/error  2016-10-02 21:01:46  2        @@ -26,8 +26,8 @@ Object        TYPENAME  5        +            TYPENAME      IMessagePublication                                         
                                                             thod,Object,IMessagePublication).mjava                                                                                                                                                                                                                                          

10  e2349134a2bc55891a5220c52ff7f3a0bbe1a378  183            PublicationError#public_PublicationError(Throwable,String,Me  src/main/java/net/engio/mbassy/bus/error  2016-10-02 21:01:46  2        @@ -26,8 +26,8 @@ Object        TYPENAME  6        +            VARIABLENAME  publication                                                 
                                                             thod,Object,IMessagePublication).mjava                                                                                                                                                                                                                                                                 
```
</details>



<details>
<summary>Table <code>commits_original</code></summary>

- The schema of table `commits_original` is as follows.
  - **`is_code_file_modified`** can help filter out commits that do not contain code file (e.g..java) changes.


| Field Name              | Data Type      | Nullable | Primary/Foreign Key | Description                                                       |
|-------------------------|----------------|----------|----------------------|-------------------------------------------------------------------|
| commit_id               | VARCHAR(40)    | No       | Primary Key          | Original Commit ID                            |
| repository_id           | INTEGER        | Yes      |                      | Repository ID  |
| commit_message_subject  | TEXT           | Yes      |                      | Commit message subject                                           |
| is_file_modified        | TINYINT(1)     | No       |                      | With/Without File Modification                                  |
| is_code_file_modified   | TINYINT(1)     | No       |                      | With/Without Code File Modification                            |
| commit_date             | TIMESTAMP      | No       |                      | UTC time, without timezone information                              |



- Displaying Data Stored in the Table
```shell-session
                                                                                                                                                                                                                                                             
```
</details>

<details>
<summary>Table <code>commit_file_changes_finergit</code></summary>

- The schema of table `commit_file_changes_finergit` is as follows.
  - To set the primary key, an auto-increment ID was added.

| Field Name     | Data Type      | Nullable | Primary/Foreign Key | Description                                                               |
|----------------|----------------|----------|----------------------|---------------------------------------------------------------------------|
| id             | INTEGER        | No       | Primary Key          | Auto-increment                                                           |
| commit_id      | VARCHAR(40)    | No       |                      | Finergit Commit ID                                   |
| repository_id  | INTEGER        | No       |                      | Repository ID                                                           |
| file_status    | VARCHAR(10)    | No       |                      | File status: A (added), M (modified), D (deleted), Rxx (renamed), Cxx (copied), etc |
| source_dir     | VARCHAR(255)   | No       |                      | Path part of `source_file_path`, excluding the file name                |
| source_file    | VARCHAR(255)   | No       |                      | File name part of `source_file_path`.                                    |
| target_dir     | VARCHAR(255)   | No       |                      | Path part of `target_file_path`, excluding the file name (for R and C statuses) |
| target_file    | VARCHAR(255)   | No       |                      | File name part of `target_file_path`                                    |

- File Status

| File Status | source_dir                  | source_file        | target_dir                     | target_file           |
|-------------|-----------------------------|--------------------|--------------------------------|-----------------------|
| A           | Empty                       | Empty              | Directory part of the new file path | File name part of the new file |
| M           | Directory part of the original file path | File name part of the original file | Empty                | Empty                |
| D           | Directory part of the deleted file path | File name part of the deleted file | Empty                | Empty                |
| Rxx         | Directory part of the original file path | File name part of the original file | Directory part of the renamed file path | File name part of the renamed file |
| Cxx         | Directory part of the original file path | File name part of the original file | Directory part of the copied file path | File name part of the copied file |
| T           | Directory part of the file path | File name part of the file | Empty                | Empty                |
| U           | Directory part of the conflicting file path | File name part of the conflicting file | Empty                | Empty                |



- Displaying Data Stored in the Table
```shell-session
                                                                                                                                                                                                                                                             
```
</details>

<details>
<summary>Table <code>finergit_original_mapping</code></summary>

- The schema of table `finergit_original_mapping` is as follows.





- Displaying Data Stored in the Table
```shell-session
                                                                                                                                                                                                                                                             
```
</details>

<details>
<summary>Table <code>commit_file_changes_original</code></summary>

- The schema of table `commit_file_changes_original` is as follows.

| Field Name     | Data Type      | Nullable | Primary/Foreign Key | Description                                                               |
|----------------|----------------|----------|----------------------|---------------------------------------------------------------------------|
| id             | INTEGER        | No       | Primary Key          | Auto-increment                                                           |
| commit_id      | VARCHAR(40)    | No       |                      | Original Commit ID                                   |
| repository_id  | INTEGER        | No       |                      | Repository ID                                                           |
| file_status    | VARCHAR(10)    | No       |                      | File status: A (added), M (modified), D (deleted), Rxx (renamed), Cxx (copied), etc |
| source_dir     | VARCHAR(255)   | No       |                      | Path part of `source_file_path`, excluding the file name                |
| source_file    | VARCHAR(255)   | No       |                      | File name part of `source_file_path`.                                    |
| target_dir     | VARCHAR(255)   | No       |                      | Path part of `target_file_path`, excluding the file name (for R and C statuses) |
| target_file    | VARCHAR(255)   | No       |                      | File name part of `target_file_path`                                    |




- Displaying Data Stored in the Table
```shell-session
                                                                                                                                                                                                                                                             
```
</details>

<details>
<summary>Table <code>refactor_keywords</code></summary>

- The schema of table `refactor_keywords` is as follows.





- Displaying Data Stored in the Table
```shell-session
                                                                                                                                                                                                                                                             
```
</details>

<details>
<summary>Table <code>commits_finergit_hayashi</code></summary>

- The schema of table `commits_finergit_hayashi` is as follows.





Displaying Data Stored in the Table
```shell-session
                                                                                                                                                                                                                                                             
```
</details>

<details>
<summary>Table <code>repository</code></summary>

- The schema of table `repository` is as follows.





- Displaying Data Stored in the Table
```shell-session
                                                                                                                                                                                                                                                             
```
</details>



