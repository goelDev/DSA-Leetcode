class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max=0
        count=0
        for str in sentences:
            count=len(str.split(" "))
            if count > max:
                max=count
        return max 