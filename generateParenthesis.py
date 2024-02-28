class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return ["()"]
        currentLevel = []
        returnArray = []
        OpenBracketDB = dict()
        CloseBracketDB = dict()

        OpenBracketDB["("] = n - 1
        CloseBracketDB["("] = n
        targetString = "("

        currentLevel.append("(")

        for i in range(len(currentLevel)):
            if OpenBracketDB[targetString]> 0:#length 2
                eachString = targetString + "("
                returnArray.append(eachString)
                OpenBracketDB[eachString] = OpenBracketDB[targetString] - 1
                CloseBracketDB[eachString] = CloseBracketDB[targetString]
            if CloseBracketDB[targetString] > 0 and OpenBracketDB[targetString] < CloseBracketDB[targetString]:
                eachString = targetString + ")"
                returnArray.append(eachString)
                OpenBracketDB[eachString] = OpenBracketDB[targetString]
                CloseBracketDB[eachString] = CloseBracketDB[targetString] - 1

        
        for strLen in range((2*n) - 2):
            currentLevel = returnArray
            returnArray = []
            for i in range(len(currentLevel)):
                targetString = currentLevel[i]
                if OpenBracketDB[targetString]> 0:#length 2
                    eachString = targetString + "("
                    returnArray.append(eachString)
                    OpenBracketDB[eachString] = OpenBracketDB[targetString] - 1
                    CloseBracketDB[eachString] = CloseBracketDB[targetString]
                if CloseBracketDB[targetString] > 0 and OpenBracketDB[targetString] < CloseBracketDB[targetString]:
                    eachString = targetString + ")"
                    returnArray.append(eachString)
                    OpenBracketDB[eachString] = OpenBracketDB[targetString]
                    CloseBracketDB[eachString] = CloseBracketDB[targetString] - 1

     
        
       

   
        
       
        
     
    


        

        



        
        return returnArray

            


             # for increasingStrLen in range((2 * n) - 2):
        #     currentLevel = returnArray
        #     returnArray = []
        #     for i in range(len(currentLevel)):
        #         targetString = currentLevel[i]
        #         if OpenBracketDB[targetString]> 0:#length 2
        #             eachString = targetString + "("
        #             returnArray.append(eachString)
        #             OpenBracketDB[eachString] = OpenBracketDB[targetString] - 1
        #             CloseBracketDB[eachString] = n
        #         if CloseBracketDB[targetString] > 0 and OpenBracketDB[targetString] < CloseBracketDB[targetString]:
        #             eachString = targetString + ")"
        #             returnArray.append(eachString)
        #             OpenBracketDB[eachString] = OpenBracketDB[targetString]
        #             CloseBracketDB[eachString] = CloseBracketDB[targetString] - 1

        

        

        
