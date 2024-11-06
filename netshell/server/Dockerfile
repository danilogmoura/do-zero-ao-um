# Usando uma imagem Python baseada em Alpine
FROM python:3.11-alpine

RUN apk add --no-cache iptables

# Definindo o diretório de trabalho
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .

ENV PORT=${WS_PORT}

# Expondo a porta
EXPOSE ${PORT}

CMD ["sh", "-c", "uvicorn server:app --host 0.0.0.0 --port $WS_PORT"]
