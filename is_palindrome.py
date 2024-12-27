import string

def is_palindrome(s: str) -> bool:
    # Preprocess the string
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    reversed = cleaned[::-1]
    
    if reversed != cleaned:
        print(f"{cleaned} -> {reversed}")
        return False
    else:
        print(f"{cleaned} -> {reversed}")
        return True  

# Test case
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("noon"))                           # True
print(is_palindrome("hello"))                          # False
print(is_palindrome("A dog: a big one or 2050 is coming!*")) # False