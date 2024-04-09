import mysql.connector
import re

def add_account():
    firstName = input("What is your First Name? ")
    lastName = input("What is your Last Name? ")

    pin = input("What would you like your 4 digit PIN to be? ")
    # while (re.match(pin, "\\d{4}") == None):
        # pin = input("Please put a valid 4 digit PIN: ")

    testQuery = ('INSERT INTO bank_accounts (First_name, Last_name, Balance, PIN) VALUES ("'+firstName+'", "'+lastName+'", 0.0, '+str(pin)+')')
    cursor.execute(testQuery)
    connection.commit()

    testQuery = ("Select SCOPE_IDENTITY()  as LastEmployeeId")
    cursor.execute(testQuery)

    for item in cursor:
        print(item)


userInput = input("Do you want to Add Account (1) or Withdraw or Deposit Money (2)? ")

connection = mysql.connector.connect(user = 'root', database = 'lesson_3', password = 'mySQL4me-preston')

cursor = connection.cursor()

if (userInput == "1"):
    add_account()

# testQuery = ('SELECT * FROM bank_accounts')
# cursor.execute(testQuery)

elif (userInput == "2"):
    testQuery = ("SELECT * FROM students")
    cursor.execute(testQuery)


cursor.close()
connection.close()