"""
https://leetcode.com/problems/binary-tree-right-side-view/
199. Binary Tree Right Side View
Medium

Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.
https://assets.leetcode.com/uploads/2021/02/14/tree.jpg

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []
 

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
from logging import root
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# build incomplete binary tree
def buildTree(list_item):
    if not list_item:
        return None

    root = TreeNode(list_item.pop(0))
    queueTree = [root]
    while list_item:
        left_val = list_item.pop(0) if list_item else None
        right_val = list_item.pop(0) if list_item else None
        current_node = queueTree.pop(0)
        if left_val:
            left_node = TreeNode(val=left_val)
            current_node.left = left_node
            queueTree.append(left_node)
        if right_val:
            right_node = TreeNode(val=right_val)
            current_node.right = right_node
            queueTree.append(right_node)
    return root

def bfs(root: TreeNode):
    if root == None:
        print("No tree available!")
        return
    queue = [root]
    while queue:
        current_node = queue.pop(0)
        if current_node is not None:
            left_val = current_node.left.val if current_node.left is not None else None
            right_val = current_node.right.val if current_node.right is not None else None
            print(current_node.val, "->", left_val, right_val)
            queue.append(current_node.left)
            queue.append(current_node.right)
        else:
            print(current_node)

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [root]
        right_view = []
        while queue:
            queue_size = len(queue)
            for i in range(queue_size):
                node = queue.pop(0)
                if i == queue_size - 1:
                    right_view.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return right_view



array_item = [1,2,3,None,5,None,4,6,7,None,None,8,None]

tree = buildTree(list_item=array_item)
x = Solution().rightSideView(root=tree)
print(x)