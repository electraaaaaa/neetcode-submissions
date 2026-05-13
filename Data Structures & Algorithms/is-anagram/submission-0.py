class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stack = []
        if len(s) != len(t):
            return False
        
        for val in s:
            stack.append(val)
        for val in t:
            if val in stack:
                stack.remove(val)
            else:
                return False
                
        return True