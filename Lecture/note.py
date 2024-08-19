class Cat():
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def __add__(self, other):
        # return something
        kitten = Cat(other.name[:2] + self.name[:2], min(self.height, other.height)/2)
        return kitten
    
cat1 = Cat("Lucy", 30)
cat2 = Cat("Maggie", 20)
kitten = cat1 + cat2
print(isinstance(kitten, Cat))
print(kitten.name)
print(kitten.height)

def get_best_seller(books):
    dic = dict()
    for i in books:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    best = max(dic.values())
    for i in books:
        if dic[i] == best:
            return i
        
get_best_seller(("book", "pen", "pen", "phone", "laptop", "phone", "phone", "laptop", "laptop", "laptop")) #returns "laptop"
get_best_seller(("book", "pen", "pen")) #returns "pen"
get_best_seller(("laptop", "phone", "phone", "phone", "laptop")) #returns "phone"

a = "ajkdlfjlkadjfdklfjk124u34jkdljflkdjfl43223jkldjfkldjkl12j1l0044jkldjklf1812j1k2jlkdjklfjdf8333jk4ljkldjflkd893jkldjfkldjf8922823jk2l3jkljdklfjdlfd9823232j32jdjflkdjf9823"
a += " "
n = 0
ans = 0
number = ''
while n != len(a):
    if a[n].isdigit():
        number += a[n]
        if a[n+1].isdigit():
            pass
        else:
            ans += int(number)
            number = ''
    n += 1

print(ans)
