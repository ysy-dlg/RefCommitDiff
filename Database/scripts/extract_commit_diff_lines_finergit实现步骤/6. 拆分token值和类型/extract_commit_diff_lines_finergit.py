import os
import csv
import sys
import re
from datetime import datetime, timezone

def process_logs(input_dir, output_dir):
    # Check and handle output directory
    if os.path.exists(output_dir):
        print(f"Clearing contents of the last subdirectory in output: {output_dir}")
        for item in os.listdir(output_dir):
            item_path = os.path.join(output_dir, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                for sub_item in os.listdir(item_path):
                    os.remove(os.path.join(item_path, sub_item))
    else:
        print(f"Creating output directory: {output_dir}")
        os.makedirs(output_dir)

    # Iterate through [repo_name] subdirectories
    for repo_name in os.listdir(input_dir):
        repo_path = os.path.join(input_dir, repo_name)
        if os.path.isdir(repo_path):
            csv_filename = os.path.join(output_dir, f"{repo_name}_commit_diff_lines_finergit.csv")
            
            with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['commit_id', 'commit_date', 'file_name_mjava', 'file_path', 'repository_name', 'hunk_id', 'hunk_header', 'line_id', 'token_value', 'token_type', 'change_type'])  # Adjusted headers
                
                for log_file in os.listdir(repo_path):
                    log_file_path = os.path.join(repo_path, log_file)
                    if log_file.endswith(".log") and os.path.isfile(log_file_path):
                        process_log_file(log_file_path, writer, repo_name)

def process_log_file(log_file_path, writer, repository_name):
    with open(log_file_path, 'r', encoding='utf-8') as log_file:
        lines = log_file.readlines()
        
        commit_id = None
        commit_date = None
        file_name_mjava = None
        file_path = None
        
        hunk_id = 0
        hunk_headers = []
        hunk_lines = []
        
        for line in lines:
            if line.startswith("commit_id:"):
                commit_id = line.split(":", 1)[1].strip()
            elif line.startswith("commit_date:"):
                raw_date = line.split(":", 1)[1].strip()
                commit_date = convert_to_utc(raw_date)
            elif line.startswith("file_name_mjava:"):
                file_name_mjava = line.split(":", 1)[1].strip()
            elif line.startswith("file_path:"):
                file_path = line.split(":", 1)[1].strip()
            elif line.startswith("@@"):
                if hunk_headers and hunk_lines:  # Write the previous hunk
                    write_hunk(writer, commit_id, commit_date, file_name_mjava, file_path, repository_name, hunk_id, hunk_headers[-1], hunk_lines)
                    hunk_id += 1
                hunk_headers.append(line.strip())
                hunk_lines = []  # Reset line collection
            elif hunk_headers:
                hunk_lines.append(line.rstrip())
        
        if hunk_headers and hunk_lines:  # Write the last hunk
            write_hunk(writer, commit_id, commit_date, file_name_mjava, file_path, repository_name, hunk_id, hunk_headers[-1], hunk_lines)

def write_hunk(writer, commit_id, commit_date, file_name_mjava, file_path, repository_name, hunk_id, hunk_header, hunk_lines):
    line_id = 0  # Reset line_id, starting from 0
    in_comment_block = False  # Track whether inside a comment block
    for line_content in hunk_lines:
        # Skip empty lines
        if not line_content.strip():
            line_id += 1
            continue

        # Determine change_type and adjusted line_content
        if line_content.startswith('+'):
            change_type = '+'
            line_content = line_content[1:].strip()
        elif line_content.startswith('-'):
            change_type = '-'
            line_content = line_content[1:].strip()
        elif line_content.startswith(' '):
            change_type = ''
            line_content = line_content[1:].strip()
        else:
            change_type = ''
            line_content = line_content.strip()

        # Handle comment block logic
        if line_content.startswith("/**"):
            in_comment_block = True

        if in_comment_block:
            if line_content.startswith("*/") and "JAVADOCCOMMENT" in line_content:
                # Handle comment block ending
                token_value = "*/"
                token_type = "JAVADOCCOMMENT"
                in_comment_block = False
            elif line_content.startswith("*"):
                # Handle comment lines inside the block
                token_value = line_content
                token_type = ""
            else:
                # Any other line inside a comment block
                token_value = line_content
                token_type = ""
        else:
            # Split line_content into token_value and token_type outside comment blocks
            parts = line_content.rsplit(maxsplit=1)
            token_value = parts[0]
            token_type = parts[1] if len(parts) > 1 else ""

        # Write only if it's a change line (+ or -)
        if change_type in ('+', '-'):
            writer.writerow([commit_id, commit_date, file_name_mjava, file_path, repository_name, hunk_id, hunk_header, line_id, token_value, token_type, change_type])

        # Increment line_id regardless of writing
        line_id += 1

def convert_to_utc(raw_date):
    # Convert date string to UTC format and remove timezone info
    date_obj = datetime.strptime(raw_date, "%a %b %d %H:%M:%S %Y %z")
    utc_date = date_obj.astimezone(timezone.utc).replace(tzinfo=None)
    return utc_date.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 extract_commit_diff_lines_finergit.py <input_dir> <output_dir>")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    if not os.path.isdir(input_dir):
        print(f"Input directory does not exist or is not valid: {input_dir}")
        sys.exit(1)

    process_logs(input_dir, output_dir)

