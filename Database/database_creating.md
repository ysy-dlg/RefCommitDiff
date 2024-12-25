# commit_diff_db
Testing Phase Version.

Currently, except for the `commits_finergit_hayashi` (`git log --branches --tags --no-merges -M50`), all other tables use `git log --all` to extract commit information. In the future, I may consider adding options to exclude merge commits and other entries.

The dataset can be downloaded from the following URL:

https://www.dropbox.com/scl/fi/u4ca2zrsjyks1ph1dicqr/commit_diff.db?rlkey=748zcnjkwekh5gd541qvhp95j&st=rgpkfpn4&dl=0

Due to its size exceeding 25MB, it is stored on Dropbox rather than GitHub.

## Tables in commit_diff_db

There are eight tables `commit_diff_lines_finergit`, `commits_original`, `commit_file_changes_finergit`,`finergit_original_mapping`,`commit_file_changes_original` ,`refactor_keywords`,`commits_finergit_hayashi`, 
 and `repository` in commit_diff_db.
```shell-session
sqlite> .tables
commit_diff_lines_finergit    commits_original            
commit_file_changes_finergit  finergit_original_mapping   
commit_file_changes_original  refactor_keywords           
commits_finergit_hayashi      repository  
```

### Tables for storing repository data

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
| token_type     | VARCHAR(50)    | Yes      |                      | Token type: For comment lines, non-terminal lines have a null token type, while terminal lines are `JAVADOCCOMMENT` or `BLOCKCOMMENT` |
| token_value    | TEXT           | No       |                      | Token value                                                  |





