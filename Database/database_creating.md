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
