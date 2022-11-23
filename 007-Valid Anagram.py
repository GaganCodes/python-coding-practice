class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Utilizing python's inbuilt methods, but logic remains same
        if (sorted(s.strip()) == sorted(t.strip())):
            return True
        else:
            return False
