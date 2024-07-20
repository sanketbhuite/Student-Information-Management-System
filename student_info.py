def enter_data():
    name = input("Enter student name: ")
    rollno = input("Enter roll number: ")
    marks = input("Enter marks: ")
    return name, rollno, marks

def write_data(data):
    with open("student_info.txt", "a+") as file:
        file.write("|".join(data) + "\n")

def search(s):
    with open("student_info.txt", 'r') as file:
        for i in file:
            if s in i:
                return i

def update(s, ni):
    with open("student_info.txt", 'r') as file:
        r = file.readlines()
    with open("student_info.txt", 'w') as file:
        for i in r:
            if s in i:
                file.write(ni + '\n')
            else:
                file.write(i)

def delete(s):
    with open("student_info.txt", 'r') as file:
        r = file.readlines()
    with open("student_info.txt", 'w') as file:
        for i in r:
            if s not in i:
                file.write(i)

def display_data():
    with open("student_info.txt", 'r') as file:
        print("Name\tRoll Number\tMarks")
        for line in file:
            data = line.strip().split('|')
            if len(data) >= 3:
                print(data[0],"\t",data[1],"\t",data[2])
            else:
                print("Invalid data format in file.")

while True:
    choice = input("Enter choice\n1: Add the Student ID\n2: Read the Information\n3: Search the Student ID\n4: Update the Data\n5: Delete the Data\n6: Exit\n")
    if choice == "1":
       data = enter_data()
       write_data(data)
       print("Data added!!")
    elif choice == "2":
        print("Student information:")
        display_data()
    elif choice == "3":
        s= input("Enter student ID to search: ")
        r = search(s)
        if r:
            print("Entered word/value exists")
            print("Student info:", r)
        else:
            print("Student not found.")
    elif choice == "4":
        s = input("Enter student ID to update: ")
        ni = input("Enter new information: ")
        update(s, ni)
        print("Student info updated.")
    elif choice == "5":
        s = input("Enter student ID to delete: ")
        delete(s)
        print("Student info deleted.")
    elif choice == "6":
        print("Program completed.")
        break
    else:
        print("Invalid choice. Please try again.")
