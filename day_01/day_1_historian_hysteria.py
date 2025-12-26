from collections import Counter


def parte_1(esquerda: list[int], direita: list[int]) -> int:
    esquerda = sorted(esquerda)
    direita = sorted(direita)
    dif = 0

    for i in range(len(esquerda)):
        l_1 = esquerda[i]
        l_2 = direita[i]
        dif += abs(l_1 - l_2)

    return dif


def parte_2(esquerda: set[int], direita: list[int]) -> int:
    total = 0

    contagem = Counter(direita)
    for num in esquerda:
        total += num * contagem.get(num, 0)

    return total


def main():
    with open('input.txt', 'r', encoding='utf-8') as arquivo:
        ids = arquivo.read()

    lista_ids = ids.split()

    esquerda, direita = [], []

    for i in range(len(lista_ids)):
        esquerda.append(int(lista_ids[i])) if i % 2 == 0 else direita.append(int(lista_ids[i]))

    print(parte_1(esquerda, direita))
    print(parte_2(set(esquerda), direita))


if __name__ == '__main__':
    main()
