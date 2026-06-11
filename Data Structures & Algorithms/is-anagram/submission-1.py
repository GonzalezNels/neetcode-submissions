class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = sorted(s)
        word2 = sorted(t)
        
        return word1 == word2