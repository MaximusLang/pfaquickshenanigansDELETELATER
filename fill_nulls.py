import json, re

FILE = "pfa_scoring_skeleton(1).json"

with open(FILE) as f:
    raw = f.read()

values = input("Paste numbers: ").split()

count = 0
def replacer(m):
    global count
    if count < len(values):
        v = values[count]; count += 1
        return f': {float(v) if "." in v else int(v)}'
    return m.group(0)

raw = re.sub(r': null', replacer, raw, count=len(values))

with open(FILE, "w") as f:
    f.write(raw)

print(f"Replaced {count} nulls.")
