from turtle import *

def dessin(axiome, angle, taille) :
  speed(0)
  setup(500, 500)

  memorystate = []
  pencolor((0,0,0))
  for i in axiome :
    if i == "a" : pd(); fd(taille);
    elif i == "b" : pu(); fd(taille);
    elif i == "+" : rt(angle)
    elif i == "-" : lt(angle)
    elif i == "*" : rt(180)
    elif i == "[" : memorystate.append((pos(), heading()))
    elif i == "]" :
      pu()
      place = memorystate.pop()
      goto(place[0])
      setheading(place[1])
      pd()
    elif i == "(" : taille = taille/2
    elif i == ")" : taille = taille*2
    elif i == "1": changeColor(.1, 0, 0)
    elif i == "2": changeColor(-.1, 0, 0)
    elif i == "3": changeColor(0, .1, 0)
    elif i == "4": changeColor(0, -.1, 0)
    elif i == "5": changeColor(0, 0, .1)
    elif i == "6": changeColor(0, 0, -.1)
    elif i == "{": fillcolor (pencolor()); begin_fill()
    elif i == "}": end_fill()
    elif i == "!" : pensize(pensize()*2)
    elif i == "?" : pensize(pensize()/2)

  return (axiome)

def changeColor(r,g,b):
  color = pencolor();
  pencolor((max(0, min(color[0]+r, 1)), max(0, min(color[1]+g, 1)), max(0, min(color[2]+b, 1))))

 