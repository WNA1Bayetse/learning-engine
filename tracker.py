# Import Json
import json
import os

filename = 'study_tracker.json'

# 1. LOAD: Check if file exist and read from the file
if os.path.exists(filename):
    with open(filename, 'r') as f:
        sessions = json.load(f) # Get the old data
else:
    sessions = [] # If the file does not exist get a new one


# 2. UPDATE: Add the new session.
new_entry = {
    "subjects": "AI Engineering Fundamentals",
    "duration_minutes": 60,
    "date": "2025-12-28",
}
sessions.append(new_entry)

# 3. SAVE: Write everything back to the disk.
with open("study_log.json", 'w') as f:
    json.dump(new_entry, f, indent=4)
    

print(f"Total sessions logged {len(sessions)}")

