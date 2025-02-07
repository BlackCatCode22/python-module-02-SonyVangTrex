def largestfind(number1, number2, number3) :
    if number1 > number2 and number1 > number3:
        return number1
    if number2 > number1 and number2 > number3:
        return number2
    else:
        return number3

N1 = input("Enter first number: ")
N2 = input("Enter second number: ")
N3 = input("Enter third number: ")

xp = largestfind(N1, N2, N3)

print("The largest number is", xp)