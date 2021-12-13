from os.path import isfile
from sys import argv

#récpère le nom du fichier en argument de ligne de commande ou sinon le demande
def queryFile():
  fichier = ""
  for i in range(len(argv)):
    if argv[i]=="-i" and i < len(argv)-1:
      fichier = argv[i+1]
  if fichier == "":
    fichier = input("Quel fichier souhaitez-vous lire ?")
  if not isfile(fichier):
    quit("Erreur : ce fichier n'existe pas")
  return fichier


#renvoie son contenu splitté du fichier
def stock(fichier) :  
  test = open(fichier, "r")
  contenu = test.read()
  test.close()
  decompo = []
  decompo = contenu.split()
  return decompo

def ranger(decompo) :
  axiome = ''
  regles = []
  angle = 0
  niveau = 0
  taille = 10
    
  for i in range(len(decompo)) :
    if decompo[i] == 'axiome' and decompo[i+1] == '=' :
      axiome = decompo[i+2].replace('""', '')
    elif (decompo[i] == "regles" or decompo[i] == "regle")and decompo[i+1] == '=' :
      j=2
      while decompo[i+j].count('"')==2:
        regles.append(decompo[i+j].replace('"', ''))
        j+=1
    elif decompo[i] == "angle" and decompo[i+1] == '=' :
      angle = float(decompo[i+2])
    elif decompo[i] == "niveau" and decompo[i+1] == '=' :
      niveau = int(decompo[i+2])
    elif decompo[i] == "taille" and decompo[i+1] == '=' :
      taille = float(decompo[i+2])
  return(axiome, regles, angle, niveau, taille)

def getAxiomeFinal(axiome, regles, niveau):
  for m in range(niveau) :
    for regle in regles :
      p = regle.index('=')
      axiome = axiome.replace(regle[0:p], regle[p+1:])
  return axiome