"""Faktorial hisoblash: musbat butun sonning faktorialini hisoblaydigan factorial deb
nomlangan funksiya yarating. (5 ning faktoriali 5 * 4 * 3 * 2 * 1 = 120)"""

def Factorial(a):
    S = 1
    i = 1
    # for i in range(1, a + 1):
    #     S *= i
    # return(S)
    while i < a + 1:
        S *= i
        i += 1
    print(S)
        
        
Factorial(5)