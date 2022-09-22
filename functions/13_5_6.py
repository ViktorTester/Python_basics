def is_one_away(word1, word2):
    counter = 0
    if len(txt1) == len(txt2):
        for i in range(len(txt1)):
            if txt1[i] == txt2[i]:
                counter +=1
    if counter == len(txt1) - 1:
        return True
    else:
        return False

txt1 = input()
txt2 = input()

print(is_one_away(txt1, txt2))

# The is_one_away(word1, word2) function takes two words word1
# and word2 as argumentsand returns True if the words are the same
# length and differ by exactly 1 character, and False otherwise.