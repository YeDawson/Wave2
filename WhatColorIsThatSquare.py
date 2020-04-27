#Exercise 45:What colour is that Square
print("Insert Square(example: A1):")
n = str(input())
a = n[0]
b = int(n[1])
if a == ("A" or "C" or "E" or "G") and b == (1 or 3 or 5 or 7):
    print("The tile is black")
elif a == ("B" or "D" or "F" or "H") and b == (2 or 4 or 6 or 8):
    print("The tile is black")
else:
    print("The tile is white")