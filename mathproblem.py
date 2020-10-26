#gets number from user and stores this value as "number"
print("Please enter a number: ")
number = int(input())

#checks if number is divisible by 2
if number % 2 == 0:

#prints the number divided by 2 if true
    print(number // 2)
else:
#prints the number times 3 plus 1 if false
    print(number * 3 + 1)