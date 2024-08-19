# Lecture 7-2

def func(a, b): # 1, 2
    a = a+1
    b = b+2
    print(a, b, c) # 2, 4, 3 (c는 함수 안에 없어서 밖에서 가져옴)
    return b - a # 2
# 함수 끝나면 초기화

a, b, c = 1, 2, 3 # 함수 안의 a, b와는 다른 변수
d = func(a, b) # 1, 2
print(a, b, c, d) # 1, 2, 3, 2


def func(a, b): # 1, 2
    a = a+1
    b = b+2
    c = 1
    # c = c + 1 에러
    print(a, b, c) # 2, 4, 1
    return b - a # 2
# 함수 끝나면 초기화

a, b, c = 1, 2, 3 # 함수 안의 a, b, c와는 다른 변수
d = func(a, b) # 1, 2
print(a, b, c, d) # 1, 2, 3, 2

def func(a, b): # 1, 2
    a = a+1
    b = b+2
    global c # 바깥 c 무조건 가져옴
    c = c + 1
    print(a, b, c) # 2, 4, 4
    return b - a # 2

a, b, c = 1, 2, 3 # 함수 안의 a, b와는 다른 변수
d = func(a, b) # 1, 2
print(a, b, c, d) # 1, 2, 4, 2


# 함수 안 함수
def cal(a): # 1
    b = 4
    def minus(a = 2): # 1
        b = 5
        print(a, b) # 1, 5
    # 초기화
    minus(a)
    print(a, b) # 1, 4
# 초기화

a, b = 1, 2
cal(a)
print(a, b) # 1, 2


def cal(a): # 1
    b = 4
    def minus(a = 2): # 1
        global b # 가장 바깥의 b 가져옴
        b = 5
        print(a, b) # 1, 5
    # 초기화
    minus(a)
    print(a, b) # 1, 4
# 초기화

a, b = 1, 2
cal(a)
print(a, b) # 1, 5


def cal(a): # 1
    b = 4
    def minus(a = 2): # 1
        nonlocal b # 한 칸 바깥의 b 가져옴
        b = 5
        print(a, b) # 1, 5
    # 초기화
    minus(a)
    print(a, b) # 1, 5
# 초기화

a, b = 1, 2
cal(a)
print(a, b) # 1, 2


"""
builtin > main > function
"""


s = "hello"
print(s)
print = [1, 2, 3]
print(s) # 존재하지 않음
del print # print 초기화
print(s)


a = 1
b = print
b(a) # 1


def square(num): 
    return num*num

def half(num):
    return num/2

def minus_one(num):
    return num-1

def math(func, num):
    if type(num) != int:
        return None
    result = func(num)
    return result

print(math(square, 10)) # 100
print(half(10))  # 5.0
print(minus_one(10))  # 9


def square(n):
    return n*n

L = [1, 2, 3, 4, 5]
result = map(square,  L) # 하나씩 함수에 적용
print(result)
print(list(result))


def half(n):
    return n/2

T = (2, 4, 6, 8, 10)
result = map(half, T)
print(result)
print(list(result))



def square(n):
    return n*n

L = [1, 2, 3, 4, 5]
L2 = [n*n for n in L]
L3 = [square(n) for n in L]
print(L2, L3)


square = lambda n: n*n # lambda 함수 (한 번만 사용)
result = square(10)
print(result)


def math(func, num):
    if type(num) != int:
        return None
    result = func(num)
    return result

print(math(lambda n: n*n, 10)) 



def func(n):
    print(n)
    if n==1:
        return 1 # 무한루프 방지 
    else:    
        return n + func(n-1)  # (3 + (2 + (1)))

result = func(3)  # 6
print(result)


# 연습 7
# Define a function that calculates factorial of a number

def factorial(n: int) -> int:
    # use recursive functions
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans


print(factorial(0))  # 1
print(factorial(1))  # 1 (1) 
print(factorial(5))  # 120 (1*2*3*4*5) 
print(factorial(10))  # 3628800 (1*2*3*4*5*6*7*8*9*10) 