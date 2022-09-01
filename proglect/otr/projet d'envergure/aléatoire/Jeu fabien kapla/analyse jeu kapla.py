import random,time
ans="0"
rand=0
prand=0
pers=tuple()
val1=tuple()
val2=tuple()
val3=tuple()
val4=tuple()
while ans!="end" and ans!="stop":
      ans=input("donne le nom d'un joueur (all)(end/stop) ")
      if ans=="all" or ans=="end" or ans=="stop":
            print(pers)
      else:
            pers+=(ans,)
print("dans ce jeu, y'a des Jengas, sur chacun est inscrit une catégorie:\n-DRINK (orange) -> tu bois sous certaines circonstances\n-Do or Drink (rouge) -> Fais un gage ou tu bois\n-Just do it (violet) -> juste... Fais ce qui sera choisi\n-Tell me (bleu) -> racontes un peu ta vie... Mais t'as bu, tu ne peux pas mentir\n choisis le jenga a faire tomber sagement... Ou perds et affrontes un sort de chaque catégorie")
random.seed(time.time())
ans="0"
i=0
while ans!="end" and ans!="stop":
      if i==(len(pers)):
            i=1
      joueur=pers[i]
      print("\n----- au tour de :[ "+pers[i]+" ] -----\n")
      prand=random.randint(0,len(pers)-1)
      while i==prand:
            prand=random.randint(0,len(pers)-1)
      Drink=("-Drink","-Take a shot","- Distribue 2 gorgées","- Bois sans les mains !","- Trinque avec "+pers[prand],"Tout le monde bois !","-Cul sec collectif","-Bois un shot fait par "+pers[prand],"-Bois un un verre fait par tout le monde","- Échange ton verre avec ton voisin d’en face et trinque","Donne physiquement à boire à "+pers[prand],"lance un dé","bois "+str(random.randint(1,6))+" gorgées","-Les possesseur de chat boivent !","-Les possesseur de chien boivent !","-Tourne 10 fois sur toi puis bois","-Bois pendant 5s","-le plus jeune bois","-le plus vieux bois","les célibataires boivent","les couples boivent",)
      dodrink=("- Je n’ai jamais ","-Lit sur les lèvre ","Banni un mot que les autres choisiront","cite 5 objets commencant par "+chr(65+random.randint(0,25)),"cite 5 animaux commencant par "+chr(65+random.randint(0,25)),"cite 5 pays commencant par "+chr(65+random.randint(0,25)),"épèle un mot choisi par les autres","Fait l’inverse de tout ce que te dit "+pers[prand],"-Trouve 3 objets le plus rapidement commençant par "+chr(65+random.randint(0,25)),"-Trouve 3 objets le plus rapidement de couleur choisie","-Fait une phrase avec 3 mots choisis par "+pers[prand],"fais deviner quelque chose en déssinant les yeux fermés","-Tente de reconnaître un objet les yeux fermés choisi par "+pers[prand],"-récite l’alphabet à l’envers","-dit 2 vérités et un mensonge ",)
      JDI=("-Chante avec de l’eau !","-	Mange un aliment les yeux fermés, choisi par "+pers[prand],"enlèves un vetement","Prochain tour tu joue les yeux bandés ","Et un glaçon, un !","-Échange ton verre avec ton voisin de Droite","-Échange ton verre avec ton voisin de Gauche","Échange ton verre avec ton voisin d’en face ","Créer un cocktail à qui tu veux !",pers[prand]+" fait ton verre !","-Raconte ta dernière journée en détails","Raconte un fait palpitant","-Mains attachées pour le prochain tour","-Chaussettes sur tes mains pendant 2 tours","-Dit pourquoi tu dois quitter "+pers[prand],"-Lit les lignes de vies de "+pers[prand]+" et raconte ce qui va lui arriver","-group photo !","action ou vérité")
      TM=("ta couleur,ta saison et ton animal préféré","qui est ton crush?","de quelle couleur sont tes sous-vetements ?","sur quel star as-tu un crush","qui est ta waifu ?","hobby favoris ?","boisson préférée ?","si tu dois tuer l'un d'entre nous qui tuerais-tu ?","si tu dois changer de corps avec l'un d'entre nous, avec qui et pourquoi ?")
      ans=str(i)
      if ans=="end" or ans=="stop":
            print(pers[i]+" a perdu\n")
      if ans=="1" or ans=="end" or ans=="stop":
            rand=random.randint(0,len(Drink)-1)
            print("\n                     "+Drink[rand])
            val1+=(rand,)
      if ans=="2" or ans=="end" or ans=="stop":
            rand=random.randint(0,len(dodrink)-1)
            print("\n                     "+dodrink[rand])
            val2+=(rand,)
      if ans=="3" or ans=="end" or ans=="stop":
            rand=random.randint(0,len(JDI)-1)
            print("\n                     "+JDI[rand])
            val3+=(rand,)
      if ans=="4" or ans=="end" or ans=="stop":
            rand=random.randint(0,len(TM)-1)
            print("\n                     "+TM[rand])
            val4+=(rand,)
      if ans=="1 ":
            print("\n                     bois 6 gorgées")
      if ans=="2 ":
            rand=random.randint(0,len(dodrink)-1)
            print("\n                     "+dodrink[rand])
      if ans=="3 ":
            print("\n                     enlèves un vetement")
      if ans=="4 ":
            print("\n                     qui est ton crush?")
      i+=1
