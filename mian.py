x = int(input("Enter the number you want to reverse : "))
x_rev = 0
while x != 0:
    digit = x % 10
    x_rev = x_rev * 10 + digit
    x //= 10

print("Reversed Number: " + str(x_rev))
