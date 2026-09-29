class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            o = -(i + 1)
            ex = s[i]
            print(i, o, ex)
            s[i] = s[o]
            s[o] = ex
            print(s)