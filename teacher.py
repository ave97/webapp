class Teacher:
    def __init__(self, name, email, teacher_id):
        self.name = name
        self.email = email
        self.teacher_id = teacher_id
    
    def displayInfo(self):
        print(f'Name: {self.name}, age: {self.email}, student_id: {self.teacher_id}')

    def createTest(self):
        isFinished = False
        while(isFinished):
            self.createQuestion()

    def createQuestion():
        pass

    