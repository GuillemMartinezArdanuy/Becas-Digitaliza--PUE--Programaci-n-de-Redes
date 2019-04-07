'''Tarea 2: Crear una APP para el ISS (International Space Station)

Crear un archivo llamado: numberPeopleSpace.py
Crear una app para saber el número de personas que hay en el espacio. Podéis buscar la información en la siguiente URL:
http://open-notify.org/Open-Notify-API/ (Enlaces a un sitio externo.)Enlaces a un sitio externo.
Subir el archivo a vuestro repositorio en GitHub.'''

# http://api.open-notify.org/astros.json

# importamos

import json
import requests
requests.packages.urllib3.disable_warnings()

api_url="http://api.open-notify.org/astros.json"
resp = requests.get(api_url, verify=False)
print(resp)

response_json = resp.json()
#print(response_json)

numero_personas=response_json["number"]

print("en el espacio actualmente hay {0} personas".format(numero_personas))