
def carg_berechnung(AK,EK,t):
    AK = abs(AK)
    EK = abs(EK)
    t = abs(t)
    CARG=(EK/AK)**(1/t)-1
    return CARG

x = carg_berechnung(100,700,30)

print(x)

AK=120
t=30

EK_2 = AK*(1+x)**t

print(EK_2)




