print("ievadiet teikumu")
teikums=input()
#len(teikums):
print(len(teikums), " - simbolu skaits teikumā")

print(teikums[0], " - pirmais burts")

ped_simb=teikums[-2]
print(ped_simb, " - pēdējais burts")

print(teikums.count("a"), "- a skaits teikumā")

vardu_sk = len(teikums.split())
print(vardu_sk, "- vārdu skaits teikumā")

pirm_vards=teikums.split()[0]

print(pirm_vards, " - pirmais vārds") 