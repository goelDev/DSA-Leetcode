class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def rec(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if word1[i] == word2[j]:
                res = rec(i + 1, j + 1)
            else:
                res = 1 + min(     
                    rec(i + 1, j),  
                    rec(i, j + 1)  
                )
            return res
        return rec(0, 0)