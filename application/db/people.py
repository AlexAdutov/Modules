
class Employer():
    def __init__(self,name,surname,grade):
        self.name = name
        self.surname = surname
        self.grade = grade

    def get_employees(self):
        print("Into get_employees")
        return self.grade