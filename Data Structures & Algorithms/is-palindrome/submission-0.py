class Solution:
    def isPalindrome(self, s: str) -> bool:
        # test "tat"
        new_string = ""
        for char in s:
            if char.isalnum():
                new_string += char.lower()

        half_length = len(new_string)//2
        for i in range(half_length):
            if new_string[i] != new_string[len(new_string) - 1 - i]:
                return False
        return True