class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n2=sorted(nums)[-k:]
        while sorted(nums)!=n2:
            nums.remove(min(nums))
        return nums