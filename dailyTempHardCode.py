class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        valuesVisitedArray = []
        returnArray = []
        offset = 0
        counter = 0
        i = len(temperatures)-1
        e = temperatures[i]

        if i == len(temperatures)-1:# first elem 73
            valuesVisitedArray.insert(0,temperatures[len(temperatures)-1])
            returnArray.insert(0,0)
        
        i = i - 1
        e = temperatures[i]
        counter = 0

        j = 0
        if e < valuesVisitedArray[0]:#second elem 76
            returnArray.insert(0,1)
            valuesVisitedArray.insert(0,e)
        else:
            counter = counter + 1
        if len(temperatures) - i > len(valuesVisitedArray):# if you have not added the value already
            valuesVisitedArray.insert(0,e)
            returnArray.insert(0,0)

        i = i - 1
        e = temperatures[i]
        counter = 0
        if e < valuesVisitedArray[0]:# third elem 72
            returnArray.insert(0,1)
            valuesVisitedArray.insert(0,e)
        else:
            if e < valuesVisitedArray[j]:
                returnArray.insert(0,counter)
                valuesVisitedArray.insert(0,e)
            else:
                j = j + 1
                counter = counter + 1
        
        i = i - 1
        e = temperatures[i]
        counter = 0
        if e < valuesVisitedArray[0]:# fourth elem 69
            returnArray.insert(0,1)
            valuesVisitedArray.insert(0,e)
        else:
            if e < valuesVisitedArray[j]:
                returnArray.insert(0,counter)
                valuesVisitedArray.insert(0,e)
            else:
                j = j + 1
                counter = counter + 1
        
        i = i - 1
        e = temperatures[i]
        counter = 1
        for elems in range(len(valuesVisitedArray) ):
            print(" ")
        if e < valuesVisitedArray[0]:# elem 71
            returnArray.insert(0,1)
            valuesVisitedArray.insert(0,e)
        else:
            if e < valuesVisitedArray[j]:
                returnArray.insert(0,counter)
                valuesVisitedArray.insert(0,e)
            else:
                j = j + 1
                counter = counter + 1
        if e < valuesVisitedArray[0]:# elem 71
            returnArray.insert(0,1)
            valuesVisitedArray.insert(0,e)
        else:
            if e < valuesVisitedArray[j]:
                returnArray.insert(0,counter)
                valuesVisitedArray.insert(0,e)
            else:
                j = j + 1
                counter = counter + 1
        
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
       


        i = i - 1
        counter = 1
        j = 0

        print(valuesVisitedArray, returnArray)
        return returnArray


        # if i == len(temperatures)-1:
        #     valuesVisitedArray.insert(0,temperatures[len(temperatures)-1])
        #     returnArray.insert(0,0)
        # else:
        #     j = 0
        #     if e < valuesVisitedArray[j]:
        #         print(e,valuesVisitedArray[j])
        #     else:
        #         counter = counter + 1
        #         print(counter)
        #     if len(temperatures) - i > len(valuesVisitedArray):# if you have not added the value already
        #         valuesVisitedArray.insert(0,e)
        #         returnArray.insert(0,0)

        # if i == len(temperatures)-1:
        #     valuesVisitedArray.insert(0,temperatures[len(temperatures)-1])
        #     returnArray.insert(0,0)
        
            





        
