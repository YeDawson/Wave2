#Exercise 38: Month Name to Number of Days
print("Insert a Month:")
n = str(input())
if n in ["February"]:
    print("There are 28/29 days")
elif n in ["January" , "March" , "May" , "July" , "August" , "October" , "December"]:
    print("There are 31 days")
else:
    print("There are 30 days")
