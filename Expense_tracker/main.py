from Expense_tracker.class_creation import Expense
from saving_and_handling import save_expense, load_expense


if __name__ == "__main__":

    def display_expense(rows):  # handles Displaying of expense report, separated for multiple use
        print("Amount", "Category", "Description")
        for i, n in enumerate(rows, start=1):
            print(f"{i}: {n[0]}, {n[1]},  {n[2]}")


    while True:

        choice = input("""
Choose any of the following :

1 add a expense
2 view existing expense record
3 filter by category
0 to exit 
""")

        if choice not in ['1', '2', '3', '0']: # GateKeeper for invalid Input
            print("Invalid Input, Try again!!!")
            continue

        elif choice == '1': # creates a new expense record
            try:
                new_choice = input("Please enter the expense details, 'amount', 'category', 'description':  ").split(", ")
                current_track = Expense(*new_choice)
                print(save_expense(current_track))

            except TypeError:
                print(f"Expected 3 inputs, received {len(new_choice)}, Please try again!")
                continue


        elif choice == '2': # display's existing list of expense in rows
            display_expense(load_expense())


        elif choice == '3':
            new_category = input("Please enter a category to filter: ").lower()

            cat_values = [n for n in load_expense() if n[1].lower() == new_category]
            display_expense(cat_values)


        elif choice == '0':
            break


# 200, shopping, groceries
