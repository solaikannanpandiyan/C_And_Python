# Python Practical Projects

In this assignment, you will work on three practical Python projects using built-in libraries. Each project is a real-world scenario that demonstrates how Python can automate common tasks. Use the provided starter code to help you get started, and feel free to expand and modify the solutions.

---

## Problem 1: Automatic File Organizer

### Scenario:

You often download files into a single folder and later need to manually sort them by type (e.g., images, documents, videos). Automate this process!

### Task:

Create a script that:

- Scans a designated "Downloads" folder.
- Detects each file’s type (by extension).
- Moves the files into corresponding subfolders (e.g., `Images/`, `Documents/`, `Videos/`).

### Modules to Explore:

- `os` for navigating directories.
- `shutil` for moving files.

### Hints:

- Use `os.listdir()` or `os.walk()` to iterate over files.
- Create destination directories if they don’t exist using `os.makedirs()`.
- Use `shutil.move()` to transfer files.

### Starter Code:

```python
import os
import shutil

# Change this to the path of your Downloads folder
downloads_folder = '/path/to/Downloads'

# Map file extensions to their corresponding destination subfolder
file_types = {
    'jpg': 'Images',
    'jpeg': 'Images',
    'png': 'Images',
    'gif': 'Images',
    'pdf': 'Documents',
    'doc': 'Documents',
    'docx': 'Documents',
    'txt': 'Documents',
    'mp4': 'Videos',
    'mkv': 'Videos',
    'avi': 'Videos'
}

def organize_files(folder):
    for item in os.listdir(folder):
        source = os.path.join(folder, item)
        if os.path.isfile(source):
            ext = item.split('.')[-1].lower()  # Get the file extension
            dest_folder = file_types.get(ext)
            if dest_folder:
                dest_path = os.path.join(folder, dest_folder)
                os.makedirs(dest_path, exist_ok=True)  # Create subfolder if not exists
                shutil.move(source, os.path.join(dest_path, item))
                print(f"Moved {item} to {dest_folder}/")
            else:
                print(f"No mapping found for file: {item}")

if __name__ == "__main__":
    organize_files(downloads_folder)
```

---

## Problem 2: CSV to JSON Data Converter

### Scenario:

You receive data in CSV format (perhaps exported from a spreadsheet) but need it in JSON format for a web application.

### Task:

Write a program that:

- Reads data from a CSV file.
- Converts the data into JSON format.
- Saves the JSON output to a new file.

### Modules to Explore:

- `csv` for reading CSV files.
- `json` for converting Python objects into JSON strings.

### Hints:

- Use `csv.DictReader` to read rows into dictionaries.
- Write the resulting list of dictionaries to a file using `json.dump()`.

### Starter Code:

```python
import csv
import json

# Change these file paths accordingly
csv_file_path = 'data.csv'
json_file_path = 'data.json'

def csv_to_json(csv_path, json_path):
    data = []
    with open(csv_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    with open(json_path, mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)
    print(f"Converted {csv_path} to {json_path}")

if __name__ == "__main__":
    csv_to_json(csv_file_path, json_file_path)
```
## Sample CSV
```
id,name,age,city
1,John Doe,28,New York
2,Jane Smith,32,Los Angeles
3,Bob Johnson,45,Chicago
4,Alice Williams,29,San Francisco
```

---

## Problem 3: Log File Analyzer for Error Detection

### Scenario:

You have an application log file that contains a mix of informational messages and errors. You need to quickly extract error messages to troubleshoot issues.

### Task:

Develop a script that:

- Opens a log file and reads its content.
- Filters out and displays lines that contain the word “ERROR” (or any designated keyword).
- Optionally, counts how many error messages were found.

### Modules to Explore:

- Built-in file I/O (`open()`, `.read()`, etc.).
- `re` (regular expressions) for more flexible text matching.

### Hints:

- Loop through each line of the file.
- Use string methods (like `.find()` or the `in` operator) or regular expressions to detect errors.
- Keep a counter to summarize the total errors found.

### Starter Code:

```python
import re

# Change this to the path of your log file
log_file_path = 'application.log'
error_keyword = 'ERROR'

def analyze_log(file_path):
    error_count = 0
    with open(file_path, mode='r', encoding='utf-8') as logfile:
        for line in logfile:
            # You can use regex for more complex matching: if re.search(r'ERROR', line):
            if error_keyword in line:
                print(line.strip())
                error_count += 1
    print(f"\nTotal error messages found: {error_count}")

if __name__ == "__main__":
    analyze_log(log_file_path)
```

## Sample Log File
```
2025-01-01 10:00:00,000 - INFO - Starting application
2025-01-01 10:01:00,123 - DEBUG - Loading configuration file
2025-01-01 10:02:10,456 - ERROR - Failed to load configuration: File not found
2025-01-01 10:03:15,789 - INFO - Retrying configuration load
2025-01-01 10:04:20,012 - ERROR - Configuration still missing, aborting
2025-01-01 10:05:25,345 - INFO - Application terminated

```

---

