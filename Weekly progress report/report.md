# Progress Report
## 2025/2/13

### Done
- Classified the hunks of refactoring commits
- Analyzed some commits (hunk ➡️ tokenized files ➡️ original files)
- [manual_analysis](../manual_analysis/20250213/20250213.md)



  
### To do 
1. Classification of Hunks  

2. Consider how to process the data so that it can be used to train machine learning models
3. Machine learning model selection
  

## 2025/1/6

### Done
- Time spent on this project this week (3h)
- Identify the hunks of refactoring commits (from hayashi-sensei) and try to classify the hunks by simple metrics
  1. Size of the hunk
  2. Number of tokens added and removed

    
### Doing
- Making a histogram of these hunks information
  
### To do 
1. Statistics of Files and Hunks in Refactoring Commits 
   - Number of modified files  
   - Number of hunks  
   - Average and median size of hunks (+ lines and - lines)  

2. Classification of Hunks  
   - Categorize hunks by operation type, such as "replacing an identifier," "replacing code," "removing code," etc.  

3. Classification of File Modification Operations 
   - Classify file modifications into operations such as file creation, file deletion, file renaming, or file modification, and identify refactoring types based on the hunks they contain.  


## 2024/12/30

### Done
- Time spent on this project this week (10h)
- Summarize the [patterns](/RefactoringPatterns/RefactoringPatterns.md) of refactoring types.

    
### Doing
- Summarize the [patterns](/RefactoringPatterns/RefactoringPatterns.md) of refactoring types.
 
  
### To do 
- Complete the summarization of the patterns of refactoring types.  

## 2024/12/23

### Done
- Time spent on this project this week (30h)
- Migrate the [database](/Database/database_creating.md) to SQLite and optimize the database structure.
  -  Except for the repository table, the others only store data about the Mbassador repository.
  -  After completing the pattern design for all detectable refactoring types using Mbassador, all required repository data will be added to the database.
  -  Added a file-level change log table for the original repository and the tokenized repository
  -  Fixed various issues encountered when extracting diff code lines from the tokenized repository, such as the failure to extract token values due to special characters in strings.

    
### Doing
- Summarize the [patterns](/RefactoringPatterns/RefactoringPatterns.md) of refactoring types.
  - With the database in place, I hope to complete the summary of all patterns of refactoring types.
  
### To do 
- Complete the summarization of the patterns of refactoring types.  

## 2024/12/16

### Done
- Time spent on this project this week (25h)
- Identifying Potential Refactoring Commits (mbassador)
  1. Use `is_code_file_modified = 1` from `mbassador_all_original_commits` to filter out commits that do not involve code file changes. ➡️ 110 commits
  2. Combine manual analysis and GPT-4.0 to determine potential refactoring based on commit information, file changes, and diff code, and label the possible refactoring types. ➡️ 80 commits
  3. Summarized refactoring keywords:
     - **Added**
     - **Fix**
     - **Changed**
     - **Improvements**
     - **Refactorings**
     - **Release**
     - **Update**
     - **Extend**
     - **Introduced**
     - **Performance**
     - **Moved**
     - **Extension**
  4. For mbassador, Hayashi-sensei obtained 547 refactoring instances by detecting file name changes. Using the same logic, I obtained 455 refactoring instances.     


    
### Doing
- Summarize the patterns of refactoring types.
  
### To do
- Migrate the database to SQLite and optimize the database structure.  
- Complete the summarization of the patterns of refactoring types.  
- Complete the full workflow using "mabassador" as the experimental subject.
- Consider creating prompt engineering to let GPT-4.0 handle the task of identifying potential refactoring types in the original repository commits.
