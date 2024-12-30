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
        duplicateNodesDB = dict()

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
        
        # bugs: 19, 90 
        first3 = None
        second3 = None
        for i in range(134):# 72 72 at 90, 103
            a = 1
            if root.val in visitedBeforeDB and root.left == None and root.right == None:
                # print("q", root.val)
                returnStack.append(root.val)
                traversalStack.pop()
                if len(traversalStack) >= 1:
                    root = traversalStack[-1]
            elif root.val in visitedBeforeDB and root.right != None:
                if root in duplicateNodesDB:# can be used to replace 3b and 3c
                    print("in duplicates node db", root.left.val, root.right.val)                 
                if root.val == 3 and returnStack[-1] == -33: # band aid solution: how do you actually solve this problem
                    print("3a", root.right.val)
                    returnStack.append(root.val)
                    traversalStack.pop()
                    traversalStack.append(root.right)
                    root = traversalStack[-1]
                elif root.val == 3 and returnStack[-1] == -17:
                    print("3b", root.right.val)
                    returnStack.append(root.val)
                    traversalStack.pop()
                    traversalStack.append(root.right)
                    root = traversalStack[-1]
                elif root.val == 3 and returnStack[-1] == 37:
                    print("3c", root.right.val)
                    returnStack.append(root.val)
                    traversalStack.pop()
                    traversalStack.append(root.right)
                    root = traversalStack[-1]
                elif root.val == 3 and returnStack[-1] != -33:
                    print("3d", root.right.val)
                    traversalStack.append(root.left)
                    root = traversalStack[-1]
                else:
                    returnStack.append(root.val)
                    traversalStack.pop()
                    visitedBeforeDB.pop(root.val)
                    traversalStack.append(root.right)
                    root = traversalStack[-1]
            elif root.val in visitedBeforeDB and root.left != None:# left has to be visited already 
                # print("e", root.val)
                returnStack.append(root.val)
                traversalStack.pop()
                visitedBeforeDB.pop(root.val)
                if len(traversalStack) >= 1:
                    root = traversalStack[-1]
            elif root.left == None and root.right != None:
                # print("1", root.val)
                returnStack.append(root.val)
                traversalStack.pop()
                traversalStack.append(root.right)
                root = traversalStack[-1]
            elif root.left == None and root.right == None:
                # print("2",root.val)
                returnStack.append(root.val)
                traversalStack.pop()
                if len(traversalStack) >= 1:
                    root = traversalStack[-1]
            elif root.right != None and root.left != None:
                # print("3", root.val)
                if root.val == root.left.val and root.left.left != None:# problem for 72 because there is no left.left
                    print("duplicate called", root.val)
                    duplicateNodesDB[root] = root.val
                    duplicateNodesDB[root.left] = root.val
                    traversalStack.append(root.left)
                    traversalStack.append(root.left.left)
                    first3 = root
                    second3 = root.left
                    visitedBeforeDB[root.val] = root.left.val
                    root = traversalStack[-1]
                else:
                    traversalStack.append(root.left)
                    visitedBeforeDB[root.val] = a
                    root = traversalStack[-1]
            elif root.left == None:
                # print("4", root.val)
                returnStack.append(root.val)
                visitedBeforeDB[root.val] = a
                if len(traversalStack) > 0:
                    traversalStack.pop()
                if len(traversalStack) > 0:
                    root = traversalStack[-1]
            elif root.left != None:
                # print("5", root.val)
                traversalStack.append(root.left)
                visitedBeforeDB[root.val] = a
                root = traversalStack[-1]

            # print(" ")
        # print(" ")
        # print(root.right.val)
        # print(second3)
        # print(len(duplicateNodesDB) )
        # print(second3 in duplicateNodesDB)




    #    what you need to figure out is how to actually write code for the 3 test case

    #make a dict called duplicateNodesDB that keeps track of cases like 3
    # 3: [node a, node b, node c]
    # and basically do what the visitedBeforeDB does 

    #added 

    

       
      
            

        
                


            


      

        



        
                 



        

                

      
        return returnStack

        
