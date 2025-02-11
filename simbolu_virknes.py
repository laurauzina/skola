print("ievadiet teikumu")
teikums=input()
ped_simb=teikums[-1]:

if ped_simb==".":
print("stāstījuma teikums")

if ped_simb=="!":
print("jautājuma teikums")

if ped_simb=="?":
print("rosinājuma teikums")

vardu_sk = len(teikums.split())
print(vardu_sk, "- vārdu skaits teikumā")
