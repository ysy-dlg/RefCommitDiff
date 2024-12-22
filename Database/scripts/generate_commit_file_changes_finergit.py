import os
import re
import subprocess
import csv
import sys

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <repo_directory> <output_directory>")
        sys.exit(1)

    repo_dir = sys.argv[1]
    output_dir = sys.argv[2]

    # Ensure output directory exists
    if os.path.exists(output_dir):
        print(f"Clearing directory: {output_dir}")
        for file in os.listdir(output_dir):
            file_path = os.path.join(output_dir, file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                os.rmdir(file_path)
    else:
        print(f"Creating directory: {output_dir}")
        os.makedirs(output_dir)

    # Check if file has .mjava extension
    def is_mjava_file(file_path):
        return file_path.endswith(".mjava")

    for repo in os.listdir(repo_dir):
        repo_path = os.path.join(repo_dir, repo)
        if os.path.isdir(os.path.join(repo_path, ".git")):
            output_file = os.path.join(output_dir, f"{repo}_commit_file_changes_finergit.csv")
            print(f"Processing repository: {repo}")

            with open(output_file, mode="w", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["commit_id", "file_status", "source_dir", "source_file", "target_dir", "target_file", "repository_name"])

                git_log = subprocess.run(["git", "-C", repo_path, "log", "--all", "--name-status", "--format=%H"],
                                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                if git_log.returncode != 0:
                    print(f"Error processing {repo}: {git_log.stderr}")
                    continue

                commit_id = ""
                for line in git_log.stdout.splitlines():
                    if re.match(r"^[a-f0-9]{40}$", line):
                        commit_id = line
                    elif line and commit_id:
                        parts = line.split('\t')
                        if len(parts) < 2:
                            continue

                        file_status = parts[0]

                        if file_status.startswith("R") and len(parts) > 2:
                            # Handle renames with source and target files
                            source_file_path, target_file_path = parts[1], parts[2]
                            if is_mjava_file(source_file_path) or is_mjava_file(target_file_path):
                                writer.writerow([
                                    commit_id, file_status, os.path.dirname(source_file_path), os.path.basename(source_file_path), os.path.dirname(target_file_path), os.path.basename(target_file_path), repo
                                ])
                        elif file_status.startswith("C") and len(parts) > 2:
                            # Handle copies with source and target files
                            source_file_path, target_file_path = parts[1], parts[2]
                            if is_mjava_file(source_file_path) or is_mjava_file(target_file_path):
                                writer.writerow([
                                    commit_id, file_status, os.path.dirname(source_file_path), os.path.basename(source_file_path), os.path.dirname(target_file_path), os.path.basename(target_file_path), repo
                                ])
                        elif file_status in {"A"}:
                            # Handle additions
                            target_file_path = parts[1]
                            if is_mjava_file(target_file_path):
                                writer.writerow([
                                    commit_id, file_status, "", "", os.path.dirname(target_file_path), os.path.basename(target_file_path), repo
                                ])
                        elif file_status in {"M"}:
                            # Handle modifications
                            source_file_path = parts[1]
                            if is_mjava_file(source_file_path):
                                writer.writerow([
                                    commit_id, file_status, os.path.dirname(source_file_path), os.path.basename(source_file_path), "", "", repo
                                ])
                        elif file_status in {"D"}:
                            # Handle deletions
                            source_file_path = parts[1]
                            if is_mjava_file(source_file_path):
                                writer.writerow([
                                    commit_id, file_status, os.path.dirname(source_file_path), os.path.basename(source_file_path), "", "", repo
                                ])
                        elif file_status in {"T"}:
                            # Handle type changes
                            source_file_path = parts[1]
                            if is_mjava_file(source_file_path):
                                writer.writerow([
                                    commit_id, file_status, os.path.dirname(source_file_path), os.path.basename(source_file_path), "", "", repo
                                ])
                        elif file_status in {"U"}:
                            # Handle unresolved conflicts
                            source_file_path = parts[1]
                            if is_mjava_file(source_file_path):
                                writer.writerow([
                                    commit_id, file_status, os.path.dirname(source_file_path), os.path.basename(source_file_path), "", "", repo
                                ])

            # Remove file if only header exists
            if os.path.getsize(output_file) == 0:
                os.remove(output_file)

    print("Processing completed. CSV files are saved in", output_dir)

if __name__ == "__main__":
    main()

