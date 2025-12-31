--- Dia 15: Aflições do Armazém ---

Você aparece de volta dentro de seu próprio mini submarino! Cada historiador dirige seu mini submarino em uma direção diferente; talvez o Chefe tenha seu próprio submarino aqui em algum lugar também?

Você olha para cima para ver uma vasta escola de peixe-lanterna nadando por você. Em uma inspeção mais próxima, eles parecem bastante ansiosos, então você dirige seu mini submarino para ver se você pode ajudar.

Como as populações de peixes-lanterna crescem rapidamente, elas precisam de muito alimento e esse alimento precisa ser armazenado em algum lugar. É por isso que estes peixes-lanterna construíram elaborados complexos de armazém operados por robôs!

Esses peixes-lanterna parecem tão ansiosos porque perderam o controle do robô que opera um de seus armazéns mais importantes! Atualmente, está funcionando de forma, empurrando caixas no armazém sem consideração pela logística de peixe-lanterna ou estratégias de gerenciamento de estoque de peixe-lanterna.

Neste momento, nenhum dos peixes-lanterna é corajoso o suficiente para nadar até um robô imprevisível para que eles possam desligá-lo. No entanto, se você pudesse antecipar os movimentos do robô, talvez eles pudessem encontrar uma opção segura.

O peixe-lanterna já tem um mapa do armazém e uma lista de movimentos que o robô tentará fazer (sua entrada de quebra-cabeça). O problema é que os movimentos às vezes falham à medida que as caixas são deslocadas, tornando os movimentos reais do robô difíceis de prever.

Por exemplo:

##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^

