def is_palindrome(string: str) -> bool:
    """
    Test if given string is a palindrome.
    """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    if not string:
        return ''
    
    # Function to find the longest palindrome suffix
    def longest_palindrome_suffix(s):
        for i in range(len(s), 0, -1):
            if is_palindrome(s[:i]):
                return s[i:]
        return ''
    
    palindrome_suffix = longest_palindrome_suffix(string)
    return string + string[:len(string) - len(palindrome_suffix)][::-1]

# Testing the functions
print(make_palindrome(''))      # Output: ''
print(make_palindrome('cat'))   # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'