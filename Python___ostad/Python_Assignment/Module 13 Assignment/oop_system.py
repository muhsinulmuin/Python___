"""
Module 13 Assignment - Smart School Management System

"""

from abc import ABC, abstractmethod


# Step 3: Abstraction Concept


class Person(ABC):

    @abstractmethod
    def display_role(self):
        """Abstract method to display role."""
        pass


# Step 4: Encapsulation & Step 6: Polymorphism


class Student(Person):

    def __init__(self, name="", age=0):
        
        # Encapsulated attributes using protected naming convention (_name, _age)
        
        
        self._name = name
        self._age = age

    # Setters and Getters for Encapsulation
    
    
    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_age(self, age):
        self._age = age

    def get_age(self):
        return self._age

    # Method Overriding for Polymorphism
    
    
    def display_role(self):
        print("Role: General Student")


# Step 5: Inheritance


class CollegeStudent(Student):

    def __init__(self, name="", age=0, student_id="", course_name=""):
        
        
        # Calling parent constructor
        
        
        super().__init__(name, age)
        self.student_id = student_id
        self.course_name = course_name

    # Method Overriding for Polymorphism
    
    
    def display_role(self):
        print("Role: College Student (Higher Education)")

    # Method to display full student details
    
    
    def display_details(self):
        print(f"Name       : {self.get_name()}")
        print(f"Age        : {self.get_age()}")
        print(f"Student ID : {self.student_id}")
        print(f"Course     : {self.course_name}")


def main():
    # Step 2: Program Introduction
    
    
    
    print("Welcome to Smart School Management System")
    print("==========================================\n")

    # Step 7: User Input Integration
    
    
    print("--- Enter Student Details ---")
    name = input("Enter Name: ").strip()

    try:
        age = int(input("Enter Age: ").strip())
    except ValueError:
        age = 0
        print("Invalid age input, set to default 0.")

    student_id = input("Enter Student ID: ").strip()
    course_name = input("Enter Course Name: ").strip()

    # Dynamic Object Creation
    

    gen_student = Student("Basic User", 18)
    col_student = CollegeStudent(name, age, student_id, course_name)

    # Step 6: Polymorphism Loop Practice
    
    
    print("\n--- Demonstrating Polymorphism ---")
    people = [gen_student, col_student]
    for person in people:
        person.display_role()

    # Step 8: Display Summary


    print("\n--- Student Details Summary ---")
    col_student.display_details()

    


if __name__ == "__main__":
    main()