Como o robô (@) tenta mover-se, se houver alguma caixa (O) na forma, o robô também tentará empurrar essas caixas. No entanto, se essa ação faria com que o robô ou uma caixa se movesse para uma parede (#), nada se move em vez disso, incluindo o robô. As posições iniciais destes são mostrados no mapa na parte superior do documento que o peixe-lanterna lhe deu.

O restante do documento descreve o movimentos (^ para cima, v para baixo, < para a esquerda, > por direito) que o robô tentará fazer, em ordem. (Os movimentos formam uma única sequência gigante; eles são divididos em várias linhas apenas para facilitar a cópia-colagem. As linhas novas dentro da sequência de movimento devem ser ignoradas.)

Aqui está um exemplo menor para começar:

########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<

Se o robô tentasse a sequência de movimentos, ele empurraria as caixas da seguinte forma:

Initial state:
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move <:
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move ^:
########
#.@O.O.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move ^:
########
#.@O.O.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#..@OO.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#...@OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#...@OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move v:
########
#....OO#
##..@..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##..@..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.@...#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##.....#
#..@O..#
#.#.O..#
#...O..#
#...O..#
########

Move >:
########
#....OO#
##.....#
#...@O.#
#.#.O..#
#...O..#
#...O..#
########

Move >:
########
#....OO#
##.....#
#....@O#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##.....#
#.....O#
#.#.O@.#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########

O exemplo maior tem muito mais movimentos; depois que o robô terminou esses movimentos, o armazém ficaria assim:

##########
#.O.O.OOO#
#........#
#OO......#
#OO@.....#
#O#.....O#
#O.....OO#
#O.....OO#
#OO....OO#
##########

O peixe-lanterna usa seu próprio sistema de posicionamento de mercadorias personalizado (GPS) para rastrear os locais das caixas. A coordenada GPS de uma caixa é igual a 100 vezes a sua distância da borda superior do mapa mais a sua distância da borda esquerda do mapa. (Este processo não pára em azulejos de parede; meça todo o caminho até as bordas do mapa.)

Então, a caixa mostrada abaixo tem uma distância de 1 da borda superior do mapa e 4 da borda esquerda do mapa, resultando em uma coordenada GPS de 100 * 1 + 4 = 104.

#######
#...O..
#......

O peixe-lanterna gostaria de saber o soma de todas as coordenadas GPS das caixas depois que o robô termina de se mover. No exemplo maior, a soma de todas as coordenadas GPS de todas as caixas é 10092. No exemplo menor, a soma é 2028.

Preveja o movimento do robô e das caixas no armazém. Depois que o robô termina de se mover, qual é a soma de todas as coordenadas GPS de todas as caixas?

A sua resposta de puzzle foi 1294459.

A primeira metade deste puzzle está completa! Ele fornece uma estrela dourada: *
--- Parte Dois ---

O peixe-lanterna usa suas informações para encontrar um momento seguro para nadar e desligar o robô com defeito! Assim que eles começam a preparar um festival em sua homenagem, os relatórios começam a chegar que o robô de um segundo armazém também está funcionando mal.

O layout deste armazém é surpreendentemente semelhante ao que você acabou de ajudar. Há uma diferença fundamental: tudo, exceto o robô, é duas vezes maior! A lista de movimentos do robô não muda.

Para obter o mapa do armazém mais amplo, comece com o seu mapa original e, para cada azulejo, faça as seguintes alterações:

    Se o azulejo é #, o novo mapa contém ## em vez disso.
    Se o azulejo é O, o novo mapa contém [] em vez disso.
    Se o azulejo é ., o novo mapa contém .. em vez disso.
    Se o azulejo é @, o novo mapa contém @. em vez disso.

Isso produzirá um novo mapa de armazém que é duas vezes mais largo e com caixas largas que são representadas por []. (O robô não muda de tamanho.)

O exemplo maior de antes agora ficaria assim:

####################
##....[]....[]..[]##
##............[]..##
##..[][]....[]..[]##
##....[]@.....[]..##
##[]##....[]......##
##[]....[]....[]..##
##..[][]..[]..[][]##
##........[]......##
####################

Como as caixas agora são duas vezes mais largas, mas o robô ainda tem o mesmo tamanho e velocidade, as caixas podem ser alinhadas de tal forma que empurram diretamente duas outras caixas ao mesmo tempo. Por exemplo, considere esta situação:

#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^

Depois de redimensionar apropriadamente este mapa, o robô empurraria essas caixas da seguinte forma:

Initial state:
##############
##......##..##
##..........##
##....[][]@.##
##....[]....##
##..........##
##############

Move <:
##############
##......##..##
##..........##
##...[][]@..##
##....[]....##
##..........##
##############

Move v:
##############
##......##..##
##..........##
##...[][]...##
##....[].@..##
##..........##
##############

Move v:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.......@..##
##############

Move <:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##......@...##
##############

Move <:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.....@....##
##############

Move ^:
##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############

Move ^:
##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############

Move <:
##############
##......##..##
##...[][]...##
##....[]....##
##....@.....##
##..........##
##############

Move <:
##############
##......##..##
##...[][]...##
##....[]....##
##...@......##
##..........##
##############

Move ^:
##############
##......##..##
##...[][]...##
##...@[]....##
##..........##
##..........##
##############

Move ^:
##############
##...[].##..##
##...@.[]...##
##....[]....##
##..........##
##..........##
##############

Este armazém também usa GPS para localizar as caixas. Para essas caixas maiores, as distâncias são medidas desde a borda do mapa até a borda mais próxima da caixa em questão. Então, a caixa mostrada abaixo tem uma distância de 1 da borda superior do mapa e 5 da borda esquerda do mapa, resultando em uma coordenada GPS de 100 * 1 + 5 = 105.

##########
##...[]...
##........

Na versão ampliada do exemplo maior de cima, depois que o robô terminou todos os seus movimentos, o armazém ficaria assim:

####################
##[].......[].[][]##
##[]...........[].##
##[]........[][][]##
##[]......[]....[]##
##..##......[]....##
##..[]............##
##..@......[].[][]##
##......[][]..[]..##
####################

A soma das coordenadas GPS dessas caixas é 9021.

Preveja o movimento do robô e das caixas neste novo armazém ampliado. Qual é a soma das coordenadas GPS finais de todas as caixas?
