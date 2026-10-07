class Solution(object):
    def isPalindrome(self, x):
        original = x
        rev = 0

        if x < 0:
            return False

        while x > 0:
            num = x % 10
            rev = rev * 10 + num
            x //= 10

        return rev == original