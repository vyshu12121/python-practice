from datetime import datetime
import json


# =========================
# STUDENT CLASS
# =========================

class Student:
    def __init__(self, name, roll_no, dob, branch, section):
        self.name = name
        self.roll_no = roll_no
        self.dob = dob
        self.branch = branch
        self.section = section

    def display(self):
        print(
            f"Name: {self.name}, "
            f"Roll No: {self.roll_no}, "
            f"DOB: {self.dob}, "
            f"Branch: {self.branch}, "
            f"Section: {self.section}"
        )


# =========================
# VALIDATE ROLL NUMBER
# =========================

def valid_roll_no(roll_no):

    if roll_no == "":
        return False

    # Only letters and numbers are allowed
    if not roll_no.isalnum():
        return False

    # At least one number is required
    if not any(char.isdigit() for char in roll_no):
        return False

    return True


# =========================
# VALIDATE DOB
# =========================

def valid_dob(dob):

    try:
        datetime.strptime(dob, "%d-%m-%Y")
        return True

    except ValueError:
        return False


# =========================
# VALIDATE BRANCH
# =========================

def valid_branch(branch):

    if branch.lower() == "none" or branch.lower() == "n/a":
        return True

    if branch == "":
        return False

    if branch.startswith("-") or branch.endswith("-"):
        return False

    if "--" in branch:
        return False

    # At least one letter is required
    if not any(char.isalpha() for char in branch):
        return False

    # Allow letters, numbers, spaces and hyphen
    for char in branch:

        if not (char.isalnum() or char == " " or char == "-"):
            return False

    return True


# =========================
# VALIDATE SECTION
# =========================

def valid_section(section):

    if section.lower() == "none" or section.lower() == "n/a":
        return True

    if section == "":
        return False

    if section.startswith("-") or section.endswith("-"):
        return False

    if "--" in section:
        return False

    # Section can contain letters
    # OR can be a single number like 1, 2, 3
    if not any(char.isalpha() for char in section):

        if not (len(section) == 1 and section.isdigit()):
            return False

    # Allow letters, numbers, spaces and hyphen
    for char in section:

        if not (char.isalnum() or char == " " or char == "-"):
            return False

    return True


# =========================
# STUDENT LIST
# =========================

students = []


# =========================
# SAVE STUDENTS
# =========================

def save_students():

    data = []

    for s in students:

        student_data = {
            "name": s.name,
            "roll_no": s.roll_no,
            "dob": s.dob,
            "branch": s.branch,
            "section": s.section
        }

        data.append(student_data)

    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)


# =========================
# LOAD STUDENTS
# =========================

def load_students():

    try:

        with open("students.json", "r") as file:

            data = json.load(file)

        for student_data in data:

            new_student = Student(
                student_data["name"],
                student_data["roll_no"],
                student_data["dob"],
                student_data["branch"],
                student_data["section"]
            )

            students.append(new_student)

    except FileNotFoundError:

        # If students.json does not exist,
        # start with an empty student list
        pass

    except json.JSONDecodeError:

        # If the JSON file is empty or damaged
        print("Warning: students.json could not be read.")


# Load saved students when program starts
load_students()


# =========================
# MAIN PROGRAM
# =========================

