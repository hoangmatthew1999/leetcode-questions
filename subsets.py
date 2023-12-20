class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        returnArray = [[]]
        returnArray = []
                

        currentLength = 3
        withoutLastElementArray = []
        firstElementIndex = 0
        for movingFirstIndex in range(len(nums) - firstElementIndex- 2):
          withoutLastElementArray = []
          for createArray in range(currentLength - 1):
            withoutLastElementArray.append(nums[firstElementIndex + createArray])
          firstElementIndex = firstElementIndex + 1
          lastElementIndex = firstElementIndex + currentLength - 2
          
          lastElementIndex = firstElementIndex + currentLength - 2
          for movingSecondIndex in range(len(nums) - lastElementIndex):
            for movingThirdIndex in range(len(nums) - lastElementIndex):
              if len(withoutLastElementArray) < currentLength:
                withoutLastElementArray.append(nums[lastElementIndex+movingThirdIndex])
                arrayTemp = withoutLastElementArray[:]
                returnArray.append(arrayTemp)
              else:
                wleaLastElement = len(withoutLastElementArray) - 1
                withoutLastElementArray[wleaLastElement]=nums[lastElementIndex+movingThirdIndex]
                arrayTemp = withoutLastElementArray[:]
                returnArray.append(arrayTemp)
            withoutLastElementArray.pop()
            lastElementIndex = lastElementIndex + 1
            withoutLastElementArray[len(withoutLastElementArray)-1] = nums[lastElementIndex - 1]
            
        
            
            
     


        return returnArray
        
    
