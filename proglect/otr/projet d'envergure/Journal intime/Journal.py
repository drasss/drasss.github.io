import time,os,os.path,time
choix=""
date=time.localtime()
romancr=""
journom=("lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche")
moisnom=("janvier","fevrier","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","decembre")
mdp=input("mot de passe ?\n")
while (mdp!="3844OO"):
      mdp=input("FAUX, Réessayes\n")
while choix!="3":
      choix=input("veux-tu 1) écrire ou 2)lire 3)Arreter ")
      if choix == "1":
            roman=input("racontes moi tout\n")
            sec=str(date[5])
            if int(sec)<10:
                  sec="0"+sec
            min=str(date[4])
            if int(min)<10:
                  min="0"+min
            hour=str(date[3])
            day=str(date[2])
            if int(day)<10:
                  day="0"+day
            dayn=int(date[6])
            month=str(date[1])
            if int(month)<10:
                  month="0"+month
            year=str(date[0])
            name=str(dayn)+day+month+year+hour+min+sec      
                  #traitement du string en l'encodant
            for i in range(len(roman)):
                  romancr+=chr(ord(roman[i])-int(day))
            fichier=open("textes/"+name+".txt","x")
            fichier.write(romancr)
            fichier.close()
      if choix == "2":
            os.system("start recuptxt.bat")
            time.sleep(1)
            recup=open("recup.txt","r")
            nomfich=recup.read()+"₾"
            recup.close()
            tab=("",)
            i,j=0,0
            st=""
            while nomfich[i]!="₾":
                  while (nomfich[i]!="." or nomfich[i+1]!="t" or nomfich[i+2]!="x" or nomfich[i+3]!="t") and nomfich[i]!="₾":
                        st+=nomfich[i]
                        i+=1
                  tab+=(st,)
                  st=""
                  i+=5
            info=("",)
            print("quel fichier veux-tu lire ?\n celui fait le:")
            for i in range(1,len(tab)):
                  info+=((journom[int(tab[i][0])]+" "+tab[i][1]+tab[i][2]+" "+moisnom[int(str(tab[i][3]+tab[i][4]))-1]+" "+tab[i][5]+tab[i][6]+tab[i][7]+tab[i][8]+" à "+tab[i][9]+tab[i][10]+"h"+tab[i][11]+tab[i][12]+"m"+tab[i][13]+tab[i][14]),)
                  print(info[i]+" : "+tab[i])
            choixlect="-"
            while os.path.exists("textes\\"+choixlect+".txt")==False:
                  choixlect=input("entres le numéro du fichier que tu veux lire\n")
            lecture=open("textes\\"+choixlect+".txt","r")
            journalcr=lecture.read()
            lecture.close()
            journal=""
            for i in range(len(journalcr)):
                  journal+=chr(ord(journalcr[i])+int(choixlect[1]+choixlect[2]))
            print(journal)
