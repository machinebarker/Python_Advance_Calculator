# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x // y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

def Calculator():

    while True:
        # take input from the user
        choice = int(input("Enter choice(1/2/3/4): "))
        if choice >4 or choice <1:
            print("Enter your choice from 1 to 4")
        else:
            print("Enter your numbers: ")
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        # check if choice is one of the four options
            if choice == 1:
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == 2:
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == 3:
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == 4:
                print(num1, "/", num2, "=", divide(num1, num2))            
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ").lower()
        if next_calculation == 'yes':
            Calculator()
        else:
            print("Press any key to exit")
            return 0

if __name__ == '__main__':
    Calculator()