import re


def part_1(arquivo: str) -> int:
    regex = r"mul\((\d{1,3}),(\d{1,3})\)"
    mul_all = re.findall(regex, arquivo)

    total = 0

    for n1, n2 in mul_all:
        total += int(n1) * int(n2)

    return total


def part_2(arquivo: str) -> int:
    regex = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
    matches = re.finditer(regex, arquivo)

    total = 0
    ativo = True

    for m in matches:
        instrucao = m.group(0)
        print(m,'\n\n')
        if instrucao == "do()":
            ativo = True
        elif instrucao == "don't()":
            ativo = False
        elif instrucao.startswith("mul") and ativo:
            n1, n2 = m.groups()[0:2]
            total += int(n1) * int(n2)

    return total


def main():
    with open('Mull.txt', 'r', encoding='utf-8') as f:
        arquivo = f.read()

    print(f'Parte 1 = {part_1(arquivo)}')

    print(f'Parte 2 = {part_2(arquivo)}')


if __name__ == '__main__':
    main()
