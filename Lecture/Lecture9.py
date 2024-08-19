# Lecture 9
# variable_name = open(file, mode='r', encoding=None, ...)
# file: 파일 경로/이름
# mode: r: 읽기, w: 새파일, a: 추가, 

name = "Python"
f = open("./test.txt", "wt")
f.write("Hello\n")
f.writelines(["World\n", "Python\n"])
f.write(f"My name: {name}")
f.close()

f = open("./test.txt", "r")  
content = f.read() # 전체 읽기
print(content)
contents = f.readlines()  # 전체 리스트로 읽기
print(contents)
content = f.readline() # 한 줄 읽기
print(content)
content = f.readline() # 다음 줄 읽기
print(content)
f.close()  # 파일 닫기

with open("./test.txt", "r") as f: # close 필요 없음
    content = f.readline()
    while content: # 모든 줄 읽을 때 까지 반복
        print(content)
        content = f.readline 

# 연습 1-1
with open("./account.txt", "wt") as f:
    f.write("yoonseok\n")
    f.write("031020")

# 연습 1-2
tf = True
while tf:
    name = input("name: ")+"\n"
    password = input("password: ")
    with open("./account.txt", "r") as f:
        if name=="":
            break
        content = f.readline()
        if content != name:
            print("아이디가 일치하지 않습니다.")
            print(content, type(content))
            continue
        content = f.readline()
        if content != password:
            print("비밀번호가 일치하지 않습니다.")
            continue
        tf = False
        print("로그인 성공!")


def function5(*a, **b):
    sm = 0
    for i in b:
        if i[0]=='a':
            sm += b[i]
    return sm
