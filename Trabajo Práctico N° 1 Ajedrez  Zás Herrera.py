'''Crear un programa que genere tableros de ajedrez aleatorios como se ve en la imagen de ejemplo.

 a) Un tablero de ajedrez debe tener en cada equipo (blancas y negras):

 Entre 0 y 8 Peones
 Entre 0 y 2 Caballos
 Entre 0 y 2 Alfiles
 Entre 0 y 2 Torres
 Entre 0 y 1 Reina
 1 Rey
b) El programa debe poder calcular el puntaje de cada jugador dependiendo de qué piezas poseen en el tablero:

 Peones valen 1 punto
 Caballos valen 3 puntos
 Alfiles valen 3 puntos
 Torres valen 5 puntos
 Reinas valen 9 puntos
 Reyes valen 4 puntos
c) El programa debe poder reconocer cuando un Rey está en jaque. Como no todo el mundo conoce las reglas de Ajedrez, en este ejercicio diremos que el Rey está en jaque cuando 2 piezas del otro equipo se encuentran adyacentes al Rey.

'''

#Ajedrez Zás Herrera Elian
import random

#GeneroTableroVacío
RestoTablero=[]

for i in range(0,64):
    CampoVacío='❏'
    RestoTablero.append(CampoVacío)

def GenerafichasBYN():

    #REINABLANCA
    AzarPos=random.randint(0,63)
    Azar_apareceono=random.randint(1,2)
    if Azar_apareceono==1:
        if RestoTablero[AzarPos]=='❏':
            RestoTablero[AzarPos]='QB'
    elif Azar_apareceono==2:
        if RestoTablero[AzarPos]=='❏':
            RestoTablero[AzarPos]='❏'
    elif RestoTablero[AzarPos]!='❏':
        AzarPos=random.randint(0,63)
        if RestoTablero[AzarPos]=='❏':
            RestoTablero[AzarPos]='QB'

    #REINABLANCA
    AzarPos=random.randint(0,63)
    Azar_apareceono=random.randint(1,2)
    if Azar_apareceono==1:
        if RestoTablero[AzarPos]=='❏':
            RestoTablero[AzarPos]='QN'
    elif Azar_apareceono==2:
        if RestoTablero[AzarPos]=='❏':
            RestoTablero[AzarPos]='❏'
    elif RestoTablero[AzarPos]!='❏':
        AzarPos=random.randint(0,63)
        if RestoTablero[AzarPos]=='❏':
            RestoTablero[AzarPos]='QN'

    #Inserta CABALLOSBLANCOS
    for i in range(0,2):
        AzarPos=random.randint(0,63)
        Azar_apareceono=random.randint(1,2)
        if Azar_apareceono==1:
            if RestoTablero[AzarPos]=='❏':
                RestoTablero[AzarPos]='CB'
        elif Azar_apareceono==2:
            if RestoTablero[AzarPos]=='❏':
                RestoTablero[AzarPos]='❏'
        elif RestoTablero[AzarPos]!='❏':
            AzarPos=random.randint(0,63)
            if RestoTablero[AzarPos]=='❏':
                RestoTablero[AzarPos]='CB'

    #Inserta CABALLOSNEGROS
    for i in range(0,2):
        AzarPos=random.randint(0,63)
        Azar_apareceono=random.randint(1,2)
        if Azar_apareceono==1:
            if RestoTablero[AzarPos]=='❏':
                RestoTablero[AzarPos]='CN'
        elif Azar_apareceono==2:
            if RestoTablero[AzarPos]=='❏':
                RestoTablero[AzarPos]='❏'
        elif RestoTablero[AzarPos]!='❏':
            AzarPos=random.randint(0,63)
            if RestoTablero[AzarPos]=='❏':
                RestoTablero[AzarPos]='CN'

    #Inserta TORRESBLANCAS
    for i in range(0,2):
        AzarPos=random.randint(0,63)
        Azar_apareceono=random.randint(1,2)
        if Azar_apareceono==1:
            if RestoTablero[AzarPos]=='❏':
                RestoTablero[AzarPos]='TB'
        elif Azar_apareceono==2:
            if RestoTablero[AzarPos]=='❏':
                RestoTablero[AzarPos]='❏'
        elif RestoTablero[AzarPos]!='❏':
            AzarPos=random.randint(0,63)
            if RestoTablero[AzarPos]=='❏':
                RestoTablero[AzarPos]='TB'

    #Inserta TORRESNEGRAS
    for i in range(0,2):
        AzarPos=random.randint(0,63)
        Azar_apareceono=random.randint(1,2)
        if Azar_apareceono==1:
            if RestoTablero[AzarPos]=='❏':
                RestoTablero[AzarPos]='TN'
        elif Azar_apareceono==2:
            if RestoTablero[AzarPos]=='❏':
                RestoTablero[AzarPos]='❏'
        elif RestoTablero[AzarPos]!='❏':
            AzarPos=random.randint(0,63)
            if RestoTablero[AzarPos]=='❏':
                RestoTablero[AzarPos]='TN'
    #ReyBlanco
    while True:
        AzarPos=random.randint(0,63)
        if RestoTablero[AzarPos]!='❏':
            AzarPos=random.randint(0,63)
            continue
        elif RestoTablero[AzarPos]=='❏':
            RestoTablero[AzarPos]='RB'
            break

    #Inserta ALFILESBLANCOS
    for i in range(0,2):
        AzarPos=random.randint(0,63)
        Azar_apareceono=random.randint(1,2)
        if Azar_apareceono==1:
            if RestoTablero[AzarPos]=='❏':
                RestoTablero[AzarPos]='AB'
        elif Azar_apareceono==2:
            if RestoTablero[AzarPos]=='❏':
                RestoTablero[AzarPos]='❏'
        elif RestoTablero[AzarPos]!='❏':
            AzarPos=random.randint(0,63)
            if RestoTablero[AzarPos]=='❏':
                RestoTablero[AzarPos]='AB'

    #ReyNegro
    while True:
        AzarPos=random.randint(0,63)
        if RestoTablero[AzarPos]!='❏':
            AzarPos=random.randint(0,63)
            continue
        elif RestoTablero[AzarPos]=='❏':
            RestoTablero[AzarPos]='RN'
            break

    #Inserta ALFILESNEGROS
    for i in range(0,2):
        AzarPos=random.randint(0,63)
        Azar_apareceono=random.randint(1,2)
        if Azar_apareceono==1:
            if RestoTablero[AzarPos]=='❏':
                RestoTablero[AzarPos]='AN'
        elif Azar_apareceono==2:
            if RestoTablero[AzarPos]=='❏':
                RestoTablero[AzarPos]='❏'
        elif RestoTablero[AzarPos]!='❏':
            AzarPos=random.randint(0,63)
            if RestoTablero[AzarPos]=='❏':
                RestoTablero[AzarPos]='AN'

    #Inserta PEONESBLANCOS
    for i in range(0,8):
        AzarPos=random.randint(0,63)
        Azar_apareceono=random.randint(1,2)
        if Azar_apareceono==1:
            if RestoTablero[AzarPos]=='❏':
                RestoTablero[AzarPos]='PB'
        elif Azar_apareceono==2:
            if RestoTablero[AzarPos]=='❏':
                RestoTablero[AzarPos]='❏'
        elif RestoTablero[AzarPos]!='❏':
            AzarPos=random.randint(0,63)
            if RestoTablero[AzarPos]=='❏':
                RestoTablero[AzarPos]='PB'

    #Inserta PEONESNEGROS
    for i in range(0,8):
        AzarPos=random.randint(0,63)
        Azar_apareceono=random.randint(1,2)
        if Azar_apareceono==1:
            if RestoTablero[AzarPos]=='❏':
                RestoTablero[AzarPos]='PN'
        elif Azar_apareceono==2:
            if RestoTablero[AzarPos]=='❏':
                RestoTablero[AzarPos]='❏'
        elif RestoTablero[AzarPos]!='❏':
            AzarPos=random.randint(0,63)
            if RestoTablero[AzarPos]=='❏':
                RestoTablero[AzarPos]='PN'

