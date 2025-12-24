import itertools


def part_1(arquivo: list[str]) -> int:
    total = 0

    for linha in arquivo:
        partes = list(map(int, linha.split()))
        total_linha = partes[0]
        numeros = partes[1:]

        for combinacao in itertools.product(['+', '*'], repeat=len(numeros) - 1):
            sub_total = numeros[0]

            i = 0
            while i < len(numeros) - 1:
                if combinacao[i] == '+':
                    sub_total += numeros[i + 1]
                elif combinacao[i] == '*':
                    sub_total *= numeros[i + 1]

                i += 1

            if sub_total == total_linha:
                total += total_linha
                break

    return total


def main():
    with open('input.txt', 'r', encoding='utf-8') as arquivo:
        arquivo = [linha.replace(':', '') for linha in arquivo.read().split('\n')]
    print(part_1(arquivo))


if __name__ == '__main__':
    main()
