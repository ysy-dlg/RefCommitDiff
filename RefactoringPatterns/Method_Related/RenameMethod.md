### **Key Concept**

`Rename Method` refactoring typically involves the following changes:
1. **Method Declaration Change**: The method name in the same file is modified.  
2. **Invocation Relationship Change**: The method invocation names are updated.  
3. **Filename Change**: Since `.mjava` filenames embed method names, renaming a method may also change the filename.

---

### **Data Sources**

Detecting this type of refactoring requires the following data:
- **Change Lines**: The `commit_diff_lines_finergit` table records line-by-line code changes (`+` for additions, `-` for deletions).  
- **File Status**: The `commit_file_changes_finergit` table records the addition, modification, deletion, or renaming of files.  
- **Commit Records**: The `commits_original` table or related tables associate commit times and commit messages with changes.

---

### **Step 1: Filtering Renamed (`Rxx`) Files**

#### **Objective**:
Filter records with `Rxx` file status from the `commit_file_changes_finergit` table. These records indicate renamed files, and comparing `source_file` with `target_file` filenames can help identify potential method name changes.

#### **SQL Query**:
```sql
SELECT 
    commit_id, 
    source_file, 
    target_file, 
    file_status
FROM 
    commit_file_changes_finergit
WHERE 
    file_status LIKE 'R%';
```

#### **Query Results Example**:
| commit_id | source_file                          | target_file                          | file_status |
|-----------|--------------------------------------|--------------------------------------|-------------|
| 123abc    | ExampleClass#oldMethod(String).mjava | ExampleClass#newMethod(String).mjava | R95         |
| 456def    | OldClass#oldMethod(String).mjava     | NewClass#newMethod(String).mjava     | R87         |

---

### **Step 2: Comparing Method Name Changes in Filenames**

#### **Possible Filename Formats**

1. **Complete Format**:  
   ```
   ClassName#AccessModifier_ReturnType_MethodName(ParameterList).mjava
   ```
2. **Without Access Modifier**:  
   ```
   ClassName#ReturnType_MethodName(ParameterList).mjava
   ```
3. **Without Parameter List**:  
   ```
   ClassName#AccessModifier_ReturnType_MethodName().mjava
   ```
4. **Only ReturnType and MethodName**:  
   ```
   ClassName#ReturnType_MethodName().mjava
   ```

---

### **Filename Parsing Rules**

| Format                  | Example                                                   | Parsing Rule                              |
|-------------------------|----------------------------------------------------------|------------------------------------------|
| Complete Format         | `ClassName#AccessModifier_ReturnType_MethodName(ParameterList).mjava` | Extract the 3rd segment after `#`, split by `_` |
| Without `AccessModifier`| `ClassName#ReturnType_MethodName(ParameterList).mjava`               | Extract the 2nd segment after `#`, split by `_` |
| Without `ParameterList` | `ClassName#AccessModifier_ReturnType_MethodName().mjava`             | Extract the 2nd segment after `#`, split by `_` |
| Only `ReturnType` and `MethodName` | `ClassName#ReturnType_MethodName().mjava`                        | Extract the 2nd segment after `#`, split by `_` |

---

### **Python Script Implementation**

- The script extracts method names from filenames and identifies `Rename Method` refactorings where the `ClassName` is the same, but the `MethodName` has changed.
- Results are stored in the SQLite `rename_method` table.

