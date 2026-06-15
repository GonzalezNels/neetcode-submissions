class Solution:
    def isPalindrome(self, s: str) -> bool:
     letters = []
     for char in s:
        if char.isalnum():
            letters.append(char.lower())

     new_word = ''.join(letters)

     left = 0
     right = len(new_word) - 1

     while left < right:
        if new_word[left] == new_word[right]:
            left += 1
            right -= 1
        else: 
            return False
     return True  