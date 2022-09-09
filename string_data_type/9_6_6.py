a, s = int(input()), input()

for i in range(len(s)):
    if ord(s[i]) - a < 97:
        print(chr(122 - (96 - ord(s[i]) + a)), end='')
    else:
        print(chr(ord(s[i]) - a), end='')

# The input is a number (shift) and a string
# (an encrypted message using the Caesar encryption method).
# The program displays the decrypted message.

