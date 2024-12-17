# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #balanced binary tree is easy
    #unbalanced tree might be hard

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        elif root.right == None and root.left == None:
            return [root.val]
        
        traversalStack = []
        returnStack = []
        visitedBeforeDB = dict()

        visitedRootLeft = "inialized value"
        if root.left == None:
            returnStack.append(root.val)
            root = root.right
            while root != None:
                visitedRootLeft = "visited root left"
                visitedBeforeDB[root.val] = "1"
                traversalStack.append(root)
                root = root.left
        elif root.left != None:
            visitedRootLeft = "visited root left"
            while(root != None):
                visitedBeforeDB[root.val] = "1"
                traversalStack.append(root)
                root = root.left
        

        if visitedRootLeft == "visited root left":
            root = traversalStack[-1]
        # for a in range(len(traversalStack)):
        #     print(traversalStack[a].val)
        
        while( len(traversalStack) > 0 ):
            a = 1
            if root.val in visitedBeforeDB and root.left == None and root.right == None:
                returnStack.append(root.val)
                traversalStack.pop()
                if len(traversalStack) >= 1:
                    root = traversalStack[-1]
            elif root.val in visitedBeforeDB and root.right != None:
                returnStack.append(root.val)
                traversalStack.pop()
                traversalStack.append(root.right)
                root = traversalStack[-1]
            elif root.val in visitedBeforeDB and root.left != None:# left has to be visited already 
                returnStack.append(root.val)
                traversalStack.pop()
                if len(traversalStack) >= 1:
                    root = traversalStack[-1]
            elif root.left == None and root.right != None:
                returnStack.append(root.val)
                traversalStack.pop()
                visitedBeforeDB[root.val] = "1"
                traversalStack.append(root.right)
                root = traversalStack[-1]
            elif root.left == None and root.right == None:
                returnStack.append(root.val)
                traversalStack.pop()
                if len(traversalStack) >= 1:
                    root = traversalStack[-1]
            elif root.right != None and root.left != None:
                traversalStack.append(root.left)
                visitedBeforeDB[root.val] = a
                visitedBeforeDB[root.right.val] = a
                root = traversalStack[-1]
            elif root.left == None:
                returnStack.append(root.val)
                visitedBeforeDB[root.val] = a
                if len(traversalStack) > 0:
                    traversalStack.pop()
                if len(traversalStack) > 0:
                    root = traversalStack[-1]
            elif root.left != None:
                traversalStack.append(root.left)
                visitedBeforeDB[root.val] = a
                root = traversalStack[-1]

            


        # while(len(traversalStack) != 0):
        #     if root.val in visitedBeforeDB:
        #         returnStack.append(root.val)
        #         traversalStack.pop()
        #         if len(traversalStack) >= 1:
        #             root = traversalStack
        #     else:
        #         traversalStack.pop()

        



        
                 



        

                

      
        return returnStack

        
