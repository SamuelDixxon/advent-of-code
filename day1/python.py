llist = []
rlist = []

with open('input.txt', 'r') as data:
    for line in data:
        parts = line.strip('\n').split('   ')
        llist.append(int(parts[0]))
        rlist.append(int(parts[1]))

rlist.sort()
llist.sort()
sum = 0

for i, j in zip(rlist, llist):
    sum += abs(i-j)
    
print(sum)
    