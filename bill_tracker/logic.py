import json
from model import Bill


def load_bill():
    try:
        with open("Bills.json", "r") as file:
            data = json.load(file)
            bills = [Bill(**x) for x in data]
            return bills

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def add_bill():

    while True:

        bill_info = input("Please enter the bill details: ").split(", ")

        if len(bill_info) != 6:
            print(f"Expected 6 inputs, received {len(bill_info)}, Kindly try again.")
            continue

        print(f"""
\nPlease validate your details

vendor          : {bill_info[0]}
service         : {bill_info[1]}
amount          : {bill_info[2]}
invoice date    : {bill_info[3]}
due date        : {bill_info[4]}
status          : {bill_info[5]}
""")

        while True:

            choice = input("Do you wish to save this bill, Please enter 'Yes' to confirm or 'No' to go back to the main menu: ").lower()
            if choice not in ['yes', 'no']:
                print("Invalid Input, Please choose 'Yes' or 'No'")

            elif choice == 'yes':
                new_object = Bill(*bill_info)
                bill_list  = load_bill()
                bill_list.append(new_object)
                save_bill(bill_list)
                return "Bill has been saved."

            elif choice == 'no':
                print("Action has been cancelled.")
                break

        return "Bill has not been saved"


def edit_bill():
    bill = load_bill()

    for i, b in enumerate(bill, start=1):
        print(f"""
{i}:    {b}
""")

    while True:
        try:
            choice = int(input("""
Please choose a bill to change the status of the payment.
Choose a number associated to the bill:
"""))

            bill[choice -1].mark_as_paid()
            save_bill(bill)

            print("Bill status has been Updated.")
            return bill[choice - 1]

        except ValueError:
            print("Expecting a Whole number!!!.")
            continue

        except IndexError:
            print("Entered number is out range!!!.")
            continue


def delete_bill():
    bill = load_bill()

    for i, b in enumerate(bill, start=1):
        print(f"""
{i}:    {b}
    """)

    while True:
        try:
            choice = int(input("Choose a number associated to the bill: "))

            deleted_bill = bill.pop(choice - 1)
            save_bill(bill)

            return (f"""
Bill has been deleted
{deleted_bill}
""")

        except ValueError:
            print("Expecting a Whole number!!!.")
            continue

        except IndexError:
            print("Entered number is out range!!!.")
            continue


def search_bill():

    bill = load_bill()

    choice = input("""
Choose a category to search with,
'vendor', 'service', 'amount', 'status': 
""").lower()

    new_choice = input("Enter the details: ").lower()

    counter = 0

    for i, n in enumerate(bill, start=1):
        if getattr(n, choice) == new_choice:
            counter += 1
            print(f"{i}:    {n}")

        else:
            continue

    return f"Search Complete, {counter} results found."


def save_bill(bills):
    with open("Bills.json", "w") as file:
        json.dump([b.to_dict() for b in bills], file)
