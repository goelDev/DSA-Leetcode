class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = sorted(nums)
        low=0
        high=len(a)-1
        mid = (low+high)//2
        return a[mid]
        