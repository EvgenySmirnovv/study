import json
import requests
from config import (keys)

class ConvertionException(Exception):
    pass

class ValuesConverter:
    @staticmethod
    def convert(quote:str, base:str, amout:str):

        if quote == base:
            raise ConvertionException("Нельзя конвертировать в ту же валюту")

        try:
            quote_tiker = keys[quote]
        except KeyError:
            raise ConvertionException(f"{quote}-Нет такой валюты")

        try:
            base_tiker = keys[base]
        except KeyError:
            raise ConvertionException(f"{base}-Нет такой валюты")

        try:
            amout = float(amout)
        except KeyError:
            raise ConvertionException(f"Напишите количество цифрами.")
        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_tiker}&tsyms={base_tiker}")
        price = json.loads(r.content)[keys[base]]
        return price
