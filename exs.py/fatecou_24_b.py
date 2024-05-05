while True:
    direcao = 0
    N = int(input())
    if 1<=N<=1000:
        serie = str(input()).upper()
        if len(serie) == N:
            for i in range(N):
                if serie[i] == "D":
                    direcao += 1
                else:
                    direcao -= 1
                if direcao == 4 or direcao == -4:
                    direcao = 0
        else:
            break
    else:
        break
    if direcao == 0:
        print('Norte')
    elif direcao == 1 or direcao == -3:
        print('Leste')
    elif direcao == 2 or direcao == -2:
        print('Sul')
    else:
        print('Oeste')