k="""1C a soupe sirop grenadine
1C a soupe sirop de litchi 
20cl d'eau/alcool
colorant rouge
40cl jus d'orange sanguine
70cl de soda au citron (7Up)
50gr de coulis de fruits rouges
50 gr de sirop de grenadine
jus d'1/2 citron
15 gouttes de colorants rouges
10 litchis dénoyautés
10 myrtilles 
4 œufs
du mascarpone 
 biscuits a la cuillère
du café
chocolat en poudre
fraise congelé
ne 
chocolat
Pate feuuilletée (Momie a la banane, minizza ; tarte a la citrouille ?)
Ficello
baton bretzell
toast/pain de mie
tranche de cheddar
Charcuterie (toast citrouille ;minizza)
Monster munch
sauce tomate
olives noires
fromage taillable (dur)
betterave
pomme de terre
carotte
chou
bouillon
sauce tomate
potimaron
patate douce
patate 
bonbons"""
print(k)
l=k.split(sep="\n")
html="""<head>
<style type="text/css" media="all">@import "quizz.css";</style>
<title>Liste</title>
<link rel="icon" href="CHAD.jpg" />
</head>
<body>
<form>
<table >"""
for i in l:

    html+="""		<th id="question">
			"""+str(i)+"""
		</th>
		<th>
			<input type="checkbox" id="yes" name="gender" value="yes">
			<label for="yes"></label><br>
		</th>

		</th>
	</tr>"""
fichier=open("quizz.html","w")
fichier.write(html)
fichier.close()
