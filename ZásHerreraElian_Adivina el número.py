'''Programar un juego para adivinar un número entre 1 y 10:

El jugador tiene 3 intentos para adivinar.
Luego de cada intento se dará una pista del estilo "el número es más bajo" o "más alto"
Para generar un número aleatorio pueden utilizar el siguiente código:
import random

numAleatorio = random.randint(1,10)
'''

import msvcrt
import random

numal=random.randint(1,10)
numing=int(input('Ingrese el número que cree que saldrá en pantalla entre 1 y 10: '))

if(numing>0 and numing<11):
    if(numing==numal):
        print('¡Has acertado, felicitaciones! :): '+str(numal)+','+str(numing))
    else:
        if(numing<numal):
            print('\nPista: el número es MAS ALTO que el ingresado\n')
            numing=int(input('Ingrese el número que cree que saldrá en pantalla: '))
            if(numing>0 and numing<11):
                if(numing==numal):
                    print('\n¡Has acertado, felicitaciones :)!: '+str(numal)+','+str(numing))
                else:
                    if(numing<numal):
                        print('\nPista: el número es MAS ALTO que el ingresado\n')
                        numing=int(input('Ingrese el número que cree que saldrá en pantalla: '))
                        if(numing>0 and numing<11):
                            if(numing==numal):
                                print('¡Has acertado, felicitaciones :)!: '+str(numal)+','+str(numing))
                            else:
                                print('\nIntentos agotados, has fallado')
                        else:
                            print('\nEl número ingresado no es correcto')
                                
                    elif(numing>numal):
                        print('\nPista: el número es MAS BAJO que el ingresado\n')
                        numing=int(input('Ingrese el número que cree que saldrá en pantalla: '))
                        if(numing>0 and numing<11):
                            if(numing==numal):
                                print('\n¡Has acertado, felicitaciones :)!: '+str(numal)+','+str(numing))
                            else:
                                print('\nIntentos agotados, has fallado')
                        else:
                             print('\nEl número ingresado no es correcto')
            else:
                print('\nEl número ingresado no es correcto')
            
        elif(numing>numal and numing<=10):
            print('\nPista: el número es MAS BAJO que el ingresado\n')
            numing=int(input('Ingrese el número que cree que saldrá en pantalla: '))
            if(numing>0 and numing<11):
                if(numing==numal):
                    print('\n¡Has acertado, felicitaciones :)!: '+str(numal)+','+str(numing))
                else:

                    if(numing<numal):
                        print('\nPista: el número es MAS ALTO que el ingresado\n')
                        numing=int(input('Ingrese el número que cree que saldrá en pantalla: '))
                        if(numing>0 and numing<11):
                            if(numing==numal):
                                print('\n¡Has acertado, felicitaciones :)!: '+str(numal)+','+str(numing))
                            else:
                                print('\nIntentos agotados, has fallado')
                        else:
                            print('\nEl número ingresado no es correcto')

                    elif(numing>numal):
                        print('\nPista: el número es MAS BAJO que el ingresado\n')
                        numing=int(input('Ingrese el número que cree que saldrá en pantalla: '))
                        if(numing>0 and numing<11):
                            if(numing==numal):
                                print('\n¡Has acertado, felicitaciones :)!: '+str(numal)+','+str(numing))
                            else:
                                print('\nIntentos agotados, has fallado')
                        else:
                            print('El número ingresado no es correcto')
            else:
                print('\nEl número ingresado no es correcto')
else:
    print('\nEl número ingresado no es correcto')

msvcrt.getch()
