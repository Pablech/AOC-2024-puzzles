def resolver_1(alvo: str, faixas: list[str], cache: dict[str, bool]) -> bool:
    if not alvo:
        return True

    if alvo in cache:
        return cache[alvo]

    for faixa in faixas:
        if alvo.startswith(faixa):
            resto = alvo[len(faixa):]

            if resolver_1(resto, faixas, cache):
                cache[alvo] = True
                return True
    
    cache[alvo] = False
    return False


def resolver_2(alvo: str, faixas: list[str], cache: dict[str, int]) -> int:
    if not alvo:
        return 1

    if alvo in cache:
        return cache[alvo]

    total = 0

    for faixa in faixas:
        if alvo.startswith(faixa):
            resto = alvo[len(faixa):]
            
            total += resolver_2(resto, faixas, cache)

    cache[alvo] = total
    return cache[alvo]


def main():
    
    with open('input.txt', 'r', encoding='utf-8') as f:
        entrada = f.read().replace(',', '').split('\n\n')
    
    faixas = entrada[0].split()
    designs = entrada[1].split()

    cont_part_1 = 0
    cont_part_2 = 0
    for d in designs:
        cache_1 = {}
        cache_2 = {}
        total = resolver_2(d, faixas, cache_1)
        if total > 0:
            cont_part_2 += total
            cont_part_1 += 1
    
    print(f'{cont_part_1 = }')
    print(f'{cont_part_2 = }')


if __name__ == '__main__':
    main()