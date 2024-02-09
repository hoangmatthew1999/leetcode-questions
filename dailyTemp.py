class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        valuesVisitedArray = []
        returnArray = []
        offset = 0
        counter = 0
        i = len(temperatures)-1
        e = temperatures[i]
        if i == len(temperatures)-1:# first elem 73
            valuesVisitedArray.insert(0,temperatures[len(temperatures)-1])
            returnArray.insert(0,0)

        for index in range( 1,len(temperatures) ):
            i = i - 1
            e = temperatures[i]
            counter = 1
            j = 0
            if e < valuesVisitedArray[0]:# elem 75
                returnArray.insert(0,1)
                valuesVisitedArray.insert(0,e)
            else:
                for elem in range(len(valuesVisitedArray)):
                    if e < valuesVisitedArray[j]:
                        returnArray.insert(0,counter)
                        valuesVisitedArray.insert(0,e)
                        break
                    else:
                        j = j + 1
                        counter = counter + 1
                if len(temperatures) - i > len(valuesVisitedArray):# if you have not added the value already
                    valuesVisitedArray.insert(0,e)
                    returnArray.insert(0,0)

        return returnArray
