while True:
    try:
        a = int(input("Enter a number"))
        b = int(input("Enter a second number"))
        if (a % 6) == 0:
            print("One number is divisible by 6")
        elif (b % 6) == 0:
            print("One number is divisible by 6")
        else:
            print("None of the numbers is divisible by 6")

        if (a % 10) == 0 and (b % 10) == 0:
            print("Both numbers are divisible by 10")
        break
    except:
        print("Please enter a number")
# das ist ein test 1.2
im kreis herum
