print("Welcome to the Pattern Generator and Number Analyzer!")
while True:
    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    n=int(input("Enter your choice: "))
    match n:
        case 1:
            m = int(input("Enter the number of rows for the pattern: "))

            print("Pattern: ")
            for i in range(1, m + 1):
                for j in range(1, i + 1):
                    print("*", end=" ")

                print()

        case 2:
            a=int(input("Enter the start of the range: "))
            c=a
            b=int(input("Enter the end of the range: "))
            d=b
            sum=0
            while a<=b:
                if a%2==0:
                    print(f"Number {a} is Even")
                else:
                    print(f"Number {a} is Odd")
                sum+=a
                a+=1

            print(f"Sum of all numbers from {c} to {d} is: {sum}")


        case 3:
            print("Exiting the program. Goodbye!")
            break

        case _:
            print("Invalid Input. Please try again.")
