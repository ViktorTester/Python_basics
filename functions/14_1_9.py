def is_magic(date):
    arr = date.split('.')

    for i in range(len(arr)):
        arr[i] = int(arr[i])

    if arr[0] * arr[1] == arr[2] % 100:
        return True
    else:
        return False


date = input()

print(is_magic(date))

# The magical date is the date when the day multiplied by the month
# equals the number formed by the last two digits of the year.

# The is_magic(date) function takes a string representation of a valid date
# as an argument and returns True if the date is magical and False otherwise.
