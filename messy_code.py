# simple_adder.py
"""Simple adder program with input validation."""

def add_numbers(a, b):
    return a + b

def main():
    print("This is a simple adder program.")
    try:
        a = input("Enter first number: ").strip()
        b = input("Enter second number: ").strip()
        a_num = int(a)
        b_num = int(b)
    except ValueError:
        print("Error: please enter valid integers.")
        return

    result = add_numbers(a_num, b_num)
    print("The sum is:", result)

if __name__ == "__main__":
    main()
