class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1 - Clean the string - Remove all non-alphanumeric characters and convert to lowercase
        cleaned_string = ""
        for char in s:
            if(char.isalnum()):
                cleaned_string += char.lower()
        # Step 2 - Check if the cleaned string is a palindrome 
        return cleaned_string == cleaned_string[::-1] 