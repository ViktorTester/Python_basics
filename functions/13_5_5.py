def is_password_good(password):
    flag = False
    counter = 0
    upper_case = 0
    lower_case = 0

    if len(txt) >= 8:
        flag = True
    else:
        return flag

    if flag:
        for i in txt:
            if i.isdigit():
                counter +=1
        if counter > 0:
            for i in txt:
                if i.isupper():
                    upper_case +=1
        else:
            return False

        if upper_case > 0:
            for i in txt:
                if i.islower():
                    lower_case += 1

        if lower_case > 0:
            return True
        else:
            return False

txt = input()

print(is_password_good(txt))

# The is_password_good(password) function takes the string password as an
# argument and returns True if the password is strong, False otherwise.

# A password is strong if:

# its length is at least 8 characters;
# it contains at least one capital letter
# it contains at least one lowercase letter
# it contains at least one digit.