# Lecture 7-1

def plus_one(n):
    print(f"n is not {n} anymore.")
    n += 1
    print(f"n is {n} from now.")
    return n


result = plus_one(1)
print(result)

def plus(a, b):
    print(f"{a} plus {b} is {a+b}")
    # return a + b
result = plus(1, 2)
print(result) # None 출력 (그냥 return이라 써도 None 출력)


def op(a, b):
    p = a+b
    m = a-b
    return p,m
re = op(1,2)
print(re) #tuple
v1, v2 = op(4,3)
print(v1, v2) #각각 int


def plus():
    a = int(input("a: "))
    b = int(input("b: "))
    return a + b
result = plus()
print(result)


def function1(value):
    "This function return a sum of values in a given list"
    # do something here
    # Hint: Use for loop
    st = 0
    for i in value:
        st += i
    return st


L = [1, 2, 3, 4, 5]
result = function1(L)  # 1 + 2 + 3 + 4  + 5
print(result)


def function2(value):
    "This function return a sum of even values in a given list"
    # do something here
    # Hint: Use for loop and if statement
    st=0
    for i in value:
        if(i%2==0):
            st+=i
    return st


L = [1, 2, 3, 4, 5]
result = function2(L)  # 2 + 4
print(result)


def function3(value):
    """This function return a sum of last two values in a given list
    If a length of a list is shorter than 2, return -1
    """ 
    # do something here. Hint: Use for loop, if statement, or slicing 
    st = 0
    for i in range(1,3):
        st += value[i * -1] 
    return st


L = [1, 2, 3, 4, 5]
result = function3(L)  # 4 + 5
print(result)

def divide(a, b):
    c = a / b
    return c

result = divide(b=2, a=1) # 직접 지정으로 가능 (전부 지정해야 함)
print(result)


def divide(a, b = 10): # 먼저 지정 (한번 지정하면 뒤에도 전부 지정해야 함)
    c = a / b
    return c

result = divide(1, 2) # b = 2 로 변경
print(result)


def divide(a, b = 10):
    c = a / b
    return c

result = divide(1)  # a 만 지정 (b는 이미 정해줌)
print(result)


'''
def divide(a = 10, b): 
    return a / b
result = divide(1, 2) # 에러
print(result)
'''


def f(a, L=[]):
    L.append(a)
    return L

print(f(1))  # [1]
print(f(2))  # [1, 2]
print(f(3))  # [1, 2, 3]


def test(n :int) -> int: # 이 딴것도 가능
    return
print(test("P"))


def percentile(score):
    ratio = score / 4.3 * 100
    return ratio

scores = {"Park": 4.30, "Kim": 3.72} # scores로 값 가져옴
result = percentile(scores["Park"]) # 가져온 값으로 result 출력
print(result)  


def percentile(score, maximum=4.3):
    """to calculate a percentile of the grade"""
    ratio = score / maximum * 100
    return ratio

scores = {"Hong": 4.50, "Kang": 4.41}  
result = percentile(scores["Hong"], 4.5)
print(result)  


"""정리"""
def func(a, b=10):
    print(a)
    print(b)
    return a+b

func(1)  # = 11 positional arguments
func(1, 2)  # = 3 positional arguments
func(a=2, b=2) # = 4 keyword arguments
func(1, b=2)  # = 3 positional + keyword
# func(a=1, b)  # error


a = 1, 2  # a=(1, 2)
a, b = 1, 2  # a=1, b=2
*a, b = 1, 2, 3, 4  # a=[1, 2, 3], b=4
a, *b = 1, 2, 3, 4  # a=1, b=[2, 3, 4]
a, *b, c = 1, 2, 3, 4   # a=1, b=[2, 3], c=4
a, *b, c = (1, 2, 3, 4)   # a=1, b=[2, 3], c=4
a, *b, c = [1, 2, 3, 4]   # a=1, b=[2, 3], c=4

# *변수 는 다른 변수 외의 값을 list로 전부 가져옴


def func(*values): # 함수에서는 tuple로 가져옴
    print(values)
    for n in values:
        print(n)

func(1, 2, 3, 4) # values = (1,2,3,4)


def func(*num, val): # 함수에서 *변수는 항상 뒤에 있어야함 (아니면 에러)
    for n in num:
        print(n)

func(1, 2, val=3) # 뒤를 keyword로 바꾸면 가능


def func(a, *b, **c): # **는 dict로 가져옴
    print(a)    
    print(b)
    print(c)

func("Hi", 1, 2, name="Park", age=20)


'''
def func(a, *b, **c={'name': 'park'}): # 직접 지정 안됨
    print(a)
    print(b)
    print(c)
'''


'''
def func(**kwargs, *val): # **는 *보다 뒤에 와야함
    for k, v in kwargs.items():
        print(k, v)
'''


def func(a, b=10, *c, d, e=1, **f):
    print(a, b, c, d, e)

func(1, 2, 3, 4, d=5, e=6, f=10)  # 1 2 (3, 4) 5 6 {'f': 10}


'''
def func(positional parameters, keyword parameters):
positional: Parameters(a) > Parameters with default values(b=10) >*args(*c) (일반 값)
keyword: Parameters(d) = Parameters with default values(e=1) > **kwargs(**f) (변수 값)
'''

print(help(print)) # 명령어 도움


# 예시
def func1(a, b, c=10):
    print(a, b, c)

