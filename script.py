# Importing the yfinance package
import yfinance as yf
from datetime import date

#
# Este metodo retorna un pandas dataframe con datos economicos relacionados
# con un 'stock' (e.g. GOOGL, AMZN) entre una fecha inicial (sd) y una fecha
# final (ed). Las fechas pueden estar en formato 'YYYY-MM-DD'.
#
# sd: fecha inicial
# stock: nombre código de la acción
# ed: fecha final. En caso que el usuario no lo indique, se tomara la fecha 
# del dia de hoy
#
import sys

def get_stock_data(sd, stock, ed = date.today()):
    #parametros: una accion, fecha de inicio, fecha de fin
    return yf.download(stock, sd, ed)

#si solo se ejecuta test, muestra 
def test(ticker = 'GOOGL'):
    start_date = '2020-01-01'
    end_date = '2020-02-28'
    # esta funcion recibe 3 argumentos: fecha 
    # inicial, nombre de la acción y fecha final 
    # sino se coloca la fecha de fin será el día actual
    return get_stock_data(start_date,ticker,end_date)
#si el usuario no pasa argumentos asume que se va a consultar Google
#si los pasa es porque quiere una acción
if __name__ == "__main__":
    ticker = 'GOOGL'
    if len(sys.argv) == 2:
        ticker = sys.argv[1]
    print(f"Se recuperara informacion del stock ${ticker}")
    data = test(ticker)
    print(data.tail())