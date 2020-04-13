import random

lista_general = [['¿Buenos Aires limita con Santiago del Estero?','no'],['¿Jujuy limita con Bolivia?','si'],['¿San Juan Limita con Misiones?','no']]

lista_de_preguntas = []

puntaje=0

for i in lista_general:
    preg = i[0]
    resp = i[1]
    lista_de_preguntas.extend([preg])
    
#contador = len(lista_general)
while len(lista_de_preguntas) != 0:
    #print(len(lista_general))
    aleatoria= lista_de_preguntas[random.randrange(len(lista_de_preguntas))]

    print('Pregunta: ',aleatoria)
    respuesta = input('Respuesta: ').lower()
    
    for c in lista_general:
        if aleatoria == c[0]:
            if respuesta == c[1]:
                puntaje = puntaje + 1
                print('Respuesta correcta!, has sumado ',puntaje,' punto/s')
            else:
                print('Respuesta incorrecta')
            lista_general.remove(c)
            lista_de_preguntas.remove(aleatoria)
            #contador = contador - 1       

    #print('Lista general quedo ',lista_general)
    #print('Lista general quedo ',lista_de_preguntas)
#print('cantidad de preg ',len(lista_general))
print('El puntaje obtenido fue de: ',puntaje)

#Dentro de los que llegue a resolver, este me costó un poco mas.
#El ejercicio lo pude resolver, pero no se si es correcto generar una nueva lista
#con solo las preguntas y de ahi ir comparando con la general, o se podia resolver 
# solo usando la general.
#Lo que me pasó en este caso es que tuve que eliminar los elementos de las dos listas 
#para que me funcione correctamente."# Ejercicio4_Practica2" 