func1(1, 2)  # 1 2 10
func1(1, 2, 3)  # 1 2 3
func1(a=1, b=2)  # 1 2 10
func1(b=2, a=1)  # 1 2 10
func1(a=1, b=2, c=3)  # 1 2 3
func1(c=3, b=2, a=1)  # 1 2 3


def func2(a, *b, c):
    print(a, b, c)

func2(1, 2, c=3)  # 1 (2,) 3
func2(a=1, c=3)  # 1 () 3


def func3(a, *b, c=10):
    print(a, b, c)

func3(1, 2)  # 1 (2,) 10
func3(1, 2, 3)  # 1 (2, 3) 10
func3(1, 2, 3, 4)  # 1 (2, 3, 4) 10
func3(1, 2, c=3)  # 1 (2,) 3
func3(1, 2, 3, c=4) # 1 (2, 3) 4


def func4(a, *b, c=10, **d):
    print(a, b, c, d)

func4(1, 2)  # 1 (2,) 10 {}
func4(1, 2, c=3)  # 1 (2,) 3 {}
func4(1, b=2)  # 1 () 10 {'b': 2}
func4(a=1, b=2)  # 1 () 10 {'b': 2}


def func5(a, b=10, *c, d, e=20, **f):
    print(a, b, c, d, e, f)

func5(1, d=2)  
func5(1, 11, 12, 13, d=2, e=21, name="Park", age=20) 


def func6(a, b=10, *c, d, e=20, f, g):
    print(a, b, c, d, e, f, g)

func6(1, 22, 33, 44, d=1, e=2, f=3, g=4) 
func6(1, 22, 33, 44, d=1, f=2, g=3) 


'''
def func(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
앞, /: position only
*, 뒤: keyword only
'''


def plus(*, a, b):  # a, b: keyword only.
    return a + b

print(plus(a=1, b=2))  # = plus(b=2, a=1)


def plus(a, b, /):  # a, b: position only.
    return a + b

print(plus(1, 2))  # 3


def plus(a, b, /, *, c):  # a, b, c: keyword only.
    return a + b + c

print(plus(1, 2, c=3))  # 6




print(1, 2, 3)
print(1, 2, 3, sep='@') # 중간마다 @ 추가
print(1, 2, 3, end='END') # 끝에 END 추가
print(1, 2, 3, end='END', sep='@') 


def plus(a, b):
    "Return a total sum of the two parameters"    
    return a + b

print(help(plus)) # ""안에 있는 설명 출력


#연습 1
def func1(a, b, c=10):
    print(a, b, c)

func1(1, 2)  # 1 2 10
func1(1, 2, 3)  # 1 2 3
func1(a=1, b=2)  # 1 2 10
func1(b=2, a=1)  # 1 2 10
func1(a=1, b=2, c=3)  # 1 2 3
func1(c=3, b=2, a=1)  # 1 2 3
# func1(a=1, b=2, 10) 에러(포지션 먼저)

#연습 2
def func2(a, *b, c):
    print(a, b, c)

func2(1, 2, c=3)  # 1 (2,) 3
func2(a=1, c=3)  # 1 () 3
# func2(c=3) 에러(a 없음)
# func2(1, 2, 3, 4) 에러(c 없음)


#연습 3
def func3(a, *b, c=10):
    print(a, b, c)

func3(1, 2)  # 1 (2,) 10
func3(1, 2, 3)  # 1 (2, 3) 10
func3(1, 2, 3, 4)  # 1 (2, 3, 4) 10
func3(1, 2, c=3)  # 1 (2,) 3
func3(1, 2, 3, c=4) # 1 (2, 3) 4
# func3(1, b=2, c=3) 에러(키워드 1개만 있어야함)


#연습 4
def func4(a, *b, c=10, **d):
    print(a, b, c, d)

func4(1, 2)  # 1 (2,) 10 {}
func4(1, 2, c=3)  # 1 (2,) 3 {}
func4(1, b=2)  # 1 () 10 {'b': 2}
func4(a=1, b=2)  # 1 () 10 {'b': 2}
# func4(b=2, 1)  에러(포지션 먼저)
# func4(1, 2, 3, 4, a=1) 에러(a는 키워드가 아닌 포지션)


def function4(a, *value):
    "This function return a sum of the parameter value"
    # do something here
    # Hint: Use *args
    ans=0
    for i in value:
        ans += i
    return ans

result = function4(1, 2, 3)
print(result)  # 5
result = function4(1, 2, 3, 4, 5)
print(result)  # 14


#연습 5
def function5(a, *value, **info):
    "This function return a sum of the parameter value and info's values"
    # do something here
    # Hint: Use *args and **kwargs
    something = 0
    for i in value:
        something += i
    if info:
        for i in info.values():
            something += i
    return something

result = function5(1, 2, 3)
print(result)  # 5
result = function5(1, 2, 3, 4, 5)
print(result)  # 14
result = function5(1, 2, 3, b=4)
print(result)  # 9
result = function5(1, 2, 3, b=4, c=5)
print(result)  # 14


#연습 6
def factorial(n: int) -> int:
    # use for or while loop
    'Define a function that calculates factorial of a number'
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans

print(factorial(0))  # 1
print(factorial(1))  # 1 (1) 
print(factorial(5))  # 120 (1*2*3*4*5) 
print(factorial(10))  # 3628800 (1*2*3*4*5*6*7*8*9*10) 