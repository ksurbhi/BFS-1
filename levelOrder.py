# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the tree is empty, return an empty list.
        if root is None:
            return []
        
        # Initialize a queue to keep track of nodes at each level.
        q = Queue()
        
        # List to store the final level order traversal result.
        result = []
        
        # Start with the root node.
        q.put(root)
        
        # Continue the loop until the queue is empty.
        while not q.empty():
            # Temporary list to store the values of nodes at the current level.
            temp = []
            
            # Get the number of nodes at the current level.
            qSize = q.qsize()
            
            # Iterate over all nodes at the current level.
            for i in range(qSize):
                # Get the front node from the queue.
                curr = q.get()
                
                # Add the value of the current node to the temporary list.
                temp.append(curr.val)
                
                # If the current node has a left child, add it to the queue.
                if curr.left is not None:
                    q.put(curr.left)
                
                # If the current node has a right child, add it to the queue.
                if curr.right is not None:
                    q.put(curr.right)
            
            # After processing all nodes at the current level, add the temporary list to the result.
            result.append(temp)
        
        # Return the final level order traversal result.
        return result


####### Method 2 using DFS ###### 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        self.result = []
        self.dfs(root,0)
        return self.result

    def dfs(self,root: Optional[TreeNode],lvl) -> None:
        if root == None:
            return
        if lvl == len(self.result):
            temp =[]
            temp.append(root.val)
            self.result.append(temp)
        else:
            self.result[lvl].append(root.val)
        self.dfs(root.left,lvl+1)
        self.dfs(root.right,lvl+1)

"""
The time complexity of both algorithms is O(n), 
where n is the number of nodes in the tree.
This is because each node is visited exactly once.

The space complexity is also O(n) because, in the worst case, 
the queue can contain all the leaf nodes.
This happens when the tree is a complete binary tree, 
and there are n/2 leaf nodes in the last level.
"""