- Displaying Data Stored in the Table
```shell-session
sqlite> .mode column
sqlite> .headers on
sqlite> select * from commit_diff_lines_finergit limit 10;
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
sqlite> .mode column
sqlite> .headers on
sqlite> select * from commits_original limit 10;
commit_id                                 repository_id  commit_message_subject                                        is_file_modified  is_code_file_modified  commit_date        
----------------------------------------  -------------  ------------------------------------------------------------  ----------------  ---------------------  -------------------
04b9cd080446ac733ce1aba9ea12d6a4493c3aea  183            Merge pull request #165 from manish364824/master              0                 0                      2021-11-02 11:17:18

8217637f1bb8bf1a4ffbc975496f1ba6ae10260b  183            Merge pull request #164 from bennidi/dependabot/maven/junit-  0                 0                      2021-11-02 11:14:15
                                                         junit-4.13.1                                                                                                              

e341ece35b2f835e5a8240acbc6a441a494620e5  183            Merge pull request #163 from kolybelkin/master                0                 0                      2021-11-02 11:13:51

3e7d5fdb362f4bf9236c4b1f0483c90684b5e2f2  183            Add travis jobs on ppc64le                                    1                 0                      2020-11-16 10:19:55

499ae3a4a3beb4c20de6d856a3eadeb7aaa0119b  183            Bump junit from 4.12 to 4.13.1                                1                 0                      2020-10-13 06:50:00

521ce6e6d96c238b14eb2e0c83e5ffadba8c3785  183            Made it possible to extend MessagePublication class           1                 1                      2019-09-26 09:42:18

3da444255c2abf840c3cafda73081e9b3476098e  183            Added performance chart                                       1                 0                      2019-06-26 15:55:18

5974076faa647b8dd426bde5d26f7df68bb23b7a  183            Update README.md                                              1                 0                      2019-06-26 15:54:00

f173c6406544bed5cd86c407818591ac64648f83  183            Publishing javadoc for mbassador:1.3.3-SNAPSHOT               1                 0                      2018-03-09 14:27:40

60c153fb72868fc31e535852cf0c420022d26c2b  183            Added changelog and version bump                              1                 0                      2018-03-07 14:35:24
                                                                  
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
sqlite> .mode column
sqlite> .headers on
sqlite> select * from commit_file_changes_finergit limit 10;
id  commit_id                                 repository_id  file_status  source_dir                                   source_file                                                   target_dir                               target_file                                                 
--  ----------------------------------------  -------------  -----------  -------------------------------------------  ------------------------------------------------------------  ---------------------------------------  ------------------------------------------------------------
1   666d74dcadad0008601edc5f0a5cde2d7c688f85  183            M            src/main/java/net/engio/mbassy/listener      MetadataReader#public_MessageListener_getMessageListener(Cla                                                                                                       
                                                                                                                       ss).mjava                                                                                                                                                          

2   666d74dcadad0008601edc5f0a5cde2d7c688f85  183            A                                                                                                                       src/test/java/net/engio/mbassy           MetadataReaderTest#public_void_testInterfacedEnveloped().mja
                                                                                                                                                                                                                              va                                                          

3   db7f02c182f6383e05ac8411ff9a18d94ca8a7de  183            M            src/main/java/net/engio/mbassy/common        ReflectionUtils#public_void_getMethods(IPredicate[Method],Cl                                                                                                       
                                                                                                                       ass[#],ArrayList[Method]).mjava                                                                                                                                    

4   db7f02c182f6383e05ac8411ff9a18d94ca8a7de  183            A                                                                                                                       src/test/java/net/engio/mbassy           MetadataReaderTest#public_void_testInterfaced().mjava       

5   8ec06418727afb9cae3ec2180ba5e0875922199a  183            M            src/main/java/net/engio/mbassy/listener      MetadataReader#private_Filter[]_collectFilters(Method,Handle                                                                                                       
                                                                                                                       r).mjava                                                                                                                                                           

6   6fb4a6fc6532c146e9294e0be34555733fdf9da6  183            A                                                                                                                       src/main/java/net/engio/mbassy/listener  MetadataReader#private_Filter[]_collectFilters(Method,Handle
                                                                                                                                                                                                                              r).mjava                                                    

7   6fb4a6fc6532c146e9294e0be34555733fdf9da6  183            R087         src/main/java/net/engio/mbassy/listener      MetadataReader#private_IMessageFilter[]_getFilter(Handler).m  src/main/java/net/engio/mbassy/listener  MetadataReader#private_IMessageFilter[]_getFilter(Method,Han
                                                                                                                       java                                                                                                   dler).mjava                                                 

8   6fb4a6fc6532c146e9294e0be34555733fdf9da6  183            M            src/main/java/net/engio/mbassy/listener      MetadataReader#public_MessageListener_getMessageListener(Cla                                                                                                       
                                                                                                                       ss).mjava                                                                                                                                                          

9   e0f691b68e519b8d9ded82c7235db41bf3724d4a  183            M            src/main/java/net/engio/mbassy/subscription  SubscriptionFactory#protected_IHandlerInvocation_buildInvoca                                                                                                       
                                                                                                                       tionForHandler(SubscriptionContext).mjava                                                                                                                          

10  e0f691b68e519b8d9ded82c7235db41bf3724d4a  183            M            src/main/java/net/engio/mbassy/subscription  SubscriptionFactory#protected_IMessageDispatcher_buildDispat                                                                                                                                                                                                                                                                                                                                                                    
```
</details>

<details>
<summary>Table <code>finergit_original_mapping</code></summary>

- The schema of table `finergit_original_mapping` is as follows.
  
| Field Name         | Data Type      | Nullable | Primary/Foreign Key | Description                |
|--------------------|----------------|----------|----------------------|----------------------------|
| commit_id          | VARCHAR(40)    | No       | Primary Key          | FinerGit commit ID         |
| original_commit_id | VARCHAR(7)     | No       |                      | Original Commit ID         |
| repository_id      | INTEGER        | No       |                      | Repository ID              |
| commit_date        | TIMESTAMP      | Yes      |                      | UTC time, without timezone information  |





