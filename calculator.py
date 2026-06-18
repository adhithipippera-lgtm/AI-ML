while True:
    print("\n==== Calculator ====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. division")
    print("5. Modulus")
    print("6. Exit")


    choice = input("Enter your choice: ")
    print("Goodbye!")
    break
    
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter Second number"))

    if choice == "1":
        print("Result =", num1 + num2)

    elif choice == "2":
        print("Result =", num1 - num2)

    elif choice =="3":
        print("Result =", num1 * num2)

    elif choice =="4":
        print("Result =", num1 / num2)
    
    elif choice =="5":
        print("Result =", num1 % num2)
        
    else:
        print("Invalid Choice")
