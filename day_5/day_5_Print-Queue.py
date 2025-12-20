import re
from typing import Dict, List


def part_1(regras: Dict[str, List[str]], atualizacoes: list[str]):
    total = 0
    is_valido = False

    for atualizacao in atualizacoes:
        atualizacao = atualizacao.split(',')

        for i in range(len(atualizacao) - 1):
            is_valido = False
            num_atual = atualizacao[i]
            num_proximo = atualizacao[i + 1]
            valores = regras.get(num_atual, [])

            if num_proximo in valores:
                is_valido = True
            else:
                break

        if is_valido:
            total += int(atualizacao[len(atualizacao) // 2])

    return total


def main():
    with open('protocolos.txt', 'r', encoding='utf-8') as arquivo:
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


if __name__ == '__main__':
    main()
