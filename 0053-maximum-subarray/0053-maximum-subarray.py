class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # tracking the sum
        currentSum = nums[0]
        overallSum = nums[0]

        # iterate over the array 
        for i in range(1, len(nums)):
            if currentSum + nums[i] > nums[i]:
                currentSum = currentSum + nums[i]
            else:
                currentSum = nums[i]
            overallSum = max( overallSum, currentSum )
        return overallSum
            
