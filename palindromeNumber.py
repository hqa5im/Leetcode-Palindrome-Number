class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        forward = x
        backward = x[::-1]
        if forward == backward:
            return True
        else:
            return False
