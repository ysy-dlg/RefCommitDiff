# RefCommitDiff
Language-agnostic Refactoring Detection

## all_commit_diff_db
Testing Phase Version.

Considering the data volume in the later stages, I chose MySQL instead of SQLite.

Currently, I am using `git log --all`. In the future, I may consider adding options to exclude merge commits and other entries.

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
mysql> desc mbassador_all_original_commits;
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
- `commit_id_short`, will be deleted later.
- `repository_id`, Repository ID, linked to the repository table.
- `repository_name`, will be deleted later.
- `commit_message_subject`, The subject or title of the commit message.
- `is_file_modified`, Indicates whether a file was modified.
- `is_code_file_modified`, Indicates whether a code file was modified.
- `commit_message_body`, Detailed commit message describing the changes in the commit.
- `refactor_keyword_id`, Refactoring keyword ID, linked to the refactor_keywords table.
- `commit_date`, UTC time without timezone information.

**`is_code_file_modified`** can help filter out commits that do not contain code file (e.g..java) changes.

### Table `mbassador_all_finergit_commits`

The schema of table `mbassador_all_finergit_commits` is as follows.

```shell-session
mysql> desc mbassador_all_finergit_commits;
+--------------------+-------------+------+-----+---------+-------+
| Field              | Type        | Null | Key | Default | Extra |
+--------------------+-------------+------+-----+---------+-------+
| commit_id          | varchar(40) | NO   | PRI | NULL    |       |
| original_commit_id | varchar(7)  | NO   |     | NULL    |       |
| commit_date        | timestamp   | YES  |     | NULL    |       |
+--------------------+-------------+------+-----+---------+-------+
```

- `commit_id` Represents the commit ID of a repository tokenized using FinerGit.
- `original_commit_id`, Represents the original repository commit ID (SHA1 hash value).
- `commit_date`, UTC time without timezone information.
  
This table stores the mapping between the commit IDs of the original repository and the tokenized repository.

### Table `mbassador_all_diff_lines`


The schema of table `mbassador_all_diff_lines` is as follows.

```shell-session
mysql> desc mbassador_all_diff_lines;
+---------------+---------------+------+-----+---------+----------------+
| Field         | Type          | Null | Key | Default | Extra          |
+---------------+---------------+------+-----+---------+----------------+
| id            | int           | NO   | PRI | NULL    | auto_increment |
| commit_id     | varchar(40)   | NO   |     | NULL    |                |
| file_name     | varchar(255)  | NO   |     | NULL    |                |
| file_path     | text          | NO   |     | NULL    |                |
| commit_date   | timestamp     | NO   |     | NULL    |                |
| hunk_id       | int           | NO   |     | NULL    |                |
| hunk_header   | text          | NO   |     | NULL    |                |
| line_id       | int           | NO   |     | NULL    |                |
| change_type   | enum('+','-') | NO   |     | NULL    |                |
| token_type    | varchar(50)   | YES  |     | NULL    |                |
| token_value   | text          | NO   |     | NULL    |                |
| refactor_type | varchar(50)   | YES  |     | NULL    |                |
+---------------+---------------+------+-----+---------+----------------+
```

- `id`, Auto-increment primary key.
- `commit_id`, Represents the commit ID of a repository tokenized using FinerGit.
- `file_name`, File name of the .mjava file, without path information.
- `file_path`, File path of the .mjava file.
- `commit_date`, UTC time without timezone information.
- `hunk_id`, Unique identifier for a hunk (Hunk ID), starting from 0, indicating the sequence number of each hunk in the diff.
- `hunk_header`, Header information of the hunk.
- `line_id`, Unique identifier for a line (Line ID), starting from 0, representing the relative line number in the diff file.
- `change_type`, Type of change (+ for additions, - for deletions).
- `token_type`, Type of token. If empty, it is a comment and can be ignored. JAVADOC comments are also considered comments and can be ignored.
- `token_value`, Refactoring keyword ID, linked to the refactor_keywords table.
- `refactor_type`, Value of the token.
