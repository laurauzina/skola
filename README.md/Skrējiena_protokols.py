print("ievadiet h1,m1,s1 un h2,m2,s2")
h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())

print(h2-h1," stundas ")

if s2<s1:
    m2=m2-1
    s2=s2+60
    
if m2<m1:
    h2-1 
    m2=m2+60

stundas=h2-h1

min=m2-m1

sekundes=s2-s1

print(stundas,min,sekundes)