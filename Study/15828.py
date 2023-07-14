import sys
N = int(sys.stdin.readline())

stack_list = []
while True:
    temp = int(sys.stdin.readline())
    if temp == -1: break
    elif temp == 0: stack_list.pop(0)
    elif len(stack_list)>=N: pass
    else: stack_list.append(str(temp))
    

if len(stack_list)==0: print("empty")
else : print(' '.join(stack_list))


#############################################

import sys

size = int(sys.stdin.readline())
packets = []
while True:
    packet = int(sys.stdin.readline()
    packets.append(packet)
    if packet == -1:
        break
packets.pop()

buffer = []
for i in packets:
    if len(buffer) < size:
        if i != 0:
            buffer.append(i)
    if i == 0:
        buffer.pop(0)

if len(buffer) > 0:
    print(' '.join(map(str, buffer)))
if len(buffer) == 0:
    print('empty')