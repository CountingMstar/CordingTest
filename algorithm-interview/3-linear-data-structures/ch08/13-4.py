import time

"""
Linked list(연결리스트) 만들기
"""
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
input = [1, 2, 3, 3, 2, 1]

for i in input:
    I.append(i)

print(I.head.data)
print(I.head.next.data)
print(I.head.next.next.data)
print(I.tail.data)

"""
팰린드롬 인지 판별
"""
start = time.time()
def isPalindrome(head):
    rev = None
    slow = fast = head.next

    # 런너를 이용해 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next

    # 팰린드롬 여부 확인
    while rev and rev.data == slow.data:
        slow, rev = slow.next, rev.next

    return not rev

result = isPalindrome(I.head)
end = time.time()
print(result)
print(f"{end - start:.20f} sec")

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev
