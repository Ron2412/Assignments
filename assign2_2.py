studentData = {
    "student1": "A",
    "student2": "B",
    "student3": "C",
}
def addData():
    add = input("Enter the student name to add: ")
    grade = input("Enter the grade for the student: ")
    studentData[add] = grade
def displayData():
    print("Student Data:")
    print(studentData)

def updateData():
    updateName = input("Enter the student name to update:")
    if updateName in studentData:
        newGrade = input("Enter the new grade for the student: ")
        studentData[updateName] = newGrade
    else:
        print("Student not found.")

print("Welcome to the Student Management System")
choice = input("Choose an option: \n1. Add Student Data\n2. Display Student Data\n3. Update Student Data\n4. Exit\n")

if choice == '1':
    addData()
elif choice == '2':
    displayData()
elif choice == '3':
    updateData()
elif choice == '4':
    print("Exiting the system.")
else:
    print("Invalid choice. Please try again.")  
    
