import re
from typing import Dict, List


def valida_atualizacao(regras_dict: Dict[str, List[str]], atualizacao: List[str]) -> bool:
    for i in range(len(atualizacao) - 1):
        atual = atualizacao[i]
        proximo = atualizacao[i + 1]
        valores = regras_dict.get(atual, [])

        if proximo not in valores:
            return False

    return True


def ordenar(regras_dict: Dict[str, List[str]], atualizacao: List[str]) -> List[str]:
    alterado = True

    while alterado:
        alterado = False
        for i in range(len(atualizacao) - 1):
            atual = atualizacao[i]
            proximo = atualizacao[i + 1]
            valores = regras_dict.get(atual, [])

            if valores is None or proximo not in valores:
                atualizacao[i], atualizacao[i + 1] = proximo, atual
                alterado = True

    return atualizacao


def part_2(regras_dict: Dict[str, List[str]], atualizacoes: List[str]) -> int:
    total = 0

    for atualizacao in atualizacoes:
        atualizacao = atualizacao.split(',')

        if not valida_atualizacao(regras_dict, atualizacao):
            atualizacao = ordenar(regras_dict, atualizacao)
            total += int(atualizacao[len(atualizacao) // 2])

    return total


def part_1(regras_dict: Dict[str, List[str]], atualizacoes: List[str]) -> int:
    total = 0

    for atualizacao in atualizacoes:
        atualizacao = atualizacao.split(',')

        if valida_atualizacao(regras_dict, atualizacao):
            total += int(atualizacao[len(atualizacao) // 2])

    return total


def main():
    with open('input.txt', 'r', encoding='utf-8') as arquivo:
        arquivo = arquivo.read()

    regex = r'(\d{2})\|(\d{2})'
    regras = re.findall(regex, arquivo)

    regex = r'\d+(?:,\d+)+'
    atualizacoes = re.findall(regex, arquivo)

    dicionario_regras = {}
    for esq, dir in regras:
        if esq not in dicionario_regras:
            dicionario_regras[esq] = []
        dicionario_regras[esq].append(dir)

    print(part_1(dicionario_regras, atualizacoes))
    print(part_2(dicionario_regras, atualizacoes))


if __name__ == '__main__':
    main()
