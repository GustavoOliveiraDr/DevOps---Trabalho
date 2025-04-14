# Usa imagem oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos da sua aplicação para o container
COPY . .

# Instala as dependências (requests, no seu caso)
RUN pip install --no-cache-dir requests

# Comando padrão para rodar o app
CMD ["python", "app.py"]
