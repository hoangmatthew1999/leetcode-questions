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
            OpenBracketDB[eachString] = n-1
            CloseBracketDB[eachString] = n
        if CloseBracketNum > 0 and currentLevel[0] == "(":
            eachString = currentLevel[0] + ")"
            returnArray.append(eachString)
            OpenBracketDB[eachString] = n
            CloseBracketDB[eachString] = n-1
        currentLevel.pop(0)

        targetString = currentLevel[0]
        if OpenBracketDB[targetString] > 0:
            eachString = targetString + "("
            returnArray.append(eachString)
            OpenBracketDB[eachString] = OpenBracketDB[targetString] + 1
            CloseBracketDB[eachString] = n
        

        print(OpenBracketDB,"seperator", CloseBracketDB)
        return returnArray

        



