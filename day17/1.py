def parse():
    # to do parse the input
    print('123')

#in = parse()
registers = [22817223,0,0]
instruction_set = [2,4,1,2,7,5,4,5,0,3,1,7,5,5,3,0]
pointer = 0
toappend = []
while pointer < len(instruction_set):
    
    instruction = instruction_set[pointer]
    val = instruction_set[pointer+1]
    flag = False

    match val:
        case 0:
            operand = 0
        case 1:
            operand = 1
        case 2:
            operand = 2
        case 3:
            operand = 3
        case 4:
            operand = registers[0]
        case 5:
            operand = registers[1]
        case 6:
            operand = registers[2]
        case _:
            print('None')
    
    if instruction == 0:
        registers[0] = registers[0] / ( 2 ** operand )
    elif instruction == 1:
        registers[0] = registers[0] ^ operand
    elif instruction == 2:
        registers[1] = registers[1] % 8
    elif instruction == 3:
        if registers[0] != 0:
            flag = True
    elif instruction == 4:
        registers[1] = registers[1] ^ registers[2]
    elif instruction == 5:
        toappend.append(operand % 8)
    elif instruction == 6:
       registers[1] = registers[0] / ( 2 ** operand )
    elif instruction == 7:
       registers[2] = registers[0] / ( 2 ** operand )

    if flag == False:
    
        pointer+=2

    else:

        pointer = operand 


print(','.join(toappend))
