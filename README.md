## Autores

- Juan José Viafara - 2040751
- Juan Esteban Mazuera - 2043008
- Sheilly Ortega - 2040051

# Intrucciones de ejecución

Paso 1: se crea el ambiente.

```
python3 -m venv venv
```

Paso 2: se activa el ambiente virtual.

```
source venv/bin/activate
```

Paso 3: se instalan los requirements.

```
pip install -r requirements.txt
```

Paso 4: se corre el web service. 

```
python3 app.py
```

Si todo salió bien debe observar un mensaje así en la terminal:

```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.19.244.14:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 219-599-364
```

Paso 5: hacer una petición POST. 

Puede hacerlo desde la línea de comandos así: 

```
curl -X POST -H "Content-Type: application/json" -d '{
  "ticker": "GOOGL",
  "start_date": "2020-01-01",
  "end_date": "2020-02-28"
}' http://localhost:5000/stock-data
```

O desde python: 

```
python3 request_example.py
```# web-service
