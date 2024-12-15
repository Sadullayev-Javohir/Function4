"""Berilgan sonning toq yoki juft ekanligini tekshiruvchi funksiya yarating"""

def ToqOrJuft(a):
    if a % 2 == 0 and a != 0:
        return f"Juft: {a}"
    elif a % 2 == 1 and a != 0:
        return f"Toq {a}"
    else:
        return f"{a} toq ham juft ham emas"
    
    
print(ToqOrJuft(-2))