--- Dia 9: Fragmentador de Disco ---

Outro apertar do botão deixa você nos corredores familiares de alguns anfípodes amigáveis! Ainda bem que cada um deles tem o seu mini submarino pessoal. Os historiadores se afastam em busca do Chefe, principalmente dirigindo diretamente para as paredes.

Enquanto os historiadores rapidamente descobrem como pilotar essas coisas, você percebe um anfípode no canto lutando com seu computador. Ele está tentando fazer um espaço livre mais contíguo compactando todos os arquivos, mas seu programa não está funcionando; você se oferece para ajudar.

Ele mostra o mapa do disco (sua entrada de quebra-cabeça) que ele já gerou. Por exemplo:

2333133121414131402

O mapa de disco usa um formato denso para representar o layout de arquivos e espaço livre no disco. Os dígitos alternam entre indicar o comprimento de um arquivo e o comprimento do espaço livre.

Então, um mapa de disco como 12345 representaria um arquivo de um bloco, dois blocos de espaço livre, um arquivo de três blocos, quatro blocos de espaço livre e, em seguida, um arquivo de cinco blocos. Um mapa de disco como 90909 representaria três arquivos de nove blocos seguidos (sem espaço livre entre eles).

Cada arquivo no disco também tem um Número de identificação com base na ordem dos arquivos como eles aparecem antes eles são reorganizados, começando com o ID 0. Então, o mapa do disco 12345 tem três arquivos: um arquivo de um bloco com ID 0, um arquivo de três blocos com ID 1, e um arquivo de cinco blocos com ID 2. Usando um caractere para cada bloco onde os dígitos são o ID do arquivo e . é espaço livre, o mapa de disco 12345 representa estes blocos individuais:

0..111....22222

O primeiro exemplo acima, 2333133121414131402, representa estes blocos individuais:

00...111...2...333.44.5555.6666.777.888899

O anfípode gostaria de mover blocos de arquivo um de cada vez do final do disco para o bloco de espaço livre mais à esquerda (até que não haja lacunas restantes entre os blocos de arquivos). Para o mapa do disco 12345, o processo se parece com isso:

0..111....22222
02.111....2222.
022111....222..
0221112...22...
02211122..2....
022111222......

O primeiro exemplo requer mais alguns passos:

00...111...2...333.44.5555.6666.777.888899
009..111...2...333.44.5555.6666.777.88889.
0099.111...2...333.44.5555.6666.777.8888..
00998111...2...333.44.5555.6666.777.888...
009981118..2...333.44.5555.6666.777.88....
0099811188.2...333.44.5555.6666.777.8.....
009981118882...333.44.5555.6666.777.......
0099811188827..333.44.5555.6666.77........
00998111888277.333.44.5555.6666.7.........
009981118882777333.44.5555.6666...........
009981118882777333644.5555.666............
00998111888277733364465555.66.............
0099811188827773336446555566..............

A etapa final deste processo de compactação de arquivos é atualizar o análise de verificação do sistema de arquivos. Para calcular a soma de verificação, adicione o resultado de multiplicar cada posição desses blocos com o número de identificação do arquivo que ele contém. O bloco mais à esquerda está em posição 0. Se um bloco contiver espaço livre, pule-o em vez disso.

Continuando o primeiro exemplo, a posição dos primeiros blocos multiplicada pelo número de identificação do arquivo é 0 * 0 = 0, 1 * 0 = 0, 2 * 9 = 18, 3 * 9 = 27, 4 * 8 = 32, e assim por diante. Neste exemplo, a soma de verificação é a soma destes, 1928.

Compacte o disco rígido do anfípode usando o processo que ele solicitou. Qual é a soma de verificação do sistema de arquivos resultante? (Tenha cuidado com a cópia/colagem da entrada para este quebra-cabeça; é uma linha única e muito longa.)

A sua resposta de puzzle foi 6340197768906.

A primeira metade deste puzzle está completa! Ele fornece uma estrela dourada: *

--- Parte Dois ---

Após a conclusão, duas coisas imediatamente se tornam claras. Primeiro, o disco definitivamente tem muito mais espaço livre contíguo, assim como o anfípode esperava. Segundo, o computador está funcionando muito mais devagar! Talvez a introdução de toda essa fragmentação do sistema de arquivos tenha sido uma má ideia?

O anfípode ansioso já tem um novo plano: em vez de mover blocos individuais, ele gostaria de tentar compactar os arquivos em seu disco movendo arquivos inteiros em vez disso.

Desta vez, tente mover arquivos inteiros para o vão mais à esquerda de blocos de espaço livre que poderiam caber o arquivo. Tente mover cada arquivo exatamente uma vez, a fim de diminuir o número de identificação do arquivo, começando com o arquivo com o número de identificação de arquivo mais alto. Se não houver nenhum espaço livre à esquerda de um arquivo que seja grande o suficiente para caber no arquivo, o arquivo não se move.

O primeiro exemplo de cima agora prossegue de forma diferente:

00...111...2...333.44.5555.6666.777.888899
0099.111...2...333.44.5555.6666.777.8888..
0099.1117772...333.44.5555.6666.....8888..
0099.111777244.333....5555.6666.....8888..
00992111777.44.333....5555.6666.....8888..

O processo de atualização da soma de verificação do sistema de arquivos é o mesmo; agora, a soma de verificação deste exemplo seria 2858.

Comece de novo, agora compactando o disco rígido do anfípode usando esse novo método. Qual é a soma de verificação do sistema de arquivos resultante?
