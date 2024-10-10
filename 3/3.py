#!/usr/bin/env python3
import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

N, M = map(int, lines[0].split())
grid = lines[1:N+1]
times = {}

for c in range(M):
    row, col = 0, c
    time = 0
    visited = set()

    while True:
        if (row, col) in visited:
            break  # L'athlète est dans une boucle infinie
        visited.add((row, col))

        if row == N:
            times[c] = time
            break  # L'athlète a atteint la ligne d'arrivée

        if not (0 <= row < N and 0 <= col < M):
            break  # L'athlète sort du bassin

        direction = grid[row][col]
        if direction == 'v':
            row += 1
        elif direction == '^':
            row -= 1
        elif direction == '>':
            col += 1
        elif direction == '<':
            col -= 1

        time += 1

        # Vérifie si l'athlète sort du bassin latéralement ou vers le haut
        if row < 0 or col < 0 or col >= M:
            break  

if times:
    min_time = min(times.values())
    result_positions = [str(c + 1) for c in range(M) if times.get(c) == min_time]
    print(' '.join(result_positions))
