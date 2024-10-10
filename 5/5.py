#!/usr/bin/env python3
#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

T = int(lines[0]) # Temps total disponible
N = int(lines[1]) # Nombre de figures disponibles

items = []
for i in range(N):
    Si, Pi = map(int, lines[2 + i].split())  # Si : temps pour la figure i, Pi : points pour la figure i
    max_m = min(Pi, T // Si)  # Nombre maximal de répétitions possibles pour la figure i
    for m in range(1, max_m + 1):
        net_gain = Pi - (m - 1)  # Gain net après application des malus
        if net_gain <= 0:
            break  # On arrête si le gain net devient nul ou négatif
        items.append((Si, net_gain))  # On ajoute l'item (coût, valeur) à la liste des items

# Initialisation du tableau DP
DP = [0] * (T + 1)

# Algorithme de sac à dos (0-1 Knapsack)
for cost, value in items:
    for t in range(T, cost - 1, -1):
        if DP[t - cost] + value > DP[t]:
            DP[t] = DP[t - cost] + value

# Extraction du score maximal
max_score = max(DP)
print(int(max_score))
