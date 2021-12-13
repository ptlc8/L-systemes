caracteresRegleDroite = 'abcdefghijklmnopqrstuvwxyz123456*-+[]"(){}!?'
caracteresRegleGauche = 'abcdefghijklmnopqrstuvwxyz'

def verifaxiome(decompo) :
  if not 'axiome' in decompo :print("INCOMPLET : manque axiome"); return 1;
  elif decompo.count('axiome') >1 : print("probleme axiome : nombre d'axiomes > 1"); return 1;
  else :
    i = decompo.index('axiome');
    if i+2 >= len(decompo):
      print("manque la valeur de l'axiome")
      return 1
    if decompo[i+1] != '=' :
      print("problème écriture de l'axiome : manque un signe '='")
      return 1
    elif decompo[i+2].count('"') != 2 :
      print("problème écriture de l'axiome")
      return 1
    elif decompo[i+1] == '=' :
      for j in decompo[i+2] :
        if j not in caracteresRegleDroite : #TODO
          print("caractere incorrect trouvé dans l'axiome :", j)
          return 1
      return 0
    else:
      print("Erreur....")
      return 1

def verifregles(decompo) :
  if not ('regles' in decompo) and not ('regle' in decompo) :
    print("INCOMPLET : manque regles"); return 1;
  for i in range(len(decompo)) :
    if decompo[i] == 'regles' or decompo[i]== 'regle':
      if i+2 >= len(decompo):
        print("Une règle est vide")
        return 1
      if decompo[i+1] != '=': 
        print("problème écriture des regles : manque un signe '='")
        return 1
      j=2
      while decompo[i+j].count('"') == 2 :
        if not '=' in decompo[i+j] :
          print("manque '=' dans une regle")
          return 1
        l = decompo[i+j].index('=')
        gauche = decompo[i+j][1:l]
        droite = decompo[i+j][l+1:-1]
        for c in gauche :
          if not c in caracteresRegleGauche :
            print("caractere incorrect trouvé dans les regles :", c)
            return 1
        for c in droite :
          if not c in caracteresRegleDroite :
            print("caractere incorrect trouvé dans les regles :", c)
            return 1
        j+=1
  return 0

def verifangle(decompo) :
  if not 'angle' in decompo :
    print("INCOMPLET : manque angle"); return 1;
  if decompo.count('angle') >1 :
    print("probleme angle : nombre d'angles > 1"); return 1;
  for i in range(len(decompo)) :
    if decompo[i] == 'angle' :
      if i+2 >= len(decompo):
        print("manque la valeur de l'angle")
        return 1
      if decompo[i+1] != '=' :
        print("problème écriture de l'angle : manque un signe '='")
        return 1
      for j in str(decompo[i+2]) :
        if j not in '0123456789.' :
          print(decompo[i+2])
          print("caractere incorrect trouvé dans l'angle : "+j)
          return 1
  return 0

def verifniveau(decompo) :
  if not 'niveau' in decompo :
    print("INCOMPLET : manque niveau"); return 1;
  if decompo.count('niveau') >1 :
    print("probleme niveau : nombre de niveaux > 1"); return 1;
  for i in range(len(decompo)) :
    if decompo[i] == 'niveau' :
      if i+2 >= len(decompo):
        print("manque la valeur du niveau")
        return 1
      if decompo[i+1] != '=' :
        print("problème écriture du niveau : manque un signe '='")
        return 1
      for j in str(decompo[i+2]) :
        if j not in '0123456789' :
          print(decompo[i+2])
          print("caractere incorrect trouvé dans le niveau")
          return 1
  return 0

def veriftaille(decompo) :
  if decompo.count('taille') >1 :
    print("probleme taille : nombre de tailles > 1"); return 1;
  for i in range(len(decompo)) :
    if decompo[i] == 'taille' :
      if i+2 >= len(decompo):
        print("manque la valeur du taille")
        return 1
      if decompo[i+1] != '=' :
        print("problème écriture de la taille : manque un signe '='")
        return 1 
      for j in str(decompo[i+2]) :
        if j not in '0123456789.' :
          print("caractere incorrect trouvé dans la taille")
          return 1
  return 0

def verifglob(decompo) : 
    return (verifaxiome(decompo)==0 and verifregles(decompo)==0 and verifangle(decompo)==0 and verifniveau(decompo)==0 and veriftaille(decompo)==0)
