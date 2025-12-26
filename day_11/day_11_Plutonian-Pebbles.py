def part_1(entrada: list[str], j: int = 0) -> list[str]:
    while j <= 24:
        temp_entrada = []

        for i in range(len(entrada)):

            if entrada[i] == '0':
                temp_entrada.append('1')

            elif len(entrada[i]) % 2 == 0:
                metade = len(entrada[i]) // 2
                temp_entrada.append(str(int(entrada[i][:metade])))
                temp_entrada.append(str(int(entrada[i][metade:])))

            else:
                vezes = int(entrada[i]) * 2024
                temp_entrada.append(str(vezes))

        return part_1(temp_entrada, j + 1)

    return entrada


def main():
    with open('input.txt', 'r', encoding='utf-8') as f:
        pedras = f.read().split()

    print(len(part_1(pedras)))


if __name__ == '__main__':
    main()
