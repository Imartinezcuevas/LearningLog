import os
from datetime import datetime

# Get date
today = datetime.today()
year = today.strftime("%Y")
month = today.strftime("%B")
day = today.strftime("%d")
day_of_week = today.strftime("%A")

# Define the entry
month_folder = os.path.join(year, month)
entry_path = os.path.join(month_folder, f"{day}.txt")

# Create month folder if it doesn't exist
os.makedirs(month_folder, exist_ok=True)

# Create entry file if it doesn't exist
if not os.path.exists(entry_path):
    with open(entry_path, "w") as file:
        file.write(f"Date: {day_of_week}, {month} {day}, {year}\n\n")
        file.write("What I learned today:\n\n")

    print(f"Entry created: {entry_path}")
else:
    print(f"Entry already exists: {entry_path}")