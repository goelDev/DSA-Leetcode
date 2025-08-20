class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        x=word.find(ch)
        if x>=0:
            reversepart = word[0:x+1]
            orginalpart = word[x+1:len(word)]
            reversepart = reversepart [::-1]
            return reversepart+orginalpart
        else:
            return word