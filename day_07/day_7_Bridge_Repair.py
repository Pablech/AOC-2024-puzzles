def resolver(alvo: int, numeros: list, acumulado: int, idx: int, parte_2: bool = False):
    if idx == len(numeros):
        return acumulado == alvo

    if acumulado > alvo:
        return False

    prox_num = numeros[idx]

    if resolver(alvo, numeros, acumulado + prox_num, idx + 1, parte_2):
        return True

    if resolver(alvo, numeros, acumulado * prox_num, idx + 1, parte_2):
        return True

    if parte_2:
        concatenados = int(str(acumulado) + str(prox_num))
        if resolver(alvo, numeros, concatenados, idx + 1, parte_2):
            return True

    return False


def main():
    with open('input.txt', 'r', encoding='utf-8') as arquivo:
        arquivo = [linha.replace(':', '') for linha in arquivo.read().split('\n')]

    i = 0
    while i <= 1:
        total = 0

        for linha in arquivo:
            partes = list(map(int, linha.split()))
            alvo, numeros = partes[0], partes[1:]

            if resolver(alvo, numeros, numeros[0], 1, False if i < 1 else True):
                total += alvo
        i += 1

        print(f'Total parte {i}: {total}')


if __name__ == '__main__':
    main()
