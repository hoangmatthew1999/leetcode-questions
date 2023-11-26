 def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        numberOfOuterLoops = len(matrix) - 1
        offset = 0
        # i = 0

        # if i == 0:
        #     temp = matrix[0][0+offset]
        #     matrix[0][0+offset] = matrix[len(matrix) - 1][0+offset]
        #     # print(matrix[0][0+offset])
        
        # offset = offset + 1
        # temp = matrix[0][0+offset]
        # if i == 0:
        #     temp = matrix[0][0+offset]
        #     matrix[0][0+offset] = matrix[len(matrix) - 1 - offset][0]
        #     print(matrix[0][0+offset])
        for i in range(numberOfOuterLoops):
            counter = 0
            for counter in range(4):
                if counter == 0:
                    temp = matrix[0][0+offset]
                    matrix[0][0+offset] = matrix[len(matrix) - 1 - offset][0]
                if counter == 1 :
                    secondTemp = matrix[0][len(matrix)-1]
                    matrix[0+offset][len(matrix)-1] =  temp
                    
            offset = offset + 1
        
