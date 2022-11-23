import random
import string
import zipfile
import os
from pathlib import Path

abc=string.ascii_lowercase
abecedario=[]
for ab in abc:
    abecedario.append(ab)
numeros=[1,2,3,4,5,6,7,8,9,10]

#Crea carpeta 'Exámenes'
os.makedirs('Exámenes')
#Crea exámenes vacíos
for examen in range(0,20):
    archivoEx=open(f'.\Exámenes\Exámen{examen+1}.txt','w')
    archivoEx.close()
dicPreguntas={
0:'¿Qué comando extrae datos de la base de datos?',
1:'¿Qué palabra clave se usa para devolver solamente valores diferentes?',
2:'¿Qué es una relación?',
3:'¿Qué es una clave primaria?',
4:'¿Qué comando modifica la estructura de las tablas en la base de datos?',
5:'Comando que crea una tabla dentro de la base de datos',
6:'¿Qué palabra clave se utiliza para ordenar el resultado?',
7:'Comando que elimina una tabla de la base de datos',
8:'Sentencia de SQL que agrega uno o más registros a una tabla.',
9:'Sentencia de SQL que permite borrar cero o más registros en una tabla.'
}
dicRespuestas={
0:['Select [X]', 'Alter [ ]','Update [ ]','Modify[ ]'],
1:['Distinct[X]','Count[ ]','NotSame[ ]','Not!=[ ]'],
2:['Son vínculos entre tablas[X]','Ambas son ciertas[ ]','Ninguna es correcta[ ]','Específica si es necesario que exista un valor en un campo[ ]'],
3:['Algo que permite identificar en forma unívoca un registro[X]','Un dato que puede ser nulo[ ]','Un dato que se repite[ ]','Algo que permite identificar en forma unívoca una tabla[ ]'],
4:['Alter[X]','Create[ ]','Select[ ]','Update[ ]'],
5:['Create[X]','Alter[ ]','Insertinto[ ]','Modify[ ]'],
6:['Order by[X]','Sort[ ]','Orden by[ ]','Sortear[ ]'],
7:['Drop[X]','Delete[ ]','Dropdelete[ ]','Erase[ ]'],
8:['Insert[X]','Create[ ]','Into[ ]','Add[ ]'],
9:['Delete[X]','Drop[ ]','Clean[ ]','Empty[ ]']
}
#Crea carpeta 'Respuestas_Exámenes'
os.makedirs('Respuestas_Exámenes')
def generaRandomPregRes():
    #Genera un exámen con contenido aleatorio
    archivoRes=open(f'.\Respuestas_Exámenes\Respuestas{examen+1}.txt','w')
    archivoRes.close()
    resExamenes={0:[],1:[],2:[],3:[]}
    dicCuestionario={}
    preguntas=list(dicPreguntas.keys())
    random.shuffle(preguntas)
    for clave in preguntas:
        print(numeros[clave],end=") ")
        print(dicPreguntas[clave])
        random.shuffle(dicRespuestas[clave])
        for respuesta in range(4):
            print(abecedario[respuesta],end=")")
            print(dicRespuestas[clave][respuesta])
        dicCuestionario[dicPreguntas[clave]]=dicRespuestas[clave]
        for cada in range(4):
            for i in range(4):
                resExamenes[cada]=dicRespuestas[clave]
        respuestas=list(resExamenes.values())
        for valor in range(4):
            archivoRes=open(f'.\Respuestas_Exámenes\Respuestas{examen+1}.txt','a')
            respuestasExamen=respuestas[valor][valor]
            archivoRes.write(respuestasExamen+'\n')
        archivoRes.write('\n')
        archivoRes.close()
        print('\n')
    return dicCuestionario

#Crea Exámenes aleatorios
for examen in range(0,20):
    archivoEx=open(f'.\Exámenes\Exámen{examen+1}.txt','a')
    cuestionarios=generaRandomPregRes()
    examenClaves=list(cuestionarios.keys())
    examenValores=list(cuestionarios.values())
    for clave in range(len(examenClaves)):
        numeroP=numeros[clave]
        preguntaEx=examenClaves[clave]
        archivoEx.write(str(numeroP)+') ')
        archivoEx.write(str(preguntaEx)+'\n')
        for respuesta in range(4):
            letraR=abecedario[respuesta]
            examenRes=examenValores[clave][respuesta]
            archivoEx.write(str(letraR)+'-')
            archivoEx.write(str(examenRes)+'\n')
        archivoEx.write('\n')
    print('\n')
archivoEx.close()
#Crea Zip con Exámenes
zipExámenes=zipfile.ZipFile('Preguntas.zip','w')
zipExámenes.write(f'.\Exámenes\Exámen1.txt',compress_type=zipfile.ZIP_DEFLATED)
zipExámenes.close()
for examenCuenta in range(2,21):
    zipExámenes = zipfile.ZipFile('Preguntas.zip', 'a')
    zipExámenes.write(f'.\Exámenes\Exámen{examenCuenta}.txt', compress_type=zipfile.ZIP_DEFLATED)
    zipExámenes.close()
#Crea Zip con Respuestas
zipRespuestas=zipfile.ZipFile('Respuestas.zip','w')
zipRespuestas.write(f'.\Respuestas_Exámenes\Respuestas1.txt',compress_type=zipfile.ZIP_DEFLATED)
zipRespuestas.close()
for examenCuenta in range(2,21):
    zipRespuestas = zipfile.ZipFile('Respuestas.zip', 'a')
    zipRespuestas.write(f'.\Respuestas_Exámenes\Respuestas{examenCuenta}.txt', compress_type=zipfile.ZIP_DEFLATED)
    zipRespuestas.close()
