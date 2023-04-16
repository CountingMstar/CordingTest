from typing import List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        init = Node(None)
        self.head = init
        self.tail = init
        self.number_of_data = 0

    def append(self, data):
        new_node = Node(data)
        # 원래 마지막노드(tail)의 next노드를 새로운노드로 입력
        self.tail.next = new_node
        # 새로운 노드가 이제 제일 마지막 노드이므로 tail노드로 교체
        self.tail = new_node
        self.number_of_data += 1

I = LinkedList()
input = [10, 20, 30]

for i in input:
    I.append(i)

print(I.head.data)
print(I.head.next.data)
print(I.head.next.next.data)