def isPalindrome( x):
        if(x < 0):
            return False
        elif(x > 0 and x < 10):
            return True
        else:
            smaller = 10
            digits = []
            digits.append(x % 10)
            while(x >= smaller ):
                digit = x // smaller
                pushing = digit % 10
                digits.append(pushing)
                smaller = smaller * 10
            print(digits)
            i = 0
            j = len(digits) - 1
            for i in range(len(digits)):
                print(digits[i],digits[j],"printing")
                if(digits[i] == digits[j] ):
                    print("in if")
                    i = i + 1
                    j = j - 1
                else:
                    print("in else")
                    return False
                    break 
print( isPalindrome(10)  )
