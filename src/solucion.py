#! /usr/bin/python
#!encoding: UTF-8
import time
import math

def f(x):
  return (math.cos(x*math.pi))
  
def biseccion(a,b,e):
  c=(a+b)/2.0
  while((f(c)!=0.000001) and (abs(b-a)>e)):
    if f(a)*f(c)<0.000001:
      b=c
    else:
      a=c
    c=(a+b)/2.0
  return c

import sys

A=float(raw_input("Introduzca el extremo inferior del intervalo (a) en el que se desea buscar la raiz: "))
B=float(raw_input("Introduzca el extremo superior del intervalo (b) en el que se desea buscar la raiz: "))
E=float(raw_input("Introduzca el margen de error a partir del cual no afecte demasiado a sus calculos: "))
if f(A)*f(B)<0.000001:
  start=time.time()
  r=biseccion(A,B,E)
  finish=time.time()-start
  print "El tiempo que ha tardado en ejecutarse el cálculo en segundos es:"
  print finish
  print "La raíz que se ha calculado en ese intervalo de forma aproximada es:%4.3f" %r
else:
  print "En el intervalo introducido no existe raíz, lo sentimos."