def Tablero():
    #Inserta IMPRIME TABLERO
    print('\n      TABLERO')
    for i in range(0,64):
        if i==8 or i==16 or i==24 or i==32 or i==40 or i==48 or i==56 or i==64:
            print('\n')
        print(RestoTablero[i],end="|")

def TableroVacío():
    for i in range(len(RestoTablero)):
        RestoTablero[i]='❏'
        if i==8 or i==16 or i==24 or i==32 or i==40 or i==48 or i==56 or i==64:
            print('\n')
        print(RestoTablero[i],end="|")

def JaqueB():
    PosReyB=RestoTablero.index('RB')
    if PosReyB<56 and PosReyB>14:
        if RestoTablero[PosReyB-8]=='PN' or RestoTablero[PosReyB-8]=='CN' or RestoTablero[PosReyB-8]=='TN' or RestoTablero[PosReyB-8]=='RN' or RestoTablero[PosReyB-8]=='QN':
            if RestoTablero[PosReyB-7]=='PN' or RestoTablero[PosReyB-7]=='CN' or RestoTablero[PosReyB-7]=='TN' or RestoTablero[PosReyB-7]=='RN' or RestoTablero[PosReyB-7]=='QN':
                print('\nEL REY BLANCO ESTA EN JAQUE')
            elif RestoTablero[PosReyB-9]=='PN' or RestoTablero[PosReyB-9]=='CN' or RestoTablero[PosReyB-9]=='TN' or RestoTablero[PosReyB-9]=='RN' or RestoTablero[PosReyB-9]=='QN':
                print('\nEL REY BLANCO ESTA EN JAQUE')
    elif PosReyB<14 and PosReyB<63:
        if RestoTablero[PosReyB+8]=='PN' or RestoTablero[PosReyB+8]=='CN' or RestoTablero[PosReyB+8]=='TN' or RestoTablero[PosReyB+8]=='RN' or RestoTablero[PosReyB+8]=='QN':
            if RestoTablero[PosReyB+7]=='PN' or RestoTablero[PosReyB+7]=='CN' or RestoTablero[PosReyB+7]=='TN' or RestoTablero[PosReyB+7]=='RN' or RestoTablero[PosReyB+7]=='QN':
                print('\nEL REY BLANCO ESTA EN JAQUE')
            elif RestoTablero[PosReyB+9]=='PN' or RestoTablero[PosReyB+9]=='CN' or RestoTablero[PosReyB+9]=='TN' or RestoTablero[PosReyB+9]=='RN' or RestoTablero[PosReyB+9]=='QN':
                print('\nEL REY BLANCO ESTA EN JAQUE')
    elif PosReyB<56 and PosReyB>14:
        if RestoTablero[PosReyB-1]=='PN' or RestoTablero[PosReyB-1]=='CN' or RestoTablero[PosReyB-1]=='TN' or RestoTablero[PosReyB-1]=='RN' or RestoTablero[PosReyB-1]=='QN':
            if RestoTablero[PosReyB-8]=='PN' or RestoTablero[PosReyB-8]=='CN' or RestoTablero[PosReyB-8]=='TN' or RestoTablero[PosReyB-8]=='RN' or RestoTablero[PosReyB-8]=='QN':
                print('\nEL REY BLANCO ESTA EN JAQUE')
            elif RestoTablero[PosReyB-9]=='PN' or RestoTablero[PosReyB-9]=='CN' or RestoTablero[PosReyB-9]=='TN' or RestoTablero[PosReyB-9]=='RN' or RestoTablero[PosReyB-9]=='QN':
                print('\nEL REY BLANCO ESTA EN JAQUE')

