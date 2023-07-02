import face_recognition as fr
import cv2

# cargar imágenes
foto_control = fr.load_image_file('fotoA.jpg')
foto_prueba = fr.load_image_file('fotoB.jpg')

# Pasar imagenes a RGB
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# Localizar cara control
lugar_cara_A = fr.face_locations(foto_control)[0]
# Entiende através de números
cara_codificada_A = fr.face_encodings(foto_control)[0]

# Localizar cara prueba
lugar_cara_B = fr.face_locations(foto_prueba)[0]
cara_codificada_B = fr.face_encodings(foto_prueba)[0]

# Mostar rectangulo
cv2.rectangle(foto_control,
              (lugar_cara_A[3], lugar_cara_A[0]),
              (lugar_cara_A[1], lugar_cara_A[2]),
              (0, 255, 0,),
              2)

cv2.rectangle(foto_prueba,
              (lugar_cara_B[3], lugar_cara_B[0]),
              (lugar_cara_B[1], lugar_cara_B[2]),
              (0, 255, 0,),
              2)

# Realizar comparación
resultado = fr.compare_faces([cara_codificada_A], cara_codificada_B)

# Medida de la distancia
distancia = fr.face_distance([cara_codificada_A], cara_codificada_B)

# Mostrar resultado
cv2.putText(foto_prueba,
            f'{resultado} {distancia.round(2)}',
            (10,40),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0, 255, 0),
            2)

# Mostrar imagenes
cv2.imshow('Foto Control', foto_control)
cv2.imshow('Foto Prueba', foto_prueba)

# Mantener el programa abierto
cv2.waitKey(0)