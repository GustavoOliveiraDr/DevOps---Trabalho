# App de clima - versão inicial

import requests

API_KEY = 'SUA_API_KEY_AQUI'
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def pegar_clima(cidade):
    params = {
        "q": cidade,
        "appid": API_KEY,
        "lang": "pt_br",
        "units": "metric"

    }

    resposta = resquests.get(BASE_URL, params=params)
    dados = resposta.json()
    return dados

#entrada do usuário
cidade = input("Digite o nome da cidade: ")
dados = pegar_clima(cidade)

if dados:
    print(dados)
else:
    print("Cidade não encontrada ou erro na requisição")
