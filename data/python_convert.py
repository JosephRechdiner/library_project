import json
PATH = "test"
d = {"israel": "val123", "yossi": "123val"}

with open(PATH, 'a') as f:
    json.dump(d, f, indent = 3)

with open(PATH, 'r') as f:
    data = json.load(f)

print(type(data))
print("done")