ch = input("voulez vous changer les contenances des boites Y/N ")
vge = 300
vga = 100
vno = 50
vpe = 10
if ch=="Y" or ch=="y":
    vge = input("combien y a-t-il de boites dans le type géant ? ")
    vga = input("combien y a-t-il de boites dans le type grand ? ")
    vno = input("combien y a-t-il de boites dans le type moyen ? ")
    vpe = input("combien y a-t-il de boites dans le type petit ? ")
    vge=int(vge)
    vga=int(vga)
    vno=int(vno)
    vpe=int(vpe)
q=input("combien de boites voulez vous ?  ")
q=int(q)
ge = int
ge = (q-q%vge)/vge
q= q-vge*ge
ga = int
ga = (q-q%vga)/vga
q= q-vga*ga
no= int
no = (q-q%vno)/vno
q= q-vno*no
pe = int
pe = (q-q%vpe)/vpe
q= q-vpe*pe
if q!=0:
    print("on aura un colis qui ne sera pas plein c'est inconcevable !!  ")
    print("pour seulement ",q," boites!")
pe = int(pe)
no=int(no)
ga=int(ga)
ge=int(ge)
if q==0:
    print(ge,"colis de type géant (",vge,"boites)")
    print(ga,"colis de type grand (",vga,"boites)")
    print(no,"colis de type moyen (",vno,"boites)")
    print(pe,"colis de type petit (",vpe,"boites)")

