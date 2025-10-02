class Student:
    def __init__(self, name, age, grade):
        self.name = name      
        self.age = age          
        self.grade = grade      # پایه تحصیلی

    def info(self):
        print(f"نام: {self.name}")
        print(f"سن: {self.age}")
        print(f"پایه تحصیلی: {self.grade}")

student1 = Student("ali", 15, "tenth")
student1.info()
