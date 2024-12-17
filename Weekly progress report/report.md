# Progress Report

## 12/16

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
