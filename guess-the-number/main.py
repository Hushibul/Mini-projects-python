import random
try:
    while True:
        inputNumber = int(input("Enter the a number between 1 to 10: "))

        num = random.randint(1, 10)

        if inputNumber > 10 or inputNumber < 1:
            print("Please the enter the number between 1 to 10")
        else:
            if num == inputNumber:
                print("Lucky Number", inputNumber, "!!!You have won")
                break
            else:
                print("Sorry better luck next time...", "And the lucky number is: ", num)
except Exception as error:
    print("Some error occurred!!!", error)