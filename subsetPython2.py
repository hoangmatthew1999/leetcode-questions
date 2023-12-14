class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        currentLength = 3
        returnArray = []
        withoutLastElementArray = []
        for i in range(currentLength - 1):
            withoutLastElementArray.append(nums[i])
        lastElementIndex = 2
        for iterations in range(len(nums) - lastElementIndex):
            if len(withoutLastElementArray) - 1 < lastElementIndex:
                withoutLastElementArray.append(nums[lastElementIndex+iterations])
            else:
                withoutLastElementArray[lastElementIndex] = nums[lastElementIndex+iterations]
                arrayTemp = withoutLastElementArray[:]
                returnArray.append(arrayTemp)

        return returnArray


        
