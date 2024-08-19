def devide(a, b):
    try: # 코드 시도
        c = a / b
    except ZeroDivisionError: # 에러 종류 부합 시 에러 대신 이 코드 실행
        print("Cannot divide by 0.")
    except (NameError, KeyError): # 이 에러 중 하나만 있어도
        print("One of the two errors")
    except: # 아무 에러 있으면
        print("Another Error!")
    else: # 에러 없으면
        print("No Error")
        return ("return")
    finally: # 에러 나도 출력
        print("Done") 
        return "Finally"
print(devide(1, 2)) # No Error > Done > return > Finally 순
#  Finally는 리턴 전에 출력, Finally 안에 return은 예외


def divide(a, b):
    try:
        if b==0 :
            raise ZeroDivisionError # raise는 강제 에러 실행
        print("PRINT TEST")
        c = a / b
    except NameError:
        return "Use a defined variable."
    '''
    except ZeroDivisionError: 
        return "Division by zero" 이 코드 있으면 에러 대신 이 코드 출력
    '''
print(divide(1, 0))


try:
    print(a) # NameError 해당
except NameError as msg:
    print(msg, type(msg), isinstance(msg, NameError))


class MyError(Exception): 
    def __str__(self):
        return "Hello Error"

try:
    raise MyError
except MyError:
    print("I found MyError")
else:
    print("No error found")

class MyError(Exception): 
    def __init__(self):
        super().__init__("Hello")

try:
    raise MyError
except MyError as e:
    print(e)
else:
    print("No error found")


# 연습 1
def divide(a, b):
    """use try-except here"""
    try:
        c = a / b
    except ZeroDivisionError:
        return "Division by zero is not allowed"
    except TypeError:
        try:
            int(a) / int(b)
        except ValueError:
            return "Division by str is not allowed"
        else:
            return int(a) / int(b)
    return a / b

print(divide(1, 0)) # Division by zero is not allowed
print(divide(1, "5")) # 0.2
print(divide(1, "Hello")) # Division by str is not allowed


# 연습 2
class OhMyGodError(Exception):
    def __str__(self) -> str:
        return "Oh, my god!"


def divide(a, b):
    try:
        if b=="Python":
            raise OhMyGodError
        return a / b
    except OhMyGodError as e:
        return e 
    
print(divide(1, 10))  # No Error 0.1
print(divide(1, "Python")) # Oh, my god!
