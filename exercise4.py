"""Uchta sonning eng kattasini topish: find_max deb nomlangan funksiya yozing,
u uchta sonni argument sifatida qabul qiladi va ularning eng kattasini qaytaradi"""

def find_max(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c 
    
a = int(input("a sonni kiriting: "))
b = int(input("b sonni kiriting: "))
c = int(input("c sonni kiriting: "))

print(find_max(a, b, c))