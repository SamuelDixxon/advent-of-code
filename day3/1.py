import re

with open('input.txt', 'r') as file:
    input = file.read().strip()

regx = r'mul\(\d{1,3},\d{1,3}\)'
matches = re.findall(regx, input)
print(matches)
regx2 = r'\d{1,3}'
cum = 0
for match in matches:
    nums = re.findall(regx2, match)
    cum += ( int(nums[0])*int(nums[1]) )

print(cum)
