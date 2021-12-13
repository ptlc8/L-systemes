from read import *
from dessin import *
from write import *
from verif import *

decompo = stock(queryFile())

v = verifglob(decompo)

if (not v) :
  print("FICHIER ILLISIBLE")
else :
  (axiome, regles, angle, niveau, taille) = ranger(decompo)

  axiomef = getAxiomeFinal(axiome, regles, niveau)
  dessin(axiomef, angle, taille)
  write(axiomef, angle, taille)
  exitonclick()