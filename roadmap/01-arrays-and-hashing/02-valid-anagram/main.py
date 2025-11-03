"""
https://leetcode.com/problems/valid-anagram/description/

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        return count_s == count_t

if __name__ == "__main__":
    cases = {
        'case-1': {
            'case': {
                's1': "anagram",
                's2': "nagaram"
            },
            'result': True
        },
        'case-2': {
            'case': {
                's1': "rat",
                's2': "car"
            },
            'result': False
        },
        'case-3': {
            'case': {
                's1': "listen",
                's2': "silent"
            },
            'result': True
        }
    }

    solution = Solution()
    for name, case in cases.items():
        result = solution.isAnagram(case["case"]["s1"], case["case"]["s2"])
        print(f"{name} -> {"Passed" if result == case["result"] else "Failed"}")

