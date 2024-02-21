class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
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

        



