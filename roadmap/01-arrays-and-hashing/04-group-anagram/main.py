"""
https://leetcode.com/problems/group-anagrams/

"""
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                count[index] += 1
            res[tuple(count)].append(s)
        return list(res.values())

if __name__ == "__main__":
    cases = {
        'case-1': {
            'input': ["eat","tea","tan","ate","nat","bat"],
            'result': [["bat"],["nat","tan"],["ate","eat","tea"]]
        },
         'case-2': {
            'input': [""],
            'result': [[""]]
        },
        'case-3': {
            'input': ["a"],
            'result': [["a"]]
        },
    }

    solution = Solution()
    for name, case in cases.items():
        result = solution.groupAnagrams(case["input"])
        print(sorted(result))
        print(sorted(case["result"]))
        print(f"{name} -> {"Passed" if sorted(result) == sorted(case["result"]) else "Failed"}")

