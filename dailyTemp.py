class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        returnArray = [0] * len(temperatures)
        valuesVisitedStack = []
        indexVisitedStack = []

        i = 0
        valuesVisitedStack.append(i)
        indexVisitedStack.append(temperatures[i])

        for loopingArray in range(len(temperatures) - 1):
            i = i + 1
            valuesVisitedStack.append(i)
            indexVisitedStack.append(temperatures[i])
            top = len(valuesVisitedStack)-1
            while indexVisitedStack[top-1] < indexVisitedStack[top]:
                diff = valuesVisitedStack[top] - valuesVisitedStack[top-1]
                returnArray[valuesVisitedStack[top-1]] = diff
                valuesVisitedStack.pop(top-1)
                indexVisitedStack.pop(top-1)
                top = len(valuesVisitedStack)-1
        
        if i == len(temperatures) -1:
            returnArray[len(temperatures)-1] = 0
        

        return returnArray
