from sys import argv

def write(axiomef, angle, taille) :
  code = "from turtle import *\nspeed(0)\nsetup(500, 500)\nmemorystate = []\npencolor((0,0,0))\ndef changeColor(r,g,b):\n\tcolor = pencolor();\n\tpencolor((max(0, min(color[0]+r, 1)), max(0, min(color[1]+g, 1)), max(0, min(color[2]+b, 1))))"
  for i in axiomef :
    if i == 'a' : code += "\npd()\nfd(" + str(taille) + ")"
    if i == 'b' : code += "\npu()\nfd(" + str(taille) + ")"
    if i == '+' : code += "\nright(" + str(angle) + ")"
    if i == '-' : code += "\nleft(" + str(angle) + ")"
    if i == '*' : code += "\nright(180)"
    if i == '[' : code += "\nmemorystate.append(pos())"
    if i == ']' : code += "pu()\nplace = memorystate.pop()\ngoto(place[0])\nsetheading(place[1])\npd()"
    elif i == "(" : taille = taille/2
    elif i == ")" : taille = taille*2
    elif i == "1": code += "\nchangeColor(.1, 0, 0)"
    elif i == "2": code += "\nchangeColor(-.1, 0, 0)"
    elif i == "3": code += "\nchangeColor(0, .1, 0)"
    elif i == "4": code += "\nchangeColor(0, -.1, 0)"
    elif i == "5": code += "\nchangeColor(0, 0, .1)"
    elif i == "6": code += "\nchangeColor(0, 0, -.1)"
    elif i == "{": code += "\nfillcolor (pencolor()); begin_fill()"
    elif i == "}": code += "\nend_fill()"
    elif i == "!": code += "\npensize(pensize()*2)"
    elif i == "?": code += "\npensize(pensize()/2)"
  code += "\nexitonclick()"
  print (code)
  fichierNom = ""
  for i in range(len(argv)):
    if argv[i]=="-o" and i < len(argv)-1:
      fichierNom = argv[i+1]
  if fichierNom == "": return
  fichiernew = open(fichierNom, 'w')
  fichiernew.write(code)
  fichiernew.close()