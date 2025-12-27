import re


def resolver(valores: list[tuple[int, int]], adicionar: int):
    button_a, button_b, prize = valores

    xa, ya = button_a
    xb, yb = button_b
    x, y = prize

    deter = xa * yb - xb * ya
    deter_a = (x + adicionar) * yb - (y + adicionar) * xb
    deter_b = xa * (y + adicionar) - ya * (x + adicionar)

    a = deter_a // deter
    b = deter_b // deter

    if deter_a % deter == 0 and deter_b % deter == 0:
        return (a * 3) + b

    return 0


def main():
    with open('input.txt', 'r', encoding='utf-8') as f:
        maquinas = f.read().strip().split('\n\n')

    dict_maquinas = {}

    for i, maquina in enumerate(maquinas):
        dict_maquinas['maquina' + str(i)] = []

        linhas = maquina.splitlines()
        for linha in linhas:
            x, y = re.findall(r'\d+', linha)
            dict_maquinas['maquina' + str(i)].append((int(x), int(y)))

    i = 0
    while i <= 1:
        total = 0
        adicionar = 10000000000000 if i > 0 else 0

        for valores in dict_maquinas.values():
            total += resolver(valores, adicionar)

        i += 1

        print(f'Total part {i}: {total}')


if __name__ == '__main__':
    main()
