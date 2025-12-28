from typing import Any

VISITADOS = set()


def lados_parte_2(grupo: tuple[set[Any]] | set[tuple[int, int]], mapa: list[list[str]]) -> int:
    vertices = 0

    def vizinho(r: int, c: int) -> str:
        if 0 <= r < len(mapa) and 0 <= c < len(mapa[0]):
            return mapa[r][c]
        return ' '

    cantos = [
        ((-1, 0), (0, -1), (-1, -1)),
        ((-1, 0), (0, 1), (- 1, 1)),
        ((1, 0), (0, - 1), (1, - 1)),
        ((1, 0), (0, 1), (1, 1))
    ]

    for i, j in grupo:

        eixo = mapa[i][j]
        for k_c, l_c, m_c in cantos:
            k = vizinho(i + k_c[0], j + k_c[1])
            l = vizinho(i + l_c[0], j + l_c[1])
            m = vizinho(i + m_c[0], j + m_c[1])

            if eixo != k and eixo != l:
                vertices += 1
            elif eixo == k and eixo == l and eixo != m:
                vertices += 1

    return vertices


def perimetro_e_area_parte_1(grupo: set[tuple[int, int]]) -> tuple[int, int]:
    perimetro = 0

    for i, j in grupo:
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if (ni, nj) not in grupo:
                perimetro += 1

    return perimetro, len(grupo)


def mapear(mapa: list[list[str]], inicio: tuple[int, int], alvo: str, grupo_param: set[tuple[int, int]]) -> \
        tuple[set[Any]] | set[tuple[int, int]]:
    global VISITADOS

    altura = len(mapa)
    largura = len(mapa[0])

    i, j = inicio
    testes = [inicio]

    grupo = set() if not grupo_param else grupo_param

    if i < altura - 1:
        baixo = (i + 1, j)
        testes.append(baixo)

    if i > 0:
        cima = (i - 1, j)
        testes.append(cima)

    if j < largura - 1:
        direita = (i, j + 1)
        testes.append(direita)

    if j > 0:
        esquerda = (i, j - 1)
        testes.append(esquerda)

    for t in testes:
        i, j = t
        if (i, j) not in VISITADOS and mapa[i][j] == alvo:
            VISITADOS.add((i, j))
            grupo.add((i, j))
            mapear(mapa, (i, j), alvo, grupo)

    return grupo


def main():
    global VISITADOS

    with open('input.txt', 'r', encoding='utf-8') as f:
        mapa = [list(linha) for linha in f.read().splitlines()]

    preco_parte_1 = 0
    preco_parte_2 = 0

    visitados = set()
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if (i, j) not in VISITADOS:
                grupo = mapear(mapa, (i, j), mapa[i][j], set())

                perimetro, area = perimetro_e_area_parte_1(grupo)
                preco_parte_1 += perimetro * area
                preco_parte_2 += lados_parte_2(grupo, mapa) * area

    print(f'Total part 1: {preco_parte_1}')
    print(f'Total part 2: {preco_parte_2}')


if __name__ == '__main__':
    main()
