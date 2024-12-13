import re

'''
Idea is to rotate around an arbitrary spot and do 
what I'll coin as a clockwise search up, urdiag, 
right, bldiag, down, brdiag, left, uldiag for
possibilities, ignore spots where there are negative
indices, because we can't wrap and find target from
other sides
'''
 
TARGET = 'XMAS'

with open('sample.txt', 'r') as file:
    lines = file.read().split('\n')

possibilities = []

for i, row in enumerate(lines):

    for j, col in enumerate(row):
        
        # (i, j) reperesents a target to look from in our search
        # need to make sure we have non-negative values in path

        print(f'{i},{j}',end=' ')
        
    print()

        
        

        
                
        
