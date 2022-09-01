import numpy as np
import time
#ce programme calcule la moyenne annuelle en fonction de chaucn de mes controles inconnus
#pour me donner la valeur la plus probable et un intervalle de confiance pour ma moyenne

#----------------initialisation---------------------
ecart=(0.0,0.25,0.5,0.75,1.0,1.25,1.5,1.75,2.0,2.25,2.5,2.75,3.0,3.25,3.5,3.75,4.0,4.25,4.5,4.75,5.0,5.25,5.5,5.75,6.0,6.25,6.5,6.75,7.0,7.25,7.5,7.75,8.0,8.25,8.5,8.75,9.0,9.25,9.5,9.75,10.0,10.25,10.5,10.75,11.0,11.25,11.5,11.75,12.0,12.25,12.5,12.75,13.0,13.25,13.5,13.75,14.0,14.25,14.5,14.75,15.0,15.25,15.5,15.75,16.0,16.25,16.5,16.75,17.0,17.25,17.5,17.75,18.0,18.25,18.5,18.75,19.0,19.25,19.5,19.75,20)
CA=0 #complement d'analyse
MNR=0 #methodes num Rapport
MNP=0 #methodes num Partiel
EDO=0
ANOVA=0
MS=0 #methodes stats
DSA=0 #droit social approfondi
TP=0 #test paramétrique
SC=0 #série chrono
values=tuple()

EDO=np.array(ecart)
SC=np.array(ecart)
DSA=np.array(ecart)
moylevi=np.array(ecart)
moywarno=np.array(ecart)
moyeric=tuple()
moyamr=np.array(ecart)
moyluce=np.array(ecart)
for i in range(len(ecart)):
      moylevi[i]=0.8*max(ecart[i],13.5)+0.2*min(ecart[i],13.5)
      moywarno[i]=0.3*17+0.7*ecart[i]
      for j in range(len(ecart)):
            moyeric+=(16*0.15+ecart[i]*0.15+0.7*ecart[j],)
      if ecart[i]>7.5:
            moyamr[i]=ecart[i]
      else:
            moyamr[i]=0.4*7.5+ecart[i]*0.6
      moyluce[i]=max(19.5/3+19/3+ecart[i]/3,19.5*0.15+19*0.15+ecart[i]*0.7)
moyeric=np.array(moyeric)
# une fois les moyennes par matières obtenues, go les analyser et faire la moyenne avec les valeurs les + probables de chaque matières
MOY=(4*moylevi.mean()+2*SC.mean()+4*moywarno.mean()+4*moyeric.mean()+4*moyamr.mean()+4*moyluce.mean()+2*EDO.mean()+2*DSA.mean()+2*12.25+2*17.7)/30
