class Solution:

    def permute(nums):
        results = []
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0:
                results.append(prev_elements[:])
                print('11111111')
                print(prev_elements[:])
                print(elements)
                print(results)

            for e in elements:
                print('2222222')
                print(elements)
                next_elements = elements[:]
                print(next_elements)
                next_elements.remove(e)
                print(next_elements)

                print('3333333')
                prev_elements.append(e)
                print(prev_elements)
                dfs(next_elements)
                prev_elements.pop()
                print('8888888')
                print(prev_elements)

                print('4444444')
                print(elements)
                print('5555555')

        dfs(nums)
        return results


nums = [1, 2, 3]
answer = Solution.permute(nums)
print(answer)
