import matplotlib.pyplot as plt
from sympy import *
from sympy.plotting import *
init_printing(pretty_print=true)
import numpy as np
from pprint import pprint
tempos = np.arange(0,1,0.05)
tdhgraf = np.arange(0,24,1.2)
firstRmax = 3000
secondRmax = 1500
Ci2 = 40000
firstKs = 234
secondKs = 117
taxasRec = np.arange(0,2.5,0.5)
y = dict()
resolucoes = list()
Cx2 = symbols("Cx2")
solucao = 0


def index_in_list(a_list, index):
    return index < len(a_list)

for rec in taxasRec:
  y[rec] = list()
  print("rec=", rec)
  solucao = Ci2 + (solucao * rec)
  print("\n soy yo",solucao , "\n")
  count = 0
  flag = True

  for tempo in tempos:
    if(count % 4 == 0):
      if(flag):
        firstRmax = 3000
        firstKs = 234
        flag = False
      else:
        firstRmax = secondRmax
        firstKs = secondKs
        flag = True

    print(f"\ttdh={tempo:.2f}", f"Ci2={solucao:.2f}",  f"rmax2={firstRmax:.2f}",  f"Ks2={firstKs:.2f}")
    eqn2 = Eq(tempo,(((rec*Cx2+solucao)/(rec+1))-Cx2) / (firstRmax*Cx2/(Cx2+firstKs)))
    solucao = solve(eqn2)[1] if (index_in_list(solve(eqn2), 1)) else 0
    resolucoes.append(Eq(Cx2, solucao))
    print("\t\t",Eq(Cx2, solucao))
    y[rec].append(float(solucao))

    count = count + 1
# for yrec in y:
#   plt.plot(tdhgraf, y[yrec], label=f'rec {yrec:.2f}')

# plt.xlabel('TDH (h)')
# plt.ylabel('C (saída) (mg/L)')
# plt.title("consumodecarbono")
# plt.legend()
# plt.show()