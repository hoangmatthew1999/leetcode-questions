# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        elemVisitedCounter = 0
        traverseStack = []
        nodesDB = dict()

        if k == 1:
            while root.left != None:
                root = root.left
            return root.val
        if root.left == None:
            while root.right != None:
                elemVisitedCounter = elemVisitedCounter + 1
                root = root.right
                if elemVisitedCounter== k:
                    return root.val
            if root.right == None:# adding last value 
                elemVisitedCounter = elemVisitedCounter + 1
                if elemVisitedCounter == k:
                    return root.val

        while root.left != None:
            traverseStack.append(root)
            nodesDB[root.val] = 0
            root = root.left
        traverseStack.append(root)
        nodesDB[root.val] = 0

        
        # print(root.val)
        # print(" ")
        # if elemVisitedCounter == k:
        #     return root.val
        # if root.val not in nodesDB:
        #     nodesDB[root.val] = elemVisitedCounter
        # if root.left != None:
        #     root = root.left
        #     if root.val in nodesDB:
        #         root = traverseStack[-1]
        #     else:
        #         print("need to write else case ")
        # if root.right != None:
        #     traverseStack.append(root.right)
        #     traverseStack.pop(-2)
        #     root = traverseStack[-1]
        # elif root.right == None:
        #     traverseStack.pop(-1)
        #     root = traverseStack[-1]
        # elemVisitedCounter = elemVisitedCounter + 1

        # print(root.val)
        # print(" ")
        # if elemVisitedCounter == k:
        #     return root.val
        # if root.val not in nodesDB:
        #     nodesDB[root.val] = k
        # if root.left.val in nodesDB:# you have visited the left node
        #     traverseStack.append(root.right)
        #     traverseStack.pop(-2)
        #     root = traverseStack[-1]
        # elemVisitedCounter = elemVisitedCounter + 1

        # print(root.val)
        # print(" ")
        # if elemVisitedCounter == k:
        #     return root.val
        # if root.val not in nodesDB:
        #     nodesDB[root.val] = k
        # if root.left == None and root.right != None:
        #     traverseStack.append(root.right)
        #     traverseStack.pop(-2)
        #     root = traverseStack[-1]
        #     elemVisitedCounter = elemVisitedCounter + 1
        # elif root.left.val in nodesDB:
        #     traverseStack.append(root.right)
        #     traverseStack.pop(-2)
        #     root = traverseStack[-1]
        #     elemVisitedCounter = elemVisitedCounter + 1
        
        # print(root.val)
        # print(" ")
        # if elemVisitedCounter == k:
        #     return root.val
        # if root.val not in nodesDB:
        #     nodesDB[root.val] = k
        # if root.left == None and root.right != None:
        #     traverseStack.append(root.right)
        #     traverseStack.pop(-2)
        #     root = traverseStack[-1]
        #     elemVisitedCounter = elemVisitedCounter + 1
        # elif root.left.val in nodesDB:
        #     traverseStack.append(root.right)
        #     traverseStack.pop(-2)
        #     root = traverseStack[-1]
        #     elemVisitedCounter = elemVisitedCounter + 1
        # elif root.left.val not in nodesDB:
        #     traverseStack.append(root.left)
        #     root = traverseStack[-1]

        # print(root.val)
        # print(" ")
        # if elemVisitedCounter == k:
        #     return root.val
        # if root.val not in nodesDB:
        #     nodesDB[root.val] = k
        # if root.left == None and root.right != None:
        #     traverseStack.append(root.right)
        #     traverseStack.pop(-2)
        #     root = traverseStack[-1]
        #     elemVisitedCounter = elemVisitedCounter + 1
        # elif root.left == None and root.right == None:
        #     traverseStack.pop(-1)
        #     elemVisitedCounter = elemVisitedCounter + 1
        #     root = traverseStack[-1]
        # elif root.left.val in nodesDB:
        #     traverseStack.append(root.right)
        #     traverseStack.pop(-2)
        #     root = traverseStack[-1]
        #     elemVisitedCounter = elemVisitedCounter + 1
        # elif root.left.val not in nodesDB:
        #     traverseStack.append(root.left)
        #     root = traverseStack[-1]
        
        for i in range(6):
            print(root.val)
            print(" ")
            if elemVisitedCounter == k:
                return root.val
            if root.val not in nodesDB:
                nodesDB[root.val] = k
            if root.left == None and root.right != None:
                traverseStack.append(root.right)
                traverseStack.pop(-2)
                root = traverseStack[-1]
                elemVisitedCounter = elemVisitedCounter + 1
            elif root.left == None and root.right == None:
                traverseStack.pop(-1)
                elemVisitedCounter = elemVisitedCounter + 1
                root = traverseStack[-1]
            elif root.left.val in nodesDB:
                traverseStack.append(root.right)
                traverseStack.pop(-2)
                root = traverseStack[-1]
                elemVisitedCounter = elemVisitedCounter + 1
            elif root.left.val not in nodesDB:
                traverseStack.append(root.left)
                root = traverseStack[-1]
            




        

        
            
    

        
        # print(root.val)
        # elemVisitedCounter = elemVisitedCounter + 1
        # if elemVisitedCounter == k:
        #     return root.val
        # if root.val not in nodesDB:
        #     nodesDB[root.val] = 0
        # if root.left != None:
        #     root = root.left
        #     if root.val in nodesDB:
        #         print("ewr")
        #         root = traverseStack[-1]
        #     else:
        #         print("need to traverse")
        #     #else need to add later
        # if root.right != None:
        #     traverseStack.append(root.right)
        #     traverseStack.pop(-2)
        #     root = traverseStack[-1]
        # else:
        #     traverseStack.pop(-1)
        #     root = traverseStack[-1]
        # print(" ")

        # print(root.val)
        # elemVisitedCounter = elemVisitedCounter + 1
        # if elemVisitedCounter == k:
        #     return root.val
        # if root.val not in nodesDB:
        #     nodesDB[root.val] = 0
        # if root.left != None:
        #     root = root.left
        #     if root.val in nodesDB:
        #         print("ewr")
        #         root = traverseStack[-1]
        #     else:
        #         print("need to traverse")
        #     #else need to add later
        # if root.right != None:
        #     traverseStack.append(root.right)
        #     traverseStack.pop(-2)
        #     root = traverseStack[-1]
        # else:
        #     traverseStack.pop(-1)
        #     root = traverseStack[-1]
        # print(" ")

        # print(root.val)
        # elemVisitedCounter = elemVisitedCounter + 1
        # if elemVisitedCounter == k:
        #     return root.val
        # if root.val not in nodesDB:
        #     nodesDB[root.val] = 0
        # if root.left != None and root.right != None:
        #     if root.right.val not in nodesDB:
        #         nodesDB[root.right.val] = 0
        #         traverseStack.append(root.right)
        #     if root.left.val not in nodesDB:
        #         nodesDB[root.left.val] = 0
        #         traverseStack.append(root.left)
        #     traverseStack.pop(-3)
        #     root = traverseStack[-1]
        # if root.left != None and root.right == None:
        #     if root.left.val in nodesDB:
        #         root = traverseStack[-1]
        #     elif root.left.val not in nodesDB:
        #         nodesDB[root.left.val] = 0
        #         traverseStack.append(root.left)
        # #     #else need to add later
        # if root.right != None and root.left == None:
        #     traverseStack.append(root.right)
        #     traverseStack.pop(-2)
        #     root = traverseStack[-1]
        # print(" ")
        # # else:
        # #     traverseStack.pop(-1)
        # #     root = traverseStack[-1]
        # # print(" ")

        # print(root.val)
        # elemVisitedCounter = elemVisitedCounter + 1
        # if elemVisitedCounter == k:
        #     return root.val
        # if root.val not in nodesDB:
        #     nodesDB[root.val] = 0
        # if root.left != None and root.right != None:
        #     if root.right.val not in nodesDB:
        #         nodesDB[root.right.val] = 0
        #         traverseStack.append(root.right)
        #     if root.left.val not in nodesDB:
        #         nodesDB[root.left.val] = 0
        #         traverseStack.append(root.left)
        #     traverseStack.pop(-3)
        #     root = traverseStack[-1]
        # if root.left != None and root.right == None:
        #     if root.left.val in nodesDB:
        #         root = traverseStack[-1]
        #     elif root.left.val not in nodesDB:
        #         nodesDB[root.left.val] = 0
        #         traverseStack.append(root.left)
        # #     #else need to add later
        # if root.right != None and root.left == None:
        #     traverseStack.append(root.right)
        #     traverseStack.pop(-2)
        #     root = traverseStack[-1]
        # if root.right == None and root.left == None:
        #     traverseStack.pop(-1)
        #     root = traverseStack[-1]
        # print(" ")

        # rightPriority = []
        # leftPriority = []
        # print(root.val)
        # elemVisitedCounter = elemVisitedCounter + 1
        # if elemVisitedCounter == k:
        #     return root.val
        # if root.val not in nodesDB:
        #     nodesDB[root.val] = elemVisitedCounter
        # if root.left != None and root.right != None:
        #     if root.right.val not in nodesDB: #not the right time to add to 
        #         nodesDB[root.right.val] = elemVisitedCounter
        #         traverseStack.append(root.right)
        #         rightPriority.append(root.right.val)
            
        #     while root.left != None:
        #         if root.left.val not in nodesDB:
        #             nodesDB[root.left.val] = elemVisitedCounter
        #             traverseStack.append(root.left)
        #             leftPriority.append(root.val)
        #             root = traverseStack[-1]
        # #     traverseStack.pop(-3)
        #     # root = traverseStack[-1]
        # elif root.left != None and root.right == None:
        #     if root.left.val in nodesDB:
        #         root = traverseStack[-1]
        #     elif root.left.val not in nodesDB:
        #         nodesDB[root.left.val] = 0
        #         traverseStack.append(root.left)
        # # #     #else need to add later
        # elif root.right != None and root.left == None:
        #     traverseStack.append(root.right)
        #     traverseStack.pop(-2)
        #     root = traverseStack[-1]
        # elif root.right == None and root.left == None:
        #     traverseStack.pop(-1)
        #     root = traverseStack[-1]
        # print(" ")


        


        
            


            
       

        # while len(traverseStack) != 0:
        #     elemVisitedCounter = elemVisitedCounter + 1
        #     if elemVisitedCounter == k:
        #         return root.val
        #     if root.val not in nodesDB:
        #         nodesDB[root.val] = 0
        #         print("added", root.val)
        #     if root.right != None:
        #         traverseStack.append(root.right)
        #         traverseStack.pop(-2)
        #         root = traverseStack[-1]
        #     else:
        #         traverseStack.pop(-1)
        #         root = traverseStack[-1]

        for elems in traverseStack:
            print(elems.val)
        
        
        


        return elemVisitedCounter
        

        

        
        
        
