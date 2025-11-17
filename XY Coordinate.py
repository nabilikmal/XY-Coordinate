import os
import time

class Point:
    __match_args__ = ("x", "y")
    def __init__ (self, x, y):
        self.x = x
        self.y = y

def where_is (point):
    match (point):
        case Point(0, 0):
            print("\nOrigin")
        case Point(0, y):
            print(f"\ny = {y}")
        case Point(x, 0):
            print(f"\nx = {x}")
        case Point(x, y):
            print(f"\nx = {x}, y = {y}")
        case _:
            print("\nNot a valid Point object")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    try:
        clear_console()
        x = float(input("Enter x coordinate: "))
        y = float(input("Enter y coordinate: "))
        p = Point(x, y)
        where_is(p)

        continue_input = input("\nContinue? (y/n): ").strip().lower()
        if continue_input != 'y':
            time.sleep(0.5)
            clear_console()
            break

    except ValueError:
        # In the exception handler:
        print("Invalid input. Please enter numeric values.")
        time.sleep(2)

""" 
    Add colors with colorama

    Add ASCII graphics (quadrants)

    Turn this into a mini coordinate system program

    Make a GUI version
"""