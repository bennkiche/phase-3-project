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

def update_lab():
    lab_id = int(input("Enter LAB ID to update: "))
    lab = session.get(LAB,lab_id)
    if not lab:
        print(f"LAB with ID {lab_id} does not exist.")
        return
    lab.name = input(f"Enter new name for LAB (current: {lab.name}): ") or lab.name
    lab.section = input(f"Enter new section for LAB (current: {lab.section}): ") or lab.section
    session.commit()
    print(f"LAB ID {lab_id} updated successfully")

def delete_lab():
    lab_id = int(input("Enter LAB ID to delete: "))
    lab = session.get(LAB,lab_id)

    if not lab:
        print(f"LAB with ID {lab_id} deos not exist.")
        return
    session.delete(lab)
    session.commit()
    print(f"LAB ID {lab_id} deleted successfully.")

def create_test():
    name = input("Enter test name: ")
    price = int(input("Enter test price: "))
    lab_id = int(input("Enter LAB ID: "))
    lab = session.get(LAB,lab_id)
    if not lab:
        print(f"LAB with ID {lab_id} does not exist")
        return
    test = Test(name= name,price=price,lab_id=lab_id)
    session.add(test)
    session.commit()
    print(f"Test '{name}' created with ID {test.id} and assigned to LAB_ID {lab_id}")

def update_test():
    test_id = int(input("Enter Test ID to update: "))
    test = session.get(Test,test_id)

    if not test:
        print(f"Test with id {test_id} does not exist")
        return
    test.name = input("Enter new name for test (current: {test.name}): ") or test.name
    test.price = input("Enter new price for test (current: {test.price}): ") or test.price
    new_lab_id = input(f"Enter new LAB ID for Test (current: {test.lab_id}): ") or test.lab_id
    if new_lab_id:
        new_lab = session.get(LAB,int(new_lab_id))
        if not new_lab:
            print (f"LAB with ID {new_lab_id} does not exist. Skipping LAB update.")
        else: 
            test.lab_id = new_lab_id
    session.commit()
    print(f"Test ID {test_id} updated successfully")

def delete_test():
    test_id = int(input("Enter Test id to delete: "))
    test = session.get(Test,test_id)
    if not test:
        print(f"Test with ID {test_id} does not exist")
        return
    session.delete(test)
    session.commit()
    print(f"Test ID {test_id} deleted successfully")

def assign_test():
    test_id = int(input("Enter Test ID: "))
    lab_id = int(input("Enter the new LAB ID: "))
    test = session.get(Test,test_id)
    lab =  session.get(LAB,lab_id)

    if not test or not lab:
        print("Invalid test Id or Lab id.")
        return
    test.lab_id = lab_id
    session.commit()
    print("LAB assigned successfully")

def list_labs():
    labs = session.query(LAB).all()
    if not labs:
        print("No LABs found.")
    for lab in labs:
        print(lab)

def list_tests():
    tests = session.query(Test).all()
    if not tests:
        print("No Tests found.")
    for test in tests:
        print(test)

def view_tests_by_lab():
    lab_id = int(input("Enter LAB ID to view tests: "))
    lab = session.get(LAB,lab_id)
    if not lab:
        print("LAB with ID {lab_id} does not exist")
        return
    tests = lab.tests
    if not tests:
        print(f"No tests found for LAB with ID {lab_id}")
        return
    print(f"Tests belonging to LAB'{lab.name}' (ID {lab_id}):")
    for test in tests:
        print(test)

def main_menu():
    while True:
        print("\nWelcome to Precision Diagnostics. How can I help you?")
        print("1. Create LAB")
        print("2. Update LAB")
        print("3. Delete LAB")
        print("4. Create Test")
        print("5. Update Test")
        print("6. Delete Test")
        print("7. Assign Test to LAB")
        print("8. List LABs")
        print("9. List Tests")
        print("10. View Test by LAB")
        print("11. EXit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_lab()
        elif choice == "2":
            update_lab()
        elif choice == "3":
            delete_lab()
        elif choice == "4":
            create_test()
        elif choice == "5":
            update_test()
        elif choice == "6":
            delete_test()
        elif choice == "7":
            assign_test()
        elif choice == "8":
            list_labs()
        elif choice == "9":
            list_tests()
        elif choice == "10":
            view_tests_by_lab()
        elif choice == "11":
            print("Exiting.......")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__== "__main__":
    init_db()
    main_menu()