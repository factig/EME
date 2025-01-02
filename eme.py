# app.py
def main():
    try:
        print("Enter two numbers:")
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        
        print("\nSelect an operation:")
        print("1. Subtraction")
        print("2. Multiplication")
        choice = input("Enter choice (1/2): ")

        if choice == '1':
            result = num1 - num2
            print(f"\nThe result of subtraction is: {result}")
        elif choice == '2':
            result = num1 * num2
            print(f"\nThe result of multiplication is: {result}")
        else:
            print("\nInvalid choice.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
