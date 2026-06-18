from time import perf_counter

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

    for i in range(1, 3):
        total = 0

        inicio = perf_counter()
        for linha in arquivo:
            partes = list(map(int, linha.split()))
            alvo, numeros = partes[0], partes[1:]

            if resolver(alvo, numeros, numeros[0], 1, False if i < 2 else True):
                total += alvo
        fim = perf_counter()

        print(f'Total parte {i}: {total} - execusão em {fim - inicio:.4f}s.')


if __name__ == '__main__':
    main()
