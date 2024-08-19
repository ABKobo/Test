# Lecture 10 part 2
class Person:
    def __init__(self, name):
        self.name = name
    def get_uppercase_name(self):
        return self.name.upper()

class Student(Person): # Person에 상속됨 (Person의 함수 가져옴)
    def __init__(self, name, major):
        self.name = name
        self.major = major
    
    def get_uppercase_major(self):
        return self.major.upper()

s = Student("Park", "Software")
print(s.get_uppercase_name())


class Pet():
    def __init__(self, name) -> None:
        self.name = name
    def cry(self):
        return self.name

class Cat(Pet):
    def cry(self):  # Cat 안에 있는 cry 실행
        return "Meow!"
    
c = Cat("Luna") 
print(c.cry())


class A:
    def hello(self):
        print("I am A")

class B(A):
    def hello(self):
        print("I am B")

class C(B):
    def hello(self):
        print("I am C")

c = C()
super(C, c).hello()  # I am B (C의 상위 B의 hello 실행)
super(B, c).hello()  # I am A (B의 상위 A의 hello 실행)


class Dog(Pet):
    def cry(self):  
        sound = super().cry() # = super(Dog, self).cry()
        sound += " doesn't cry!"
        return sound

d = Dog("Max") 
print(d.cry()) 


class Person:
    def __init__(self, name, std_no, dept):
        if type(name)!=str:
            self.name = str(name)
        if len(std_no)!=10:
            self.student_no = std_no.ljust(10, "0")
        if len(dept)==0:
            self.dept.add("Software")

class Student(Person):
    def __init__(self, name, std_no, dept, age):
        super().__init__(name, std_no, dept) # 상위 초기화 가져옴
        if age<20:
            self.age = 20


class Ancient():
    def __init__(self, name):
        self.name = name
        print("I am an ancient.")
class Mother(Ancient):
    def __init__(self, name):
        super().__init__(name)
class Father(Ancient):
    def __init__(self, name):
        self.name = name
        print("I am a father.")
class Child(Mother, Father):
    def __init__(self, name):
        super().__init__(name)

c = Child("A")
print(c.name)
print(Child.__mro__) # Child > Mother(먼저 상속) > Father > Ancient(상속의 상속) 이 순서 우선으로 실행


class Person(object):
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name):
        self.name = name

print(isinstance(1, int)) # 앞이 뒤의 Class에 속하는지 (bool)
student001 = Student("Park")
print(isinstance(student001, Student)) # True
print(isinstance(student001, Person)) # ''
print(issubclass(Student, Person)) # ''
print(issubclass(Student, object)) # ''
print(issubclass(Person, Student)) # False


class Person():
    def __init__(self, name):
        self.name = name

class Laptop():
    def __init__(self, brand):
        self.brand = brand

class Student(Person):
    def __init__(self, name, device):
        super().__init__(name)
        self.device = device

p = Person("Park")
print(p.name)
s = Student("Ko", None)
print(s.name, s.device)
s.device = Laptop("Samsung") # Student안의 변수를 Laptop으로 설정
print(s.name, s.device.brand)


class Account:
    rate = 5  # interest rate %
    def __init__(self, balance): 
        self.balance = balance
    def set_rate(value):
        Account.rate = value # 전체 이율 변경 (따로 변경 불가)
    @classmethod # 특정 class에만 적용 시키기(self가 변수라면 해당 변수의 class에 추가)
    def set_rate(cls, value):
        cls.rate = value

class HanaAccount(Account):
    pass

a1 = Account(0)
a2 = Account(0)
h1, h2 = HanaAccount(100), HanaAccount(100)
print(a1.rate, a2.rate) # 5 5

Account.set_rate(9)
print(a1.rate, a2.rate, h1.rate, h2.rate) # 9 9 9 9 
# a1 안에 rate가 없으니 Account에 찾음

HanaAccount.set_rate(10) # HanaAccount.rate = 10 (자식 class 안에 따로 rate 생성)
print(a1.rate, a2.rate, h1.rate, h2.rate) # 9 9 10 10

