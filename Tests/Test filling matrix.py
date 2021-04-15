List = []
for i in range(10):
    List.append([" " for i in range(10)])


for i in range(5):
    List[i+3][1] = "A"

for i in range(6):
    List[7][i+2] = "A"


for El in List:
    print(El)

"""
(3,1)
(7,7)
6/4*3 + b = 1
36/4 +b = 1
8 + b = 0
b = -8


7-1/7-3
6/4


Penser au line filling alogirthm.
    Regarder dans quelles mesures il est applicable
        De part la présence du calcul de normale , les points sont normalement dans le bon sens .
        Etudier trois cas 1 : le cas du triangle rectangle classique ( peut poser problème lors de l'étude de la ligne horizontale)
            cas 2 : le cas du triangle quelconque orienté vers le bas (Normalement le plus simple)
            cas 3 : le cas du triangle quelconque orienté vers le haut( Valider la méthode du dessus)

        Commencer l'itération par le haut du triangle
            -> identifier le point culminant.


"""