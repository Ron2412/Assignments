userInput = input("Enter Your marks out of 100:")
userInput =int(userInput)

if (userInput>= 90):
    {
        print("Your grade is A")
    }
elif (userInput>= 80 and userInput<90):
    {
        print("Your grade is B")
    }
elif(userInput>= 70 and userInput<80):
    {
        print("Your grade is C")
    }
elif(userInput>=60 and userInput<70):
    {
        print("Your grade is D")
    }
else:
    {
        print("Your grade is F")
    }


