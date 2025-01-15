# commit_diff_db
Testing Phase Version.

Currently, except for the `commits_finergit_hayashi` (`git log --branches --tags --no-merges -M50`), all other tables use `git log --all` to extract commit information. In the future, I may consider adding options to exclude merge commits and other entries.

The dataset can be downloaded from the following URL:

https://github.com/ysy-dlg/RefCommitDiff/releases/tag/v1.0.0



## Tables in commit_diff_db

There are eight tables in commit_diff_db.
```shell-session
sqlite> .tables
commit_diff_lines_finergit    commits_finergit_hayashi    
commit_file_changes_finergit  commits_original            
commit_file_changes_original  finergit_original_mapping   
commit_hunks_finergit         repository                   
```

### Tables for storing repository data

<details>
<summary>Table <code>commit_diff_lines_finergit</code></summary>

- The schema of table `commit_diff_lines_finergit` is as follows.
  - To set the primary key, an auto-increment ID was added.

| Field Name       | Data Type           | Nullable | Primary/Foreign Key | Description                                                   |
|------------------|---------------------|----------|----------------------|---------------------------------------------------------------|
| id               | INTEGER             | No       | Primary Key          | Auto-incremented unique identifier                            |
| commit_id        | VARCHAR(40)         | No       |                      | FinerGit commit ID                                            |
| repository_name  | VARCHAR(255)        | No       |                      | Repository name                                               |
| old_filename     | VARCHAR(255)        | Yes       |                      | Old file name including path                                  |
| new_filename     | VARCHAR(255)        | Yes       |                      | New file name including path                                  |
| hunk_id          | INTEGER             | No       |                      | Unique identifier for the hunk, starting from 0              |
| hunk_header      | TEXT                | No       |                      | Header information of the hunk, describing the context or code location |
| hunk_size_lines  | INTEGER             | No       |                      | Total number of lines in the hunk                             |
| line_id          | INTEGER                 | No       |                      | Unique identifier for the line, starting from 0              |
| change_type      | ENUM('+', '-')      | No       |                      | Type of change (`+` for addition, `-` for deletion)           |
| token_type       | VARCHAR(50)         | Yes      |                      | Type of token; for comment lines, it may be empty or `JAVADOCCOMMENT` |
| token_value      | TEXT                | No       |                      | Value of the token                                            |


</details>





<details>
<summary>Table <code>commits_original</code></summary>

- The schema of table `commits_original` is as follows.
  - **`is_code_file_modified`** can help filter out commits that do not contain code file (e.g..java) changes.


| Field Name              | Data Type      | Nullable | Primary/Foreign Key | Description                                                       |
|-------------------------|----------------|----------|----------------------|-------------------------------------------------------------------|
| commit_id               | VARCHAR(40)    | No       | Primary Key          | Original Commit ID                            |
| repository_name         | VARCHAR(255)   | No      |                      | Name of the repository, used to identify or describe it      |
| commit_message_subject  | TEXT           | Yes      |                      | Commit message subject                                           |
| is_file_modified        | TINYINT(1)     | No       |                      | With/Without File Modification                                  |
| is_code_file_modified   | TINYINT(1)     | No       |                      | With/Without Code File Modification                            |
| commit_date             | TIMESTAMP      | No       |                      | UTC time, without timezone information                              |

</details>


<details>
<summary>Table <code>commit_file_changes_finergit</code></summary>

- The schema of table `commit_file_changes_finergit` is as follows.
  - To set the primary key, an auto-increment ID was added.

| Field Name       | Data Type       | Nullable | Primary/Foreign Key | Description                                                   |
|------------------|-----------------|----------|----------------------|---------------------------------------------------------------|
| id               | INTEGER         | No       | Primary Key          | Auto-increment                                                |
| commit_id        | VARCHAR(40)     | No       |                      | Finergit commit ID (SHA1 hash value)                         |
| repository_name  | VARCHAR(255)    | No       |                      | Repository name                                               |
| file_status      | VARCHAR(10)     | No       |                      | File status: A (Added), M (Modified), D (Deleted), Rxx (Renamed), Cxx (Copied), etc. |
| old_filename     | VARCHAR(255)    | Yes       |                      | Old file name including path                                  |
| new_filename     | VARCHAR(255)    | Yes       |                      | New file name including path                                  |

