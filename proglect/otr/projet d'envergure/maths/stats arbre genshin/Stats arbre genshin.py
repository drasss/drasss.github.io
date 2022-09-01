
fichier=open("arbr.txt","r")
arbr=fichier.read()
fichier.close()
three=0
four=0
five=0
six=0
print(arbr)
for i in range(len(arbr)):
      if arbr[i]=="3":
            three+=1
      if arbr[i]=="4":
            four+=1
      if arbr[i]=="5":
            five+=1
      if arbr[i]=="6":
            six+=1
N=three+four+five+six
print("sur un total de: ",N," arbres")
sixth=N/64
fiveth=N*9/64
fourth=N*27/64
threeth=N*27/64
print("tu as eu : ",3*three+4*four+5*five+6*six," de bois")
print("ce qui représente ",(3*three+4*four+5*five+6*six)/3," arbres")
print("3 bois : ",three," fois // théorque: ",threeth)
print("4 bois : ",four," fois // théorque: ",fourth)
print("5 bois : ",five," fois // théorque: ",fiveth)
print("6 bois : ",six," fois // théorque: ",sixth)


chi2=(six-sixth)*(six-sixth)/sixth+(five-fiveth)*(five-fiveth)/fiveth+(four-fourth)*(four-fourth)/fourth+(three-threeth)*(three-threeth)/threeth
print(chi2)
print("pour info :\n chi2 0,5:1,39 0,9:4,61 0,95:5,99 0,975:7,38 0,99:9,21")

