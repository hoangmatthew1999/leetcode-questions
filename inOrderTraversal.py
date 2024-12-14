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
        if root == None:
            return []
        elif root.right == None and root.left == None:
            return [root.val]
        
        visitedRootLeft = "not visited root left"
        if root.left == None:
            returnStack.append(root.val)# adding root
            root = root.right
            while root != None:
                if root.left != None:
                    visitedRootLeft = "visited root left"
                    traverseStack.append(root)
                    visitedBeforeDB[root.val] = "1"
                    root = root.left
                elif root.right != None:
                    traverseStack.append(root)
                    visitedBeforeDB[root.val] = "1"
                    root = root.right
                elif root.left == None and root.right == None:#leaf node
                    traverseStack.append(root)
                    visitedBeforeDB[root.val] = "1"
                    root = root.left
        elif root.left != None:
            visitedRootLeft = "visited root left"
            while (root != None):
                traverseStack.append(root)
                visitedBeforeDB[root.val] = "1"
                root = root.left

        # root = traverseStack[-1]
        if visitedRootLeft == "not visited root left":#special case where only has root.right
            while( len(traverseStack) > 0):
                root = traverseStack[0]
                returnStack.append(root.val)
                traverseStack.pop(0)
            return returnStack
        elif visitedRootLeft == "visited root left":
            root = traverseStack[-1]
        for a in range(len(traverseStack)):
            print(traverseStack[a].val)
        while( len(traverseStack) > 0):
            a = 0
            if root.val in visitedBeforeDB and root.right == None:
                returnStack.append(root.val)
                traverseStack.pop()
                if len(traverseStack) >= 1:
                    root = traverseStack[-1]
            elif root.val in visitedBeforeDB and root.right != None:
                returnStack.append(root.val)
                traverseStack.pop()
                traverseStack.append(root.right)
                root = traverseStack[-1]
            elif root.right != None and root.left != None:
                traverseStack.append(root.left)
                visitedBeforeDB[root.val] = a
                visitedBeforeDB[root.right.val] = a
                root = traverseStack[-1]
            elif root.right != None and root.left == None:
                returnStack.append(root.val)
                traverseStack.pop()
                visitedBeforeDB[root.val] = a
                traverseStack.append(root.right)
                root = traverseStack[-1]
            elif root.left == None:
                returnStack.append(root.val)
                visitedBeforeDB[root.val] = a
                if len(traverseStack) > 0:
                    traverseStack.pop()
                if len(traverseStack) > 0:
                    root = traverseStack[-1]
            elif root.left != None:
                traverseStack.append(root.left)
                visitedBeforeDB[root.val] = a
                root = traverseStack[-1]

            
       

            

        
        # for i in range(11):
        #     if root.val in visitedBeforeDB:# 8 revisiting parent or right node
        #         returnStack.append(root.val)
        #         traverseStack.pop()
        #         if root.right not in visitedBeforeDB and root.right != None:# solves problem of 1 node
        #                 root = root.right
        #         elif len(traverseStack) > 0:
        #             root = traverseStack[-1]
        #     elif root.left == None:
        #         returnStack.append(root.val)
        #         visitedBeforeDB[root.val] = "a"
        #         if root.right != None:# the problem line
        #             root = root.right
        #             # traverseStack.append(root.right)
        #             # # traverseStack.pop()
        #             # root = traverseStack[-1]
        #         elif root.right == None:
        #             root = traverseStack[-1]
        #     elif root.left != None:
        #         traverseStack.append(root)
        #         visitedBeforeDB[root.val] = "a" 
        #         if root.right != None:
        #             traverseStack.insert(-1, root.right)#probably the problem
        #             visitedBeforeDB[root.right.val] = "a"
        #         root = root.left

            

        '''
        to do list
        problem with 3 node 
        double insert problem 
        '''
        
        
        

        

        
        
            

     
        
        
        


    



    

     
        

        
        
        

       

        

        return returnStack


          
        
        
        
        
        
        
        
