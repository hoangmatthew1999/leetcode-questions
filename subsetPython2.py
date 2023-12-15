 currentLength = 3
        returnArray = []
        withoutLastElementArray = []
        # for i in range(currentLength - 1):
        #     withoutLastElementArray.append(nums[i])
        # lastElementIndex = 2
        # for iterations in range(len(nums) - lastElementIndex):
        #     if len(withoutLastElementArray) - 1 < lastElementIndex:
        #         withoutLastElementArray.append(nums[lastElementIndex+iterations])
        #         arrayTemp = withoutLastElementArray[:]
        #         returnArray.append(arrayTemp)
        #     else:
        #         withoutLastElementArray[len(withoutLastElementArray)-1] = nums[lastElementIndex+iterations]
        #         arrayTemp = withoutLastElementArray[:]
        #         returnArray.append(arrayTemp)

        # withoutLastElementArray.pop()
        # withoutLastElementArray.pop()
        # lastElementIndex = 3
        # withoutLastElementArray.append(nums[lastElementIndex-1])
        # for i in range(len(nums) - lastElementIndex):
        #     # withoutLastElementArray[lastElementIndex-1] = nums[lastElementIndex+i]
        #     if len(withoutLastElementArray)  < lastElementIndex:
        #         withoutLastElementArray.append(nums[lastElementIndex+i])
        #         arrayTemp = withoutLastElementArray[:]
        #         returnArray.append(arrayTemp)
        #     else:
        #         withoutLastElementArray[len(withoutLastElementArray)-1] = nums[lastElementIndex+i]
        #         arrayTemp = withoutLastElementArray[:]
        #         returnArray.append(arrayTemp)
                
        lastElementIndex = 2
        for i in range(currentLength - 1):
            withoutLastElementArray.append(nums[i])


        for j in range(len(nums) - lastElementIndex):
          for i in range(len(nums) - lastElementIndex):
            if len(withoutLastElementArray) < currentLength:# if the length of WLE is 2 then append so = 3
              withoutLastElementArray.append(nums[lastElementIndex+i])
              print(withoutLastElementArray)
              arrayTemp = withoutLastElementArray[:]
              returnArray.append(arrayTemp)
            else:
              withoutLastElementArray[len(withoutLastElementArray)-1] = nums[lastElementIndex+i]
              arrayTemp = withoutLastElementArray[:]
              returnArray.append(arrayTemp)
          
          lastElementIndex = lastElementIndex + 1
          withoutLastElementArray.pop()
          withoutLastElementArray[len(withoutLastElementArray)-1] = nums[lastElementIndex-1]

        print(withoutLastElementArray)


          






            

        

        return returnArray
