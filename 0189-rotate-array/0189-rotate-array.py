class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        g = math.gcd(n, k)

        for i in range(g):
            temp = nums[i]
            j = i 
            while True:
                #For right rotation
                d = (j - k) % n   #for left ratation we have add j & k
                if d == i:
                    break
                nums[j] = nums[d]
                j = d
            nums[j] = temp
        