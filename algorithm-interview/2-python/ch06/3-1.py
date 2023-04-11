from typing import List
import time

start = time.time()
text1 = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let2 art zero"]
logs = text1

print('###########')
print(logs[0])
print(logs[0].isdigit())
print(logs[0].split())
print(logs[0].split()[1].isdigit())

end = time.time()
print(f"{end - start:.5f} sec")
# print(log)

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        print('===========')
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        print(letters)
        print(digits)

        # 두 개의 키를 람다 표현식으로 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        # letters.sort(key=func)
        print(letters)
        return letters + digits

Solution().reorderLogFiles(logs)
