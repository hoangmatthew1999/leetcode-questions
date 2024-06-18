class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        returnArray = []
        returnArrayMax = 1
        returnArrayMin = 1
        freqDB = dict()
        valueToKeyDB = dict()
        returnArrayDB = dict()
        if len(nums) == 1:
            return nums
        if len(nums) == k:
            return nums
        if k == 1:
            min = 1
            for j in range(len(nums)):
                if nums[j] not in freqDB:
                    freqDB[nums[j]] = 1    
                elif nums[j] in freqDB:
                    freqDB[nums[j]] =    freqDB[nums[j]] + 1
                    if freqDB[nums[j]] > min:
                        returnArray.append(nums[j])
            return returnArray

        i = 0
        while(len(returnArray) < k):
            if nums[i] not in freqDB:
                freqDB[nums[i]] = 1    
                returnArray.append(nums[i])
                returnArrayDB[nums[i]] = len(returnArray) - 1
            elif nums[i] in freqDB:
                freqDB[nums[i]] =    freqDB[nums[i]] + 1
            if freqDB[nums[i]] not in valueToKeyDB:# next time write this in else and put short if in front 
                valueToKeyDB[freqDB[nums[i]]] = [nums[i]] # makes code neater
                if len(valueToKeyDB) >= 2 and freqDB[nums[i]] >= 2:
                    prev = freqDB[nums[i]] - 1
                    for iter in range(len(valueToKeyDB[prev])):
                        if valueToKeyDB[prev][iter] == nums[i]:
                            valueToKeyDB[prev].pop(iter)
            elif freqDB[nums[i]] in valueToKeyDB:
                valueToKeyDB[freqDB[nums[i]]].append(nums[i])  
            if len(valueToKeyDB[returnArrayMin]) == 0:
                valueToKeyDB.pop(returnArrayMin)
            returnArrayMin = valueToKeyDB.items()[0][0]
            i = i + 1

        print(" ")
        print(returnArrayMin, "min")
        print(freqDB,'freqdb')
        print(valueToKeyDB)
        print(returnArrayDB,"returnArraydb")
      


        # for iterations in range(i, len(nums)):
            #need to add a   valueToKeyDB updater
            # if nums[i] not in freqDB:
            #     freqDB[nums[i]] = 1    
            # elif nums[i] in freqDB:
            #     freqDB[nums[i]] =    freqDB[nums[i]] + 1
        #     if freqDB[nums[i]] > returnArrayMin:
        #         valueToRemove = valueToKeyDB[returnArrayMin][0]
        #         indexToRemove = returnArrayDB[valueToRemove]
        #         valueToKeyDB[returnArrayMin].pop(0)
        #         returnArray[indexToRemove] = nums[i]
        #         returnArrayDB.pop(valueToRemove)
        #         returnArrayDB[nums[i]] = indexToRemove
        #         if freqDB[nums[i]] not in valueToKeyDB:
        #                 valueToKeyDB[freqDB[nums[i]]] = [nums[i]]
        #         elif freqDB[nums[i]] in valueToKeyDB:
        #             valueToKeyDB[freqDB[nums[i]]].append(nums[i])
        #         if len(valueToKeyDB[returnArrayMin]) == 0:
        #             valueToKeyDB.pop(returnArrayMin)
        #     returnArrayMin = valueToKeyDB.items()[0][0]
        #     i = i + 1
        
        print(" ")
        print(returnArrayMin, "min")
        print(freqDB,'freqdb')
        print(valueToKeyDB)
        print(returnArrayDB,"returnArraydb")

        return returnArray
        # if freqDB[nums[i]] > returnArrayMin:
        #     removingElem = valueToKeyDB[1]
        #     returnArray[0] = nums[i]
        #     returnArrayMin = 2
       
    
       

    

        
