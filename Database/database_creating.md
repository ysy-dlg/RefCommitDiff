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


### Table `commit_diff_lines_finergit`

The schema of table `commit_diff_lines_finergit` is as follows.

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
| token_type     | VARCHAR(50)    | Yes      |                      | Token type: For comment lines, non-terminal lines have a     |
|                |                |          |                      | null token type, while terminal lines are `JAVADOCCOMMENT`.  |
| token_value    | TEXT           | No       |                      | Token value                                                  |


- **`is_code_file_modified`** can help filter out commits that do not contain code file (e.g..java) changes.
- To set the primary key, an auto-increment ID was added.

**Displaying Data Stored in the Table**
```shell-session
 
```
