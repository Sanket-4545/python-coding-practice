# Q7. Design a program to continuously input a number from user & print if it is 
# positive or negative until the user enters “Quit”. 
def continuously_input():
    while True:
        value = input("Enter any number or Quit: ")
        if value.strip().lower() == "quit":
            print("Exiting the program")
            break
        try:
            number = float(value)
        except ValueError:
            print("Please enter a valid number or Quit")
            continue

        if number > 0:
            print("You entered a positive number")
        elif number < 0:
            print("You entered a negative number")
        else:
            print("You entered zero")

continuously_input()

