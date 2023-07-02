import speech_recognition as sr
import pyttsx3
import pywhatkit
import urllib.request
import json
import pyjokes
import webbrowser
import datetime
import wikipedia
import yfinance as yf 

# escuchar nuestro microfono y devolver el audio comotexto

def transformar_audio_en_texto():

    # almacenar recognizer en variable
    r = sr.Recognizer()

    # configurar el microfono

    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzo la grabacion
        print('Escuchando...')

         # guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language='es-pe')
            pedido = pedido.lower()

            delimitador = ' '

            pedido_lista = pedido.split(delimitador)

            for elemento in pedido_lista:

                indice = pedido_lista.index('alexa')
                pedido_lista = pedido_lista[0:indice + 1]
                pedido_string = ' '.join(pedido_lista)
                print(pedido_string)


                print('Dijiste: '+ pedido_string)

            #devolver pedido
                return pedido_string

        # En caso de que no comprenda el audio
        except sr.UnknownValueError:
            #prueba de que no comprendio el audio
            print('ups, no hay servicio')

            # devolver error
            return 'sigo esperando'
        
        # en caso de no resolver el pedido
        except sr.RequestError:

            # prueba de que no comprendio el audio
            print('ups, no entendi')

            return 'sigo esperando'
        
        except:
            
            print('ups, algo ha salido mal')

            return 'sigo esperando'


# funcion para el que asistente pueda ser escuchado

def hablar(mensaje):
    
    #encender el motor de pyttsx3
    engine = pyttsx3.init()

    # pronunciar el mensaje

    engine.say(mensaje)
    engine.runAndWait()

# informa el dia de la semana
def pedir_dia():

    #crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    #crear variable para el dia de la semana
    dia_semana = dia.weekday()

    # diccionario con nombres de los días
    calendario = {0:'Lunes', 
                  1:'Martes',
                  2:'Miércoles',
                  3:'Jueves',
                  4:'Viernes',
                  5:'Sábado',
                  6:'Domingo'}
    
    # decir el dia de la semana
    print(calendario[dia_semana])
    hablar(f'Hoy es {calendario[dia_semana]}')


def pedir_hora():

    # crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento, son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    
    # decir la hora
    hablar(hora)


def saludo_inicial():
    
    # crear variable con datos de hora
    hora = datetime.datetime.now()

    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'

    elif 6 <= hora.hour < 13:
        momento = 'Buenos días' 
    else:
        momento = 'Buenas tardes'

    
    # decir el saludo
    hablar(f'{momento}, soy Alexa tu asistente personal. Por favor dime en que te puedo ayudar')


def main():

    # activar saludo inicial
    saludo_inicial()

    # loop para que no se detenga
    # variable de corte
    comenzar = True

    while comenzar:
        # activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if 'abre youtube' in pedido:
            hablar('Con gusto, estoy abriendo Youtube')

            webbrowser.open('https://www.youtube.com')
            continue

        elif 'abre navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue

        elif 'qué hora es' in pedido:
            pedir_hora()
            continue

        elif 'busca en wikipedia' in pedido:
            hablar('Buscando en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences = 1)
            hablar('Wikipedia dice lo siguiente: ')
            hablar(resultado)
            continue

        elif 'busca en internet' in pedido:
            hablar('Ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue

        elif 'reproduce' in pedido:
            hablar('Buena idea, ya comienzo a reproducirlo')
            pedido = pedido.replace('reproduce','')
            pywhatkit.playonyt(pedido)
            continue

        elif 'escribe' in pedido:
            hablar('A quién deseas hablar?')
            pywhatkit.sendwhatmsg()

        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue

        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue


            except:
                hablar('Perdón, pero no la he encontrado')
                continue
        

        elif 'escribe a' in pedido:
            # Crear una red de contactos sin repetir
            contactos = {'shirley':'+51986726281',
                         'andrea': '+51986369047'}
            pedido = pedido.replace('escribe a', '').strip()
            contacto = contactos[pedido]

            hablar('¿A qué contacto desea escribir?: ')
            mensaje = transformar_audio_en_texto()
                        
            # contacto = input()
            # contacto = contactos[contacto]            

            # Función para escribir mensaje a un contacto
            pywhatkit.sendwhatmsg(contacto, mensaje, 14, )

        for i in ['apágate','apaga te', 'apagate', 'jarvis fuera']:
            if i in pedido:
                hablar('Muchas gracias')
                comenzar = False     
        

main()




