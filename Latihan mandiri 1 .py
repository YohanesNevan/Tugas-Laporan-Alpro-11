def cek(t):
    return len(set(t)) == 1
    
tA = (90,90,90,90)
print(cek(tA))

tb = (90,90,60,90)
print(cek(tb))