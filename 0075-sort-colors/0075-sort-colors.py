class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # variable for counting the no of each ball present in the array
        count0 = 0
        count1 = 0 
        count2 = 0

        # Cont the ball

        for i in range(len(nums)):
            if nums[i] == 0:
                count0 += 1
            elif nums[i] == 1:
                count1 += 1
            else:
                count2 +=1
        # inserting each different ball at different place consecutively
        for i in range(count0):
            nums[i] = 0

        for i in range(count0,count0+count1):
            nums[i] = 1
        
        for i in range(count0+count1, len(nums)):
            nums[i] = 2
        


        