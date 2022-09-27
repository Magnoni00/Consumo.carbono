import matplotlib.pyplot as plt
from sympy import *
from sympy.plotting import *
init_printing(pretty_print=true)
import numpy as np
from pprint import pprint
tempos = np.arange(0,1,0.05)
tdhgraf = np.arange(0,24,1.2)
rmax2 = 3000
Ci2 = 512
Ks2 = 234
taxasRec = np.arange(0,2.5,0.5)
y = dict()
resolucoes = list()
Cx2 = symbols("Cx2")

for rec in taxasRec:
  y[rec] = list()
  print("rec=", rec)
  for tempo in tempos:
    print(f"\ttdh={tempo:.2f}")
    eqn2 = Eq(tempo,(((rec*Cx2+Ci2)/(rec+1))-Cx2) / (rmax2*Cx2/(Cx2+Ks2)))
    solucao = solve(eqn2)[1]
    resolucoes.append(Eq(Cx2, solucao))
    print("\t\t",Eq(Cx2, solucao))
    y[rec].append(float(solucao))

for yrec in y:
  plt.plot(tdhgraf, y[yrec], label=f'rec {yrec:.2f}')

# plt.xlabel('TDH (h)')
# plt.ylabel('C (saída) (mg/L)')
# plt.title("consumodecarbono")
# plt.legend()
# plt.show()