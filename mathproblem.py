def test(number):


    #checks if number is divisible by 2
    if number % 2 == 0:

    #prints the number divided by 2 if true
        print(number // 2)
    else:
    #prints the number times 3 plus 1 if false
        print(number * 3 + 1)

#gets a number from the user 
print("Please enter a number: ")

#converts this number to an integer
number = int(input())

#this runs the number through the test function, I removed the print statement from this line because the 'test' function is already printing the result.
(test(number))
