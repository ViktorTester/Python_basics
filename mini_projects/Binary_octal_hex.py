def main():
    a = int(input("Enter you number please\n"))
    print("Binary -", bin(a)[2:])
    print("Octal - ", oct(a)[2:])
    print("Hex -", hex(a).upper()[2:])

    answer = input("Once more? (Yes/No)\n").lower()
    one_more_time(answer)


def one_more_time(answer):
    while True:
        if answer == 'yes':
            return main()
        elif answer == 'no':
            print('Good luck. See you soon!')
            break
        else:
            answer = input("Please only answer 'Yes' or 'No'\n").lower()


main()