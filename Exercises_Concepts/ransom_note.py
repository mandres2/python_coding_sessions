"""
Objective: Write a function that returns a true or false value (boolean) given a magazine and a word that contain a particular array set of letters

Algorithm:



Time-Space Complexity:
Time: O(n) + O(m)
Space: O(1)

"""
# import a letter hashmap which is defaultdict; By default all values will be intialized to: 0
from collections import defaultdict

class Solution(object):
    # Create a function: canSpell that takes in 3 paramaters: self, magazine and note
    def canSpell(self, magazine, note):
        letters = defaultdict(int)
        # For each character in the magazine, let the letters at the character be plus-equals 1 -- so by default it is 0
        for c in magazine:
            letters[c] += 1
        # Go through all the letters in the note
        for c in note:
            # If the letters in the characters are less than or equal to 0 return false because we can not match the values
            if letters[c] <= 0:
                return False
            # Otherwise decrement the value by 1
            letters[c] -= 1

        return True


print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'bed'))
# True

print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'cat'))
# False
