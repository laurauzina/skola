teikums = input()
vardi=teikums.split()

# 1. uzdevums
if len(vardi)==3:
    print("1. uzdevums IR 3 SIMBOLI")
else:
    print("1. uzdevums NAV 3 SIMBOLI")

# 2. uzdevums    
if len(vardi)==3:
    print("2. uzdevums ", len(vardi)==3)
else: 
    print("2. uzdevums NAV TADU VARDU")

# 3. uzdevums
for i in range(len(vardi)):
    vardu_sk=len(vardi)
    for j in range(len(vardi[i])):
        #if vardu_sk%2==0:
    if vardu_sk==len(vardi[i]):
        print("3. uzdevums", i+1)

# 4. uzdevums
for i in range(len(vardi)):
    viens_simb=0
    if vardi[0]==vardi[i-1]:
        viens_sim=viens_simb+1
    print("4. uzdevums ", viens_simb)