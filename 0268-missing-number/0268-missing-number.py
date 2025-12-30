class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        x1 = 0
        x2 = 0
        for i in range(0, n):
            x1 = x1 ^ nums[i]

        for j in range(0, n+1):
            x2 = x2 ^ j 

        return (x1^x2)
        