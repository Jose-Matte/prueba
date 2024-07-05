import csv

encoding='utf-8'
with open('objetos.csv', 'r') as archivo_csv:
 lector_csv = csv.DictReader(archivo_csv)

def funcion(x):
    y=lector_csv.get(x)
    print('la cantidad es',y)
    if y>=respuesta2:
        y-respuesta2
        print('quedan',y )
    else:
        print('no hay mas')
precio=0
while True: 
    print('que quieres???\n perro \n gato \n pistola')
    respuesta=input('\ningrese lo que quiere ')
    try:
        respuesta2=int(input('ingresa la cantidad'))
    except ValueError:
        print('escribe un numero')
    if respuesta=='perro':
        funcion('perro')
        precio=250*respuesta2
    elif respuesta=='gato':
        funcion('gato')
        precio=50*respuesta2
    elif respuesta=='pistola':
        funcion('pistola')
        precio=25*respuesta2
    else:
        print('tienes que elegir alguna de las opciones')
    seguir=input('quieres seguir comprando?, si no quieres seguir escribe no \n si quieres seguir comprando escribe cualquier cosa')
    
    if seguir =='no':
        break
    else:
        print('okay\n')
print('ciclo finalizado')

