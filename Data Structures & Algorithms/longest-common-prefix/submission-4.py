class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        for i in range(min(len(string) for string in strs)):
            current = strs[0][i]
            print("current:", current)
            for string in strs:
                if string[i] != current:
                    return pre
            pre += current
        return pre