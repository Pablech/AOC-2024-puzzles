import collections


def achar_caminho_BTF(grid, start, end, reverse=False, caminho=False):

    if reverse:
        start, end = end, start
    
    fim = grid[end[0]][end[1]]

    fila = collections.deque([start])
    visitadas = {start}
    previo = {}
    custo = {start: 1}

    while fila:
        i, j = fila.popleft()

        for ni, nj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            pi, pj = i + ni, j + nj

            if grid[pi][pj] == '#' or (pi, pj) in visitadas:
                continue

            previo[(pi, pj)] = (i, j)
            custo[(pi, pj)] = custo[(i, j)] + 1
            visitadas.add((pi, pj))

            if grid[pi][pj] == fim:
                fila.clear()
                break

            fila.append((pi, pj))

    if caminho:
        return custo, previo
    
    return custo


def resolver_1(grid, custo_S, custo_F, final):
    total = 0
    altura, largura = len(grid), len(grid[0])

    for r, c in [(2, 0), (-2, 0), (0, 2), (0, -2)]:
        for i, j in custo_S:
            ni, nj = i + r, j + c

            if 0 <= ni < altura and 0 <= nj < largura:
                if (ni, nj) in custo_F and (ni, nj in custo_S):
                    if (custo_S[(final)] - (custo_S[(i, j)] + 1 + custo_F[(ni, nj)])) >= 100:
                        total += 1
    
    return total


def resolver_2(caminho_S, start, end):
    caminho_original = []
    atual = end

    while atual != start:
        caminho_original.append(atual)
        atual = caminho_S[atual]
    
    caminho_original.append(start)
    caminho_original.reverse()

    cont = 0
    n = len(caminho_original)

    for i in range(n):
        for j in range(i + 1, n):
            pos_i = caminho_original[i]
            pos_j = caminho_original[j]

            custo = abs(pos_i[0] - pos_j[0]) + abs(pos_i[1] - pos_j[1])
            if custo <= 20:
                pasos = j - i
                economia = pasos - custo
                if economia >= 100:
                    cont += 1

    return cont
    

def main():
    with open('input.txt', 'r', encoding='utf-8') as f:
        grid = [list(linha) for linha in f.read().splitlines()]

    inicio = next(((i, row.index('S')) for i, row in enumerate(grid) if 'S' in row), None)
    final = next(((i, row.index('E')) for i, row in enumerate(grid) if 'E' in row), None)

    custo_S, previo_S  = achar_caminho_BTF(grid, start=inicio, end=final, caminho=True)
    custo_F = achar_caminho_BTF(grid, start=inicio, end=final, reverse=True)

    print(f'Parte 1: {resolver_1(grid, custo_S, custo_F, final)}')
    print(f'Parte 2: {resolver_2(previo_S, inicio, final)}')


if __name__ == '__main__':
    main()