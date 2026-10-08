print("Hello, GitHub!")
class student:
    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Branch: {self.branch}")
student1 = student("Vyshnavi1", 20, "CSE")
student2 = student("Vyshnavi2", 30, "CSE")
student3 = student("Vyshnavi3", 40, "CSE")

students = []

students.append(student1)
students.append(student2)
students.append(student3)

for s in students:
    s.display()
    
student1.display()
