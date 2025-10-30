class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c=0
        s=sorted(s)
        t=sorted(t)
        if t==s:
            return True            
        else :
            return False
                 