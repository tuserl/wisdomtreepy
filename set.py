import pickle
from pathlib import Path

# Define the file path
treedata_path = Path("res/treedata")

# Step 1: Load and print current age
try:
    with open(treedata_path, "rb") as f:
        current_age = pickle.load(f)
    print(f"🌳 Current tree age: {current_age}")
except FileNotFoundError:
    current_age = None
    print("🌱 No age data found. Setting new age...")
except Exception as e:
    print(f"❌ Error reading age: {e}")
    exit(1)

# Step 2: Ask user for new age
try:
    new_age = int(input("✏️  Enter new tree age: "))

    with open(treedata_path, "wb") as f:
        pickle.dump(new_age, f)

    print(f"✅ New tree age saved: {new_age}")

except ValueError:
    print("❌ Invalid input. Please enter a number.")

