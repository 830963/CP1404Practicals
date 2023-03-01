"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def celsius(f):
    return (f - 32) * 5 / 9.0


def fahrenheit(c):
    return c * 9.0 / 5 + 32



def main();
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            c = float(input("Celsius: "))
            f = fahrenheit(c)
            print("Result: {:.2f} F".format(f))
        elif choice == "F":
            f = float(input("Fahrenheit: "))
            c = celsius(f)
            print("Result: {:.2f} F".format(c))

        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


menu()