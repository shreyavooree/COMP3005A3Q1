import A3Q1
import datetime

print("To edit the database, please enter your selection of operation and follow the prompts. If you give any value other than C, R, U, or D, the program will quit")

while(True):
    operation = input("Select operation type (C, R, U, D):")
    if operation == 'C':
        #gather inputs
        firstName = input("Enter first name: ")
        lastName = input("Enter last name: ")
        email = input("Enter email: ")
        year = input("Enter year: ")
        month = input("Enter month: ")
        day = input("Enter day: ")

        #run function
        A3Q1.addStudent(firstName, lastName, email, datetime.date(int(year), int(month), int(day)).strftime('%Y-%m-%d'))

        print("All done")

    elif operation == 'R':
        A3Q1.getAllStudents()
        print("All done")

    elif operation == 'U':
        #gather inputs
        index = input("Enter id/index: ")
        email = input("Enter new email: ")
        
        A3Q1.updateStudent(int(index), email)

        print("All done")

    elif operation == 'D':
        index = input("Enter id/index: ")

        A3Q1.deleteStudent(index)
        print("All done")
    else:
        exit()
