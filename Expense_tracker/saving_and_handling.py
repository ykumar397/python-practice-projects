import csv

def save_expense(expense):

    with open("expenses.csv", 'a', newline='') as file:
        write_out = csv.writer(file)
        write_out.writerow(expense.to_list())

        return ("Expense Saved")




def load_expense():
    try:
        with open("expenses.csv", 'r') as file:
            read_out = csv.reader(file)

            return list(read_out)

    except (FileNotFoundError, csv.Error):
        return []