def JaqueN():
    PosReyN=RestoTablero.index('RN')
    if PosReyN<56 and PosReyN>14:
        if RestoTablero[PosReyN-8]=='PB' or RestoTablero[PosReyN-8]=='CB' or RestoTablero[PosReyN-8]=='TB' or RestoTablero[PosReyN-8]=='RB' or RestoTablero[PosReyN-8]=='QB':
            if RestoTablero[PosReyN-7]=='PB' or RestoTablero[PosReyN-7]=='CB' or RestoTablero[PosReyN-7]=='TB' or RestoTablero[PosReyN-7]=='RB' or RestoTablero[PosReyN-7]=='QB':
                print('\nEL REY NEGRO ESTA EN JAQUE')
            elif RestoTablero[PosReyN-9]=='PB' or RestoTablero[PosReyN-9]=='CB' or RestoTablero[PosReyN-9]=='TB' or RestoTablero[PosReyN-9]=='RB' or RestoTablero[PosReyN-9]=='QB':
                print('\nEL REY NEGRO ESTA EN JAQUE')
    elif PosReyN<14 and PosReyN<63:
        if RestoTablero[PosReyN+8]=='PB' or RestoTablero[PosReyN+8]=='CB' or RestoTablero[PosReyN+8]=='TB' or RestoTablero[PosReyN+8]=='RB' or RestoTablero[PosReyN+8]=='QB':
            if RestoTablero[PosReyN+7]=='PB' or RestoTablero[PosReyN+7]=='CB' or RestoTablero[PosReyN+7]=='TB' or RestoTablero[PosReyN+7]=='RB' or RestoTablero[PosReyN+7]=='QB':
                print('\nEL REY NEGRO ESTA EN JAQUE')
            elif RestoTablero[PosReyN+9]=='PB' or RestoTablero[PosReyN+9]=='CB' or RestoTablero[PosReyN+9]=='TB' or RestoTablero[PosReyN+9]=='RB' or RestoTablero[PosReyN+9]=='QB':
                print('\nEL REY NEGRO ESTA EN JAQUE')
    elif PosReyN<14 and PosReyN<63:
        if RestoTablero[PosReyN+1]=='PB' or RestoTablero[PosReyN+1]=='CB' or RestoTablero[PosReyN+1]=='TB' or RestoTablero[PosReyN+1]=='RB' or RestoTablero[PosReyN+1]=='QB':
            if RestoTablero[PosReyN-1]=='PB' or RestoTablero[PosReyN-1]=='CB' or RestoTablero[PosReyN-1]=='TB' or RestoTablero[PosReyN-1]=='RB' or RestoTablero[PosReyN-1]=='QB':
                print('\nEL REY NEGRO ESTA EN JAQUE')
            elif RestoTablero[PosReyN+9]=='PB' or RestoTablero[PosReyN+9]=='CB' or RestoTablero[PosReyN+9]=='TB' or RestoTablero[PosReyN+9]=='RB' or RestoTablero[PosReyN+9]=='QB':
                print('\nEL REY NEGRO ESTA EN JAQUE')
