
# função definida para retornar a posição de uma peça de xadrez no tabuleiro segundo notação algébrica
def posPeçaTab(posiçãox, posiçãoy):

    # o tabuleiro é criado com base nos 4 pontos relativos às bordas de cada posição
    tabuleiro = []
    row = []
    for e in range(1, 9):
        for i in range(1, 9):
            pos = (e, e + 1, i, i + 1)
            row.append(pos)
        tabuleiro.append(row)
        row = []

    # através da função round, é possível inferir em qual posição a peça se encontra majoritariamente
    posx = round(posiçãox)
    posy = round(posiçãoy)

    print(tabuleiro)
    for e in range(0, 8):
        for i in range(0, 8):
            if posx == tabuleiro[e][i][0] and posy == tabuleiro[e][i][2]:
                notAlg = chr(64 + tabuleiro[e][i][0]) + str(tabuleiro[e][i][2])
                return notAlg

# função definida para retornar a matriz correspondente ao tabuleiro de xadrez. Em cada linha deste,
# há pontos relativos às bordas das posições, os quais estão armazenados em 4-tuplas
def getTable():

    # o tabuleiro é criado com base nos 4 pontos relativos às bordas de cada posição

    tabuleiro = []
    row = []
    for e in range(1, 9):
        for i in range(1, 9):
            pos = (e, e + 1, i, i + 1)
            row.append(pos)
        tabuleiro.append(row)
        row = []
    return tabuleiro

# função definida para retornar a posição de uma peça de xadrez no tabuleiro segundo a 4-tupla desta
def posPeçaTabCoords(posiçãox, posiçãoy):

    # o tabuleiro é criado com base nos 4 pontos relativos às bordas de cada posição
    tabuleiro = []
    row = []
    for e in range(1, 9):
        for i in range(1, 9):
            pos = (e, e + 1, i, i + 1)
            row.append(pos)
        tabuleiro.append(row)
        row = []

    # através da função round, é possível inferir em qual posição a peça se encontra majoritariamente
    posx = round(posiçãox)
    posy = round(posiçãoy)

    print(tabuleiro)
    for e in range(0, 8):
        for i in range(0, 8):
            if posx == tabuleiro[e][i][0] and posy == tabuleiro[e][i][2]:
                return tabuleiro[e][i]
