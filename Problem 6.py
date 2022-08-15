# Michelle Patlan
# 8/13/2022
#Use a for statement to calculate the factorial of a user input value. Print this value
#as well as the calculated value using the factorial function in the math module.
import math

#factorial equation
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)

#user imput
fact_input = int (input("Please enter a number: "))
print("Factorial of", fact_input, "is",
      factorial(fact_input))

#using module
print('The factorial using factorial module is: ', math.factorial(fact_input))