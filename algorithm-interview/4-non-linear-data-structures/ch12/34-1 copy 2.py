def dfs(nums, elements, results):

    if len(nums) == 0:
        results.append(elements[:])

    for i in nums:
        tmp = nums[:]
        elements.append(i)
        tmp.remove(i)

        dfs(tmp, elements, results)

        elements.pop()

    return results


nums = [1, 2, 3]
elements = []
results = []

answer = dfs(nums, elements, results)
print(answer)