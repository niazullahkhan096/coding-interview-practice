"""
https://leetcode.com/problems/encode-and-decode-strings/

"""
from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res

if __name__ == "__main__":
    cases = {
        'case-1': ["neet","code","love","you"],
        'case-2': ["we","say",":","yes"],
        'case-3': ["2we","3#say",":","3yes"]
    }

    solution = Solution()
    for name, case in cases.items():
        encoded = solution.encode(case)
        decoded = solution.decode(encoded)
        print(f"{name} -> {"Passed" if case == decoded else "Failed"}")

