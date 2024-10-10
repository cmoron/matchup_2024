#!/usr/bin/env python3

import sys
import random

def main():
    lines = [line.rstrip('\n') for line in sys.stdin]

    B = int(lines[0])  # Nombre de bits
    S_bin = lines[1]
    S = int(S_bin, 2)  # Sortie cible en binaire
    N = int(lines[2])  # Nombre de nœuds

    nodes = {}
    operations = {}
    input_nodes = []
    output_node = None

    for i in range(3, 3 + N):
        parts = lines[i].split()
        op = parts[0]
        idx = int(parts[1])

        if op == "INPUT":
            nodes[idx] = {'op': op, 'inputs': [], 'outputs': [], 'index': idx}
            input_nodes.append(idx)
        else:
            inputs = list(map(int, parts[3:]))
            nodes[idx] = {'op': op, 'inputs': inputs, 'outputs': [], 'index': idx}
            for inp in inputs:
                nodes[inp]['outputs'].append(idx)
            if op == "OUTPUT":
                output_node = idx

    B_max = 1 << B  # 2^B

    for _ in range(10000):  # Essayer 10 000 fois
        # Choisir aléatoirement C et D
        C = random.randint(0, B_max - 1)
        D = random.randint(0, B_max - 1)
        E = C | D
        RHS = (E ^ S) % B_max  # Calculer RHS

        # Choisir aléatoirement B et calculer A
        B_value = random.randint(0, B_max - 1)
        A_value = (RHS - B_value) % B_max

        # Vérifier si les valeurs satisfont le circuit
        Node = {}
        Node[0] = A_value
        Node[1] = B_value
        Node[2] = C
        Node[3] = D
        Node[4] = Node[2] | Node[3]
        Node[5] = (Node[0] + Node[1]) % B_max
        Node[6] = Node[4] ^ Node[5]

        if Node[6] == S:
            # Afficher les valeurs des entrées en binaire
            for idx in [0, 1, 2, 3]:
                value = Node[idx]
                print(format(value, f'0{B}b'))
            return

    print("Pas de solution trouvée.")

if __name__ == "__main__":
    main()
