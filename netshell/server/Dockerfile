# Usando uma imagem Python baseada em Alpine
FROM python:3.11-alpine

RUN apk add --no-cache iptables

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando o arquivo de dependências
COPY requirements.txt .

# Instalando as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o arquivo do servidor Python
COPY server.py .

# Definindo a variável de ambiente para a porta
ENV PORT=${WS_PORT}

# Expondo a porta
EXPOSE ${PORT}

# Comando para iniciar o servidor com uvicorn
# Comando para iniciar o servidor com uvicorn
CMD ["sh", "-c", "uvicorn server:app --host 0.0.0.0 --port $WS_PORT"]
