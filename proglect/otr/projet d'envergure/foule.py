import random
#etablissement de la sous matrice de base
#initialisation
ncols = 15
nrows = 15
inj=""
matrix = [[0] * ncols for i in range(nrows)]

pop=int(input("combien de gens (max:"+str(ncols*nrows)+") : "))
cor = [[0] * 2 for i in range(pop)]
for i in range(pop):
    X=random.randint(0,ncols-1)
    Y=random.randint(0,nrows-1)
    cor[i][0]=X
    cor[i][1]=Y
    matrix[X][Y]=1
print(matrix)
print("\n")
#comportement
    #mouvement
while inj!="stop":
    for i in range(pop):
        X=random.randint(-2,2)
        Y=random.randint(-2,2)
        state=matrix[cor[i][0]][cor[i][1]]
        matrix[cor[i][0]][cor[i][1]]=0
        cor[i][0]= cor[i][0] + X
        cor[i][1]= cor[i][1] + Y
        if cor[i][0]>ncols-1:
            cor[i][0]=ncols-1
        if cor[i][1]>nrows-1:
            cor[i][1]=nrows-1
        if cor[i][0]<0:
            cor[i][0]=0
        if cor[i][1]<0:
            cor[i][1]=0
        matrix[cor[i][0]][cor[i][1]]=state
        #effet apres mouvement
    print(matrix)
    inj=input("")

