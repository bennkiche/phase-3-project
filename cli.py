import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base,LAB,Test


DATABASE_URL = "sqlite:///labs.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    # Initialize Database
    Base.metadata.create_all(engine)
    print("Database Initialized")

def create_lab():
    # create new lab
    name = input("Enter LAB name: ")
    section = input("Enter LAB section: ")
    lab = LAB(name=name,section=section)
    session.add(lab)
    session.commit()
    print(f"LAB '{name}' created with ID {lab.id}")

def update_tm():
    tm_id = int(input("Enter TM ID to update: "))
    tm = session.get(TM,tm_id)
    if not tm:
        print(f"TM with ID {tm_id} does not exist.")
        return
    tm.name = input(f"Enter new name for TM (current: {tm.name}): ") or tm.name
    tm.email = input(f"Enter new email for TM (current: {tm.email}): ") or tm.email
    session.commit()
    print(f"TM ID {tm_id} updated successfully")

def delete_tm():
    tm_id = int(input("Enter TM ID to delete: "))
    tm = session.get(TM,tm_id)

    if not tm:
        print(f"TM with ID {tm_id} deos not exist.")
        return
    session.delete(tm)
    session.commit()
    print(f"TM ID {tm_id} deleted successfully.")

def create_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    tm_id = int(input("Enter TM ID: "))
    tm = session.get(TM,tm_id)
    if not tm:
        print(f"TM with ID {tm_id} does not exist")
        return
    student = Student(name= name,age=age,tm_id=tm_id)
    session.add(student)
    session.commit()
    print(f"Student '{name}' created with ID {student.id} and assigned to TM_ID {tm_id}")

def update_student():
    student_id = int(input("Enter Student ID to update: "))
    student = session.get(Student,student_id)

    if not student:
        print(f"Student with id {student_id} does not exist")
        return
    student.name = input("Enter new name for student (current: {student.name}): ") or student.name
    student.age = input("Enter new age for student (current: {student.age}): ") or student.age
    new_tm_id = input(f"Enter new TM ID for Student (current: {student.tm_id}): ") or student.tm_id
    if new_tm_id:
        new_tm = session.get(TM,int(new_tm_id))
        if not new_tm:
            print (f"TM with ID {new_tm_id} does not exist. Skipping TM update.")
        else: 
            student.tm_id = new_tm_id
    session.commit()
    print(f"Student ID {student_id} updated successfully")

def delete_student():
    student_id = int(input("Enter Student id to delete: "))
    student = session.get(Student,student_id)
    if not student:
        print(f"Student with ID {student_id} does not exist")
        return
    session.delete(student)
    session.commit()
    print(f"Student ID {student_id} deleted successfully")

def assign_student():
    student_id = int(input("Enter Student ID: "))
    tm_id = int(input("Enter the new TM ID: "))
    student = session.get(Student,student_id)
    tm =  session.get(TM,tm_id)

    if not student or not tm:
        print("Invalid student Id or Tm id.")
        return
    student.tm_id = tm_id
    session.commit()
    print("TM assigned successfully")

def list_tms():
    tms = session.query(TM).all()
    if not tms:
        print("No TMs found.")
    for tm in tms:
        print(tm)

def list_students():
    students = session.query(Student).all()
    if not students:
        print("No Students found.")
    for student in students:
        print(student)

def view_students_by_tm():
    tm_id = int(input("Enter TM ID to view students: "))
    tm = session.get(TM,tm_id)
    if not tm:
        print("TM with ID {tm_id} does not exist")
        return
    students = tm.students
    if not students:
        print(f"No students found for TM with ID {tm_id}")
        return
    print(f"Students belonging to TM '{tm.name}' (ID {tm_id}):")
    for student in students:
        print(student)

def main_menu():
    while True:
        print("\nWelcome to the Application. What would you like to do?")
        print("1. Create TM")
        print("2. Update TM")
        print("3. Delete TM")
        print("4. Create Student")
        print("5. Update Student")
        print("6. Delete Student")
        print("7. Assign Student to TM")
        print("8. List TMs")
        print("9. List Students")
        print("10. View Students by TM")
        print("11. EXit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_tm()
        elif choice == "2":
            update_tm()
        elif choice == "3":
            delete_tm()
        elif choice == "4":
            create_student()
        elif choice == "5":
            update_student()
        elif choice == "6":
            delete_student()
        elif choice == "7":
            assign_student()
        elif choice == "8":
            list_tms()
        elif choice == "9":
            list_students()
        elif choice == "10":
            view_students_by_tm()
        elif choice == "11":
            print("Exiting.......")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__== "__main__":
    init_db()
    main_menu()