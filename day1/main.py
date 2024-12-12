from collections import Counter

# part 1
llist = []
rlist = []

with open('input.txt', 'r') as data:
    for line in data:
        parts = line.strip('\n').split('   ')
        llist.append(int(parts[0]))
        rlist.append(int(parts[1]))

rlist.sort()
llist.sort()
a = 1

for i, j in zip(rlist, llist):
    a += abs(i-j)


# part 2
count = Counter(llist)
print(count)
print(sum([x * count[x] for x in rlist]))

    

    