class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return  ["()"]

        returnArray = []
        currentLevel = []
        OpenBracketDB = dict()
        CloseBracketDB = dict()

        OpenBracketDB["("] = n-1
        CloseBracketDB["("] = n
        targetString = "("
        if OpenBracketDB[targetString]> 0:#length 2
            eachString = targetString + "("
            returnArray.append(eachString)
            OpenBracketDB[eachString] = OpenBracketDB[targetString] - 1
            CloseBracketDB[eachString] = n
        if CloseBracketDB[targetString] > 0 and targetString[-1] == "(":
            eachString = targetString + ")"
            returnArray.append(eachString)
            OpenBracketDB[eachString] = OpenBracketDB[targetString]
            CloseBracketDB[eachString] = CloseBracketDB[targetString] - 1
        OpenBracketDB.pop(targetString)
        CloseBracketDB.pop(targetString)

        currentLevel = returnArray
        returnArray = []
        targetString = currentLevel[0]#length 3
        if OpenBracketDB[targetString] > 0:
            eachString = targetString + "("
            returnArray.append(eachString)
            OpenBracketDB[eachString] = OpenBracketDB[targetString] - 1
            CloseBracketDB[eachString] = CloseBracketDB[targetString]
        if CloseBracketDB[targetString] > 0 and targetString[-1] == "(":
            eachString = targetString + ")"
            returnArray.append(eachString)
            OpenBracketDB[eachString] = OpenBracketDB[targetString] 
            CloseBracketDB[eachString] = CloseBracketDB[targetString] - 1
        OpenBracketDB.pop(targetString)
        CloseBracketDB.pop(targetString)

        targetString = currentLevel[1]
        if OpenBracketDB[targetString] > 0:
            eachString = targetString + "("
            returnArray.append(eachString)
            OpenBracketDB[eachString] = OpenBracketDB[targetString] - 1
            CloseBracketDB[eachString] = OpenBracketDB[targetString]
        if CloseBracketDB[targetString] > 0 and targetString[-1] == "(":
            eachString = targetString + ")"
            returnArray.append(eachString)
            OpenBracketDB[eachString] = OpenBracketDB[targetString] 
            CloseBracketDB[eachString] = CloseBracketDB[targetString] - 1
        OpenBracketDB.pop(targetString)
        CloseBracketDB.pop(targetString)
        currentLevel = returnArray
        returnArray = []

        targetString = currentLevel[0]#length 4
        if CloseBracketDB[targetString] > 0:#band aided solution possible 
            eachString = targetString + ")"
            returnArray.append(eachString)
            OpenBracketDB[eachString] = OpenBracketDB[targetString] 
            CloseBracketDB[eachString] = CloseBracketDB[targetString] - 1

        targetString = currentLevel[1]
        if CloseBracketDB[targetString] > 0:#band aided solution possible 
            eachString = targetString + ")"
            returnArray.append(eachString)
            OpenBracketDB[eachString] = OpenBracketDB[targetString] 
            CloseBracketDB[eachString] = CloseBracketDB[targetString] - 1

        '''
        possible for ) able to fit with ( being -1 
        ex (()
        '''

        print(OpenBracketDB,"seperator", CloseBracketDB)
        return returnArray

        




            return  ["()"]

        returnArray = []
        OpenBracketNum = n - 1
        CloseBracketNum = n
        returnArray.append("(")

        currentLevel = returnArray
        OpenBracketDB = dict()
        CloseBracketDB = dict()

        if OpenBracketNum > 0:
            eachString = currentLevel[0] + "("
            returnArray.append(eachString)
            OpenBracketDB[eachString] = n-1-1
            CloseBracketDB[eachString] = n
        if CloseBracketNum > 0 and currentLevel[0] == "(":
            eachString = currentLevel[0] + ")"
            returnArray.append(eachString)
            OpenBracketDB[eachString] = n-1
            CloseBracketDB[eachString] = n-1
        currentLevel.pop(0)

        targetString = currentLevel[0]
        if OpenBracketDB[targetString] > 0:
            eachString = targetString + "("
            returnArray.append(eachString)
            OpenBracketDB[eachString] = OpenBracketDB[targetString] - 1
            CloseBracketDB[eachString] = n
        if CloseBracketDB[targetString] > 0:
            eachString = targetString + ")"
            returnArray.append(eachString)
            OpenBracketDB[eachString] = OpenBracketDB[targetString] 
            CloseBracketDB[eachString] = CloseBracketDB[targetString] - 1
        OpenBracketDB.pop(targetString)
        CloseBracketDB.pop(targetString)

        targetString = currentLevel[1]
        if OpenBracketDB[targetString] > 0:
            eachString = targetString + "("
            returnArray.append(eachString)
            OpenBracketDB[eachString] = OpenBracketDB[targetString] - 1
            CloseBracketDB[eachString] = n
        if CloseBracketDB[targetString] > 0 and targetString[-1] == "(":
            eachString = targetString + ")"
            returnArray.append(eachString)
            OpenBracketDB[eachString] = OpenBracketDB[targetString] 
            CloseBracketDB[eachString] = CloseBracketDB[targetString] - 1
        OpenBracketDB.pop(targetString)
        CloseBracketDB.pop(targetString)

        targetString = currentLevel[2]
        if CloseBracketDB[targetString] > 0:
            eachString = targetString + ")"
            returnArray.append(eachString)
            OpenBracketDB[eachString] = OpenBracketDB[targetString] 
            CloseBracketDB[eachString] = CloseBracketDB[targetString] - 1




        
        

        print(OpenBracketDB,"seperator", CloseBracketDB)
        return returnArray

        



