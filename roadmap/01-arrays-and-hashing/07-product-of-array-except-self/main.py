"""
https://leetcode.com/problems/product-of-array-except-self/

"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        print(pref)
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        print(suff)
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res


if __name__ == "__main__":
    cases = {
        'case-1': {
            'input': {
                'nums': [1,2,3,4]
            },
            'output': [24,12,8,6]
        },
        'case-2': {
            'input': {
                'nums': [-1,1,0,-3,3]
            },
            'output': [0,0,9,0,0]
        }
    }

    solution = Solution()
    for name, case in cases.items():
        result = solution.productExceptSelf(case["input"]['nums'])
        print(f"{name} -> {"Passed" if sorted(result) == sorted(case["output"]) else "Failed"}")

