llist = []
count = 0
flag = False

with open('input.txt', 'r') as data:
    lines = data.readlines()
    for line in lines:
        data = line.strip('\n').split(' ')
        int_data = [int(i) for i in data]
        flag = False
        neg = False
        pos = False
        for i in range(1, len(int_data)):
            if 3 < abs(int_data[i-1] - int_data[i]) or abs(int_data[i-1] - int_data[i]) == 0:
                flag = True
            if (int_data[i-1] - int_data[i]) < 0:
                neg = True
            else:
                pos = True
            if neg and pos:
                flag = True
                
        if flag == False:
            count+=1

print(count)


        