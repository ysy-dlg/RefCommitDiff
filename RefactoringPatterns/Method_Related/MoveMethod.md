### **Move Method Detection**

To detect `Move Method` refactorings, we focus on cases where:

- The `ClassName` changes, indicating the method has moved to a different class.
- The method signature (`AccessModifier_ReturnType_MethodName(ParameterList)`) remains unchanged.

This detection requires comparing the `source_file` and `target_file` in renamed files (`Rxx`), extracting the `ClassName` and method signature, and identifying changes.

---

### **Steps to Detect Move Method**

1. **Filter Renamed Files (`Rxx`)**:
   - Use the `commit_file_changes_finergit` table to find renamed files where the file status is `Rxx`.

2. **Extract ClassName and Method Signature**:
   - From `source_file` and `target_file`, extract:
     - `ClassName`: The portion before the `#`.
     - `Method Signature`: The portion after the `#` (e.g., `AccessModifier_ReturnType_MethodName(ParameterList)`).

3. **Compare ClassName and Method Signature**:
   - If `ClassName` differs but the `Method Signature` is identical, classify it as a `Move Method`.

---

### **Filename Parsing Rules**

For the filename format `ClassName#AccessModifier_ReturnType_MethodName(ParameterList).mjava`:

| Component         | Parsing Rule                          |
|-------------------|---------------------------------------|
| `ClassName`       | The part before `#`.                 |
| `Method Signature`| The part after `#`, split into segments separated by `_`. |

---

### **SQL Query to Filter Renamed Files**

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

---

### **Python Script Implementation**


- The script identifies `Move Method` refactorings based on filename changes where the `ClassName` changes but the `Method Signature` remains identical.
- Results are stored in the SQLite `move_method` table.



