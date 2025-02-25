saraksts=[5, 1, 3, 7, 2, 6, 4]
saraksts.sort()
print(saraksts[0])
print(saraksts[-1])
summa=sum(saraksts)
print(summa)
para_saraksts=[]
for skaitlis in saraksts:
    if skaitlis%2==0:
        para_saraksts.append(skaitlis) 
print(para_saraksts)