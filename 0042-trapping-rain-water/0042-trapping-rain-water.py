class Solution:
    # similar to container with most water
    def trap(self, height: List[int]) -> int:
        waterTrapped = 0
        left = 0
        right = len(height)-1
        leftMax = 0
        rightMax = 0
        while(left < right):
            if(height[left] < height[right]):
                if(height[left]>= leftMax):
                    leftMax = height[left]
                else:
                    waterTrapped += leftMax - height[left]
                left+=1
            else:
                if(height[right]>=rightMax):
                    rightMax = height[right]
                else:
                    waterTrapped += rightMax - height[right]
                right-=1
        
        return waterTrapped
            
 