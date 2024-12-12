import re

with open('input.txt', 'r') as file:
    input = file.read().strip()

regx = r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'
matches = re.findall(regx, input)
# regx2 = r'\d{1,3}'
cum = 0
res = 0
enabled = True
for match in matches:
    if match == "do()":
        enabled = True
    elif match == "don't()":
        enabled = False
    else:
        if enabled:
            args = match.replace(")", "").split("(")[1]
            x, y = args.split(",")
            res += int(x) * int(y)
print(res)