</details>


<details>
<summary>Table <code>finergit_original_mapping</code></summary>

- The schema of table `finergit_original_mapping` is as follows.
  
| Field Name         | Data Type      | Nullable | Primary/Foreign Key | Description                |
|--------------------|----------------|----------|----------------------|----------------------------|
| commit_id          | VARCHAR(40)    | No       | Primary Key          | FinerGit commit ID         |
| original_commit_id | VARCHAR(7)     | No       |                      | Original Commit ID         |
| repository_name  | VARCHAR(255)    | No       |                      | Repository name                                               |
| commit_date        | TIMESTAMP      | No      |                      | UTC time, without timezone information  |

</details>


<details>
<summary>Table <code>commit_file_changes_original</code></summary>

- The schema of table `commit_file_changes_original` is as follows.
  - To set the primary key, an auto-increment ID was added.


| Field Name       | Data Type       | Nullable | Primary/Foreign Key | Description                                                   |
|------------------|-----------------|----------|----------------------|---------------------------------------------------------------|
| id               | INTEGER         | No       | Primary Key          | Auto-increment                                                |
| commit_id        | VARCHAR(40)     | No       |                      | Original commit ID (SHA1 hash value)                         |
| repository_name  | VARCHAR(255)    | No       |                      | Repository name                                               |
| file_status      | VARCHAR(10)     | No       |                      | File status: A (Added), M (Modified), D (Deleted), Rxx (Renamed), Cxx (Copied), etc. |
| old_filename     | VARCHAR(255)    | Yes       |                      | Old file name including path                                  |
| new_filename     | VARCHAR(255)    | Yes       |                      | New file name including path                                  |


| File Status | old_filename               | new_filename              |
|-------------|----------------------------|---------------------------|
| A           | Empty                      | Full path of the new file |
| M           | Full path of the original file | Empty                    |
| D           | Full path of the deleted file | Empty                    |
| Rxx         | Full path of the original file | Full path after renaming |
| Cxx         | Full path of the original file | Full path after copying  |
| T           | Full path of the file          | Empty                    |
| U           | Full path of the conflicting file | Empty                |

</details>

<details>
<summary>Table <code>commits_finergit_hayashi</code></summary>

- The schema of table `commits_finergit_hayashi` is as follows.
  - To set the primary key, an auto-increment ID was added.

| Field Name             | Data Type      | Nullable | Primary/Foreign Key | Description                              |
|-------------------------|----------------|----------|----------------------|------------------------------------------|
| id                      | INTEGER        | No       | Primary Key          | Auto-increment                          |
| commit_id               | VARCHAR(40)    | No       |                      | FinerGit commit ID                      |
| repository_name   | VARCHAR(255)   | No      |                      | Name of the repository, used to identify or describe it      |
| file_similarity_score   | INTEGER            | No       |                      | Rxx                                  |
| change_type             | VARCHAR(30)    | No       |                      | Rename Method, Change Parameter, Rename Method+, Move Method, Move Method+, Move and Rename Method, Move and Rename Method+ |
| change_type_info        | TEXT           | No       |                      |                                          |
| old_filename           | VARCHAR(255)   | No       |                      |                                          |
| new_filename           | VARCHAR(255)   | No       |                      |                                          |


</details>

<details>
<summary>Table <code>repository</code></summary>

- The schema of table `repository` is as follows.

| Field Name       | Data Type      | Nullable | Primary/Foreign Key | Description                                                   |
|-------------------|----------------|----------|----------------------|---------------------------------------------------------------|
| id                | INTEGER        | No       | Primary Key          | Unique identifier for the repository, auto-increment primary key |
| repository_url    | TEXT           | No       |                      | Repository URL (e.g., GitHub, GitLab, etc.)                 |
| repository_name   | VARCHAR(255)   | Yes      |                      | Name of the repository, used to identify or describe it      |
| language          | VARCHAR(50)    | No       |                      | Primary programming language of the repository (e.g., Java, Python) |


</details>


