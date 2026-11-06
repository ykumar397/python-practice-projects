from logic import load_bill, add_bill, edit_bill, delete_bill, search_bill


if __name__ == "__main__":

    print(f"""
                {'-' * 20}Welcome to Bill Tracker{'-' * 20}\n
{'-' * 100}

Please enter the Bill information in the following sequence ("vendor name, service, amount, invoice date, due date", to save a bill).\n
""")

    while True:

        choice = input("""
Choose any of the following :

1 Add a new bill
2 View existing bills
3 Change payment status of a bill
4 Delete Bill
5 Search Bill
0 to exit
""")

        if choice not in ['1', '2', '3', '4', '5', '0']:
            print("Invalid input, Please try again!!!.")
            print("-" * 60)
            continue

        elif choice == '1':
            print("\n")
            print("-" * 60)
            print(add_bill())
            print("-" * 60)

        elif choice == '2':
            print("\n")
            print("-" * 60)
            bill = load_bill()
            if not bill:
                print("There are no bills!")
                print("-" * 60)
            else:
                for i, b in enumerate(bill, start=1):
                    print(i, b)
            print("-" * 60)

        elif choice == '3':
            print("\n")
            print("-" * 60)
            print(edit_bill())
            print("-" * 60)

        elif choice == '4':
            print("\n")
            print("-" * 60)
            print(delete_bill())
            print("-" * 60)

        elif choice == '5':
            print("\n")
            print("-" * 60)
            print(search_bill())
            print("-" * 60)

        elif choice == '0':
            print("\n")
            print("-" * 60)
            print("Thank you for using Bill Tracker")
            break




# print(add_bill("Microsoft", "Office 365 Suite", 100, "1st july", "2026-07-15", unpaid))
# Microsoft, Office 365 Suite, 100, 1st july, 2026-07-15, paid
# Microsoft, Intune, 300, 1st july, 2026-07-15, unpaid
# Google, GWS, 500, 1st july, 2026-07-15, unpaid
# zscaler, VPN, 500, 1st july, 2026-07-15, unpaid

