def avaliar(relatorio: list[int]) -> bool:
    inverte = relatorio[0] > relatorio[-1]
    dif_validas = {1, 2, 3}

    for i in range(len(relatorio) - 1):
        l, r = relatorio[i], relatorio[i + 1]

        if inverte and l < r:
            return False
        if not inverte and l > r:
            return False

        dif = abs(l - r)

        if dif not in dif_validas:
            return False

    return True


def dampener(relatorio: list[int]) -> bool:
    if avaliar(relatorio):
        return True

    for i in range(len(relatorio)):

        temp_relatorio = relatorio.copy()
        temp_relatorio.pop(i)

        if avaliar(temp_relatorio):
            return True

    return False


def main():
    with open('input.txt', 'r', encoding='utf-8') as arquivo:
        relatorios = arquivo.read().split('\n')

    seguros = 0

    for relatorio_str in relatorios:
        relatorio_int = [int(n) for n in relatorio_str.split(' ')]

        if dampener(relatorio_int):
            seguros += 1

    print(f'{seguros = }')


if __name__ == '__main__':
    main()
