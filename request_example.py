# Este script en Python ejemplifica como desde el lenguaje Python se pueden
# enviar peticiones a nuestra aplicacion
import requests

URL = "http://localhost:5000/stock-data"

# Envío de solicitud 'POST'
response = requests.post(URL, json={
    "ticker": "GOOGL",
    "start_date": "2020-01-01",
    "end_date": "2020-02-28"
})

print(f"Respuesta a POST:\n {response.text}")
input("Presione ENTER para cerrar...")