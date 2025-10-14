class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storeNum = {}

        for i , num in enumerate(nums):
            complement = target - num

            if complement in storeNum:
                return [storeNum[complement], i ]
            
            storeNum[num] = i
            
        