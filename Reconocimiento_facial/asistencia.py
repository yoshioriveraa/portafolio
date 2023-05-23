import cv2
import face_recognition as fr
import os
import numpy as np

# crear base de datos
ruta = 'Empleados'
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}\{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])

print(nombres_empleados)

# codificar imagenes
def codificar(imagenes):

    # crear una lista nueva
    lista_codificada = []

    # Imagenes a RGB
    for imagen in imagenes:

        imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)

        # Codificar
        codificado = fr.face_encodings(imagen)[0]

        # Agregar a la lista
        lista_codificada.append(codificado)

    # Devolver lista codificada
    return lista_codificada

# Llamada de la función
lista_empleados_codificada = codificar(mis_imagenes)

# tomar una imagen de camara web
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Leer imagen de la camara
exito, imagen = captura.read()

if not exito:
    print('No se ha podido tomar la captura')
else:
    # Reconocer una cara en captura
    cara_captura = fr.face_locations(imagen)

    # Codificar cara capturada
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

    # Buscar concidencias
    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):

        coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)

        print(distancias)
        # Mínimo valor
        indice_coincidencia = np.argmin(distancias)
        # Mostrar coincidencia si las hay
        if distancias[indice_coincidencia] > 0.6:
            print('No coincide con niguno de nuestros empleados')

        else:
            print('Bienvenido al trabajo')
