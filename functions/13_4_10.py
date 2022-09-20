def find_all(target, symbol):
    arr = []
    for i in range(len(s)):
        if s[i] == char:
            arr.append(i)
            s.replace(s[s.find(char)], '')

    return arr

s = input()
char = input()

print(find_all(s, char))

# The find_all(target, symbol) function takes two arguments, the string (target) and
# the symbol (symbol),and returns a list containing all the locations of that symbol in the string.