#SumaPuntajes
def PuntajeBYN():
    PuntajeB=0
    PuntajeN=0
    for i in range(0,64):
        if 'PB' in RestoTablero[i]:
            PuntajeB=PuntajeB+1
        elif 'TB'in RestoTablero[i]:
            PuntajeB=PuntajeB+5
        elif 'RB' in RestoTablero[i]:
            PuntajeB=PuntajeB+4
        elif 'QB' in RestoTablero[i]:
            PuntajeB=PuntajeB+9
        elif 'CB' in RestoTablero[i]:
            PuntajeB=PuntajeB+3
        elif 'AB' in RestoTablero[i]:
            PuntajeB=PuntajeB+3
        if 'PN' in RestoTablero[i]:
            PuntajeN=PuntajeN+1
        elif 'TN'in RestoTablero[i]:
            PuntajeN=PuntajeN+5
        elif 'RN' in RestoTablero[i]:
            PuntajeN=PuntajeN+4
        elif 'QN' in RestoTablero[i]:
            PuntajeN=PuntajeN+9
        elif 'CN' in RestoTablero[i]:
            PuntajeN=PuntajeN+3
        elif 'AN' in RestoTablero[i]:
            PuntajeN=PuntajeN+3

    return PuntajeN,PuntajeB

#IniciaPrograma
while True:
    #IMPRIME TABLERO VACÍO
    print('\nBIENVENIDO AL AJEDREZ')
    print('\n      TABLERO\n')
    TableroVacío()
    print('\n\n¿Generar un tablero con fichas?\n1-Sí\n2-No')
    opción=int(input())
    if opción==1:
        GenerafichasBYN()
        #Se Actualiza tablero
        Tablero()
        JaqueB()
        JaqueN()
        PuntajeN,PuntajeB=PuntajeBYN()
        print('\n\nPUNTAJE FICHAS BLANCAS: '+str(PuntajeB))
        print('\nPUNTAJE FICHAS NEGRAS: '+str(PuntajeN))
        print('\n¿Desea continuar?\n1-Sí\n2-No')
        opciónb=int(input())
        if opciónb==1:
            continue
        else:
            break
    elif opción==2:
        break
    elif opción!=1 or opción!=2:
        print('\nElección errónea. Intente denuevo')



