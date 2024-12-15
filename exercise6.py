"""Fibonachchi ketma-ketligi: n ta hadni qabul qilib, Fibonachchi ketma-ketligining
birinchi n ta hadini ro'yxat ko'rinishida qaytaradigan fibonacci deb nomlangan 
funksiya yozing"""

def fibonachchi(n):
    finbonachison = [0, 1]
    
    for i in range(2, n):
        finbonachison.append(finbonachison[i - 1] + finbonachison[i - 2])
    return finbonachison

print(fibonachchi(10))