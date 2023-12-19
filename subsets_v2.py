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
        for i in range(currentLength - 1):
            withoutLastElementArray.append(nums[i])

        for movingSecondIndex in range(len(nums)-lastElementIndex):
          for movingThirdIndex in range(len(nums) - lastElementIndex):
            if len(withoutLastElementArray) < currentLength:# if the length of WLE is 2 then append so = 3
              withoutLastElementArray.append(nums[lastElementIndex+movingThirdIndex])
              arrayTemp = withoutLastElementArray[:]
              returnArray.append(arrayTemp)
            else:
              withoutLastElementArray[len(withoutLastElementArray)-1] = nums[lastElementIndex+movingThirdIndex]
              arrayTemp = withoutLastElementArray[:]
              returnArray.append(arrayTemp)
          lastElementIndex = lastElementIndex + 1
          withoutLastElementArray.pop()
          withoutLastElementArray[len(withoutLastElementArray)-1] = nums[lastElementIndex-1]
        firstElementIndex = firstElementIndex + 1
        
        if len(nums) > 4:
          for movingFirstIndex in range(len(nums) - firstElementIndex - 2):
            withoutLastElementArray = []
            for createArray in range(currentLength - 1):
              withoutLastElementArray.append(nums[firstElementIndex + movingFirstIndex + createArray])
            lastElementIndex = firstElementIndex + 2
            for movingThirdIndex in range(len(nums) - lastElementIndex):
              if len(withoutLastElementArray) < currentLength:# if the length of WLE is 2 then append so=3
                withoutLastElementArray.append(nums[lastElementIndex+movingThirdIndex])
                arrayTemp = withoutLastElementArray[:]
                returnArray.append(arrayTemp)
              else:
                withoutLastElementArray[len(withoutLastElementArray)-1] = nums[lastElementIndex+movingThirdIndex]
                arrayTemp = withoutLastElementArray[:]
                returnArray.append(arrayTemp)
            lastElementIndex = lastElementIndex + 1
            withoutLastElementArray.pop()
            withoutLastElementArray[len(withoutLastElementArray)-1] = nums[lastElementIndex-1]
          firstElementIndex = firstElementIndex + 1


                
            
            
            

        return returnArray






         # for j in range(len(nums) - lastElementIndex):
        #   for i in range(len(nums) - lastElementIndex):
        #     if len(withoutLastElementArray) < currentLength:# if the length of WLE is 2 then append so = 3
        #       withoutLastElementArray.append(nums[lastElementIndex+i])
        #       arrayTemp = withoutLastElementArray[:]
        #       returnArray.append(arrayTemp)
        #     else:
        #       withoutLastElementArray[len(withoutLastElementArray)-1] = nums[lastElementIndex+i]
        #       arrayTemp = withoutLastElementArray[:]
        #       returnArray.append(arrayTemp)
          
        #   lastElementIndex = lastElementIndex + 1
        #   withoutLastElementArray.pop()
        #   withoutLastElementArray[len(withoutLastElementArray)-1] = nums[lastElementIndex-1]

        # withoutLastElementArray = []
        # withoutLastElementStartIndex = 1
        # for i in range(currentLength-1):
        #   withoutLastElementArray.append(nums[withoutLastElementStartIndex])
        #   withoutLastElementStartIndex = withoutLastElementStartIndex + 1
        # lastElementIndex = withoutLastElementStartIndex


        
