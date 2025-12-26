from collections import Counter


def blink(contagem: dict[int, int]) -> dict[int, int]:
    temp_contagem = Counter()

    for pedra, quantidade in contagem.items():

        if pedra == 0:
            temp_contagem[1] += quantidade

        elif len(str(pedra)) % 2 == 0:
            pedras_str = str(pedra)
            metade = len(pedras_str) // 2
            esquerda = int(pedras_str[:metade])
            direita = int(pedras_str[metade:])
            temp_contagem[esquerda] += quantidade
            temp_contagem[direita] += quantidade

        else:
            temp_contagem[pedra * 2024] += quantidade

    return temp_contagem


def main(entrada: list[str], blinks: int):
    pedras = Counter(map(int, entrada))

    for b in range(blinks):
        pedras = blink(pedras)

    return sum(pedras.values())


if __name__ == '__main__':
    with open('input.txt', 'r', encoding='utf-8') as f:
        entrada = f.read().split()

    print(main(entrada, 25))
    print(main(entrada, 75))