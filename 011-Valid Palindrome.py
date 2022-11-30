# Solution 1 utilizing inbuilt Python function to check alphanumeric value
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_format = []

        for char in s:
            if char.isalnum():
                s_format.append(char.lower())
            else:
                continue
        
        for i in range(len(s_format)):
            if s_format[i] != s_format[-1-i]:
                return False
        
        return True

# Solution 2 which is more language agnostic
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Using moving pointers instead of hashmap, memory efficient
        l, r = 0, len(s)-1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1

        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
