import pickle

with open("res/treedata", "rb") as f:
    age = pickle.load(f)

print(f"Tree age: {age}")

