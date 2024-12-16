# RefCommitDiff
Language-agnostic Refactoring Detection

## all_commit_diff_db
Testing Phase Version
Considering the data volume in the later stages, I chose MySQL instead of SQLite.

### Tables in all_commit_diff_db


There are six tables `repository`, `refactor_keywords`, `mbassador_all_original_commits`,`mbassador_all_finergit_commits`,`mbassador_all_diff_lines`, and `hayashi_mbassador` in all_commit_diff_db.
```shell-session
mysql> show tables;
+--------------------------------+
| Tables_in_all_commit_diff_db   |
+--------------------------------+
| hayashi_mbassador              |
| mbassador_all_diff_lines       |
| mbassador_all_finergit_commits |
| mbassador_all_original_commits |
| refactor_keywords              |
| repository                     |
+--------------------------------+
```

### Table `mbassador_all_original_commits`
The schema of table `mbassador_all_original_commits` is as follows.

```shell-session
+------------------------+--------------+------+-----+---------+-------+
| Field                  | Type         | Null | Key | Default | Extra |
+------------------------+--------------+------+-----+---------+-------+
| commit_id              | varchar(40)  | NO   | PRI | NULL    |       |
| commit_id_short        | varchar(7)   | YES  |     | NULL    |       |
| repository_id          | int          | YES  |     | NULL    |       |
| repository_name        | varchar(255) | YES  |     | NULL    |       |
| commit_message_subject | text         | YES  |     | NULL    |       |
| is_file_modified       | tinyint(1)   | NO   |     | NULL    |       |
| is_code_file_modified  | tinyint(1)   | NO   |     | NULL    |       |
| commit_message_body    | text         | YES  |     | NULL    |       |
| refactor_keyword_id    | int          | YES  |     | NULL    |       |
| commit_date            | timestamp    | NO   |     | NULL    |       |
+------------------------+--------------+------+-----+---------+-------+
```

- `commit_id` Represents the original repository commit ID (SHA1 hash value).
- `commit_id_short`, will be deleted later
- `repository_id`, Repository ID, linked to the repository table.
- `repository_name`, will be deleted later
- `commit_message_subject`, The subject or title of the commit message.
- `is_file_modified`, Indicates whether a file was modified
- `is_code_file_modified`, Indicates whether a code file was modified
- `commit_message_body`, Detailed commit message describing the changes in the commit.
- `refactor_keyword_id`, Refactoring keyword ID, linked to the refactor_keywords table
- `commit_date`, The full date and time of the commit in standardized UTC format.
