"""
https://leetcode.com/problems/two-sum/description/

"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            if nums[i] in m:
                return [m[nums[i]], i]
            d = target - nums[i]
            m[d] = i
        return []

if __name__ == "__main__":
    cases = {
         'case-1': {
            'case': {
                'nums': [2,7,11,15],
                'target': 9
            },
            'result': [0,1]
        },
        'case-2': {
            'case': {
                'nums': [3,2,4],
                'target': 6
            },
            'result': [1,2]
        },
        'case-3': {
            'case': {
                'nums': [3,3],
                'target': 6
            },
            'result': [0,1]
        },
        'case-4': {
            'case': {
                'nums': [1,7,3,3,5,10,8],
                'target': 9
            },
            'result': [0,6]
        }
    }

    solution = Solution()
    for name, case in cases.items():
        result = solution.twoSum(case["case"]["nums"], case["case"]["target"])
        print(f"{name} -> {"Passed" if result == case["result"] else "Failed"}")

