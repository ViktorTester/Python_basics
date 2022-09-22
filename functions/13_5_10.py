def convert_to_python_case(text):
    arr = txt[0]

    for i in range(1, len(txt)):
        if txt[i].islower():
            arr += txt[i]
        elif txt[i].isdigit():
            arr += txt[i]
        elif txt[i].isupper():
            arr += ' ' + txt[i]

    arr = arr.split()

    return '_'.join(arr).lower()

txt = input()

print(convert_to_python_case(txt))

# The convert_to_python_case(text) function takes a camel case
# string as an argument and converts it to snake case.