VISITADOS = set()
CONTADOR = 0


def mapear(mapa: list[list[str]], inicio: tuple[int, int], alvo: str, plantas: int = 0):
    global VISITADOS, CONTADOR

    altura = len(mapa)
    largura = len(mapa[0])

    i, j = inicio
    testes = []

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
            CONTADOR += 1
            print(f'{mapa[i][j] = } - {CONTADOR = } - {i} {j}')
            mapear(mapa, (i, j), alvo)




def main():
    global  VISITADOS

    with open('input.txt', 'r', encoding='utf-8') as f:
        mapa = [list(linha) for linha in f.read().splitlines()]


    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if (i, j) not in VISITADOS:
                # VISITADOS.add((i, j))
                mapear(mapa, (i,j), mapa[i][j])


if __name__ == '__main__':
    main()
