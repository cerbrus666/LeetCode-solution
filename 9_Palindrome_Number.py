class Solution:
    def isPalindrome(self, x: int) -> bool:
        indexing = str(x)
        if indexing[0] == indexing[len(indexing) - 1]:
            return True
        else:
            return False
