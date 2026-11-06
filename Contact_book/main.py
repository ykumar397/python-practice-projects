from logic import save_contact, load_contact, search_contact
from model import Contacts

if __name__ == "__main__":

    def display_contacts(rows):
        for i, n in enumerate(rows, start=1):
            print(f"""
{i}. {n}
""")


    while True:
        choice = input("""
Please select from the below options
'1' add contact
'2' view all
'3' edit contact
'4' search contact
'5' delete contact
'0' to exit : """)

        contact_list = load_contact()

        if choice not in ['1', '2', '3', '4', '5', '0']:
            print("Invalid input, please try again!")
            continue

        elif choice == '1':
            new_contact = input("Please enter the details in following format 'Name', 'Phone', 'Email', 'Label': ").split(", ")
            if len(new_contact) != 4:
                print(f"\nExpected 4 values but received {len(new_contact)}")
                continue

            new_object = Contacts(*new_contact)
            contact_list.append(new_object)
            print(save_contact(contact_list))


        elif choice == '2':
            if not contact_list:
                print("\nThere are no contacts saved.")

            else:
                display_contacts(contact_list)



        elif choice == '3':
            display_contacts(contact_list)



            select_row_column = input("""
Please enter a number associated to a specific contact and the field you would like to update.
Ex: 1, Name
""").lower().split(", ")

            if len(select_row_column) != 2:
                print(f"Expected two inputs, received {len(select_row_column)}. Please make sure to use ","")
                continue

            elif select_row_column[1] not in ["name", "phone", "email", "label"]:
                print(f"'{select_row_column[1]}', does not exist!")
                continue



            validation = False

            for i, n in enumerate(contact_list, start=1):
                if select_row_column[0] == str(i) and hasattr(n, select_row_column[1]):
                    update_field = input("Enter here: ").lower()

                    setattr(n, select_row_column[1], update_field)
                    save_contact(contact_list)
                    validation = True
                    print(f"""
Changes saved
{i}.
{n}
""")
            if validation == False:
                print("details do not match")



        elif choice == '4':
            print(search_contact())


        elif choice == '5':
            display_contacts(contact_list)
            print("\n")

            try:
                record_delete = int(input("Please select a number associated to a contact to delete the record: "))

                removed_contact = contact_list.pop(record_delete - 1)

                save_contact(contact_list)
                print(f"""
{removed_contact}           
contact deleted""")

            except IndexError:
                print("number out of range!!!")

            except ValueError:
                print("Expecting a Whole number!!!.")


# pop, 9743549890, pop2rock@gmail.com, home
# yogesh Kumar A, 9743325456, yogesh_kumar1@intuit.com, work
# hemanth kumar, 8050324031, hemanth_nyah@gmail.com, home


