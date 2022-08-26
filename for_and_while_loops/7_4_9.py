word = input()

while word != "END" and word != "end":
    print(word)
    word = input()

# or:

a = input()

while a not in ('end', 'END'):
    print(a)
    a = input()

# The input to the program is a sequence of words, each word on a separate line.
# The end of the sequence is the word "end" or "END".
# The program outputs the members of the given sequence.