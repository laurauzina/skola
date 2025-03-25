saraksts=("banāns", "melone", "zemene", "apelsīns", "vīnogas")
saraksts.insert("pasiflora")

gars="s"

for i in range(len(saraksts)):
    if len(vards[i])>len(gars):
        print(len(vards[i]))
'''        
if "papaija" in saraksts:
    print("IR VISMAZ VIENS")
if "karambola"in saraksts:
    print("IR VISMAZ VIENS")
else:
    print("VISMAZ VIENA NAV")    
'''

if "papaija" or "karambola" in saraksts:
    print("IR VISMAZ VIENS")
else:
    print("VISMAZ VIENA NAV")

iss="tomermaznavtikissvards"

for i in range(len(saraksts)):
    if len(vards[i])>iss:
        vards[i]=iss
        print(iss)

saraksts2=()
for i in range(len(saraksts)):
    if len(vards[i])>5:
        saraksts2.insert(vards[i])

print(saraksts)
print(saraksts2)