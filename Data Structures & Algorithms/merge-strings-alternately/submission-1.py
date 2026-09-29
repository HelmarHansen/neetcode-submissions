class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1, w2 = 0, 0
        res = ""
        while w1 < len(word1):
            if w2 == len(word2):
                res += word1[w1:]
                return res
            res += word1[w1]
            res += word2[w2]
            w1 += 1
            w2 += 1
        
        if w2 < len(word2):
            res += word2[w2:]
        return res