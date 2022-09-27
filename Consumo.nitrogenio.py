import matplotlib.pyplot as plt
from sympy import *
from sympy.plotting import *
init_printing(pretty_print=true)
import numpy as np
from pprint import pprint
tdh1 = np.arange(0,1,0.05)
tdhgraf= np.arange(0,24,1.2)
rmax1 = 240
Ci1= 54.5
Ks1= 12
rec1= np.arange(0,2.5,0.5)
y = dict()
resolucoes = list()
Cx1 = symbols("Cx1")

for rec in rec1:
  print("rec=",rec)
  y[rec] = list()

  for tdh in tdh1:
    print(f"\ttdh={tdh:.2f}")
    eqn1=Eq(tdh,(((rec*Cx1+Ci1)/(rec+1))-Cx1) / (rmax1*Cx1/(Cx1+Ks1)))
    solucao = solve(eqn1)[1]
    resolucoes.append(Eq(Cx1, solucao))
    print("\t\t",Eq(Cx1, solucao))
    y[rec].append(float(solucao))

x = np.linspace(0, 1, 100)
y1 = ([54.5, 40.6059958386229, 29.0291097596484, 20.4618770789121,
14.7722373813368, 11.1507521408923, 8.80192534648665,
7.2098049424219, 6.07923983302962 , 5.24278806144571,
4.60231761846384, 4.09780082567888, 3.69093376342374, 3.35631917289634,
3.07653894102323, 2.83928981686097, 2.63565508063512, 2.45902540440416,
2.30440398673506, 2.16794660276316])

y2 = ([54.5, 36.4448984186373, 22.9708572951992, 14.7722373813368, 10.2576005706936,
       7.67803571119502, 6.07923983302962, 5.01106920644036, 4.25356004636753,
       3.69093376342374, 3.25765902617313, 2.91425339569165, 2.63565508063512,
       2.405249626108, 2.2116141829834, 2.04664952977099, 1.90445983234838, 1.78065463494135,
       1.67189923733046, 1.57561652374871])

for yrec in y:
  plt.plot(tdhgraf, y[yrec], label=f'rec {yrec:.2f}')

plt.xlabel('TDH (h)')
plt.ylabel('N (saída) (mg/L)')
plt.title("Consumo de Nitrogênio")
plt.legend()
plt.show()