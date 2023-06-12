from flask import Flask, request, Response
import yfinance as yf
from datetime import date

app = Flask(__name__)

def get_stock_data(sd, stock, ed = date.today()):
    return yf.download(stock, sd, ed)

@app.route('/stock-data', methods=['POST'])
def stock_data():
    data = request.get_json()
    ticker = data['ticker']
    start_date = data['start_date']
    end_date = data.get('end_date', str(date.today()))

    stock_data = get_stock_data(start_date, ticker, end_date)

    # Obtener las columnas específicas que deseas mostrar
    #columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    #filtered_stock_data = stock_data[columns]

    # Obtener las últimas 5 filas del DataFrame filtrado
    last_rows = stock_data.tail(5)

    stock_data_csv = last_rows.to_csv(index=True)  # Convertir a CSV

    return Response(stock_data_csv, mimetype='text/csv')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)