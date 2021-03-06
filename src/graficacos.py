import matplotlib.pyplot as pl
import math
x=[-10,-5,0,5,10]
y=return (math.cos(x*math.pi))
pl.plot(x, y, '--d')
pl.xticks([10,50,100,150,500,550,1000])
pl.xlim(-10.0,1100.0)
pl.ylim(-0.001,0.014)
pl.xlabel('Intervalos')
pl.ylabel('Tiempos en segundos')
pl.title('Tiempo')
pl.savefig("graficapi.eps", dpi=72)
pl.show()