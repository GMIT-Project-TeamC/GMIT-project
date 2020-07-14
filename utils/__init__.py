import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from bs4 import BeautifulSoup

API_KEY = os.environ['API_KEY']
NUM_OF_DAYS = 300


def _form_arg_dic(stock_symbol):
    return {
        'function': 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol': stock_symbol,
        'apikey': API_KEY,
        'outputsize': 'full'
    }


def _form_query_string(arg_dic):
    # return a formatted query string for alpha_vantage
    api_endpoint = 'https://www.alphavantage.co/query?'
    api_headers = '&'.join([f'{key}={val}' for key, val in arg_dic.items()])
    return api_endpoint + api_headers


def query_dataset(stock_symbol, num_of_days=NUM_OF_DAYS):
    # return: stock_meta (dic contains meta data), prices_df (pandas data frame contains price info)
    arg_dic = _form_arg_dic(stock_symbol)
    query_string = _form_query_string(arg_dic)
    r = requests.get(query_string, stream=True)
    is_successful = True
    if 'Meta Data' in r.json():
        stock_meta = r.json()['Meta Data']
        stock_prices = r.json()['Time Series (Daily)']
        prices_df = pd.DataFrame.from_dict(stock_prices, orient='index')
        prices_df.index = pd.to_datetime(
            prices_df.index)  # change index from str to datatime
        prices_df = prices_df.astype(float)  # change prices from str to float
        print(r)
        return is_successful, stock_meta, prices_df[:num_of_days]
    else:
        return (not is_successful), arg_dic['symbol'], None


def plot_column_vs_time(column_name, prices_dfs, symbols, ax):
    # a helper function for
    # plotting on the ax inputed and return a formatted string for title
    for prices_df in prices_dfs:
        prices_df.index = pd.to_datetime(
            prices_df.index)  # change index to datetime format
        prices_df[column_name].plot(ax=ax)
    ax.legend(symbols)
    return f'Daily {column_name} Time Series of {symbols}'
