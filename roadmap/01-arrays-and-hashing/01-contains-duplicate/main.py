"""
https://leetcode.com/problems/contains-duplicate/description/

"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        exists = set()
        for num in nums:
            if num in exists:
                return True
            exists.add(num)
        return False

if __name__ == "__main__":
    cases = {
        'case-1': {
            'case': [1, 2, 3, 1],
            'result': True
        },
        'case-2': {
            'case': [1, 2, 3, 4],
            'result': False
        },
        'case-3': {
            'case': [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
            'result': True
        }
    }

    solution = Solution()
    for name, case in cases.items():
        result = solution.containsDuplicate(case["case"])
        print(f"{name} -> {"Passed" if result == case["result"] else "Failed"}")

