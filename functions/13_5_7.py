def is_palindrome(text):
    a = txt.split()
    s = ''.join(a).lower()

    arr = [s[i] for i in range(len(s)) if s[i].isalpha()]

    arr = ''.join(arr)

    if arr == arr[::-1]:
        return True
    else:
        return False

txt = input()

print(is_palindrome(txt))

# The is_palindrome(text) function takes the string text as an argument
# and returns True if the specified text is a palindrome, False otherwise.

# When checking, the program considers uppercase and lowercase letters
# to be the same, and also ignores spaces, as well as characters , . ! ? -.