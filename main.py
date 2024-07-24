def calculateProduct(a, b):
    return a * b

def calculateQuotient(a, b):
    if b == 0:
        return "Cannot divide by 0!"
    else:
        return a / b

def calculateSum(a, b):
    return a + b

def calculateDifference(a, b):
    return a - b


def main():
    running = True
    while(running):
        print("Please select an option: \n 1: Add \n 2: Subtract \n 3: Multiply \n 4: Divide \n Anything else to quit")
        selectInput = int(input())
        if(selectInput > 4 or selectInput < 1):
            exit()
        print("Now please select two numbers: ")
        num1 = float(input())
        num2 = float(input())
        if(selectInput == 1):
            print(calculateSum(num1, num2))
        if(selectInput == 2):
            print(calculateDifference(num1, num2))
        if(selectInput == 3):
            print(calculateProduct(num1, num2))
        if(selectInput == 4):
            print(calculateQuotient(num1, num2))

main()