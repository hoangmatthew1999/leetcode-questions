class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 1:
            return [nums[0]]
        returnArray = []
        returnArrayMax = 0
        returnArrayMin = 0
        freqDB = dict()
        valueToKeyDB = dict()
        returnArrayDB = dict()


        i = 0
        if nums[i] not in freqDB:
            freqDB[nums[i]] = 1
        elif nums[i] in freqDB:
            freqDB[nums[i]] = freqDB[nums[i]] + 1
        if len(returnArray) < k:
            returnArray.append(nums[i])
            valueToKeyDB[1] = [nums[i]]
            returnArrayMin = 1
            returnArrayMax = 1
            returnArrayDB[nums[i]] = 0

        i = 1
        if nums[i] not in freqDB:
            freqDB[nums[i]] = 1
        elif nums[i] in freqDB:
            freqDB[nums[i]] = freqDB[nums[i]] + 1
        if len(returnArray) < k:
            returnArray.append(nums[i])
            valueToKeyDB[1].append(nums[i])
            returnArrayDB[nums[i]] = 1
            if freqDB[nums[i]] > returnArrayMax:
                returnArrayMax = returnArrayDB[nums[i]]
            

        i = 2
        if nums[i] not in freqDB:
            freqDB[nums[i]] = 1
        elif nums[i] in freqDB:
            freqDB[nums[i]] = freqDB[nums[i]] + 1
        if freqDB[nums[i]] > returnArrayMax:
            valueToKeyDB[2] = [nums[i]]
            valueToKeyDB[1].pop()
            returnArrayMax = freqDB[nums[i]]
        #     if nums[i] not in returnArrayDB:
        #         returnArray.append(nums[i])
        #     else:
        #         returnArrayDB[nums[i]] = freqDB[nums[i]]
        #         returnArrayMax = returnArrayDB[nums[i]]

        i = 3
        if nums[i] not in freqDB:
            freqDB[nums[i]] = 1
        elif nums[i] in freqDB:
            freqDB[nums[i]] = freqDB[nums[i]] + 1
        if freqDB[nums[i]] > returnArrayMin:
                removingElem = valueToKeyDB[1]
                returnArray[0] = nums[i]
                returnArrayMin = 2
        
        # valueToKeyDB[1].append(nums[i])

        i = 4
        if nums[i] not in freqDB:
            freqDB[nums[i]] = 1
        elif nums[i] in freqDB:
            freqDB[nums[i]] = freqDB[nums[i]] + 1
        if freqDB[nums[i]] > returnArrayMin: # problem is after how do you know what is the next min 
            valueToRemove = valueToKeyDB[returnArrayMin]
            valueToRemove = valueToRemove[0]
            indexToRemove = returnArrayDB[valueToRemove]
            returnArray[indexToRemove] = nums[i]
            returnArrayDB[nums[i]] = indexToRemove
            returnArrayDB.pop(valueToRemove)
            valueToKeyDB.pop(1)
            valueToKeyDB[2].append(3)
            returnArrayMin = next ( iter(valueToKeyDB) )

        i = 5
        if nums[i] not in freqDB:
            freqDB[nums[i]] = 1
        elif nums[i] in freqDB:
            freqDB[nums[i]] = freqDB[nums[i]] + 1
        if nums[i] in returnArrayDB and freqDB[nums[i]] > returnArrayMin:
            valueToKeyDB[3] = [nums[i]]
        elif freqDB[nums[i]] > returnArrayMin and nums[i] not in returnArrayDB:
            valueToRemove = valueToKeyDB[returnArrayMin]
            valueToRemove = valueToRemove[0]
            indexToRemove = returnArrayDB[valueToRemove]
            returnArray[indexToRemove] = nums[i]
            returnArrayDB[nums[i]] = indexToRemove
            returnArrayDB.pop(valueToRemove)
            valueToKeyDB.pop(1)
            valueToKeyDB[2].append(3)
            returnArrayMin = next ( iter(valueToKeyDB) )
            
        i = 6
        if nums[i] not in freqDB:
            freqDB[nums[i]] = 1
        elif nums[i] in freqDB:
            freqDB[nums[i]] = freqDB[nums[i]] + 1
        if nums[i] in returnArrayDB and freqDB[nums[i]] > returnArrayMin:
            valueToKeyDB[3] = [nums[i]]
        elif freqDB[nums[i]] > returnArrayMin and nums[i] not in returnArrayDB:
            valueToRemove = valueToKeyDB[returnArrayMin]
            valueToRemove = valueToRemove[0]
            indexToRemove = returnArrayDB[valueToRemove]
            returnArray[indexToRemove] = nums[i]
            returnArrayDB[nums[i]] = indexToRemove
            returnArrayDB.pop(valueToRemove)
            valueToKeyDB.pop(1)
            valueToKeyDB[2].append(3)
            returnArrayMin = next ( iter(valueToKeyDB) )
        # if freqDB[nums[i]] > returnArrayMin:
        #     removingElem = valueToKeyDB[1]
        #     returnArray[0] = nums[i]
        #     returnArrayMin = 2
        i = 7
        if nums[i] not in freqDB:
            freqDB[nums[i]] = 1
        elif nums[i] in freqDB:
            freqDB[nums[i]] = freqDB[nums[i]] + 1
        if nums[i] in returnArrayDB and freqDB[nums[i]] > returnArrayMin:
            valueToKeyDB[3] = [nums[i]]
            print("asd")
        elif freqDB[nums[i]] > returnArrayMin and nums[i] not in returnArrayDB:
            print("qwe")
        
        i = 8
        if nums[i] not in freqDB:
            freqDB[nums[i]] = 1
        elif nums[i] in freqDB:
            freqDB[nums[i]] = freqDB[nums[i]] + 1
        if nums[i] in returnArrayDB and freqDB[nums[i]] > returnArrayMin:
            # valueToKeyDB[3] = [nums[i]]
            print("asd")
        elif freqDB[nums[i]] > returnArrayMin and nums[i] not in returnArrayDB:
            print("qwe")

        i = 9
        if nums[i] not in freqDB:
            freqDB[nums[i]] = 1
        elif nums[i] in freqDB:
            freqDB[nums[i]] = freqDB[nums[i]] + 1
        if nums[i] in returnArrayDB and freqDB[nums[i]] > returnArrayMin:
            # valueToKeyDB[3] = [nums[i]]
            print("asd")
        elif freqDB[nums[i]] > returnArrayMin and nums[i] not in returnArrayDB:
            valueToRemove = valueToKeyDB[returnArrayMin][0]
            indexToRemove = returnArrayDB[valueToRemove]
            returnArrayDB.pop(valueToRemove)
            returnArrayDB[nums[i]] = indexToRemove
            returnArray[indexToRemove] = nums[i]
            valueToKeyDB[2] = []
            if len(valueToKeyDB[3]) == 0:
                valueToKeyDB[2] = [nums[i]]
            else:
                valueToKeyDB[3].append(nums[i])

            

        

        


        

        print(" ")
        print(returnArrayMin)
        print(freqDB)
        print(valueToKeyDB)
        print(returnArrayDB)

        return returnArray

        
        # if freqDB[nums[i]] > returnArrayMin:
        #     removingElem = valueToKeyDB[1]
        #     returnArray[0] = nums[i]
        #     returnArrayMin = 2
       
        

        
        
        # i = 7# 2
        # if nums[i] not in freqDB:
        #     freqDB[nums[i]] = 1
        # elif nums[i] in freqDB:
        #     freqDB[nums[i]] = freqDB[nums[i]] + 1

        # i = 8
        # if nums[i] not in freqDB:
        #     freqDB[nums[i]] = 1
        # elif nums[i] in freqDB:
        #     freqDB[nums[i]] = freqDB[nums[i]] + 1
        
        # i = 9
        # if nums[i] not in freqDB:
        #     freqDB[nums[i]] = 1
        # elif nums[i] in freqDB:
        #     freqDB[nums[i]] = freqDB[nums[i]] + 1
        # if freqDB[nums[i]] > returnArrayMin:
        #     print('asd')
        #     returnArray.pop()
        #     returnArray.append(nums[i])

        # i = 1
        # if nums[i] not in freqDB:
        #     freqDB[nums[i]] = 1
        #     valueToKeyDB[freqDB[nums[i]]] = nums[i]
        # elif nums[i] in freqDB:
        #     freqDB[nums[i]] = freqDB[nums[i]] + 1
        #     valueToKeyDB[freqDB[nums[i]]] = nums[i]
        #     valueToKeyDB.pop(freqDB[nums[i]] - 1)

        # i = 2
        # if nums[i] not in freqDB:
        #     freqDB[nums[i]] = 1
        #     valueToKeyDB[freqDB[nums[i]]] = nums[i]
        # elif nums[i] in freqDB:
        #     freqDB[nums[i]] = freqDB[nums[i]] + 1
        #     valueToKeyDB[freqDB[nums[i]]] = nums[i]
        #     valueToKeyDB.pop(freqDB[nums[i]] - 1)

        # i = 3
        # if nums[i] not in freqDB:
        #     freqDB[nums[i]] = 1
        #     valueToKeyDB[freqDB[nums[i]]] = nums[i]
        # elif nums[i] in freqDB:
        #     freqDB[nums[i]] = freqDB[nums[i]] + 1
        #     valueToKeyDB[freqDB[nums[i]]] = nums[i]
        #     valueToKeyDB.pop(freqDB[nums[i]] - 1)

        # i = 4
        # if nums[i] not in freqDB:
        #     freqDB[nums[i]] = 1
        #     valueToKeyDB[freqDB[nums[i]]] = nums[i]
        # elif nums[i] in freqDB:
        #     freqDB[nums[i]] = freqDB[nums[i]] + 1
        #     valueToKeyDB[freqDB[nums[i]]] = nums[i]
        #     valueToKeyDB.pop(freqDB[nums[i]] - 1)

        # i = 5
        # if nums[i] not in freqDB:
        #     freqDB[nums[i]] = 1
        #     valueToKeyDB[freqDB[nums[i]]] = nums[i]
        # elif nums[i] in freqDB:
        #     freqDB[nums[i]] = freqDB[nums[i]] + 1
        #     valueToKeyDB[freqDB[nums[i]]] = nums[i]
        #     valueToKeyDB.pop(freqDB[nums[i]] - 1)
       

    

        
