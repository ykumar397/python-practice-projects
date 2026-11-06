import random
from operator import add, sub, mul, floordiv

def num_generator():
    lhs = random.randint(a=9, b=999)
    rhs = random.randint(a=9, b=999)

    return lhs, rhs


def operations(spot):
    counter = 0

    arithmetic = [add, sub, mul, floordiv]
    ops = {1: "+", 2: "-", 3: "*", 4: "//"}

    for i in range(1, 6):
        lhs, rhs = num_generator()
        answer = arithmetic[spot - 1](lhs, rhs)

        while True:
            try:
                new_choice = int(input(f"{i}: {lhs} {ops[spot]} {rhs} = "))
                break

            except ValueError:
                print("Invalid Input, No empty number or floats allowed!!!")


        if new_choice == answer:
            counter += 1
            print(f"Correct answer\n")


        else:
            print(f"Wrong answer, Correct answer: {answer}\n")

    return f"Session concluded, Correct answer: {counter}, Wrong answer: {5 - counter}"



