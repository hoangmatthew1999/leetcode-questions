class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        returnArray = []
        returnArrayMin = 0# will need to add var to first loop
        valueToKeyDB = dict()
        freqDB = dict()
        returnArrayDB = dict()
        valueToKeyLookup = dict()

        i = 0
        while(len(returnArray) < k):
            if nums[i] not in freqDB:
                freqDB[nums[i]] = 1
                returnArray.append( nums[i] )
                returnArrayDB[nums[i]] = len(returnArray) - 1
                if freqDB[nums[i]] not in valueToKeyDB:
                    valueToKeyDB[freqDB[nums[i]]] = [nums[i]]
                    valueToKeyLookup[nums[i]] = (1,0)
                elif freqDB[nums[i]] in valueToKeyDB:
                    valueToKeyDB[1].append(nums[i])
                    valueToKeyLookup[nums[i]] = (1,len(valueToKeyDB[1]) - 1)
            elif nums[i] in freqDB:
                freqDB[nums[i]] = freqDB[nums[i]] + 1
                if freqDB[nums[i]] not in valueToKeyDB:
                    valueToKeyDB[freqDB[nums[i]]] = [nums[i]]
                    valueToKeyDB[freqDB[nums[i]] - 1].pop(valueToKeyLookup[1][1])
                    
            if freqDB[nums[i]] > returnArrayMin:
                returnArrayMin = freqDB[nums[i]]
            i = i + 1
        
        i = 2
        if nums[i] not in freqDB:
            freqDB[nums[i]] = 1
        elif nums[i] in freqDB:
            freqDB[nums[i]] = freqDB[nums[i]] + 1
        if nums[i] in returnArrayDB:# updating returnArrayDB
            indexToRemove = valueToKeyLookup[nums[i]]
            valueToKeyDB[returnArrayMin].pop(indexToRemove[1])
            if freqDB[nums[i]] not in valueToKeyDB:# is the num of occurence in the stack
                valueToKeyDB[freqDB[nums[i]]] = [nums[i]]
                valueToKeyLookup.pop(nums[i])
                valueToKeyLookup[nums[i]] = (freqDB[nums[i]], 0)
        if freqDB[nums[i]] > returnArrayMin and nums[i] not in returnArrayDB: 
            valueToRemove = valueToKeyDB[returnArrayMin]
            valueToRemove = valueToRemove[0]    
            indexToRemove = returnArrayDB[valueToRemove]
            returnArray[indexToRemove] = nums[i]
            returnArrayDB[nums[i]] = indexToRemove    
            returnArrayDB.pop(valueToRemove)
            valueToKeyDB[returnArrayMin].pop(valueToKeyLookup[valueToRemove][1])
            valueToKeyDB[freqDB[nums[i]]].append(nums[i])
            valueToKeyLookup.pop(valueToRemove)
            valueToKeyLookup[nums[i]] = (     freqDB[nums[i]],len(valueToKeyDB[freqDB[nums[i]]]) - 1 )
            returnArrayMin = next ( iter(valueToKeyDB) )
            print(valueToKeyDB)
        i = i + 1
        #     else:
        #         valueToKeyDB[2].append(nums[i])
        #     valueToKeyLookup.pop(4)
        #     valueToKeyLookup[4] = (2,0)

        # if nums[i] not in freqDB:
        #     freqDB[nums[i]] = 1
        # elif nums[i] in freqDB:
        #     freqDB[nums[i]] = freqDB[nums[i]] + 1
        # if nums[i] in returnArrayDB:# updating returnArrayDB
        #     indexToRemove = valueToKeyLookup[nums[i]]
        #     valueToKeyDB[returnArrayMin].pop(indexToRemove[1])
        #     if freqDB[nums[i]] not in valueToKeyDB:# is the num of occurence in the stack
        #         valueToKeyDB[freqDB[nums[i]]] = [nums[i]]
        #         valueToKeyLookup.pop(nums[i])
        #         valueToKeyLookup[nums[i]] = (freqDB[nums[i]], 0)
        # if freqDB[nums[i]] > returnArrayMin and nums[i] not in returnArrayDB: 
        #     valueToRemove = valueToKeyDB[returnArrayMin]
        #     valueToRemove = valueToRemove[0]    
        #     indexToRemove = returnArrayDB[valueToRemove]
        #     returnArray[indexToRemove] = nums[i]
        #     returnArrayDB[nums[i]] = indexToRemove    
        #     returnArrayDB.pop(valueToRemove)
        #     valueToKeyDB[returnArrayMin].pop(valueToKeyLookup[valueToRemove][1])
        #     valueToKeyDB[freqDB[nums[i]]].append(nums[i])
        #     valueToKeyLookup.pop(valueToRemove)
        #     valueToKeyLookup[nums[i]] = (     freqDB[nums[i]],len(valueToKeyDB[freqDB[nums[i]]]) - 1 )
        #     returnArrayMin = next ( iter(valueToKeyDB) )
        # i = i + 1
        

        # for iterations in range(len(nums) - i):
        #     if nums[i] not in freqDB:
        #         freqDB[nums[i]] = 1
        #     elif nums[i] in freqDB:
        #         freqDB[nums[i]] = freqDB[nums[i]] + 1
        #     if nums[i] in returnArrayDB:# updating returnArrayDB
        #         indexToRemove = valueToKeyLookup[nums[i]]
        #         print(indexToRemove)
        #         valueToKeyDB[indexToRemove[0]].pop(indexToRemove[1])
        #         if freqDB[nums[i]] not in valueToKeyDB:# is the num of occurence in the stack
        #             valueToKeyDB[freqDB[nums[i]]] = [nums[i]]
        #             valueToKeyLookup.pop(nums[i])
        #             valueToKeyLookup[nums[i]] = (freqDB[nums[i]], 0)
        #         for elem,index in enumerate(valueToKeyDB[indexToRemove[0]]):
        #             valueToKeyLookup[index] = (indexToRemove[0],elem)
        #     if freqDB[nums[i]] > returnArrayMin and nums[i] not in returnArrayDB: 
        #         valueToRemove = valueToKeyDB[returnArrayMin]
        #         valueToRemove = valueToRemove[0]    
        #         indexToRemove = returnArrayDB[valueToRemove]
        #         returnArray[indexToRemove] = nums[i]
        #         returnArrayDB[nums[i]] = indexToRemove    
        #         returnArrayDB.pop(valueToRemove)
        #         valueToKeyDB[returnArrayMin].pop(valueToKeyLookup[valueToRemove][1])
        #         valueToKeyDB[freqDB[nums[i]]].append(nums[i])
        #         valueToKeyLookup.pop(valueToRemove)
        #         valueToKeyLookup[nums[i]] = (     freqDB[nums[i]],len(valueToKeyDB[freqDB[nums[i]]]) - 1 )
        #         if len(valueToKeyDB[returnArrayMin])== 0:
        #             valueToKeyDB.pop(returnArrayMin)
        #         returnArrayMin = next ( iter(valueToKeyDB) )
        #     print(valueToKeyDB)
        #     print(returnArrayMin)
        #     print(i)
        #     print(" ")

        #     i = i + 1

        # # #breakpoint for bug
        if nums[i] not in freqDB:
            freqDB[nums[i]] = 1
        elif nums[i] in freqDB:
            freqDB[nums[i]] = freqDB[nums[i]] + 1
        if nums[i] in returnArrayDB:# updating returnArrayDB
            indexToRemove = valueToKeyLookup[nums[i]]
            valueToKeyDB[indexToRemove[0]].pop(indexToRemove[1]) # problematic line
            if freqDB[nums[i]] not in valueToKeyDB:# is the num of occurence in the stack
                valueToKeyDB[freqDB[nums[i]]] = [nums[i]]
                valueToKeyLookup.pop(nums[i])
                valueToKeyLookup[nums[i]] = (freqDB[nums[i]], 0)
        if freqDB[nums[i]] > returnArrayMin and nums[i] not in returnArrayDB: 
            valueToRemove = valueToKeyDB[returnArrayMin]
            valueToRemove = valueToRemove[0]    
            indexToRemove = returnArrayDB[valueToRemove]
            returnArray[indexToRemove] = nums[i]
            returnArrayDB[nums[i]] = indexToRemove    
            returnArrayDB.pop(valueToRemove)
            valueToKeyDB[returnArrayMin].pop(valueToKeyLookup[valueToRemove][1])
            valueToKeyDB[freqDB[nums[i]]].append(nums[i])
            valueToKeyLookup.pop(valueToRemove)
            valueToKeyLookup[nums[i]] = (     freqDB[nums[i]],len(valueToKeyDB[freqDB[nums[i]]]) - 1 )
            if len(valueToKeyDB[returnArrayMin])== 0:
                valueToKeyDB.pop(returnArrayMin)
            returnArrayMin = next ( iter(valueToKeyDB) )
        i = i + 1

        if nums[i] not in freqDB:
            freqDB[nums[i]] = 1
        elif nums[i] in freqDB:
            freqDB[nums[i]] = freqDB[nums[i]] + 1
        if nums[i] in returnArrayDB:# updating returnArrayDB
            indexToRemove = valueToKeyLookup[nums[i]]
            valueToKeyDB[returnArrayMin].pop(indexToRemove[1])
            if freqDB[nums[i]] not in valueToKeyDB:# is the num of occurence in the stack
                valueToKeyDB[freqDB[nums[i]]] = [nums[i]]
                valueToKeyLookup.pop(nums[i])
                valueToKeyLookup[nums[i]] = (freqDB[nums[i]], 0)
        if freqDB[nums[i]] > returnArrayMin and nums[i] not in returnArrayDB: 
            valueToRemove = valueToKeyDB[returnArrayMin]
            valueToRemove = valueToRemove[0]    
            indexToRemove = returnArrayDB[valueToRemove]
            returnArray[indexToRemove] = nums[i]
            returnArrayDB[nums[i]] = indexToRemove    
            returnArrayDB.pop(valueToRemove)
            valueToKeyDB[returnArrayMin].pop(valueToKeyLookup[valueToRemove][1])
            valueToKeyDB[freqDB[nums[i]]].append(nums[i])
            valueToKeyLookup.pop(valueToRemove)
            valueToKeyLookup[nums[i]] = (     freqDB[nums[i]],len(valueToKeyDB[freqDB[nums[i]]]) - 1 )
            if len(valueToKeyDB[returnArrayMin])== 0:
                valueToKeyDB.pop(returnArrayMin)
            returnArrayMin = next ( iter(valueToKeyDB) )
        i = i + 1

        # if nums[i] not in freqDB:
        #     freqDB[nums[i]] = 1
        # elif nums[i] in freqDB:
        #     freqDB[nums[i]] = freqDB[nums[i]] + 1
        # if nums[i] in returnArrayDB:# updating returnArrayDB
        #     indexToRemove = valueToKeyLookup[nums[i]]
        #     valueToKeyDB[returnArrayMin].pop(indexToRemove[1])
        #     if freqDB[nums[i]] not in valueToKeyDB:# is the num of occurence in the stack
        #         valueToKeyDB[freqDB[nums[i]]] = [nums[i]]
        #         valueToKeyLookup.pop(nums[i])
        #         valueToKeyLookup[nums[i]] = (freqDB[nums[i]], 0)
        # if freqDB[nums[i]] > returnArrayMin and nums[i] not in returnArrayDB: 
        #     valueToRemove = valueToKeyDB[returnArrayMin]
        #     valueToRemove = valueToRemove[0]    
        #     indexToRemove = returnArrayDB[valueToRemove]
        #     returnArray[indexToRemove] = nums[i]
        #     returnArrayDB[nums[i]] = indexToRemove    
        #     returnArrayDB.pop(valueToRemove)
        #     valueToKeyDB[returnArrayMin].pop(valueToKeyLookup[valueToRemove][1])
        #     valueToKeyDB[freqDB[nums[i]]].append(nums[i])
        #     valueToKeyLookup.pop(valueToRemove)
        #     valueToKeyLookup[nums[i]] = (     freqDB[nums[i]],len(valueToKeyDB[freqDB[nums[i]]]) - 1 )
        #     if len(valueToKeyDB[returnArrayMin])== 0:
        #         valueToKeyDB.pop(returnArrayMin)
        #     returnArrayMin = next ( iter(valueToKeyDB) )
        # i = i + 1

        # if nums[i] not in freqDB:
        #     freqDB[nums[i]] = 1
        # elif nums[i] in freqDB:
        #     freqDB[nums[i]] = freqDB[nums[i]] + 1
        # if nums[i] in returnArrayDB:# updating returnArrayDB
        #     indexToRemove = valueToKeyLookup[nums[i]]
        #     valueToKeyDB[returnArrayMin].pop(indexToRemove[1])
        #     if freqDB[nums[i]] not in valueToKeyDB:# is the num of occurence in the stack
        #         valueToKeyDB[freqDB[nums[i]]] = [nums[i]]
        #         valueToKeyLookup.pop(nums[i])
        #         valueToKeyLookup[nums[i]] = (freqDB[nums[i]], 0)
        # if freqDB[nums[i]] > returnArrayMin and nums[i] not in returnArrayDB: 
        #     print(returnArrayMin)
        #     valueToRemove = valueToKeyDB[returnArrayMin]
        #     print(valueToRemove)
        #     valueToRemove = valueToRemove[0]    
        #     indexToRemove = returnArrayDB[valueToRemove]
        #     returnArray[indexToRemove] = nums[i]
        #     returnArrayDB[nums[i]] = indexToRemove    
        #     returnArrayDB.pop(valueToRemove)
        #     valueToKeyDB[returnArrayMin].pop(valueToKeyLookup[valueToRemove][1])
        #     valueToKeyDB[freqDB[nums[i]]].append(nums[i])
        #     valueToKeyLookup.pop(valueToRemove)
        #     valueToKeyLookup[nums[i]] = (     freqDB[nums[i]],len(valueToKeyDB[freqDB[nums[i]]]) - 1 )
        #     returnArrayMin = next ( iter(valueToKeyDB) )
        #     if len(valueToKeyDB[returnArrayMin])== 0:
        #         valueToKeyDB.pop(returnArrayMin)
        # i = i + 1

        # if nums[i] not in freqDB:
        #     freqDB[nums[i]] = 1
        # elif nums[i] in freqDB:
        #     freqDB[nums[i]] = freqDB[nums[i]] + 1
        # if nums[i] in returnArrayDB:# updating returnArrayDB
        #     indexToRemove = valueToKeyLookup[nums[i]]
        #     valueToKeyDB[returnArrayMin].pop(indexToRemove[1])
        #     if freqDB[nums[i]] not in valueToKeyDB:# is the num of occurence in the stack
        #         valueToKeyDB[freqDB[nums[i]]] = [nums[i]]
        #         valueToKeyLookup.pop(nums[i])
        #         valueToKeyLookup[nums[i]] = (freqDB[nums[i]], 0)
        # if freqDB[nums[i]] > returnArrayMin and nums[i] not in returnArrayDB: 
        #     valueToRemove = valueToKeyDB[returnArrayMin]
        #     valueToRemove = valueToRemove[0]    
        #     indexToRemove = returnArrayDB[valueToRemove]
        #     returnArray[indexToRemove] = nums[i]
        #     returnArrayDB[nums[i]] = indexToRemove    
        #     returnArrayDB.pop(valueToRemove)
        #     valueToKeyDB[returnArrayMin].pop(valueToKeyLookup[valueToRemove][1])
        #     valueToKeyDB[freqDB[nums[i]]].append(nums[i])
        #     valueToKeyLookup.pop(valueToRemove)
        #     valueToKeyLookup[nums[i]] = (     freqDB[nums[i]],len(valueToKeyDB[freqDB[nums[i]]]) - 1 )
        #     if len(valueToKeyDB[returnArrayMin])== 0:
        #         valueToKeyDB.pop(returnArrayMin)
        #     returnArrayMin = next ( iter(valueToKeyDB) )
        # i = i + 1

        # if nums[i] not in freqDB:
        #     freqDB[nums[i]] = 1
        # elif nums[i] in freqDB:
        #     freqDB[nums[i]] = freqDB[nums[i]] + 1
        # if nums[i] in returnArrayDB:# updating returnArrayDB
        #     indexToRemove = valueToKeyLookup[nums[i]]
        #     valueToKeyDB[returnArrayMin].pop(indexToRemove[1])
        #     if freqDB[nums[i]] not in valueToKeyDB:# is the num of occurence in the stack
        #         valueToKeyDB[freqDB[nums[i]]] = [nums[i]]
        #         valueToKeyLookup.pop(nums[i])
        #         valueToKeyLookup[nums[i]] = (freqDB[nums[i]], 0)
        # if freqDB[nums[i]] > returnArrayMin and nums[i] not in returnArrayDB: 
        #     valueToRemove = valueToKeyDB[returnArrayMin]
        #     valueToRemove = valueToRemove[0]    
        #     indexToRemove = returnArrayDB[valueToRemove]
        #     returnArray[indexToRemove] = nums[i]
        #     returnArrayDB[nums[i]] = indexToRemove    
        #     returnArrayDB.pop(valueToRemove)
        #     valueToKeyDB[returnArrayMin].pop(valueToKeyLookup[valueToRemove][1])
        #     valueToKeyDB[freqDB[nums[i]]].append(nums[i])
        #     valueToKeyLookup.pop(valueToRemove)
        #     valueToKeyLookup[nums[i]] = (     freqDB[nums[i]],len(valueToKeyDB[freqDB[nums[i]]]) - 1 )
        #     if len(valueToKeyDB[returnArrayMin])== 0:
        #         valueToKeyDB.pop(returnArrayMin)
        #     returnArrayMin = next ( iter(valueToKeyDB) )
        # i = i + 1

        # if nums[i] not in freqDB:
        #     freqDB[nums[i]] = 1
        # elif nums[i] in freqDB:
        #     freqDB[nums[i]] = freqDB[nums[i]] + 1
        # if nums[i] in returnArrayDB:# updating returnArrayDB
        #     indexToRemove = valueToKeyLookup[nums[i]]
        #     valueToKeyDB[returnArrayMin].pop(indexToRemove[1])
        #     if freqDB[nums[i]] not in valueToKeyDB:# is the num of occurence in the stack
        #         valueToKeyDB[freqDB[nums[i]]] = [nums[i]]
        #         valueToKeyLookup.pop(nums[i])
        #         valueToKeyLookup[nums[i]] = (freqDB[nums[i]], 0)
        # if freqDB[nums[i]] > returnArrayMin and nums[i] not in returnArrayDB: 
        #     valueToRemove = valueToKeyDB[returnArrayMin]
        #     valueToRemove = valueToRemove[0]    
        #     indexToRemove = returnArrayDB[valueToRemove]
        #     returnArray[indexToRemove] = nums[i]
        #     returnArrayDB[nums[i]] = indexToRemove    
        #     returnArrayDB.pop(valueToRemove)
        #     valueToKeyDB[returnArrayMin].pop(valueToKeyLookup[valueToRemove][1])
        #     valueToKeyDB[freqDB[nums[i]]].append(nums[i])
        #     valueToKeyLookup.pop(valueToRemove)
        #     valueToKeyLookup[nums[i]] = (     freqDB[nums[i]],len(valueToKeyDB[freqDB[nums[i]]]) - 1 )
        #     if len(valueToKeyDB[returnArrayMin])== 0:
        #         valueToKeyDB.pop(returnArrayMin)
        #     returnArrayMin = next ( iter(valueToKeyDB) )
        # i = i + 1

      
        # if nums[i] not in freqDB:
        #     freqDB[nums[i]] = 1
        # elif nums[i] in freqDB:
        #     freqDB[nums[i]] = freqDB[nums[i]] + 1
        # if nums[i] in returnArrayDB:# updating returnArrayDB
        #     indexToRemove = valueToKeyLookup[nums[i]]
        #     valueToKeyDB[returnArrayMin].pop(indexToRemove[1])
        #     if freqDB[nums[i]] not in valueToKeyDB:# is the num of occurence in the stack
        #         valueToKeyDB[freqDB[nums[i]]] = [nums[i]]
        #         valueToKeyLookup.pop(nums[i])
        #         valueToKeyLookup[nums[i]] = (freqDB[nums[i]], 0)
        #     for elem,index in enumerate(valueToKeyDB[indexToRemove[0]]):
        #         valueToKeyLookup[index] = (indexToRemove[0],elem)
        # if freqDB[nums[i]] > returnArrayMin and nums[i] not in returnArrayDB: 
        #     valueToRemove = valueToKeyDB[returnArrayMin]
        #     valueToRemove = valueToRemove[0]    
        #     indexToRemove = returnArrayDB[valueToRemove]
        #     returnArray[indexToRemove] = nums[i]
        #     returnArrayDB[nums[i]] = indexToRemove    
        #     returnArrayDB.pop(valueToRemove)
        #     valueToKeyDB[returnArrayMin].pop(valueToKeyLookup[valueToRemove][1])
        #     valueToKeyDB[freqDB[nums[i]]].append(nums[i])
        #     valueToKeyLookup.pop(valueToRemove)
        #     valueToKeyLookup[nums[i]] = (     freqDB[nums[i]],len(valueToKeyDB[freqDB[nums[i]]]) - 1 )
        #     if len(valueToKeyDB[returnArrayMin])== 0:
        #         valueToKeyDB.pop(returnArrayMin)
        #     returnArrayMin = next ( iter(valueToKeyDB) )
        # i = i + 1


        # 5
        # if nums[i] not in freqDB:
        #     freqDB[nums[i]] = 1
        # elif nums[i] in freqDB:
        #     freqDB[nums[i]] = freqDB[nums[i]] + 1
        # if nums[i] in returnArrayDB:# updating returnArrayDB
        #     indexToRemove = valueToKeyLookup[nums[i]]
        #     valueToKeyDB[returnArrayMin].pop(indexToRemove[1])
        #     if freqDB[nums[i]] not in valueToKeyDB:# is the num of occurence in the stack
        #         valueToKeyDB[freqDB[nums[i]]] = [nums[i]]
        #         valueToKeyLookup.pop(nums[i])
        #         valueToKeyLookup[nums[i]] = (freqDB[nums[i]], 0)
        #     else:
        #         valueToKeyDB[freqDB[nums[i]]].append(nums[i])
        #         valueToKeyLookup[nums[i]] = (freqDB[nums[i]],len(valueToKeyDB[freqDB[nums[i]]]) - 1)
        #     for elem,index in enumerate(valueToKeyDB[indexToRemove[0]]):
        #         valueToKeyLookup[index] = (indexToRemove[0],elem)
        #     if len(valueToKeyDB[returnArrayMin])== 0:
        #         valueToKeyDB.pop(returnArrayMin)
        # if freqDB[nums[i]] > returnArrayMin and nums[i] not in returnArrayDB: 
        #     valueToRemove = valueToKeyDB[returnArrayMin]
        #     valueToRemove = valueToRemove[0]    
        #     indexToRemove = returnArrayDB[valueToRemove]
        #     returnArray[indexToRemove] = nums[i]
        #     returnArrayDB[nums[i]] = indexToRemove    
        #     returnArrayDB.pop(valueToRemove)
        #     valueToKeyDB[returnArrayMin].pop(valueToKeyLookup[valueToRemove][1])
        #     valueToKeyDB[freqDB[nums[i]]].append(nums[i])
        #     valueToKeyLookup.pop(valueToRemove)
        #     valueToKeyLookup[nums[i]] = (     freqDB[nums[i]],len(valueToKeyDB[freqDB[nums[i]]]) - 1 )
        #     if len(valueToKeyDB[returnArrayMin])== 0:
        #         valueToKeyDB.pop(returnArrayMin)
        #     returnArrayMin = next ( iter(valueToKeyDB) )
        # i = i + 1

        for iterations in range(10):
            if nums[i] not in freqDB:
                freqDB[nums[i]] = 1
            elif nums[i] in freqDB:
                freqDB[nums[i]] = freqDB[nums[i]] + 1
            if nums[i] in returnArrayDB:# updating returnArrayDB
                indexToRemove = valueToKeyLookup[nums[i]]
                valueToKeyDB[returnArrayMin].pop(indexToRemove[1])
                if freqDB[nums[i]] not in valueToKeyDB:# is the num of occurence in the stack
                    valueToKeyDB[freqDB[nums[i]]] = [nums[i]]
                    valueToKeyLookup.pop(nums[i])
                    valueToKeyLookup[nums[i]] = (freqDB[nums[i]], 0)
                else:
                    valueToKeyDB[freqDB[nums[i]]].append(nums[i])
                    valueToKeyLookup[nums[i]] = (freqDB[nums[i]],len(valueToKeyDB[freqDB[nums[i]]]) - 1)
                for elem,index in enumerate(valueToKeyDB[indexToRemove[0]]):
                    valueToKeyLookup[index] = (indexToRemove[0],elem)
                if len(valueToKeyDB[returnArrayMin])== 0:
                    valueToKeyDB.pop(returnArrayMin)
            if freqDB[nums[i]] > returnArrayMin and nums[i] not in returnArrayDB: 
                valueToRemove = valueToKeyDB[returnArrayMin]
                valueToRemove = valueToRemove[0]    
                indexToRemove = returnArrayDB[valueToRemove]
                returnArray[indexToRemove] = nums[i]
                returnArrayDB[nums[i]] = indexToRemove    
                returnArrayDB.pop(valueToRemove)
                valueToKeyDB[returnArrayMin].pop(valueToKeyLookup[valueToRemove][1])
                valueToKeyDB[freqDB[nums[i]]].append(nums[i])
                valueToKeyLookup.pop(valueToRemove)
                valueToKeyLookup[nums[i]] = (     freqDB[nums[i]],len(valueToKeyDB[freqDB[nums[i]]]) - 1 )
                if len(valueToKeyDB[returnArrayMin])== 0:
                    valueToKeyDB.pop(returnArrayMin)
                returnArrayMin = next ( iter(valueToKeyDB) )
            i = i + 1

        # if nums[i] not in freqDB:
        #     freqDB[nums[i]] = 1
        # elif nums[i] in freqDB:
        #     freqDB[nums[i]] = freqDB[nums[i]] + 1
        # if nums[i] in returnArrayDB:# updating returnArrayDB
        #     indexToRemove = valueToKeyLookup[nums[i]]
        #     valueToKeyDB[returnArrayMin].pop(indexToRemove[1])
        #     if freqDB[nums[i]] not in valueToKeyDB:# is the num of occurence in the stack
        #         valueToKeyDB[freqDB[nums[i]]] = [nums[i]]
        #         valueToKeyLookup.pop(nums[i])
        #         valueToKeyLookup[nums[i]] = (freqDB[nums[i]], 0)
        #     else:
        #         valueToKeyDB[freqDB[nums[i]]].append(nums[i])
        #         valueToKeyLookup[nums[i]] = (freqDB[nums[i]],len(valueToKeyDB[freqDB[nums[i]]]) - 1)
        #     for elem,index in enumerate(valueToKeyDB[indexToRemove[0]]):
        #         valueToKeyLookup[index] = (indexToRemove[0],elem)
        #     if len(valueToKeyDB[returnArrayMin])== 0:
        #         valueToKeyDB.pop(returnArrayMin)
        # if freqDB[nums[i]] > returnArrayMin and nums[i] not in returnArrayDB: 
        #     valueToRemove = valueToKeyDB[returnArrayMin]
        #     valueToRemove = valueToRemove[0]    
        #     indexToRemove = returnArrayDB[valueToRemove]
        #     returnArray[indexToRemove] = nums[i]
        #     returnArrayDB[nums[i]] = indexToRemove    
        #     returnArrayDB.pop(valueToRemove)
        #     valueToKeyDB[returnArrayMin].pop(valueToKeyLookup[valueToRemove][1])
        #     valueToKeyDB[freqDB[nums[i]]].append(nums[i])
        #     valueToKeyLookup.pop(valueToRemove)
        #     valueToKeyLookup[nums[i]] = (     freqDB[nums[i]],len(valueToKeyDB[freqDB[nums[i]]]) - 1 )
        #     if len(valueToKeyDB[returnArrayMin])== 0:
        #         valueToKeyDB.pop(returnArrayMin)
        #     returnArrayMin = next ( iter(valueToKeyDB) )
        # i = i + 1

       
        
        print(i)


        print(" ")
        print(valueToKeyDB)
        print(valueToKeyLookup)
        print(returnArrayDB)
        print(freqDB)
        return returnArray
