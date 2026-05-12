import re
import collections


def resolver_1(portas, instrucoes):
    while instrucoes:
        prox_inst = []

        for a, b, c, d in instrucoes:
            if a in portas and c in portas:
                if b == 'XOR': portas[d] = portas[a] ^ portas[c]
                elif b == 'OR': portas[d] = portas[a] | portas[c]
                elif b == 'AND': portas[d] = portas[a] & portas[c]
            else:
                prox_inst.append((a, b, c, d))
        
        instrucoes = prox_inst
    
    resultado, n = 0, 0
    for k in sorted(portas):
        if k.startswith('z'):
            resultado += portas[k] * 2 ** n
            n += 1
    
    return resultado


def resolver_2(instrucoes, portas):
    ultimo_z = max(portas)
    invalidos = set()

    for a, b, c, v in instrucoes:
        if v.startswith('z') and b != 'XOR' and v != ultimo_z:
            invalidos.add(v)

        if not v.startswith('z') and not (a[0] in 'xy' and c[0] in 'xy') and b == 'XOR':
            invalidos.add(v)

        if b == 'XOR' and (a[0] in 'xy' and c[0] in 'xy') and a[1:] != '00' and c[1:] != '00':
            for a2, b2, c2, v2 in instrucoes:
                if (v == a2 or v == c2) and b2 == 'OR':
                    invalidos.add(v)

        if b == 'AND' and (a[0] in 'xy' and c[0] in 'xy') and a[1:] != '00' and c[1:] != '00':
            for a2, b2, c2, v2 in instrucoes:
                if (v == a2 or v == c2) and b2 != 'OR':
                    invalidos.add(v)

    return ','.join(sorted(invalidos))


def main():
    with open('input.txt', 'r') as f:
        entrada = f.read()

    portas = {a: int(b) for a, b in re.findall(r'(\w+):\s*(\d+)', entrada)}
    instrucoes = re.findall(r'(\w+)\s+(AND|OR|XOR)\s+(\w+)\s*->\s*(\w+)', entrada)
    
    print(resolver_1(portas, instrucoes))
    print(resolver_2(instrucoes, portas))


if __name__ == '__main__':
    main()