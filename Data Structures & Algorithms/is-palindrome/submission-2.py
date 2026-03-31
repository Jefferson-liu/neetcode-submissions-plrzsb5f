class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for char in s:
            if char.isalnum():
                if not char.isdigit():
                    string  += char.lower()
                else:
                    string += char
        print(string)

        for i in range(len(string)):
            if i > len(string) - i - 1:
                return True
            if string[i] != string[len(string) - i - 1]:
                return False
        return True