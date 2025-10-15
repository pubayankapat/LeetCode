class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorEle = -1
        votes = 0

        for i in nums:
            if votes == 0:
                majorEle = i
                votes = 1
            else:
                if majorEle == i:
                    votes += 1
                else:
                    votes -=1
        return majorEle
                
