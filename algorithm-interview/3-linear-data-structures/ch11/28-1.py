import collections

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    # 초기화
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    # 삽입
    def put(self, key: int, value: int) -> None:
        index = key % self.size

        # 해당 인덱스에 노드가 없으면 삽입 후 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        
        # 해당 인덱스에 노드가 존재하면 연결 리스트 처리
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next

        p.next = ListNode(key, value)


    # 조회
    def get(self, key: int) -> int:
        index = key % self.size

        # 해당 인덱스가 노드가 없으면 -1 반환
        if self.table[index].value is None:
            return -1

        # 인덱스에 노드가 존재하면 일치하는 value값 반환
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    
    # 삭제
    def remove(self, key: int) -> None:
        index = key % self.size

        # 해당 인덱스가 노드가 없으면
        if self.table[index].value is None:
            return

        # 인덱스의 첫 번째 노드일때 삭제 및 초기화
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return
        
        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next



hash_map = MyHashMap()
hash_map.put(1, 1)
hash_map.put(2, 2)
hash_map.put(1, 3)

print(hash_map.get(2))
print(hash_map.get(3))
print(hash_map.get(100))
print(hash_map.get(1200))