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
input = [1, 2]

for i in input:
    I.append(i)

print(I.head.data)
print(I.head.next.data)
print(I.head.next.next.data)


#########################################
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q: List = []

        if not head:
            return True

        node = head
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # 팰린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True