- Displaying Data Stored in the Table
```shell-session
sqlite> .mode column
sqlite> .headers on
sqlite> select * from finergit_original_mapping limit 10;
commit_id                                 original_commit_id  repository_id  commit_date        
----------------------------------------  ------------------  -------------  -------------------
05cd010a149fa2e6eb3b40ab42fe4171b25a38de  04b9cd0             183            2021-11-02 11:17:18
4f20bf9c0b05ccebad75d3181ea2c551e2fe640f  8217637             183            2021-11-02 11:14:15
41eea3f033261ef35883fde9c7977047244adcdd  e341ece             183            2021-11-02 11:13:51
81971289a95d7ed5bc4c1a0b06cfa48c4ee4866c  3e7d5fd             183            2020-11-16 10:19:55
5d33b87f2a15a0af0aee0e3e674b9f8dcdb62781  499ae3a             183            2020-10-13 06:50:00
ef9cf0235cb0b719cc2628f122285ece276c7c38  521ce6e             183            2019-09-26 09:42:18
60bd571785505bdf70ad6a39b6dbf1f2ba3998ed  3da4442             183            2019-06-26 15:55:18
84f0c280e70fc4a5b23cee521861fd47604e710c  5974076             183            2019-06-26 15:54:00
73906f9c119316ce040445c4e020fc87ffdc8fdf  60c153f             183            2018-03-07 14:35:24
483c3ea1facbed2d3ea4bfd2ae3301e41693fca6  1e98ff4             183            2018-03-07 14:12:10                                                                                                                                                                                                                                                             
```
</details>

<details>
<summary>Table <code>commit_file_changes_original</code></summary>

- The schema of table `commit_file_changes_original` is as follows.
  - To set the primary key, an auto-increment ID was added.

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
sqlite> .mode column
sqlite> .headers on
sqlite> select * from commit_file_changes_original limit 10;
id  commit_id                                 repository_id  file_status  source_dir                                source_file              target_dir                                target_file        
--  ----------------------------------------  -------------  -----------  ----------------------------------------  -----------------------  ----------------------------------------  -------------------
1   521ce6e6d96c238b14eb2e0c83e5ffadba8c3785  183            M            src/main/java/net/engio/mbassy/bus/       MessagePublication.java                                                               
2   6af52178c3b2ad5d1a08e27f6896c3afad3db824  183            M            src/main/java/net/engio/mbassy/listener/  MessageHandler.java                                                                   
3   6af52178c3b2ad5d1a08e27f6896c3afad3db824  183            M            src/main/java/net/engio/mbassy/listener/  MetadataReader.java                                                                   
4   6af52178c3b2ad5d1a08e27f6896c3afad3db824  183            M            src/test/java/net/engio/mbassy/           MetadataReaderTest.java                                                               
5   c6565f3cfd5a6b3b807e4198690ae4daf9a10a0c  183            M            src/main/java/net/engio/mbassy/common/    ReflectionUtils.java                                                                  
6   c6565f3cfd5a6b3b807e4198690ae4daf9a10a0c  183            M            src/test/java/net/engio/mbassy/           MetadataReaderTest.java                                                               
7   3e7232147c5a7bfcadd36f13c9c3f9822c3bb552  183            R059         src/main/java/net/engio/mbassy/listener/  RepeatedFilters.java     src/main/java/net/engio/mbassy/listener/  IncludeFilters.java
8   3e7232147c5a7bfcadd36f13c9c3f9822c3bb552  183            M            src/main/java/net/engio/mbassy/listener/  MetadataReader.java                                                                   
9   3e7232147c5a7bfcadd36f13c9c3f9822c3bb552  183            M            src/test/java/net/engio/mbassy/           FilterTest.java                                                                       
10  3023b26ee0d84a0617c34a0361b00c4d63dcf1e0  183            M            src/test/java/net/engio/mbassy/           FilterTest.java                                                                                                                                                                                                                                                               
```
</details>

<details>
<summary>Table <code>refactor_keywords</code></summary>

- The schema of table `refactor_keywords` is as follows.

| Field Name      | Data Type      | Nullable | Primary/Foreign Key | Description                                  |
|------------------|----------------|----------|----------------------|----------------------------------------------|
| id               | INTEGER        | No       | Auto-increment Primary Key | Keyword group ID                           |
| base_keyword     | VARCHAR(50)    | No       |                      | Base keyword (e.g., extend)                |
| variant_keyword  | VARCHAR(50)    | No       |                      | Variant keyword (e.g., extend, extended)   |




- Displaying Data Stored in the Table
```shell-session
                                                                                                                                                                                                                                                             
