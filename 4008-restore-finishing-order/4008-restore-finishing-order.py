class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        final=[]
        friends=set(friends)
        for p in order:
            if p in friends:
                final.append(p)
        return final