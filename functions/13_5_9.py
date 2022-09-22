def is_correct_bracket(text):
    counter = 0

    for i in range(len(txt)):
        if counter < 0:
            return False
        elif txt[i] == '(':
            counter += 1
        elif txt[i] == ')':
            counter -= 1

    if counter == 0:
        return True
    else:
        return False

txt = input()

print(is_correct_bracket(txt))

# The is_correct_bracket(text) function takes as an argument a non-empty 'text'
# string consisting of the characters '(' and ')' and returns True if the input
# string is a valid bracket sequence and False otherwise.

# A correct bracket sequence is a string consisting only of the characters
# '(' and ')', where each opening bracket has a matching closing bracket.