```
</details>

<details>
<summary>Table <code>commits_finergit_hayashi</code></summary>

- The schema of table `commits_finergit_hayashi` is as follows.
  - To set the primary key, an auto-increment ID was added.

| Field Name             | Data Type      | Nullable | Primary/Foreign Key | Description                              |
|-------------------------|----------------|----------|----------------------|------------------------------------------|
| id                      | INTEGER        | No       | Primary Key          | Auto-increment                          |
| commit_id               | VARCHAR(40)    | No       |                      | FinerGit commit ID                      |
| repository_id           | INTEGER        | No       |                      | Repository ID                           |
| file_similarity_score   | INT            | No       |                      | Rxx                                  |
| change_type             | VARCHAR(30)    | No       |                      | Rename Method, Change Parameter, Rename Method+, Move Method, Move Method+, Move and Rename Method, Move and Rename Method+ |
| change_type_info        | TEXT           | No       |                      |                                          |
| old_file_path           | VARCHAR(255)   | No       |                      |                                          |
| new_file_path           | VARCHAR(255)   | No       |                      |                                          |





Displaying Data Stored in the Table
```shell-session
sqlite> .mode column
sqlite> .headers on
sqlite> select * from commits_finergit_hayashi limit 10;
id  commit_id  repository_id  file_similarity_score  change_type       change_type_info                                              old_file_path                                                 new_file_path                                               
--  ---------  -------------  ---------------------  ----------------  ------------------------------------------------------------  ------------------------------------------------------------  ------------------------------------------------------------
1   6fb4a6f    183            87                     Change Parameter  'private_IMessageFilter[]_getFilter(Handler)' to 'private_IM  src/main/java/net/engio/mbassy/listener/MetadataReader#priva  src/main/java/net/engio/mbassy/listener/MetadataReader#priva
                                                                       essageFilter[]_getFilter(Method,Handler)' at 'src/main/java/  te_IMessageFilter[]_getFilter(Handler).mjava                  te_IMessageFilter[]_getFilter(Method,Handler).mjava         
                                                                       net/engio/mbassy/listener/MetadataReader'                                                                                                                                               

2   e234913    183            98                     Rename Method     'protected_IMessagePublication_createMessagePublication' to   src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport#pro  src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport#pro
                                                                       'protected_MessagePublication_createMessagePublication' at '  tected_IMessagePublication_createMessagePublication(T).mjava  tected_MessagePublication_createMessagePublication(T).mjava 
                                                                       src/main/java/net/engio/mbassy/bus/AbstractPubSubSupport'                                                                                                                               

3   e234913    183            97                     Change Parameter  'protected_IMessagePublication_addAsynchronousPublication(IM  src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageB  src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageB
                                                                       essagePublication)' to 'protected_IMessagePublication_addAsy  us#protected_IMessagePublication_addAsynchronousPublication(  us#protected_IMessagePublication_addAsynchronousPublication(
                                                                       nchronousPublication(MessagePublication)' at 'src/main/java/  IMessagePublication).mjava                                    MessagePublication).mjava                                   
                                                                       net/engio/mbassy/bus/AbstractSyncAsyncMessageBus'                                                                                                                                       

