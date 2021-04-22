from statistics import mean
from random import uniform

NREP = 100000  # numero de vezes que o experimento é repetido
NPAS = 50     # numero de passos do caminhate
x, s = 0.0, 0.0
p = 0.8     # probabilidade de ir para a direita
mi = 0.0
xf = []

# Simulação Monte Carlo
for n in range(NREP):
    x = 0
    for m in range(NPAS):   # Passos do caminhate
        s = uniform(0, 1)
        if(s <= p):
            x = x + 1.0
    # Salva a quantidade de passos para direita
    # de cada caminhante depois de NPAS passos
    xf.append(x)

print("-=-"*18)
print(f"Probablidade de ir para a direirta:      {str(p)} ")
print(f"Numero de Passos:                        {str(NPAS}) ")
print(f"Número de Replicas de Monte Carlo:       {str(NREP}) ")
print(f"Número médio de passos para a direita:   {str(mean(xf))} ")
print(f"Número médio de passos para a direita:   {str(NPAS*p)} ")
print("-=-"*18)
