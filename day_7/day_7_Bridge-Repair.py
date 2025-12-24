import itertools
from typing import Any


def gerar_combinacoes(tamanho: int, parte_2: bool = False):
    if parte_2:
        sinais = ['+', '*', '||']
    else:
        sinais = ['+', '*']

    for combinacao in itertools.product(sinais, repeat=tamanho):
        yield combinacao


def valida_linha(total_linha: int, numeros: list[int], parte_2: bool = False) -> bool:
    for combinacao in gerar_combinacoes(len(numeros) - 1, parte_2):
        sub_total = numeros[0]

        for i, operador in enumerate(combinacao):
            proximo_num = numeros[i + 1]

            if operador == '+':
                sub_total += proximo_num
            elif operador == '*':
                sub_total *= proximo_num
            elif operador == '||':
                sub_total = int(str(sub_total) + str(proximo_num))

            if sub_total > total_linha:
                break

        if sub_total == total_linha:
            return True
    return False


def part_1(arquivo: list[str]) -> tuple[int, list[Any]]:
    total = 0
    linhas_invalidas = []

    for linha in arquivo:
        partes = list(map(int, linha.split()))
        total_linha = partes[0]
        numeros = partes[1:]

        if valida_linha(total_linha, numeros):
            total += partes[0]
        else:
            linhas_invalidas.append(linha)

    return total, linhas_invalidas


def part_2(linhas_invalidas: list[str]) -> int:
    total = 0

    for linha in linhas_invalidas:
        if not linha:
            continue
        partes = list(map(int, linha.split()))
        total_linha, numeros = partes[0], partes[1:]

        if valida_linha(total_linha, numeros, parte_2=True):
            total += total_linha

    return total


def main():
    with open('input.txt', 'r', encoding='utf-8') as arquivo:
        arquivo = [linha.replace(':', '') for linha in arquivo.read().split('\n')]

    total_part_1, arquivo_part_2 = part_1(arquivo)
    total_parte_2 = part_2(arquivo_part_2)

    print(f'Total parte 1: {total_part_1}')
    print(f'Total part 2: {total_part_1 + total_parte_2}')


if __name__ == '__main__':
    main()
