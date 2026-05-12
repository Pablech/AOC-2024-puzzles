import time


def resolver_parte_1(cpus, grafo):
    cont = 0

    for a in cpus:
        vizinhos_a = grafo[a]
        for b in vizinhos_a:
            if b > a: 
                vizinhos_b = grafo[b]
                for c in vizinhos_a & vizinhos_b:
                    if c > b and (a.startswith('t') or b.startswith('t') or c.startswith('t')):
                        cont += 1

    return cont


def resolver_parte_2(grafo, grupo_atual, candidatos, processados, melhor):
    if not candidatos and not processados:
        if len(grupo_atual) > len(melhor[0]):
            melhor[0] = grupo_atual
        return

    if len(grupo_atual) + len(candidatos) <= len(melhor[0]):
        return

    pivo = list(candidatos | processados)[0]

    for v in list(candidatos - grafo[pivo]):
        resolver_parte_2(grafo, grupo_atual | {v}, candidatos & grafo[v], processados & grafo[v], melhor)
        
        candidatos.remove(v)
        processados.add(v)


def main():
    with open('input.txt', 'r') as f:
        redes = [linha.split('-') for linha in f.read().split()]
    
    grafo = dict()
    for rede in redes:
        a, b = rede
        if a not in grafo: grafo[a] = set()
        if b not in grafo: grafo[b] = set()
        grafo[a].add(b)
        grafo[b].add(a)

    cpus = list(grafo.keys())
    
    inicio = time.perf_counter()
    parte_1 = resolver_parte_1(cpus, grafo)
    fim = time.perf_counter()
    print(f'{parte_1 = }')
    print(f'Tempo de execução parte 2 = {fim - inicio:.4f}s')

    resultado = [set()]
    inicio = time.perf_counter()
    resolver_parte_2(grafo, set(), set(cpus), set(), resultado)
    fim = time.perf_counter()
    print(f'parte_2 = {",".join(sorted(resultado[0]))}')
    print(f'Tempo de execução parte 2 = {fim - inicio:.4f}s')


if __name__ == '__main__':
    main()