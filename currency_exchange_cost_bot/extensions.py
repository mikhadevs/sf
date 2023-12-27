import json
import requests
from config import exchanges

class APIException(Exception):
    pass

class Convertor:
    @staticmethod
    def get_price(base, sym, amount):
        try:
            base_key = exchanges[base.lower()]
        except KeyError:
            raise APIException(f"Валюта {base} недоступна!")

        try:
            sym_key = exchanges[sym.lower()]
        except KeyError:
            raise APIException(f"Заданная валюта {sym} недоступна!")

        if base_key == sym_key:
            raise APIException(f'Конвертация в ту же самую валюту - трата времени! {base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Неверно задано количество {amount}!')

        r = requests.get(f"https://api.apilayer.com/exchangerates_data/latest?symbols={sym_key}&base={base_key}&apikey=Xt7sgr8BdBnwQAoB4QyDbwJpY9A5mwmU")
        resp = json.loads(r.content)
        new_price = resp['rates'][sym_key] * amount
        new_price = round(new_price, 3)
        message = f"Стоимость {amount} {base} в {sym} : {new_price}"
        return message
