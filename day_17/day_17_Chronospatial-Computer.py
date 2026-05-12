import re

def executar_programa(valor_a, programa):
    temp_programa = {'A': valor_a, 'B': programa['B'], 'C': programa['C']}
    bits = programa['Bits']
    indx = 0
    resultado = []

    a, b, c = temp_programa['A'], temp_programa['B'], temp_programa['C']

    def shift(op):
        if op <= 3: return op
        if op == 4: return temp_programa['A']
        if op == 5: return temp_programa['B']
        if op == 6: return temp_programa['C']
        return 0

    while indx < len(bits) - 1:
        opcode, operando = bits[indx], bits[indx + 1]
        
        if opcode == 0:
            temp_programa['A'] >>= shift(operando)
        elif opcode == 1: 
            temp_programa['B'] ^= operando
        elif opcode == 2: 
            temp_programa['B'] = shift(operando) % 8
        elif opcode == 3 and temp_programa['A'] != 0:
            indx = operando
            continue
        elif opcode == 4: 
            temp_programa['B'] ^= temp_programa['C']
        elif opcode == 5:
            resultado.append(shift(operando) % 8)
        elif opcode == 6: 
            temp_programa['B'] = temp_programa['A'] >> shift(operando)
        elif opcode == 7: 
            temp_programa['C'] = temp_programa['A'] >> shift(operando)
        
        indx += 2
    return resultado

def encontrar_A(programa, a_acumulado, indx_alvo):
    if indx_alvo < 0:
        return a_acumulado

    for i in range(8):
        teste_a = (a_acumulado << 3) | i
        resultado = executar_programa(teste_a, programa)

        if resultado == programa['Bits'][indx_alvo:]:
            solucao = encontrar_A(programa, teste_a, indx_alvo - 1)
            if solucao is not None:
                return solucao
    return None


def main():
    with open('input.txt', 'r', encoding='utf-8') as f:
        p = f.read()

    entrada = list(map(int, re.findall(r'\d+|\d+,\s*', p)))
    chaves = ['A', 'B', 'C', 'Bits']
    programa = {c: list(entrada[i:]) if i > 2 else entrada[i] for i, c in enumerate(chaves)} 

    saida_p1 = executar_programa(programa['A'], programa)
    print(f'Parte 1: {','.join(map(str, saida_p1))}')

    resultado_p2 = encontrar_A(programa, 0, len(programa['Bits']) - 1)
    print(f'Valor de A: {resultado_p2}')


if __name__ == '__main__':
    main()