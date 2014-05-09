#! encoding: utf8
# Ya puedo usar el español

import matplotlib.pylab as pl 
import numpy as np

pl.figure(figsize=(8,6), dpi=80)


X = np.linspace(-np.pi, np.pi, 256,)
C = np.cos(X*np.pi)
S = 0*(X)

pl.plot(X,C, color="cyan", linewidth=2.5, linestyle="-", label="Coseno")
pl.plot(X,S, color="black", linewidth=1.5, linestyle="-", label="Eje X")

pl.legend(loc='upper left')
#pl.xlim(-4.0,4.0)
pl.xlim(X.min()*1.1,X.max()*1.1)

#pl.xticks(np.linspace(-4,4,9,endpoint=True))
pl.xticks([-x, x])

#pl.ylim(-1.0,1.0)
pl.ylim(C.min()*1.1,C.max()*1.1)

#pl.yticks(np.linspace(-1,1,5,endpoint=True))
pl.yticks([-1, 0, +1],
          [r'$-1$', r'$0$', r'$+1$']
         )

pl.title("Representacion grafica")

pl.savefig("sencos.eps", dpi=72)

pl.show()
