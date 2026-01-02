import json
import os

filename = "study_log.json"

# --- DATA VALIDATION LOGIC ---
print("--- Study Session Logger ---")
subject = input("What did you study? ")

# We use a 'while' loop to keep asking until the user gives a valid number
while True:
    try:
        duration = int(input("For how many minutes? "))
        break # Success! Exit the loop
    except ValueError:
        print("❌ Error: Please enter a whole number (e.g., 60).")

date = input("Date (YYYY-MM-DD): ")

# --- STORAGE LOGIC ---
new_entry = {
    "subject": subject,
    "duration_minutes": duration,
    "date": date
}

# (Existing persistence logic from earlier goes here...)
if os.path.exists(filename):
    with open(filename, "r") as f:
        try:
            sessions = json.load(f)
            # QA CHECK: Ensure 'sessions' is actually a list
            if not isinstance(sessions, list):
                sessions = [sessions] # Force it into a list if it's just one dict
        except json.JSONDecodeError:
            sessions = [sessions] # Handle empty or broken files
else:
    sessions = []

# Now .append() will always work because sessions is guaranteed to be a list

sessions.append(new_entry)

with open(filename, "w") as f:
    json.dump(sessions, f, indent=4)

print(f"✅ Session saved! Total entries: {len(sessions)}")