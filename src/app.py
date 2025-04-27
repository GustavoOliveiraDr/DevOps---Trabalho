import app
import requests

API_KEY = "bf8f78832f2d37ff9e16200e1a68295d"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def pegar_clima(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "lang": "pt_br",
        "units": "metric"
    }

    resposta = requests.get(BASE_URL, params=params)

    if resposta.status_code == 200:
        return resposta.json()
    else:
        print("Status Code:", resposta.status_code)
        print("Resposta da API:", resposta.text)
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
    print("Ahhh Não deu certo")
    #alguma coisa ai por enquanto

@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}