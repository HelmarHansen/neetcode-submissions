class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictionarys = {}
        dictionaryt = {}
        for i in s:
            dictionarys[i] = dictionarys.get(i, 0) + 1
        for i in t:
            dictionaryt[i] = dictionaryt.get(i, 0) + 1
        return dictionarys == dictionaryt