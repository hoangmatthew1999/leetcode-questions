# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def finalFunction():
         # while len(traverseStack) != 0:
        #     if elemVisitedCounter >= k:
        #         return root.val
        #     if root.val not in nodesDB:
        #         nodesDB[root.val] = k
        #     if root.left == None and root.right != None:
        #         traverseStack.append(root.right)
        #         traverseStack.pop(-2)
        #         root = traverseStack[-1]
        #         elemVisitedCounter = elemVisitedCounter + 1
        #     elif root.left == None and root.right == None:
        #         traverseStack.pop(-1)
        #         elemVisitedCounter = elemVisitedCounter + 1
        #         root = traverseStack[-1]
        #     elif root.left.val in nodesDB:
        #         if root.right == None:
        #             traverseStack.pop(-1)
        #             root = traverseStack[-1]
        #             elemVisitedCounter = elemVisitedCounter + 1
        #         if root.right != None and root.right.left == None:
        #             traverseStack.append(root.right)
        #             traverseStack.pop(-2)
        #             root = traverseStack[-1]
        #             elemVisitedCounter = elemVisitedCounter + 1
        #         elif root.right != None and root.right.left != None:
        #             traverseStack.append(root.right)
        #             traverseStack.pop(-2)
        #             root = traverseStack[-1]
        #     elif root.left.val not in nodesDB:
        #         while root.left != None:
        #                 root = root.left
        #                 traverseStack.append(root)
        #         root = traverseStack[-1]

        # print(elemVisitedCounter, "k")
        # print(" ")
        # for elems in traverseStack:
        #     print(elems.val)
        
        # return root.val
        return 1

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        elemVisitedCounter = 0
        traverseStack = []
        nodesDB = dict()

        if k == 1:
            while root.left != None:
                root = root.left
            return root.val
        if root.left == None:
            traverseStack.append(root.right)
            nodesDB[root.val] = elemVisitedCounter
            elemVisitedCounter = elemVisitedCounter + 1
            if elemVisitedCounter == k:
                return root.val
            root = traverseStack[-1]

            if root.left != None:
                while root.left != None:
                    traverseStack.append(root.left)
                    nodesDB[root.val] = elemVisitedCounter
                    root = root.left
                # traverseStack.append(root)
                # nodesDB[root.val] = 0

            # while root.right != None:
            #     elemVisitedCounter = elemVisitedCounter + 1
            #     root = root.right
            #     if elemVisitedCounter== k:
            #         return root.val
            # if root.right == None:# adding last value 
            #     elemVisitedCounter = elemVisitedCounter + 1
            #     if elemVisitedCounter == k:
            #         return root.val
        elif root.left != None:
            while root.left != None:
                traverseStack.append(root)
                nodesDB[root.val] = 0
                root = root.left
            traverseStack.append(root)
            nodesDB[root.val] = 0
        



        
        while len(traverseStack) != 0:
            print(elemVisitedCounter, "k")
            print(root.val, "root")
            if elemVisitedCounter == k:
                return root.val
            if root.val not in nodesDB:
                nodesDB[root.val] = k
            if root.left == None and root.right != None:
                traverseStack.append(root.right)
                traverseStack.pop(-2)
                elemVisitedCounter = elemVisitedCounter + 1
                if elemVisitedCounter == k:
                    return root.val
                root = traverseStack[-1]
            elif root.left == None and root.right == None:
                traverseStack.pop(-1)
                elemVisitedCounter = elemVisitedCounter + 1
                if elemVisitedCounter == k:
                    return root.val
                root = traverseStack[-1]
            elif root.left.val in nodesDB:
                if root.right == None:
                    traverseStack.pop(-1)
                    elemVisitedCounter = elemVisitedCounter + 1
                    if elemVisitedCounter == k:
                        return root.val
                    root = traverseStack[-1]
                elif root.right != None:
                    traverseStack.append(root.right)
                    elemVisitedCounter = elemVisitedCounter + 1
                    traverseStack.pop(-2)
                    if elemVisitedCounter == k:
                        return root.val
                    root = traverseStack[-1]
                # elif root.right != None and root.right.left != None:
                #     print("the 4 node goes here and need to increment somehow")
                    
                #     traverseStack.append(root.right)
                #     traverseStack.pop(-2)
                #     root = traverseStack[-1]
            elif root.left.val not in nodesDB:
                while root.left != None:
                        root = root.left
                        traverseStack.append(root)
                root = traverseStack[-1]
            
            for elems in traverseStack:
                print(elems.val)
        
            print(elemVisitedCounter, "k")
            print(" ")

        # for b in range(10):
        #     print(elemVisitedCounter, "k")
        #     print(root.val, "root")
        #     if elemVisitedCounter == k:
        #         return root.val
        #     if root.val not in nodesDB:
        #         nodesDB[root.val] = k
        #     if root.left == None and root.right != None:
        #         traverseStack.append(root.right)
        #         traverseStack.pop(-2)
        #         elemVisitedCounter = elemVisitedCounter + 1
        #         if elemVisitedCounter == k:
        #             return root.val
        #         root = traverseStack[-1]
        #     elif root.left == None and root.right == None:
        #         traverseStack.pop(-1)
        #         elemVisitedCounter = elemVisitedCounter + 1
        #         if elemVisitedCounter == k:
        #             return root.val
        #         root = traverseStack[-1]
        #     elif root.left.val in nodesDB:
        #         if root.right == None:
        #             traverseStack.pop(-1)
        #             elemVisitedCounter = elemVisitedCounter + 1
        #             if elemVisitedCounter == k:
        #                 return root.val
        #             root = traverseStack[-1]
        #         elif root.right != None:
        #             traverseStack.append(root.right)
        #             elemVisitedCounter = elemVisitedCounter + 1
        #             traverseStack.pop(-2)
        #             if elemVisitedCounter == k:
        #                 return root.val
        #             root = traverseStack[-1]
        #         # elif root.right != None and root.right.left != None:
        #         #     print("the 4 node goes here and need to increment somehow")
                    
        #         #     traverseStack.append(root.right)
        #         #     traverseStack.pop(-2)
        #         #     root = traverseStack[-1]
        #     elif root.left.val not in nodesDB:
        #         while root.left != None:
        #                 root = root.left
        #                 traverseStack.append(root)
        #         root = traverseStack[-1]
            
        #     for elems in traverseStack:
        #         print(elems.val)
        
        #     print(elemVisitedCounter, "k")
        #     print(" ")




       
        
        
           
            
            
            

        

        
        
            
        
    
        

    
        
        return -1

    
        
       
    

            


      

        

        
        


        
        

        

        
        
        