4   e234913    183            98                     Change Parameter  'protected_IMessagePublication_addAsynchronousPublication(IM  src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageB  src/main/java/net/engio/mbassy/bus/AbstractSyncAsyncMessageB
                                                                       essagePublication,long,TimeUnit)' to 'protected_IMessagePubl  us#protected_IMessagePublication_addAsynchronousPublication(  us#protected_IMessagePublication_addAsynchronousPublication(
                                                                       ication_addAsynchronousPublication(MessagePublication,long,T  IMessagePublication,long,TimeUnit).mjava                      MessagePublication,long,TimeUnit).mjava                     
                                                                       imeUnit)' at 'src/main/java/net/engio/mbassy/bus/AbstractSyn                                                                                                                            
                                                                       cAsyncMessageBus'                                                                                                                                                                       

5   e234913    183            87                     Rename Method     'public_void_publish' to 'public_IMessagePublication_publish  src/main/java/net/engio/mbassy/bus/MBassador#public_void_pub  src/main/java/net/engio/mbassy/bus/MBassador#public_IMessage
                                                                       ' at 'src/main/java/net/engio/mbassy/bus/MBassador'           lish(T).mjava                                                 Publication_publish(T).mjava                                

6   e234913    183            86                     Rename Method     'public_void_publish' to 'public_IMessagePublication_publish  src/main/java/net/engio/mbassy/bus/SyncMessageBus#public_voi  src/main/java/net/engio/mbassy/bus/SyncMessageBus#public_IMe
                                                                       ' at 'src/main/java/net/engio/mbassy/bus/SyncMessageBus'      d_publish(T).mjava                                            ssagePublication_publish(T).mjava                           

7   e234913    183            94                     Rename Method     'void_publish' to 'IMessagePublication_publish' at 'src/main  src/main/java/net/engio/mbassy/bus/common/PubSubSupport#void  src/main/java/net/engio/mbassy/bus/common/PubSubSupport#IMes
                                                                       /java/net/engio/mbassy/bus/common/PubSubSupport'              _publish(T).mjava                                             sagePublication_publish(T).mjava                            

8   e234913    183            69                     Change Parameter  'public_PublicationError(Throwable,String,Method,Object,Obje  src/main/java/net/engio/mbassy/bus/error/PublicationError#pu  src/main/java/net/engio/mbassy/bus/error/PublicationError#pu
                                                                       ct)' to 'public_PublicationError(Throwable,String,Method,Obj  blic_PublicationError(Throwable,String,Method,Object,Object)  blic_PublicationError(Throwable,String,Method,Object,IMessag
                                                                       ect,IMessagePublication)' at 'src/main/java/net/engio/mbassy  .mjava                                                        ePublication).mjava                                         
                                                                       /bus/error/PublicationError'                                                                                                                                                            

9   e234913    183            86                     Change Parameter  'public_void_invoke(Object,Object)' to 'public_void_invoke(O  src/main/java/net/engio/mbassy/dispatch/AsynchronousHandlerI  src/main/java/net/engio/mbassy/dispatch/AsynchronousHandlerI
                                                                       bject,Object,MessagePublication)' at 'src/main/java/net/engi  nvocation#public_void_invoke(Object,Object).mjava             nvocation#public_void_invoke(Object,Object,MessagePublicatio
                                                                       o/mbassy/dispatch/AsynchronousHandlerInvocation'                                                                            n).mjava                                                    

10  e234913    183            96                     Change Parameter  'public_void_dispatch(IMessagePublication,Object,Iterable)'   src/main/java/net/engio/mbassy/dispatch/EnvelopedMessageDisp  src/main/java/net/engio/mbassy/dispatch/EnvelopedMessageDisp
                                                                       to 'public_void_dispatch(MessagePublication,Object,Iterable)  atcher#public_void_dispatch(IMessagePublication,Object,Itera  atcher#public_void_dispatch(MessagePublication,Object,Iterab
                                                                       ' at 'src/main/java/net/engio/mbassy/dispatch/EnvelopedMessa  ble).mjava                                                    le).mjava                                                   
                                                                       geDispatcher'                                                                                                                                                                           
                                                                                                                                                                                                                                                             
