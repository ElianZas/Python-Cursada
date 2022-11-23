import random

print('Reglas:\nGana el que se acerque más a 21\nSi se pasa de 21 pierde\nSi el score de ambos es igual EMPATAN')

#Defino variables
Jugador=''
Croupier=''

#Realizo las funciones para contar las rondas, generar cartas de jugador y croupier
def rondas(ronda):
    ronda=ronda
    return ronda+1

def generar_Jugador(Jugador): #Genera las cartas del Jugador1
    Jugador=random.randint(1,13)
    while Jugador==1 or Jugador==11 or Jugador==12 or Jugador==13:
            Jugador=10
    return Jugador

def generar_Croupier(Croupier): #Genera las cartas del Croupier
    Croupier=random.randint(1,13)
    while Croupier==1 or Croupier==11 or Croupier==12 or Croupier==13:
        Croupier=10
    return Croupier

#Guardo los return de las funciones en cada variable
ronda=0
rondas(ronda)
ronda=rondas(ronda)
cuenta=1
TotalScore_Jugador=0
TotalScore_Croupier=0

#Declaro y asigno variables que se utilizarán dentro del while y el juego en condiciones.
inicia=0
opciónCr=1
opción=1
opciónplanta=1

while True:
     #Genero cartas
    if opción==True or opciónCr==True:
        if opción==True:
            generar_Jugador(Jugador)#Generacartajugador
            Jugador=generar_Jugador(Jugador)
            for i in range(cuenta):#Totaldeljugador
                TotalScore_Jugador=Jugador+TotalScore_Jugador
        if opciónCr==True:
            generar_Croupier(Croupier)#GeneracartaCroupier
            Croupier=generar_Croupier(Croupier)
            for i in range(cuenta):#Totaldelcroupier
                TotalScore_Croupier=Croupier+TotalScore_Croupier
    #NO genero cartas
    elif opción==False or opciónCr==False:
        if opción==False:
            TotalScore_Jugador=TotalScore_Jugador

        if opciónCr==False:
            TotalScore_Croupier=TotalScore_Croupier
#Muestro la ronda correspondiente
    print('\nRONDA '+str(ronda)+'\n')
    print('Tú Carta: '+str(Jugador))
    print('Croupier Carta: '+str(Croupier))

#Condiciones para saber quien gana según el score total de cada jugador
    #Si el score del jugador es igual a 21 O es menor que el total del croupier, gana el jugador
    if TotalScore_Jugador==21 or (TotalScore_Jugador<21 and TotalScore_Croupier>21):
        print('\n¡BLACKJACK!, GANASTE')
        print('\nTÚ TOTAL SCORE:'+str(TotalScore_Jugador))
        print('CROUPIER TOTAL SCORE: '+str(TotalScore_Croupier))
        if TotalScore_Croupier>21:
          print('\nPERDIÓ EL CROUPIER')
          break
    #Si el score del croupier es igual a 21 O es menor que el total del jugador, gana el croupier
    elif TotalScore_Croupier==21 or (TotalScore_Croupier<21 and TotalScore_Jugador>21):
        print('\nTÚ TOTAL SCORE:'+str(TotalScore_Jugador))
        print('CROUPIER TOTAL SCORE: '+str(TotalScore_Croupier))
        print('\n¡BLACKJACK!, GANO EL CROUPIER')
        if TotalScore_Jugador>21:
            print('\nPERDISTE')
        break
#Condiciones para saber cuando empatan ambos jugadores si se pasan de 21 ambos, o de 17
    elif (TotalScore_Jugador==TotalScore_Croupier and TotalScore_Croupier>17 and TotalScore_Jugador>17) or (TotalScore_Jugador==TotalScore_Croupier and TotalScore_Jugador>21 and TotalScore_Croupier>21) or (TotalScore_Croupier>21 and TotalScore_Jugador>21):
        print('\nTÚ TOTAL SCORE:'+str(TotalScore_Jugador))
        print('CROUPIER TOTAL SCORE: '+str(TotalScore_Croupier))
        print('\n¡EMPATE!')
        break

#Condición para cuando el Croupier posea un score menor a 17 o mayor a 17
    if TotalScore_Croupier>=17:
       print('Croupier se planta')
       opciónCr=False
    else:
        opciónCr=True
        print('\nCroupier pide otra carta')

#Si el score del jugador es menor o igual a 21 que decida si pide otra carta o se planta.
    if TotalScore_Jugador<=21:
        print('\n¿JUGADOR desea pedir otra carta?')
        print('1-Sí')
        print('2-No')
        opción=int(input())
#Depende la opción, con 1 se pasa a la siguiente ronda, con 2 el jugador se planta
        if opción==1:
            rondas(ronda)
            ronda=rondas(ronda)
            opción=True
            continue
        else:

        #Si se planta y el croupier se plantó, se avisará que el croupier seguirá plantándose, y
        #para no entraer en un bucle infinito elegirá si pide otra carta o no.
        #Si elige No pedir otra carta, se calculará el total y saltará quien ganó.

        #Si se planta y el croupier NO se plantó, se pasará a la siguiente ronda.

            if opción==2:
                print('Eligió Plantarse')
                rondas(ronda)
                ronda=rondas(ronda)
                opciónplanta=False
                opción=False
                if opción==False and opciónCr==False and TotalScore_Jugador<21:
                    print('\nAMBOS SE PLANTARON')
                    print('CROUPIER SEGUIRÁ PLANTÁNDOSE:\n')
                    print('1-Pedir otra carta\n2-NO pedirá otra carta')
                    opción=int(input())
                    print(opción)
                    if  opción==1:
                        opción=True
                        rondas(ronda)
                        ronda=rondas(ronda)
                        print('HOLA')
                        continue
                    else:
                        if opción==2:
                            opción=False
                            print('Terminó el juego')
                            print('TÚ TOTAL SCORE: '+str(TotalScore_Jugador))
                            print('CROUPIER TOTAL SCORE: '+str(TotalScore_Croupier))
                            if TotalScore_Jugador>TotalScore_Croupier:
                                print('\n¡BLACKJACK!, GANASTE')
                                break
                            elif TotalScore_Croupier>TotalScore_Jugador:
                                print('\n¡BLACKJACK!, GANO EL CROUPIER')
                                break
