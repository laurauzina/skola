saraksts = [1, 2, 3, 4, 5, 13]
print(saraksts[0])
print(saraksts[-1])

skaits=len(saraksts)
if skaits%2==0:
    print(saraksts[len(saraksts)//2], saraksts[len(saraksts)//2-1])
else:
    if skaits%2!=0:
        print(saraksts[len(saraksts//2)])
        
if 13 in saraksts:
    print("IR")
else:
    print("NAV")
    
for i in range (len(saraksts)):
    if i%2!=0:
        saraksts[i]=saraksts[i]*2
        print(saraksts[i])

for i in range (len(saraksts)):
    if i%2!=0:
        saraksts[i]=saraksts[i]*(-1)
        print(saraksts[i])
saraksts2 = []
saraksts3 = []        
for i in range (len(saraksts)):
    if i%2!=0:
        saraksts2.append(skaits[i])
        print(saraksts2)
        
for i in range (len(saraksts)):
    if i%2==0:
        saraksts3.append(skaits[i])
        print(saraksts3)