```
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




- Displaying Data Stored in the Table
```shell-session
sqlite> .mode column
sqlite> .headers on
sqlite> select * from repository limit 10;
id  repository_url                                              repository_name          language
--  ----------------------------------------------------------  -----------------------  --------
1   https://github.com/CyanogenMod/android_frameworks_base.git  android_frameworks_base  Java    
2   https://github.com/dropwizard/metrics.git                   metrics                  Java    
3   https://github.com/processing/processing.git                processing               Java    
4   https://github.com/apache/hive.git                          hive                     Java    
5   https://github.com/puniverse/quasar.git                     quasar                   Java    
6   https://github.com/JoanZapata/android-iconify.git           android-iconify          Java    
7   https://github.com/redsolution/xabber-android.git           xabber-android           Java    
8   https://github.com/ReactiveX/RxJava.git                     RxJava                   Java    
9   https://github.com/google/truth.git                         truth                    Java    
10  https://github.com/brianfrankcooper/YCSB.git                YCSB                     Java                                                                                                                                                                                                                                                              
```
</details>


### Table for storing detected refactoring information


</details>

<details>
<summary>Table <code>rename_method_name</code></summary>

- The schema of table `refactor_keywords` is as follows.

| Field Name      | Data Type      | Nullable | Primary/Foreign Key | Description                                  |
|------------------|----------------|----------|----------------------|----------------------------------------------|
| id               | INTEGER        | No       | Auto-increment Primary Key | Keyword group ID                           |
| base_keyword     | VARCHAR(50)    | No       |                      | Base keyword (e.g., extend)                |
| variant_keyword  | VARCHAR(50)    | No       |                      | Variant keyword (e.g., extend, extended)   |




- Displaying Data Stored in the Table
```shell-session
                                                                                                                                                                                                                                                             
