# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        traverseStack = []
        returnStack = []
        visitedBeforeDB = dict()
        while (root != None):
            traverseStack.append(root)
            visitedBeforeDB[root.val] = "1"
            root = root.left

        root = traverseStack[-1]
        # if root.val in visitedBeforeDB:
        #     returnStack.append(root.val)
        #     traverseStack.pop()
        #     root = traverseStack[-1]
        # elif root.left != None:
        #     traversalStack.append(root)
        #     visitedBeforeDB[root.val] = "1" 
        #     root = root.left
        # elif root.left == None:
        #     returnStack.append(root.val)
        #     visitedBeforeDB[root.val] = "1" 


        # if root.val in visitedBeforeDB:# 2
        #     returnStack.append(root.val)
        #     traverseStack.pop()
        # elif root.left != None:
        #     traversalStack.append(root)
        #     visitedBeforeDB[root.val] = "1" 
        #     root = root.left
        # elif root.left == None:
        #     returnStack.append(root.val)
        #     visitedBeforeDB[root.val] = "1" 
        # if root.right != None:
        #     root = root.right


     
        # if root.val in visitedBeforeDB:# 5
        #     returnStack.append(root.val)
        #     traverseStack.pop()
        # elif root.left != None:
        #     traverseStack.append(root)
        #     visitedBeforeDB[root.val] = "1" 
        #     if root.right != None:
        #         traverseStack.insert(-1, root.right)
        #         visitedBeforeDB[root.right.val] = "a"
        #     root = root.left
        # elif root.left == None:
        #     returnStack.append(root.val)
        #     visitedBeforeDB[root.val] = "1"

        
        # if root.val in visitedBeforeDB:# 6
        #     returnStack.append(root.val)
        #     traverseStack.pop()
        # elif root.left != None:
        #     traverseStack.append(root)
        #     visitedBeforeDB[root.val] = "1" 
        #     if root.right != None:
        #         traverseStack.insert(-1, root.right)
        #     root = root.left
        # elif root.left == None:
        #     returnStack.append(root.val)
        #     visitedBeforeDB[root.val] = "1"
        #     root = traverseStack[-1]
        

        # if root.val in visitedBeforeDB:# 7
        #     returnStack.append(root.val)
        #     traverseStack.pop()
        #     root = traverseStack[-1]
        # elif root.left == None:
        #     returnStack.append(root.val)
        #     visitedBeforeDB[root.val] = "visited"
        #     root = traverseStack[-1]
        # elif root.left != None:
        #     traverseStack.append(root)
        #     visitedBeforeDB[root.val] = "visited" 
        #     if root.right != None:
        #         traverseStack.insert(-1, root.right)
        #         visitedBeforeDB[root.right.val] = "visited"
        #     root = root.left

       
        # if root.val in visitedBeforeDB:# 7
        #     returnStack.append(root.val)
        #     traverseStack.pop()
        #     root = traverseStack[-1]
        # elif root.left == None:
        #     returnStack.append(root.val)
        #     visitedBeforeDB[root.val] = "visited"
        #     root = traverseStack[-1]
        # elif root.left != None:
        #     traverseStack.append(root)
        #     visitedBeforeDB[root.val] = "visited" 
        #     if root.right != None:
        #         traverseStack.insert(-1, root.right)
        #         visitedBeforeDB[root.right.val] = "visited"
        #     root = root.left
        
        # if root.val in visitedBeforeDB:# 1
        #     returnStack.append(root.val)
        #     traverseStack.pop()
        #     if root.right not in visitedBeforeDB:# solves problem of 1 node
        #             traverseStack.append(root.right)
        #     root = traverseStack[-1]
        # elif root.left == None:
        #     returnStack.append(root.val)
        #     visitedBeforeDB[root.val] = "visited"
        #     root = traverseStack[-1]
        # elif root.left != None:
        #     traverseStack.append(root)
        #     visitedBeforeDB[root.val] = "visited" 
        #     if root.right != None:
        #         traverseStack.insert(-1, root.right)
        #         visitedBeforeDB[root.right.val] = "visited"
        #     root = root.left
        
        # if root.val in visitedBeforeDB:# 3 revisiting parent or right node
        #     returnStack.append(root.val)
        #     traverseStack.pop()
        #     if root.right not in visitedBeforeDB:# solves problem of 1 node
        #             traverseStack.append(root.right)
        #     root = traverseStack[-1]
        # elif root.left == None:
        #     returnStack.append(root.val)
        #     visitedBeforeDB[root.val] = "a"
        #     if root.right != None:
        #         traverseStack.pop()
        #         root = root.right
        # elif root.left != None:
        #     traverseStack.append(root)
        #     visitedBeforeDB[root.val] = "a" 
        #     if root.right != None:
        #         traverseStack.insert(-1, root.right)
        #         visitedBeforeDB[root.right.val] = "a"
        #     root = root.left
        
       
        # if root.val in visitedBeforeDB:# 8
        #     returnStack.append(root.val)
        #     traverseStack.pop()
        #     if root.right not in visitedBeforeDB:# solves problem of 1 node
        #             traverseStack.append(root.right)
        #             root = traverseStack[-1]
        #     else:
        #         root = traverseStack[-1]
        # elif root.left == None:
        #     returnStack.append(root.val)
        #     visitedBeforeDB[root.val] = "a"
        #     if root.right != None:
        #         traverseStack.pop()
        #         traverseStack.append(root.right)
        #         root = traverseStack[-1]
        # elif root.left != None:
        #     traverseStack.append(root)
        #     visitedBeforeDB[root.val] = "a" 
        #     if root.right != None:
        #         traverseStack.insert(-1, root.right)
        #         visitedBeforeDB[root.right.val] = "a"
        #     root = root.left
        
     
        # if root.val in visitedBeforeDB:# 9 revisiting parent or right node
        #     returnStack.append(root.val)
        #     traverseStack.pop()
        #     if root.right not in visitedBeforeDB:# solves problem of 1 node
        #             traverseStack.append(root.right)
        #     root = traverseStack[-1]
        # elif root.left == None:
        #     returnStack.append(root.val)
        #     visitedBeforeDB[root.val] = "a"
        #     if root.right != None:
        #         traverseStack.pop()
        #         traverseStack.append(root.right)
        #         root = traverseStack[-1]
        #     else:
        #         root = traverseStack[-1]
        # elif root.left != None:
        #     traverseStack.append(root)
        #     visitedBeforeDB[root.val] = "a" 
        #     if root.right != None:
        #         traverseStack.insert(-1, root.right)
        #         visitedBeforeDB[root.right.val] = "a"
        #     root = root.left


        for i in range(8):
            print(root.val, "root")
            for a in range(len(traverseStack)):
                print(traverseStack[a].val)
            if root.val in visitedBeforeDB:# 8 revisiting parent or right node
                returnStack.append(root.val)
                traverseStack.pop()
                if root.right not in visitedBeforeDB and root.right != None:# solves problem of 1 node
                        root = root.right
                else:
                    root = traverseStack[-1]
            elif root.left == None:
                returnStack.append(root.val)
                visitedBeforeDB[root.val] = "a"
                if root.right != None:
                    traverseStack.append(root.right)
                    # traverseStack.pop()
                    root = traverseStack[-1]
                elif root.right == None:
                    root = traverseStack[-1]
            elif root.left != None:
                traverseStack.append(root)
                visitedBeforeDB[root.val] = "a" 
                if root.right != None:
                    traverseStack.insert(-1, root.right)
                    visitedBeforeDB[root.right.val] = "a"
                root = root.left

        
        
            

     
        
        
        


    



    

     
        

        
        
        

       

        

        return returnStack


          
        
        
        
        
        
        
        
