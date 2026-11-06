import csv
from model import Contacts


def save_contact(contacts):

    with open("contact.csv", "w", newline='') as file:
        write_in = csv.writer(file)
        for c in contacts:
            write_in.writerow(c.to_csv())

        return ("\nContact saved")


def load_contact():
    try:
        with open("contact.csv", "r") as file:
            read_out = csv.reader(file)
            contact = [Contacts(*x) for x in read_out]

            return contact

    except (FileNotFoundError, csv.Error):
        return []


def search_contact():
    current_list = load_contact()
    counter = 0

    pattern = input("\nPlease enter any details to find a match: ")

    for i in current_list:
        if pattern.lower() in i.name.lower():
            counter += 1
            print(f"{i}")

        elif pattern.lower() in i.phone.lower():
            counter += 1
            print(f"{i}")

        elif pattern.lower() in i.email.lower():
            counter += 1
            print(f"{i}")

        elif pattern.lower() in i.label.lower():
            counter += 1
            print(f"{i}")

        else:
            continue

    return f"\nSearch Complete, {counter} results found."



