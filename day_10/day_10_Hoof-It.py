def encontrar_nines(mapa: list[list[str]], i: int, j: int, valor_atual: str, part_2: bool = False) -> int | set[tuple[int, int]]:
    if mapa[i][j] == '9' and part_2:
        return 1

    if mapa[i][j] == '9'and not part_2:
        return {(i, j)}

    encontrados_int = 0
    encontrados_set = set()
    proximo_valor = str(int(valor_atual) + 1)

    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = i + di, j + dj

        if 0 <= ni < len(mapa) and 0 <= nj < len(mapa[0]):
            if mapa[ni][nj] == proximo_valor and part_2:
                encontrados_int += encontrar_nines(mapa, ni, nj, proximo_valor, True)
            if mapa[ni][nj] == proximo_valor and not part_2:
                encontrados_set.update(encontrar_nines(mapa, ni, nj, proximo_valor))
    if part_2:
        return encontrados_int

    return encontrados_set


def main(mapa: list[list[str]], part_2: bool = False):
    total_trilhas = 0

    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            if mapa[i][j] == '0':
                if part_2:
                    total_trilhas += encontrar_nines(mapa, i, j, '0', True)
                else:
                    nines_alcancados = encontrar_nines(mapa, i, j, '0')
                    total_trilhas += len(nines_alcancados)

    print(total_trilhas)


if __name__ == '__main__':
    with open('input.txt', 'r', encoding='utf-8') as f:
        mapa = [list(linha) for linha in f.read().splitlines()]

    main(mapa)
    main(mapa, True)