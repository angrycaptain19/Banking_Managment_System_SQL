# Write your code here
from random import randint
import sqlite3

# Creates the database
conn = sqlite3.connect('card.s3db')

cur = conn.cursor()

# Creates the table

cur.execute("""
            CREATE TABLE IF NOT EXISTS card 
            (id INTEGER PRIMARY KEY,
            pin TEXT NOT NULL CHECK (length(pin) == 4),
            'number' TEXT NOT NULL UNIQUE,
            balance INTEGER DEFAULT 0) 
            ;""")
conn.commit()

# class Account:
#     def __init__(self):
#         print("Your card has been created")
#         print("Your card number:")
#         initial_number = "400000" + str(randint(0, 999999999)).zfill(9)
#         num_list = [int(digit) for digit in initial_number]
#         sum = 0
#         for index, value in enumerate(num_list, start=1):
#             if index % 2 == 0:
#                 sum += value
#             else:
#                 if value * 2 > 9:
#                     sum += value * 2 - 9
#                 else:
#                     sum += value * 2
#         if sum % 10 == 0:
#             check_digit = 0
#         else:
#             check_digit = 10 - (sum % 10)
#         self.credit_number = int(initial_number + str(check_digit))
#         print(str(self.credit_number))
#         self.pin = int(str(randint(0, 9999)).zfill(4))
#         print("Your card PIN:")
#         print(self.pin)
#         print()
#         self.balance = 0


while True:
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")
    print()

    choice = int(input(">"))

    if choice == 1:

        print("Your card has been created")
        print("Your card number:")
        initial_number = "400000" + str(randint(0, 999999999)).zfill(9)
        num_list = [int(digit) for digit in initial_number]
        sum_of_dig = 0
        for index, value in enumerate(num_list, start=1):
            if index % 2 == 0:
                sum_of_dig += value
            else:
                if value * 2 > 9:
                    sum_of_dig += value * 2 - 9
                else:
                    sum_of_dig += value * 2
        if sum_of_dig % 10 == 0:
            check_digit = 0
        else:
            check_digit = 10 - (sum_of_dig % 10)
        credit_number = int(initial_number + str(check_digit))
        print(str(credit_number))
        pin = (str(randint(0, 9999)).zfill(4))
        print("Your card PIN:")
        print(pin)
        print()
        balance = 0

        cur.execute("INSERT INTO card (\"pin\" , \"number\" ) VALUES (? ,?) ;", (pin, credit_number))
        conn.commit()

        # cur.execute('SELECT * FROM card ;')
        # print(cur.fetchall())
        # new_account = Account()
        # accounts.append(new_account)

    elif choice == 2:
        print("Enter your card number:")
        credit_attempt = input('>')
        print("Enter your PIN:")
        pin_attempt = input('>')
        flag = False
        #Check if the account is present in the card table
        cur.execute("""SELECT *
                        FROM card
                        WHERE number=? AND pin=?""", (credit_attempt, pin_attempt))
        active_account = cur.fetchall()
        if(active_account):
            flag = True
            print("You have successfully logged in!")
            while True:
                flag = True
                print("1. Balance")
                print("2. Log out")
                print("0. Exit")
                print()
                choice = int(input('>'))
                if choice == 1:
                    print("Balance: " + str(active_account[0][3]))
                elif choice == 2:
                    print("You have successfully logged out!")
                    break
                elif choice == 0:
                    print("Bye!")
                    quit()
        else:
            print("Wrong card number or PIN!")
            print()


    elif choice == 0:
        print("Bye!")
        break

    else:
        print("invalid choice!")
