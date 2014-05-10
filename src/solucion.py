#! /usr/bin/python
#!encoding: UTF-8
import time
import math
import matplotlib.pyplot as pl
import numpy as np
import numpy as np
import sys

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
  print "No podemos asegurar que en el intervalo introducido exista raíz, lo sentimos."
  
x=int(raw_input("Introduzca el maximo valor de x para la representacion: "))
lista=[]
for i in range(x):
  y=math.cos(math.pi*i)
  lista.append(y)
  

pl.figure(figsize=(8,6), dpi=80)

X = np.linspace(-x, x, 256, endpoint=True)
C = np.cos(X*np.pi)
S = 0*(X)

pl.plot(X,C, color="cyan", linewidth=2.5, linestyle="-", label="Coseno")
pl.plot(X,S, color="black", linewidth=1.5, linestyle="-", label="Eje X")
pl.legend(loc='upper left')
pl.xlim(X.min()*1.1,X.max()*1.1)
pl.ylim(C.min()*1.1,C.max()*1.1)
pl.yticks([-1, 0, +1])
pl.title("Representacion grafica")
pl.savefig("cos.jpeg", dpi=72)
pl.show()


