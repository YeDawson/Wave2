#Exercise 60: Roulette Payouts
roulette = list(range(0,36))
roulette.append("00")
import random
x = random.choice(roulette)
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
print("The spin resulted in", x)
print("Pay", x)

# If statements for the programs
if x == "0":
    print("Pay 0")
elif x == "00":
    print("Pay 00")
else:
    if x in red:
        print("Pay Red")
    else:
        print("Pay Black")
    if x % 2 == 0:
        print("Pay Even")
    else:
        print("Pay Odd")
    if x in range(1, 19):
        print("Pay 1 to 18")
    else:
        print("Pay 19 to 36")