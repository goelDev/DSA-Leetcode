class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        y=0
        for x in s:
            y+=abs(s.index(x)-t.index(x))
        return y