a1.rate = 1 # a1 자체에 rate 추가
h1.rate = 4
Account.set_rate(5) # 
print(a1.rate, a2.rate, h1.rate, h2.rate) # 1 5 4 10
# 출력 장소 > a1: a1, a2: Account, h1: h1, h2: HanaAccount

class Num:
    base = 10
    def __init__(self, number):
        self.number = number

    @classmethod
    def set_base(cls, base):
        """to safely set the base value"""
        if isinstance(base, int):
            cls.base = base
        else:
            raise ValueError # error 출력
        
class Binary(Num):
    pass

class Octal(Num):
    pass
        
Num.set_base(16) # int 아닐 시 error 출력
print(Num.base) 



Binary.set_base(2)  # Binary.set_base(Binary, 2)
print(Num.base, Binary.base) # 16 2

b = Binary(110)
b.set_base(2)  # b.set_base(Binary, 2)
print(Num.base, Binary.base) # 16 2

Octal.set_base(8)
print(Num.base, Binary.base, Octal.base) # 16 2 8


class Num:
    base = 10
    def __init__(self, number):
        self.number = number
    def __add__(self, other):
        return self.number + other.number
    
    @staticmethod  # a.def(c,d)를 무조건 cls.def(a,b,c)로 바꾸지 못하게 함
    def print_sum(a, b): 
        '''
        staticmethod 없을 시 num1.print_sum(10, 20) 에러
        def print_sum(self, a, b) > Num.print_sum(num1, num2) 에러
        '''
        print(f"The result is {a+b}")

num1 = Num(123)
num2 = Num(456)

Num.print_sum(num1, num2)
num1.print_sum(10, 20)


class Dog:
    def cry(self):
        return "Woof"
class Cat:
    def cry(self):
        return "Meow"
class Duck:
    def cry(self):
        return "Quack"

def crying(something):
    return something.cry()

dog = Dog()
cat = Cat()
duck = Duck()
print(crying(dog))  # Woof < Dog.cry(dog)
print(crying(cat))  # Meow < Cat.''
print(crying(duck))  # Quack < Duck.''


class MyName():
    def upper(self):
        return "Name"

class ABC():
    def upper(self):
        return "abc"
    
def call_upper(something):
    return something.upper()

s = "Hello"
myname = MyName()
abc = ABC()
print(call_upper(s))  # HELLO < s.upper()
print(call_upper(myname))  # Name < Myname.upper(myname)
print(call_upper(abc))  # abc < ABC.upper(abc)


class Person:
    """
    This is Person class. 설명 나옴
    """
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def get_uppercase_name(self):
        return self.name.upper()

help(Person)


class int(int): # 괄호안 int는 main에 있는 int
    """This int class is defined in __main__ scope, not built-in scope.
    This int class redefined + operator, as a+b returns a+b+1."""
    def __add__(self, other):
        """Override this method.
        To return self+other is wrong because it calls self.__add__(other).
        It is a recursive function call. """
        return self - (-other) - (-1)  # another expression of self + other + 1 (+로 입력 시 무한 루프)

a, b = int(10), int(20)
print(a+b)  # 31


class Person:
    __slots__ = ["name", "age"] # 다른 변수 추가, 변경 불가
    weight = 74 # 추가는 되지만 변경 불가 
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Park", 20)


class Person:
    def __init__(self, name, weight):
        self.name = name
        self.__weight = weight # 숨김

p = Person("Park", 90)
print(p._Person__weight) # 숨긴거 출력 방법

 
class Person:
    def __init__(self, name):
        self.name = name
        self.__do_not_override_me()
    def __do_not_override_me(self):
        print("Do not override me!")

class Student(Person):
    def __do_not_override_me(self): # 숨김
        print("Overridden!")

p = Person("Park") #Do not override me!
s = Student("Kim") #Do not override me!
p._Person__do_not_override_me() #Do not override me!
s._Student__do_not_override_me() #Overridden!

