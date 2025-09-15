class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_kadane = float('-inf')
        min_kadane = float('inf')
        total_sum = 0
        max_curr = min_curr = 0

        for num in nums:
            max_curr = max(num , max_curr + num)
            max_kadane = max(max_kadane , max_curr)

            min_curr = min(num ,  min_curr + num)
            min_kadane = min(min_kadane , min_curr)

            total_sum +=num

        return max_kadane if max_kadane<0 else max(max_kadane , total_sum - min_kadane)       