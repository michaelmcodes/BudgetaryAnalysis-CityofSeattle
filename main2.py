import csv


# class to create dept expenses
class Expense:
    name: str
    amount: float

    # define the class
    def __init__(self, name: str, amount: float):
        self.name = name
        self.amount = amount


# function to open the file and return list of expenses
def open_file(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        expense_list = []
        row_number = 1
        for row in reader:
            if row_number != 1:
                if row[3] == '':
                    continue
                else:
                    expenses = Expense(row[0], float(row[3]))
                    expense_list.append(expenses)
                    row_number += 1
            else:
                row_number += 1
    return expense_list


# function to create a dictionary of the dept and it's expenses and return it
def create_dict(file_name):
    expense_list = open_file(file_name)
    expense_dict = {}

    for dept in expense_list:
        if dept.name not in expense_dict:
            expense_dict[dept.name] = [dept.amount]
        else:
            expenses = expense_dict[dept.name]
            expenses.append(dept.amount)
            expense_dict[dept.name] = expenses

    return expense_dict


# function to calculate the sum of each department and print it
def print_sum(file_name):
    expense_dict = create_dict(file_name)

    for dept in expense_dict.keys():
        total = sum(expense_dict.get(dept))
        print("Department: " + dept + " spent: " + str(total))


print_sum('city-of-seattle-2012-expenditures-dollars.csv')
