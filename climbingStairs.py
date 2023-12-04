class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        elif n == 4:
            return 5
        else:
            n_Minus_1 = 5
            n_Minus_2 = 3
            returnCounter = 0
            for x in range(4,n):
                returnCounter =  n_Minus_1 + n_Minus_2
                print(returnCounter)
                n_Minus_2 = n_Minus_1
                n_Minus_1 = returnCounter

            return returnCounter
        
