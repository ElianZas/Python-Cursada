import random

#00 01 02  10 11 12
TColumnas=[['    ','    ','    '],['    ','    ','    '],['    ','    ','    ']]
TNumeros=[[7,4,1],[8,5,2],[9,6,3]]
TX=[[' X  ',' X  ',' X  '],[' X  ',' X  ',' X  '],[' X  ',' X  ',' X  ']]
TO=[[' O  ',' O  ',' O  '],[' O  ',' O  ',' O  '],[' O  ',' O  ',' O  ']]

print('Bienvenid@ al TATETI')
def tablero_juego():
    print(' ┄┄┄┄TABLERO┄┄┄')
    for i in range (3):
        print(TColumnas[0][i]+'┊',end="")
        print(TColumnas[1][i]+'┊',end="")
        print(TColumnas[2][i])
        print(' ┄┄┄┄┄┄┄┄┄┄┄┄┄┄')
def tablero_ref():
    for i in range (3):
        print(end="    ")
        print(TNumeros[0][i],end="┊")
        print(TNumeros[1][i],end="┊")
        print(TNumeros[2][i])
        print('    ┄┄┄┄┄')
def eligesimbolo():
    print('\n1-X\n2-O')
    símbolo=int(input('¿Qué símbolo desea usar?: '))
    print(símbolo)
    return símbolo
def jugador1():
        if símbolo==1:
            print('TU TURNO')
            print('SU SIMBOLO: X')
            print('¿Dónde desea colocarlo?')
            tablero_juego()
            posición=int(input())
            if posición<=9 or posición>=0:
                for j in range(3):
                    for i in range(3):
                        if TNumeros[j][i]==posición:
                            if TColumnas[j][i]=='    ':
                                TColumnas[j][i]=' X  '
                                tablero_juego()
                                True
                                break
                                break
                            else:
                                print('Posición Ocupada.Intente denuevo')
                                jugador1()
        elif símbolo==2:
            print('TU TURNO')
            print('SU SIMBOLO: O')
            print('¿Dónde desea colocarlo?')
            tablero_juego()
            posición=int(input())
            if posición<=9 or posición>=0:
                for j in range(3):
                    for i in range(3):
                        if TNumeros[j][i]==posición:
                            if TColumnas[j][i]=='    ':
                                TColumnas[j][i]=' O  '
                                tablero_juego()
                                True
                                break
                                break
                            else:
                                print('Posición Ocupada.Intente denuevo')
                                jugador1()
def jugador2():
        if símbolo==1:
            print('TURNO J2')
            print('SU SIMBOLO: O')
            print('¿Dónde desea colocarlo?')
            tablero_juego()
            posición=int(input())
            if posición<=9 or posición>=0:
                for j in range(3):
                    for i in range(3):
                        if TNumeros[j][i]==posición:
                            if TColumnas[j][i]=='    ':
                                TColumnas[j][i]=' O  '
                                posocupada=False
                                tablero_juego()
                                True
                                break
                            else:
                                print('Posición Ocupada.Intente denuevo')
                                jugador2()
        elif símbolo==2:
            print('TURNO J2')
            print('SU SIMBOLO: X')
            print('¿Dónde desea colocarlo?')
            tablero_juego()
            posición=int(input())
            if posición<=9 or posición>=0:
                for j in range(3):
                    for i in range(3):
                        if TNumeros[j][i]==posición:
                            if TColumnas[j][i]=='    ':
                                TColumnas[j][i]=' X  '
                                posocupada=False
                                tablero_juego()
                                True
                                break
                            else:
                                print('Posición Ocupada.Intente denuevo')
                                jugador2()

def VERTICALCOMPRUEBA():
    if TColumnas[0]==TX[0] or TColumnas[0]==TO[0]:
        ganador=TColumnas[0]
        Gana=True
        return Gana
    if TColumnas[1]==TX[1] or TColumnas[1]==TO[1]:
        ganador=TColumnas[1]
        Gana=True
        return Gana
    if TColumnas[2]==TX[2] or TColumnas[2]==TO[2]:
        ganador=TColumnas[2]
        Gana=True
        return Gana
def HORIZONTALCOMPRUEBA():
    if TColumnas[0][0]==TX[0][0] and TColumnas[1][0]==TX[1][0] and TColumnas[2][0]==TX[2][0] or  TColumnas[0][0]==TO[0][0] and TColumnas[1][0]==TO[1][0] and TColumnas[2][0]==TO[2][0]:
        ganador=TColumnas[0][0]
        Gana=True
        return Gana
    if TColumnas[0][1]==TX[0][1] and TColumnas[1][1]==TX[1][1] and TColumnas[2][1]==TX[2][1] or TColumnas[0][1]==TO[0][1] and TColumnas[1][1]==TO[1][1] and TColumnas[2][1]==TO[2][1]:
        ganador=TColumnas[0][1]
        Gana=True
        return Gana
    if TColumnas[0][2]==TX[0][2] and TColumnas[1][2]==TX[1][2] and TColumnas[2][2]==TX[2][2] or TColumnas[0][2]==TO[0][2] and TColumnas[1][2]==TO[1][2] and TColumnas[2][2]==TO[2][2]:
        ganador=TColumnas[0][2]
        Gana=True
        return Gana
def DIAGONALCOMPRUEBA():
    if TColumnas[0][0]==TX[0][0] and TColumnas[1][1]==TX[1][1] and TColumnas[2][2]==TX[2][2] or TColumnas[0][0]==TO[0][0] and TColumnas[1][1]==TO[1][1] and TColumnas[2][2]==TO[2][2]:
        ganador=TColumnas[1][1]
        Gana=True
        return Gana
    if TColumnas[0][2]==TX[0][2] and TColumnas[1][1]==TX[1][1] and TColumnas[2][0]==TX[2][0] or TColumnas[0][2]==TO[0][2] and TColumnas[1][1]==TO[1][1] and TColumnas[2][0]==TO[2][0]:
        ganador=TColumnas[2][0]
        Gana=True
        return Gana
def ganaono():
    Gana=''
    if Gana=='':
        Gana=VERTICALCOMPRUEBA()
        if Gana==True:
            print('Ya hay un ganador')
        else:
            NadieGana=False
            Gana=HORIZONTALCOMPRUEBA()
            if Gana==True:
                print('Ya hay un ganador')
            else:
                NadieGana=False
                Gana=DIAGONALCOMPRUEBA()
                if Gana==True:
                    print('Ya hay un ganador')
                else:
                    NadieGana=False
    return Gana
    return NadieGana

símbolo=eligesimbolo()
for i in range(4):
    Gana=ganaono()
    if Gana==True:
        break
    jugador1()
    Gana=ganaono()
    if Gana==True:
        break
    jugador2()

for i in range(1):
    Gana=ganaono()
    if Gana==True:
        break
    jugador1()
    Gana=ganaono()
    if Gana==True:
        break
    jugador2()

