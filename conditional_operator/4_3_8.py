a = int(input())
b = int(input())
c = input()

if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/" and b > 0:
    print(a / b)
elif c == "/" and b == 0:
    print("You can't divide by zero!")
else:
    print("Invalid operation")

# A program that reads two integers and a string from the keyboard.
# If this string represents one of the four mathematical operations (+, -, *, /),
# then print the result of applying this operation to the numbers entered earlier,
# otherwise print "Invalid operation".
# If the user wants to divide by zero, display the text "You can't divide by zero!".
