class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        currentLength = 3
        returnArray = []
        if len(nums) == 1:
          returnArray.append(nums)
          returnArray.append([])
          return returnArray
        if len(nums) == 2:
          returnArray.append([nums[0]])
          returnArray.append([nums[1]])
          returnArray.append([])
          returnArray.append(nums)
          return returnArray

        elementIndexDict = dict()
        for i in range(len(nums)):
          elementIndexDict[nums[i]] = i
                
        firstElementIndex = 0
        currentLength = 4
        lastElementIndex = firstElementIndex + currentLength

        previousLevel = []
        currentLevel = []

        for lengthOne in range(len(nums)):
          sizeOneArray = []
          sizeOneArray.append(nums[lengthOne])
          currentLevel.append(sizeOneArray)
          returnArray.append(sizeOneArray)

        previousLevel = currentLevel
        currentLevel = []
        currentLength = 2
        # for lengthTwo in range(len(nums)):
        currentArray = previousLevel[0]
        currentArray = currentArray[:]
        lastElementIndex = elementIndexDict[currentArray[len(currentArray) -1]] + 1
        for nextCurrentArrayElem in range(len(previousLevel)):
          currentArray = previousLevel[nextCurrentArrayElem]
          currentArray = currentArray[:]
          lastElementIndex = elementIndexDict[currentArray[len(currentArray) -1]] + 1
          for addLastElem in range(len(nums) - lastElementIndex):
            if len(currentArray ) < currentLength:
              currentArray.append(nums[lastElementIndex])
              arrayTemp = currentArray[:]
              returnArray.append(arrayTemp)
              currentLevel.append(arrayTemp)
            else:
              currentArray[len(currentArray)-1] = nums[lastElementIndex + addLastElem]
              arrayTemp = currentArray[:]
              returnArray.append(arrayTemp)
              currentLevel.append(arrayTemp)
        
       
        previousLevel = currentLevel
        currentLevel = []
        currentLength = currentLength + 1
        for increaseCurrentLength in range(len(nums) - currentLength):
          for nextCurrentArrayElem in range(len(previousLevel)):
              currentArray = previousLevel[nextCurrentArrayElem]
              currentArray = currentArray[:]
              lastElementIndex = elementIndexDict[currentArray[len(currentArray) -1]] + 1
              for addLastElem in range(len(nums) - lastElementIndex):
                if len(currentArray ) < currentLength:
                  currentArray.append(nums[lastElementIndex])
                  arrayTemp = currentArray[:]
                  returnArray.append(arrayTemp)
                  currentLevel.append(arrayTemp)
                else:
                  currentArray[len(currentArray)-1] = nums[lastElementIndex + addLastElem]
                  arrayTemp = currentArray[:]
                  returnArray.append(arrayTemp)
                  currentLevel.append(arrayTemp)
        
          currentLength = currentLength + 1
          previousLevel = currentLevel
          currentLevel = []
          print(previousLevel)


        returnArray.append(nums)
        returnArray.append([])
          
        return returnArray
