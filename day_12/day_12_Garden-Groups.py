VISITADOS = set()


def perimetro_e_area(grupo: set[tuple[int, int]]) -> tuple[int, int]:
    perimetro = 0

    for i, j in grupo:
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if (ni, nj) not in grupo:
                perimetro += 1

    return perimetro, len(grupo)


def mapear(mapa: list[list[str]], inicio: tuple[int, int], alvo: str, grupo_param: set[tuple[int, int]]) -> tuple[
    int, int]:
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

    return perimetro_e_area(grupo)


def main():
    global VISITADOS

    with open('input.txt', 'r', encoding='utf-8') as f:
        mapa = [list(linha) for linha in f.read().splitlines()]

    preco = 0
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if (i, j) not in VISITADOS:
                perimetro, area = mapear(mapa, (i, j), mapa[i][j], set())
                preco += perimetro * area

    print(f'Total part 1: {preco}')


if __name__ == '__main__':
    main()
