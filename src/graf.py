import matplotlib.pyplot as pl
import math

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