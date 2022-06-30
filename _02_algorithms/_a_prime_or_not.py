"""
Write code that can tell if a number is prime.
A prime number is a number that is only divisible by 1 and itself.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    # TODO)
    #  1. Ask the user for a number
    window = Tk()
    window.withdraw()
    number = simpledialog.askinteger(None, "Type in a number.")
    #  2. Use a for loop, if statement, and modulo to find if the number
    #     is prime.

    is_prime = True
    for i in range(number):
        if i > 1 and number % i == 0:
            is_prime = False
            break

    #  3. If the number is divisible by any number other than 1 or itself,
    #     the number is not prime.

    print(is_prime)
