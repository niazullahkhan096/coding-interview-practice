"""
https://leetcode.com/problems/top-k-frequent-elements

"""
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        n = len(nums)
        for i in range(n):
            num = nums[i]
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for (freq, num) in heap]

if __name__ == "__main__":
    cases = {
        'case-1': {
            'input': {
                'nums': [1,1,1,2,2,3],
                'k': 2
            },
            'result': [1,2]
        },
        'case-2': {
            'input': {
                'nums': [1],
                'k': 1
            },
            'result': [1]
        },
        'case-3': {
            'input': {
                'nums': [1,2,1,2,1,2,3,1,3,2],
                'k': 2
            },
            'result': [1, 2]
        }
    }

    solution = Solution()
    for name, case in cases.items():
        result = solution.topKFrequent(case["input"]['nums'], case["input"]['k'])
        print(sorted(result))
        print(sorted(case["result"]))
        print(f"{name} -> {"Passed" if sorted(result) == sorted(case["result"]) else "Failed"}")

