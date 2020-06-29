"""
Objective
The goal of this exercise is to validate a binary search tree (BST).

A BST maintains the property that:
  The value of the key of the left-sub tree is less than the value of its parent (root) node's key
  The value of the key of the right-sub tree is greater than or equal to the value of its parent (root) node's key

Algorithm
Step 1: Establish your data structures
  Class Node {
    value
    left
    right
  }

Step 2: Construct validation based off n.value
Class Node {
    value
    left
    right
  }

  isValid (n, low, high) {
  if (!n) return True
  n.val > low AND
  n.val < high AND
  isValid(n.left, low, n.val) AND
  isValid(n.right, n.val, high )
  }

Step 3: Determine the Time-Space Complexity:
    We are traversing through all of the nodes in one circuit; so in terms of time:
    Time: O(n) -- Linear

    The space is proportional to the recursive stack, which means that the composition would also be: O(n) -- Linear, to complement the time complexity.
"""

# Define Class
class Node(object):
  # Construct a helper function - pass low and high values as the parameters
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution(object):
  def _isValidBSTHelper(self, n, low, high):
    # Create a base case:
    if not n:
      return True
    val = n.val
    if ((val > low and val < high) and
        self._isValidBSTHelper(n.left, low, n.val) and
        self._isValidBSTHelper(n.right, n.val, high)):
        return True
    return False

  def isValidBST(self, n):
    return self._isValidBSTHelper(n, float('-inf'), float('inf'))

# Test Functionality:
#   5
#  / \
# 4   7
node = Node(5)
node.left = Node(4)
node.right = Node(7)
print(Solution().isValidBST(node))

#   5
#  / \
# 4   7
#    /
#   2
node = Node(5)
node.left = Node(4)
node.right = Node(7)
node.right.left = Node(2)
print(Solution().isValidBST(node))
# False