while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    menu = input("Enter option: ")


    # =========================
    # ADD STUDENT
    # =========================

    if menu == "1":

        roll_no = input("Enter roll number: ")

        if not valid_roll_no(roll_no):

            print(
                "Invalid roll number! "
                "Use numbers only or a combination of numbers and letters. "
                "At least one number is required."
            )

            continue


        # Check duplicate roll number
        duplicate = False

        for s in students:

            # Case-sensitive comparison
            if s.roll_no == roll_no:

                duplicate = True
                break


        if duplicate:

            print("Roll number already exists!")

            continue


        # Student name
        name = input("Enter student name: ")

        if name == "" or not name.replace(" ", "").isalpha():

            print(
                "Invalid name! "
                "Name should contain only letters."
            )

            continue


        # Date of birth
        dob = input(
            "Enter date of birth (DD-MM-YYYY): "
        )

        if not valid_dob(dob):

            print(
                "Invalid date of birth! "
                "Use DD-MM-YYYY."
            )

            continue


        # Branch
        branch = input(
            "Enter department/branch (or type 'none'): "
        )

        if not valid_branch(branch):

            print(
                "Invalid branch! "
                "Please enter a valid department/branch."
            )

            continue


        # Section
        section = input(
            "Enter section (or type 'none'): "
        )

        if not valid_section(section):

            print(
                "Invalid section! "
                "Please enter a valid section."
            )

            continue


        # Create student object
        new_student = Student(
            name,
            roll_no,
            dob,
            branch,
            section
        )

        students.append(new_student)

        # Save student to JSON
        save_students()

        print("Student added successfully!")


    # =========================
    # VIEW STUDENTS
    # =========================

    elif menu == "2":

        if len(students) == 0:

            print("No students found!")

        else:

            print("\n===== Students =====")

            for i, s in enumerate(students, start=1):
                print(f"\n===== Student {i} =====")
                print(f"Name     : {s.name}")
                print(f"Roll No  : {s.roll_no}")
                print(f"DOB      : {s.dob}")
                print(f"Branch   : {s.branch}")
                print(f"Section  : {s.section}")
                print("-------------------------")


    # =========================
    # SEARCH STUDENT
    # =========================

    elif menu == "3":

        search_roll = input(
            "Enter roll number to search: "
        )

        found = False

        for s in students:

            # Case-sensitive comparison
            if s.roll_no == search_roll:

                print("\nStudent found!")

                s.display()

                found = True

                break


        if not found:

            print("Student not found!")


    # =========================
    # UPDATE STUDENT
    # =========================

    elif menu == "4":

        update_roll = input(
            "Enter roll number to update: "
        )

        found = False

        for s in students:

            # Case-sensitive comparison
            if s.roll_no == update_roll:

                print("\nStudent found!")

                s.display()


                # New name
                new_name = input(
                    "Enter new name: "
                )

                if new_name == "" or not new_name.replace(
                    " ", ""
                ).isalpha():

                    print(
                        "Invalid name! "
                        "Name should contain only letters."
                    )

                    found = True
                    break


                # New DOB
                new_dob = input(
                    "Enter new DOB (DD-MM-YYYY): "
                )

                if not valid_dob(new_dob):

                    print(
                        "Invalid date of birth! "
                        "Use DD-MM-YYYY."
                    )

                    found = True
                    break


                # New branch
                new_branch = input(
                    "Enter new branch (or type 'none'): "
                )

                if not valid_branch(new_branch):

                    print(
                        "Invalid branch! "
                        "Please enter a valid department/branch."
                    )

                    found = True
                    break


                # New section
                new_section = input(
                    "Enter new section (or type 'none'): "
                )

                if not valid_section(new_section):

                    print(
                        "Invalid section! "
                        "Please enter a valid section."
                    )

                    found = True
                    break


                # Update details
                s.name = new_name
                s.dob = new_dob
                s.branch = new_branch
                s.section = new_section

                # Save updated data
                save_students()

                print(
                    "Student updated successfully!"
                )

                found = True

                break


        if not found:

            print("Student not found!")


    # =========================
    # DELETE STUDENT
    # =========================

    elif menu == "5":

        delete_roll = input(
            "Enter roll number to delete: "
        )

        found = False

        for s in students:

            # Case-sensitive comparison
            if s.roll_no == delete_roll:

                print("\nStudent found!")

                s.display()


                confirm = input(
                    "Are you sure you want to delete? (yes/no): "
                )


                if confirm.lower() == "yes":

                    students.remove(s)

                    # Save updated list
                    save_students()

                    print(
                        "Student deleted successfully!"
                    )

                else:

                    print("Delete cancelled.")


                found = True

                break


        if not found:

            print("Student not found!")


    # =========================
    # EXIT
    # =========================

    elif menu == "6":

        print("Program exited.")

        break


    # =========================
    # INVALID MENU OPTION
    # =========================

    else:

        print(
            "Invalid option! "
            "Please choose 1, 2, 3, 4, 5 or 6."
        )