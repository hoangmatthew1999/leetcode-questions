class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        currentLength = 3
        returnArray = []
        withoutLastElementArray = []
                
        lastElementIndex = 2
        firstElementIndex = 0
        currentLength = 4
        #correct code for length 4
        # for i in range(currentLength - 1):
        #     withoutLastElementArray.append(nums[i])
        # lastElementIndex = firstElementIndex + currentLength - 1
        # for movingSecondIndex in range(len(nums) - lastElementIndex):
        #   for movingThirdIndex in range(len(nums) - lastElementIndex):
        #     if len(withoutLastElementArray) < currentLength:
        #       withoutLastElementArray.append(nums[lastElementIndex+movingThirdIndex])
        #       arrayTemp = withoutLastElementArray[:]
        #       returnArray.append(arrayTemp)
        #     else:
        #       withoutLastElementArray[len(withoutLastElementArray)-1] = nums[lastElementIndex+movingThirdIndex]
        #       arrayTemp = withoutLastElementArray[:]
        #       returnArray.append(arrayTemp)
        #   lastElementIndex = lastElementIndex + 1
        #   withoutLastElementArray.pop()
        #   withoutLastElementArray[len(withoutLastElementArray)-1] = nums[lastElementIndex-1]
        





        withoutLastElementArray = [1,2,3,4,5]
        withoutLastElementArray[1] = nums[2]
        withoutLastElementArray[2] = nums[3]
        withoutLastElementArray[3] = nums[4]
        withoutLastElementArray[4] = nums[5]
        currentLength = 5


        secondLastIndex = 3
        lastElementIndex = secondLastIndex + 2
        for movingLastIndex in range(len(nums) - lastElementIndex):
          if len(withoutLastElementArray) < currentLength:
            withoutLastElementArray.append(nums[lastElementIndex+movingLastIndex])
            arrayTemp = withoutLastElementArray[:]
            returnArray.append(arrayTemp)
          else:
            withoutLastElementArray[len(withoutLastElementArray)-1] = nums[lastElementIndex+movingLastIndex]
            arrayTemp = withoutLastElementArray[:]
            returnArray.append(arrayTemp)  
        withoutLastElementArray.pop()  
        lastElementIndex = lastElementIndex + 1
        withoutLastElementArray[len(withoutLastElementArray)-1] = nums[lastElementIndex-1] 


        for movingLastIndex in range(len(nums) - lastElementIndex):
          if len(withoutLastElementArray) < currentLength:
            withoutLastElementArray.append(nums[lastElementIndex+movingLastIndex])
            arrayTemp = withoutLastElementArray[:]
            returnArray.append(arrayTemp)
          else:
            withoutLastElementArray[len(withoutLastElementArray)-1] = nums[lastElementIndex+movingLastIndex]
            arrayTemp = withoutLastElementArray[:]
            returnArray.append(arrayTemp)
          withoutLastElementArray.pop()  
          
        withoutLastElementArray[2] = nums[4]
        withoutLastElementArray[3] = nums[5]

        for movingLastIndex in range(len(nums)-lastElementIndex):
          if len(withoutLastElementArray) < currentLength:
            withoutLastElementArray.append(nums[lastElementIndex+movingLastIndex])
            arrayTemp = withoutLastElementArray[:]
            returnArray.append(arrayTemp)
          else:
            withoutLastElementArray[len(withoutLastElementArray)-1] = nums[lastElementIndex+movingLastIndex]
            arrayTemp = withoutLastElementArray[:]
            returnArray.append(arrayTemp)
          withoutLastElementArray.pop()

        withoutLastElementArray[1] = nums[3]

        for movingLastIndex in range(len(nums) - lastElementIndex):
          if len(withoutLastElementArray) < currentLength:
            withoutLastElementArray.append(nums[lastElementIndex+movingLastIndex])
            arrayTemp = withoutLastElementArray[:]
            returnArray.append(arrayTemp)
        
        # withoutLastElementArray[2] =   nums[4]
        # lastElementIndex = 4 + 1
        # for movLastIndex in range(len(nums) - lastElementIndex):
        #   if len(withoutLastElementArray) < currentLength:
        #               withoutLastElementArray.append(nums[lastElementIndex+movLastIndex])
        #               arrayTemp = withoutLastElementArray[:]
        #               returnArray.append(arrayTemp)
        # withoutLastElementArray.pop()
        
        # withoutLastElementArray[1] = nums[3]
        # withoutLastElementArray[2] = nums[4]





        

        
        
        # if len(nums) > 4:
        #   for movingFirstIndex in range(len(nums) - firstElementIndex - 2):
        #     withoutLastElementArray = []
        #     for createArray in range(currentLength - 1):
        #       withoutLastElementArray.append(nums[firstElementIndex + movingFirstIndex + createArray])
        #     lastElementIndex = firstElementIndex + 2
        #     for movingThirdIndex in range(len(nums) - lastElementIndex):
        #       if len(withoutLastElementArray) < currentLength:# if the length of WLE is 2 then append so=3
        #         withoutLastElementArray.append(nums[lastElementIndex+movingThirdIndex])
        #         arrayTemp = withoutLastElementArray[:]
        #         returnArray.append(arrayTemp)
        #       else:
        #         withoutLastElementArray[len(withoutLastElementArray)-1] = nums[lastElementIndex+movingThirdIndex]
        #         arrayTemp = withoutLastElementArray[:]
        #         returnArray.append(arrayTemp)
        #     lastElementIndex = lastElementIndex + 1
        #     withoutLastElementArray.pop()
        #     withoutLastElementArray[len(withoutLastElementArray)-1] = nums[lastElementIndex-1]
        #   firstElementIndex = firstElementIndex + 1

          
        return returnArray








        
