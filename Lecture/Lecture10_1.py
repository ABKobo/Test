# Lecture 10 part 1

class Student: # 기본 상태 (디폴트 값) 대문자 권장
    name = None
    student_no = None
    department = None
    grade = 1
    score = 0.0

student001 = Student()
print(type(student001))   # <class '__main__.Student'>
print(student001.name) # None

student001.name = {'last':'Ko', 'first':'Yoonseok'} 
student001.student_no = '2024105233'
student001.department = 'softwareconvergence'
student001.grade = 1
student001.score = 20.0
'''
student001에만 Student가 저장됨
'''
student001.socre = 19.0 # 오타 주의 > 새 변수 생성됨
print(student001.socre)

student002 = Student()
print(student002.grade) # 1
Student.grade = None # 디폴트를 None으로 변경
print(student002.grade) # None


class Students:
    def __init__(self, name: dict, std_no: str, dept: set, grade: int, score: float): # 초기화 함수
        self.name = name
        self.student_no = std_no
        self.department = dept
        self.grade = grade
        self.score = score if score>=0.0 else 0.0
    def get_fullname(self):
        # return full name
        return self.name['last'] + " " + self.name['middle'] + " " + self.name['first']
    def add_major(self, new_dept: str):
        # add major in department
        self.department.add(new_dept)



student001 = Students({'last':'Ko', 'middle':'', 'first':'Yoonseok'}, '2024105233', {'softwareconvergence'}, 1, -20.0)
# self                      name                                        student_no  department          grade score
# 한번에 정리 가능
print(student001.score) # 음수로 0.0으로 출력

Students.email = "" # 새 변수 추가
student001.email = "koysys031@khu.ac.kr"
print(student001.email)

fullname001 = student001.get_fullname() # = Students.get_fullname(student001)
print(fullname001)
student001.add_major('ai') # = Students.add_major(student001, 'ai')
print(student001.department)


# 예시
s = 'hi'
print(s.upper())
print(str.upper(s)) # 동일


# 연습
import math
class Circle:
    def __init__(self, radius: float) -> None:
        self.r = radius if radius > 0 else 0.0
    def get_area(self):
        return math.pi * self.r**2
    def get_circumference(self):
        return 2 * math.pi * self.r

circle1 = Circle(4)
print(circle1.get_area())
print(circle1.get_circumference())


class Person:
    def __init__(self, name): 
        self.name = name
        self.age = age

age = 99
p1 = Person("Park") # 99
print(p1.age)


class Person:
    age = 1 
    def __init__(self, name): 
        self.name = name
        self.age = Person.age # 그냥 age면 global에 있는 age(99) 사용

age = 99
p1 = Person("Park") # 1
print(p1.age)


class Person:
    age = 1
    def __init__(self, name): 
        self.name = name
    def with_heart(s):
        return s + "💙"
    def get_name_with_heart(self):
        return Person.with_heart(self.name) # class 안에 있으면 class 이름 필요

    def get_name_with_heart1(self):
        return with_heart(self.name) # 밖에 있으면 필요 x
def with_heart(s):
    return s + "❤️"

p1 = Person("Park")
print(p1.get_name_with_heart(), p1.get_name_with_heart1())

# 연습 1
class Rectangle:
    def __init__(self, w: int, h: int) -> None:
        self.width = w
        self.height = h
    
    def get_area(self) -> int:
        return self.width * self.height
    
    def is_square(self) -> bool:
        return True if self.width == self.height else False 
    
    def __eq__(self, rect: object) -> bool:
        return True if self.get_area() == rect.get_area() else False
    
rect1 = Rectangle(10, 20)
rect2 = Rectangle(10, 10)
rect3 = Rectangle(20, 10)

print(rect1.get_area())  # 200
print(rect1.is_square())  # False
print(rect2.get_area())  # 100
print(rect2.is_square())  # True
print(rect1==rect2)  # False
print(rect1==rect3)  # True


# 연습 2
class Person:
    def __init__(self, n: str, h: int =30) -> None:
        self.name = n
        self.height = h if h >30 else 30
    
    def get_uppercase_name(self) -> str:
        return self.name.upper()
    
    def __eq__(self, other: object) -> bool:
        return True if self.name == other.name else False
    
    def __len__(self) -> int:
        return self.height
        
p1 = Person("Park", 174)
print(p1.name, p1.height)
p2 = Person("Kim", 16)
print(p2.name, p2.height)
p3 = Person("Park")
print(p3.name, p3.height)

print(p1.get_uppercase_name())
print(p2.get_uppercase_name())

print(p1==p2)
print(p1==p3)

print(len(p1), p1.__len__(), Person.__len__(p1))


# 연습 3
class Account:
    def __init__(self, balance: int = 0):
        """Set balance attribute to the instance."""
        self.balance = balance
    def deposit(self, money: int) -> None:
        """Deposit a cash of the money to the balance."""
        self.balance += money
    def withdraw(self, money: int) -> None:
        """Withdraw a cash of the money from the balance."""
        self.balance -= money
    def __eq__(self, other) -> bool:
        """Return True if the balance of the two instances are same. 
        False, otherwise."""
        return True if self.balance == other.balance else False
    
account1 = Account(1000)
account2 = Account(2000)
print(account1.balance, account2.balance)  # 1000 2000
print(account1==account2)  # False

account1.deposit(500) 
account2.withdraw(500)
print(account1.balance, account2.balance)  # 1500 1500
print(account1==account2)  # True