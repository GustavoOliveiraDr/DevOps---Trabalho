
from src.app import *

API_KEY = "bf8f78832f2d37ff9e16200e1a68295d"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def test_root():
    assert root() == {"message": "Hello World"}

def test_pegar_clima():
    city = "São Paulo"
    resultado = pegar_clima(city)
    assert resultado is not None
    assert "main" in resultado
    assert "weather" in resultado

def test_pegar_clima_nome_cidade():
    city = "São Paulo"
    resultado = pegar_clima(city)
    assert resultado is not None
    assert resultado["name"].lower() == city.lower()

def test_pegar_clima_temperatura_existente():
    city = "São Paulo"
    resultado = pegar_clima(city)
    assert resultado is not None
    assert "main" in resultado
    assert "temp" in resultado["main"]

def test_pegar_clima_condicao_existente():
    city = "São Paulo"
    resultado = pegar_clima(city)
    assert resultado is not None
    assert "weather" in resultado
    assert isinstance(resultado["weather"], list)
    assert "description" in resultado["weather"][0]
