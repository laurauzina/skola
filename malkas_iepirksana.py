# H kg malkas, kas nepieciesami
# N malkas piegadataji
# P kg malkas saini
# C cena par vienu saini

N = int(input())
H = int(input())
maza_cena=10000

for i in range (N):
    P = int(input())
    C = int(input())
    
    saini=H//P
    if H%P>0:
        saini+=1
    cena=saini*C
    
    if cena<=maza_cena:
        maza_cena=cena
        atbilde=saini*C
print(atbilde)