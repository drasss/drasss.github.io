# coding: utf-8
import numpy as np
class Voiture:
      oui=45
      def __init__(self):
            self.nom = "Voiture"
      def allumer(self):
            print("La voiture démarre")

      def test(self):
            for i in range(len(self.nom)):
                  print(chr(i+97))

class VoitureSport(Voiture):

      def __init__(self):
          self.nom = "Ferrari"

kkk=Voiture()

tpl=np.array((kkk))
for i in range(10):
      np.append(tpl,kkk)
for i in range(len(tpl)):
      print(tpl[i].oui)
