def is_valid_password(password):
    a = psw.split(':')
    counter = 0

    flag1 = False
    flag2 = False
    flag3 = False

    if len(a) > 3:
        return False
    else:
        if a[0] == a[0][::-1]:
            flag1 = True

        for i in range(1, int(a[1]) + 1):
            if int(a[1]) % i == 0:
                counter +=1
        if counter == 2:
            flag2 = True

        if int(a[2]) % 2 == 0:
            flag3 = True

    return flag1 and flag2 and flag3

psw = input()

print(is_valid_password(psw))

# A valid bank password is a:b:c, where a, b, and c are natural numbers.
#
# the number 'a' must be a palindrome;
# the number 'b' must be simple;
# the number 'c' must be even.
#
# The is_valid_password(password) function takes the string password as an
# argument and returns True if the password is a valid bank password and False otherwise.