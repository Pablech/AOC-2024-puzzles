--- Dia 7: Reparação de Pontes ---

Os historiadores levam-no a uma ponte de corda familiar sobre um rio no meio de uma selva. O Chefe não está deste lado da ponte, no entanto; talvez ele esteja do outro lado?

Quando você vai atravessar a ponte, você percebe um grupo de engenheiros tentando repará-la. (Aparentemente, ele quebra com bastante frequência.) Você não poderá atravessar até que seja fixo.

Você pergunta quanto tempo levará; os engenheiros dizem que ele só precisa de calibrações finais, mas alguns jovens elefantes estavam brincando nas proximidades e roubaram todos os operadores de suas equações de calibração! Eles poderiam terminar as calibrações se apenas alguém pudesse determinar quais valores de teste poderiam ser produzidos colocando qualquer combinação de operadores em suas equações de calibração (sua entrada de quebra-cabeça).

Por exemplo:

190: 10 19

3267: 81 40 27

83: 17 5

156: 15 6

7290: 6 8 6 15

161011: 16 10 13

192: 17 8 14

21037: 9 7 18 13

292: 11 6 16 20

Cada linha representa uma única equação. O valor do teste aparece antes do cólon em cada linha; é seu trabalho determinar se os números restantes podem ser combinados com os operadores para produzir o valor de teste.

Os operadores são sempre avaliada da esquerda para a direita, não de acordo com as regras de precedência. Além disso, os números nas equações não podem ser reorganizados. Olhando para a selva, você pode ver elefantes segurando dois tipos diferentes de operadores: adicionar (+) e multiplicar (*).

Apenas três das equações acima podem ser tornadas verdadeiras inserindo operadores:

    190: 10 19 tem apenas uma posição que aceita um operador: entre 10 e 19. Escolhendo + daria 29, mas escolhendo * daria o valor de teste (10 * 19 = 190).
    3267: 81 40 27 tem duas posições para os operadores. Das quatro configurações possíveis dos operadores, dois fazer com que o lado direito corresponda ao valor do teste: 81 + 40 * 27 e 81 * 40 + 27 tanto iguais 3267 (quando avaliado da esquerda para a direita)!
    292: 11 6 16 20 pode ser resolvido exatamente de uma forma: 11 + 6 * 16 + 20.

Os engenheiros só precisam do resultado total de calibração, que é a soma dos valores de teste a partir de apenas as equações que poderiam ser verdadeiras. No exemplo acima, a soma dos valores de teste para as três equações listadas acima é 3749.

Determine quais equações poderiam ser verdadeiras. Qual é o resultado total da calibração?

A sua resposta de puzzle foi 3351424677624.

A primeira metade deste puzzle está completa! Ele fornece uma estrela dourada: *

--- Parte Dois ---

Os engenheiros parecem preocupados; o resultado total de calibração que você lhes deu não está nem perto de estar dentro das tolerâncias de segurança. Só então, você vê seu erro: alguns elefantes bem escondidos estão segurando um terceiro tipo de operador.

O concatenação operador (||) combina os dígitos de suas entradas esquerda e direita em um único número. Por exemplo, 12 || 345 se tornaria 12345. Todos os operadores ainda são avaliados da esquerda para a direita.

Agora, além das três equações que poderiam ser tornadas verdadeiras usando apenas adição e multiplicação, o exemplo acima tem mais três equações que podem ser tornadas verdadeiras inserindo operadores:

    156: 15 6 pode ser feito verdadeiro através de uma única concatenação: 15 || 6 = 156.
    7290: 6 8 6 15 pode ser tornado verdadeiro usando 6 * 8 || 6 * 15.
    192: 17 8 14 pode ser tornado verdadeiro usando 17 || 8 + 14.

Somando todos os seis valores de teste (os três que poderiam ser feitos antes de usar apenas + e * mais os novos três que agora podem ser feitos usando também ||) produz o novo resultado total de calibração de 11387.

Usando seu novo conhecimento de esconderijos de elefantes, determine quais equações poderiam ser verdadeiras. Qual é o resultado total da calibração?
