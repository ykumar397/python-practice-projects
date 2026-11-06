from logic import operations



if __name__ == "__main__":


    print(f"{'_' * 10}Welcome To Numbers Generator{'_' * 10}")

    while True:

        choice = input(f"""
Please select any one of the operation
1 for Addition
2 for subtraction
3 for multiplication
4 for division
0 to exit
""")

        if choice not in ['1', '2', '3', '4', '0']:
            print("Invalid Input, Please try again!!!")
            continue

        elif choice == '0':
            print("\nThank you for using Math Generator.")
            break

        else:
            print(operations(int(choice)))

