```









---
# Token Types Supported by [FinerGit](https://github.com/kusumotolab/FinerGit)



<details>
<summary>Token Types</summary>
	
	ABSTRACT
	AND
	AND2
	ANDAND
	ANDEQUAL
	ANNOTATION
	ANNOTATIONCOMMA
	ANNOTATIONTYPEMEMBERDECLARATIONSEMICOLON
	ARRAYINITIALIZERCOMMA
	AS
	ASM
	ASSERT
	ASSERTSTATEMENTSEMICOLON
	ASSIGN
	AUTO
	BACKQUOTELITERAL
	BACKSLASH
	BLOCKCOMMENT
	BOOLEAN
	BOOLEANLITERAL
	BREAK
	BREAKSTATEMENTSEMICOLON
	BYTE
	BooleanLiteralFactory
	CASE
	CATCH
	CHAR
	CHARLITERAL
	CLASS
	CLASSINSTANCECREATIONCOMMA
	CLASSNAME
	COLON
	COMMA
	COMMENT
	CONST
	CONSTRUCTORINVOCATIONCOMMA
	CONSTRUCTORINVOCATIONSEMICOLON
	CONTINUE
	CONTINUESTATEMENTSEMICOLON
	DECLAREDMETHODNAME
	DECREMENT
	DEF
	DEFAULT
	DEL
	DIMENSIONCOMMA
	DIVIDE
	DIVIDEDIVIDEEQUAL
	DIVIDEEQUAL
	DO
	DOSTATEMENTSEMICOLON
	DOT
	DOUBLE
	ELIF
	ELSE
	EMPTYSTATEMENTSEMICOLON
	ENDASM
	ENTRY
	ENUM
	ENUMCOMMA
	EQUAL
	EXCEPT
	EXCLUSIVEOR
	EXCLUSIVEOREQUAL
	EXPRESSIONSTATEMENTSEMICOLON
	EXTENDS
	EXTERN
	FALSE
	FALSE2
	FIELDDECLARATIONCOMMA
	FIELDDECLARATIONSEMICOLON
	FIELDNAME
	FINAL
	FINALLY
	FLOAT
	FOR
	FORCONDITIONSEMICOLON
	FORINITIALIZERCOMMA
	FORINITIALIZERSEMICOLON
	FORUPDATERCOMMA
	FROM
	FinerJavaClassToken
	FinerJavaFieldToken
	FinerJavaMethodToken
	FinerJavaRecordToken
	GLOBAL
	GOTO
	GREAT
	GREATEQUAL
	IDENTIFIER
	IF
	IMPLEMENTS
	IMPORT
	IMPORTNAME
	IN
	INCREMENT
	INSTANCEOF
	INT
	INTERFACE
	INVOKEDMETHODNAME
	IS
	JAVADOCCOMMENT
	JavaToken
	LABELNAME
	LAMBDA
	LAMBDAEXPRESSIONCOMMA
	LEFTANNOTATIONBRACKET
	LEFTANNOTATIONPAREN
	LEFTANONYMOUSCLASSBRACKET
	LEFTARRAYINITIALIZERBRACKET
	LEFTBRACKET
	LEFTCASTPAREN
	LEFTCATCHCLAUSEBRACKET
	LEFTCATCHCLAUSEPAREN
	LEFTCLASSBRACKET
	LEFTCLASSINSTANCECREATIONPAREN
	LEFTCONSTRUCTORINVOCATIONPAREN
	LEFTDOBRACKET
	LEFTDOPAREN
	LEFTENHANCEDFORBRACKET
	LEFTENHANCEDFORPAREN
	LEFTENUMBRACKET
	LEFTENUMPAREN
	LEFTFORBRACKET
	LEFTFORPAREN
	LEFTIFBRACKET
	LEFTIFPAREN
	LEFTINITIALIZERBRACKET
	LEFTLAMBDABRACKET
	LEFTLAMBDAEXPRESSIONBRACKET
	LEFTLAMBDAEXPRESSIONPAREN
	LEFTMETHODBRACKET
	LEFTMETHODINVOCATIONPAREN
	LEFTMETHODPAREN
	LEFTPAREN
	LEFTPARENTHESIZEDEXPRESSIONPAREN
	LEFTRECORDBRACKET
	LEFTRECORDPAREN
	LEFTRECORDPATTERNPAREN
	LEFTSHIFT
	LEFTSHIFTEQUAL
	LEFTSIMPLEBLOCKBRACKET
	LEFTSQUAREBRACKET
	LEFTSUPERCONSTRUCTORINVOCATIONPAREN
	LEFTSWITCHBRACKET
	LEFTSWITCHPAREN
	LEFTSYNCHRONIZEDBRACKET
	LEFTSYNCHRONIZEDPAREN
	LEFTTRYBRACKET
	LEFTTRYPAREN
	LEFTWHILEBRACKET
	LEFTWHILEPAREN
	LESS
	LESSEQUAL
	LINECOMMENT
	LINEEND
	LINEINTERRUPTION
	LONG
	LineToken
	LineType
	METHODDECLARAIONPARAMETERCOMMA
	METHODDECLARATIONSEMICOLON
	METHODDECLARATIONTHROWSCOMMA
	METHODINVOCATIONCOMMA
	METHODREFERENCE
	MINUS
	MINUSEQUAL
	MOD
	MODEQUAL
	ModifierFactory
	NATIVE
	NEW
	NONE
	NONLOCAL
	NOT
	NOT2
	NOTEQUAL
	NOTEQUAL2
	NULL
	NULL2
	NUMBERLITERAL
	OR
	OR2
	OREQUAL
	OROR
	OperatorFactory
	PACKAGE
	PACKAGENAME
	PARAMETERIZEDTYPECOMMA
	PARAMETERNAME
	PASS
	PLUS
	PLUSEQUAL
	PRIVATE
	PROTECTED
	PUBLIC
	PrimitiveTypeFactory
	QUESTION
	RAISE
	RECORD
	RECORDCOMPONENTCOMMA
	RECORDNAME
	REGISTER
	RETURN
	RETURNSTATEMENTSEMICOLON
	RIGHTANNOTATIONBRACKET
	RIGHTANNOTATIONPAREN
	RIGHTANONYMOUSCLASSBRACKET
	RIGHTARRAYINITIALIZERBRACKET
	RIGHTARROW
	RIGHTBRACKET
	RIGHTCASTPAREN
	RIGHTCATCHCLAUSEBRACKET
	RIGHTCATCHCLAUSEPAREN
	RIGHTCLASSBRACKET
	RIGHTCLASSINSTANCECREATIONPAREN
	RIGHTCONSTRUCTORINVOCATIONPAREN
	RIGHTDOBRACKET
	RIGHTDOPAREN
	RIGHTENHANCEDFORBRACKET
	RIGHTENHANCEDFORPAREN
	RIGHTENUMBRACKET
	RIGHTENUMPAREN
	RIGHTFORBRACKET
	RIGHTFORPAREN
	RIGHTIFBRACKET
	RIGHTIFPAREN
	RIGHTINITIALIZERBRACKET
	RIGHTLAMBDABRACKET
	RIGHTLAMBDAEXPRESSIONBRACKET
	RIGHTLAMBDAEXPRESSIONPAREN
	RIGHTMETHODBRACKET
	RIGHTMETHODINVOCATIONPAREN
	RIGHTMETHODPAREN
	RIGHTPAREN
	RIGHTPARENTHESIZEDEXPRESSIONPAREN
	RIGHTRECORDBRACKET
	RIGHTRECORDPAREN
	RIGHTRECORDPATTERNPAREN
	RIGHTSHIFT
	RIGHTSHIFT2
	RIGHTSHIFTEQUAL
	RIGHTSHIFTEQUAL2
	RIGHTSIMPLEBLOCKBRACKET
	RIGHTSQUAREBRACKET
	RIGHTSUPERCONSTRUCTORINVOCATIONPAREN
	RIGHTSWITCHBRACKET
	RIGHTSWITCHPAREN
	RIGHTSYNCHRONIZEDBRACKET
	RIGHTSYNCHRONIZEDPAREN
	RIGHTTRYBRACKET
	RIGHTTRYPAREN
	RIGHTWHILEBRACKET
	RIGHTWHILEPAREN
	SEMICOLON
	SHARP
	SHORT
	SIGNED
	SIZEOF
	STAR
	STAREQUAL
	STARSTAREQUAL
	STATEMENT
	STATIC
	STRICTFP
	STRINGLITERAL
	STRUCT
	SUPER
	SUPERCONSTRUCTORINVOCATIONCOMMA
	SUPERCONSTRUCTORINVOCATIONSEMICOLON
	SWITCH
	SWITCHCASEARROW
	SWITCHCASECOMMA
	SYNCHRONIZED
	TAB
	THIS
	THROW
	THROWS
	THROWSTATEMENTSEMICOLON
	TILDA
	TRANSIENT
	TRUE
	TRUE2
	TRY
	TRYRESOURCESEMICOLON
	TYPEDECLARATIONCOMMA
	TYPEDEF
	TYPENAME
	TYPEPARAMETERNAME
	UNION
	UNSIGNED
	VARIABLEDECLARATIONCOMMA
	VARIABLEDECLARATIONSTATEMENTSEMICOLON
	VARIABLENAME
	VOID
	VOLATILE
	VariableArity
	WHEN
	WHILE
	WHITESPACE
	WITH
	YIELD
	YIELDSTATEMENTSEMICOLON
</details>
