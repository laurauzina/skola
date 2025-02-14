liel_burti=0
teikums = input()
vardi=teikums.split()
for i in range(len(teikums)):
    if teikums[i]>='A' and teikums[i]<='Z':
        liel_burti+=1
if liel_burti>0:
    print("IR DRUKATAIE")
else:
    print("NAV DRUKATIE")
for vards in vardi:
    liel_burti=0
    for i in range(len(vards)):
        if vards[i]>='A' and vards[i]<='Z':
            liel_burti+=1
    print(liel_burti, end=" ")
for i in range(len(vardi)):
    liel_burti=0
    for j in range(len(vardi[i])):
        if vardi[i][j]>='A' and vardi[i][j]<='Z':
            liel_burti+=1
if liel_burti==len(vardi[i]):
    print(i+1, end=" ")