class Student:
    def __init__(self, name, age, student_id, level):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.level = level
    
    def displayInfo(self):
        print(f'Name: {self.name}, age: {self.age}, student_id: {self.student_id}, level: {self.level}')
