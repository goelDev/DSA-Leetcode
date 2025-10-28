class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash=set()
        result=False
        for item in nums:
            hash.add(item)
        if len(hash)==len(nums):
            result=False
        else:
            result=True
        return result