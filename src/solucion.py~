#! /usr/bin/python
#!encoding: UTF-8
import time
import math
import matplotlib.pyplot as pl

def f(x):
  return (math.cos(x*math.pi))
  
def biseccion(a,b,e):
  c=(a+b)/2.0
  while((f(c)!=0.00000001) and (abs(b-a)>e)):
    if f(a)*f(c)<0.00000001:
      b=c
    else:
      a=c
    c=(a+b)/2.0
  return c

import sys

A=float(raw_input("Introduzca el extremo inferior del intervalo (a) en el que se desea buscar la raiz: "))
B=float(raw_input("Introduzca el extremo superior del intervalo (b) en el que se desea buscar la raiz: "))
E=float(raw_input("Introduzca el margen de error a partir del cual no afecte demasiado a sus calculos: "))
if f(A)*f(B)<0.00000001:
  start=time.time()
  r=biseccion(A,B,E)
  finish=time.time()-start
  print "La raíz que se ha calculado en ese intervalo de forma aproximada es:%4.3f" %r
  print "El tiempo que ha tardado en ejecutarse el cálculo en segundos es:"
  print finish
  
else:
  print "En el intervalo introducido no existe raíz, lo sentimos."
  
x=int(raw_input("Introduzca el maximo valor de x para la representacion: "))
lista=[]
for i in range(x):
  y=math.cos(math.pi*i)
  lista.append(y)
  
pl.plot(range(x), lista, '--d')
pl.xticks(range(x))
pl.yticks(lista)
pl.xlabel('X')
pl.ylabel('Y')
pl.title('f(x)=cos(pix)')
pl.savefig("graficapi.eps", dpi=72)
pl.show()