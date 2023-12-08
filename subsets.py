class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        returnArray = [[]]
        if len(nums) == 1:
            insertArray = []
            insertArray.append(nums[0])
            returnArray.append(insertArray)
            return returnArray
        currentArrayLength = 1
        previousLevelArray = []
        
        #first iteration
        i = 0
        for i in range(len(nums) ):
            insertArray = []
            insertArray.append(nums[i])
            returnArray.append(insertArray)
            previousLevelArray.append(insertArray)

        i = 0
        offset = 1
        
        insertArray = []
        insertArray.append(nums[i])
        insertArray.append(nums[i + offset])
        returnArray.append(insertArray)

        offset = offset + 1
        insertArray = []
        insertArray.append(nums[i])
        insertArray.append(nums[i + offset])
        returnArray.append(insertArray)

        i = i + 1
        offset = i
        insertArray = []
        insertArray.append(nums[i])
        insertArray.append(nums[i+offset])
        returnArray.append(insertArray)


        returnArray.append(nums)# need to add the entire array



          

       



      
        return returnArray
        
    
