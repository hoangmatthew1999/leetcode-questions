# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        rootNode = root
        currentLevel = []
        nextLevel = []
        
        if root.left != None and root.right != None:
            print("hello")
        currentLevel.append(root)

        # if root.left not in nextLevel:
        #     nextLevel.append(root.left)
        # if root.right not in nextLevel:
        #     nextLevel.append(root.right)
        # root = 
        # currentLevel = nextLevel
        # nextLevel.pop(0)
        # print(nextLevel)
        # print(root.left)
        # print(root.right)
        while len(currentLevel) != None:
            
            # print(root.right)
            if root.left == None and root.right != None:# not complete
                root.left = root.right
                root.right = None
                break
                
            elif root.left != None and root.right == None:# not complete
                root.right = root.left
                root.left = None
                # print(root.right, "hello")
                # print(root.left,"esafa")
                break
            else:# does the regular swap
                temp = root.right
                root.right = root.left
                root.left = temp
            if root.left not in nextLevel:
                nextLevel.append(root.left)
            if root.right not in nextLevel:
                nextLevel.append(root.right)

            if len(currentLevel) <= 1:#moving down the tree to the next level
                currentLevel = nextLevel
                nextLevel = []
                root = currentLevel[0]
            else:# probably where most of the problems lie
                # print(currentLevel)
                currentLevel.remove(root)
                # print(currentLevel)
                root = currentLevel[0]
            # if root.left == None and root.right == None:
            #     break
        root = rootNode
        return root
