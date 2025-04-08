import requests

API_KEY = "SUA_API_KEY_AQUI"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def pegar_clima(cidade):
    params = {
        "q": cidade,
        "appid": API_KEY,
        "lang": "pt_br",
        "units": "metric"
    }

    resposta = requests.get(BASE_URL, params=params)

    if resposta.status_code == 200:
        return resposta.json()
    else:
        return None


# Entrada do usuário
cidade = input("Digite o nome da cidade: ")
dados = pegar_clima(cidade)

if dados:
    print(f"\n Clima em {cidade.title()}:")
    print(f" Temperatura: {dados['main']['temp']}°C")
    print(f" Sensação térmica: {dados['main']['feels_like']}°C")
    print(f" Umidade: {dados['main']['humidity']}%")
    print(f" ️ Condição: {dados['weather'][0]['description'].capitalize()}")
else:
    print("❌ Cidade não encontrada ou erro na requisição.")
