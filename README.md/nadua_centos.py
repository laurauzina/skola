print("ievadiet centus: ")
pilnicenti = int(input())

eiro=pilnicenti//100
centi=pilnicenti%100

print(eiro," EUR ")

if centi%10==1 and centi!=11:
    print(centi," cents")
else:
    print(centi," centi")