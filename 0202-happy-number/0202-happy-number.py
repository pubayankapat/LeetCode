class Solution:
    # driver function
    def isHappy(self, n: int) -> bool:
        # helper function
        def next_num(n):
            total = 0
            while n > 0:
                digit = n % 10
                total += digit ** 2
                n //= 10
            return total
        slow = n
        fast = next_num(n)

        while fast != 1 and slow != fast :
            slow = next_num(slow)
            fast = next_num(next_num(fast))
        
        return fast == 1
        
        

    