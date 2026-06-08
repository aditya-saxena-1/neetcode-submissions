class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        
        for char in t:
            if char in d:
                d[char] -= 1
            else:
                return False
                break
            
        for i in d:
            if d[i] == 0:
                continue
            else:
                return False
                break
        return True