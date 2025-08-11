#!/usr/bin/env python3
"""
Dynamically find missing task files from submission directory.
"""

import os
import glob
import re

def find_missing_tasks():
    # Get all task JSON files from google-code-golf-2025 directory
    task_dir = "google-code-golf-2025"
    submission_dir = "submission"
    
    # Find all task JSON files
    json_files = glob.glob(os.path.join(task_dir, "task*.json"))
    all_task_nums = set()
    for file in json_files:
        match = re.search(r'task(\d+)\.json', file)
        if match:
            all_task_nums.add(int(match.group(1)))
    
    # Find all submitted Python files
    py_files = glob.glob(os.path.join(submission_dir, "task*.py"))
    submitted_task_nums = set()
    for file in py_files:
        match = re.search(r'task(\d+)\.py', file)
        if match:
            submitted_task_nums.add(int(match.group(1)))
    
    # Find missing tasks
    missing_task_nums = sorted(all_task_nums - submitted_task_nums)
    missing_files = [f"task{num:03d}.py" for num in missing_task_nums]
    
    return missing_files, len(all_task_nums), len(submitted_task_nums)

if __name__ == "__main__":
    missing_files, total_tasks, submitted_tasks = find_missing_tasks()
    print(f"Total tasks: {total_tasks}")
    print(f"Submitted tasks: {submitted_tasks}")
    print(f"Missing {len(missing_files)} task files:")
    for filename in missing_files:
        print(filename)
