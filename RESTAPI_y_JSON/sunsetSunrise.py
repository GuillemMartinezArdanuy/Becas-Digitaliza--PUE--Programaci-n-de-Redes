'''
Crear una aplicación para acceder a la API de las horas de salida y puesta del sol de la siguiente URL:

https://api.sunrise-sunset.org/json?lat=48.8584&lng=2.2945 (Enlaces a un sitio externo.)Enlaces a un sitio externo.
En el ejemplo, se calcula para París, Francia.

Crear un archivo llamado: sunsetSunrise.py
Mostrar las horas para una latitud y longitud concretas (que no sea la del ejemplo; por ejemplo, donde vivís).
Incluir un print con texto (lo que queráis), con los valores de latitud y longitud, y con las horas obtenidas.
Subir el archivo a vuestro repositorio en GitHub.'''

#cordenadas blanes:
#Longitud: 2.7903600
#Latitud: 41.6741900

# link :   https://api.sunrise-sunset.org/json?lat=41.6741900&lng=2.7903600

# importamos

import json
import requests
from tabulate import *

def get_ticket(): # creem funcio
    requests.packages.urllib3.disable_warnings()


    #construim el request, per demanar ticket
    api_url = "https://api.sunrise-sunset.org/json?lat=41.6741900&lng=2.7903600"
    headers = {
        "content-type": "application/json"
    }
    body_json = {
        "username": "",
        "password": ""
    } # usser pass per api


    #crem resposta, on fem un post
    resp=requests.post(api_url,json.dumps(body_json),headers=headers,verify=False)
    return resp.status_code

sortir=False
while sortir==False:
    print("esta version es a modo de prueba, no hay implementado control de errores, para ello ruego si tienes problema , reinicia el programa\n te voy a pedir longitud y latitud, ponlas correctamente \n te mostrare puesta y salida del sol las horas no son las correctas en tu zona horaria segurament \n vamos a ello\n")
    Longitud=input("introduce longitud, por ejemplo 2.7903600")
    Latitud=input("introduce latitud, por ejemplo 41.6741900")

    #Longitud= 2.7903600
    #Latitud= 41.6741900



    api_url1="https://api.sunrise-sunset.org/json?lat={0}&lng={1}".format(Latitud,Longitud)  # creamos la string de la uri con las variables
    print(api_url1)
    #api_url = "https://api.sunrise-sunset.org/json?lat=41.6741900&lng=2.7903600"  # selecccionem la URI de host
    ticket = get_ticket()  # obtenim el ticket
    headers = {
        "content-type": "application/json",
        "None": ""  # activem autoritzacio
    }

    resp = requests.get(api_url1, headers=headers, verify=False)  # crrem la resposta de la url
    #print("Status of /host request: ", resp.status_code)  # obtenim el codi,
    if resp.status_code != 200:  # sino es 200, que vol dir que sino es correcte, llancem error
        raise Exception("Status code does not equal 200. Response text: " + resp.text)
    response_json = resp.json()  # daltra banda obtenim la resposta del contingut de host URI


    hora_sortida_sol=""
    for item in response_json["results"]["sunrise"]:  # per cada item de la reposta, absorbirem elque ens interesa
        hora_sortida_sol= hora_sortida_sol+item

    hora_posta_sol=""
    for item in response_json["results"]["sunset"]:  # per cada item de la reposta, absorbirem elque ens interesa
        hora_posta_sol= hora_posta_sol+item


    print("en la Longitud: {0}, y latitud: {1}, la hora de salida del sol es: {2}, y el sol se pone a las: {3}".format(Longitud,Latitud,hora_sortida_sol,hora_posta_sol))

    respuesta=input("aprieta x para salir, de lo contrario vuelvo a preguntar las cordenadas")
    if respuesta == 'x':
        print("Hasta luego Lucas!")
        sortir=True

