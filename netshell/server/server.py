import json
import pexpect
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import sys

app = FastAPI()

# Configurando CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/status")
async def status():
    return {"ok": True}

# WebSocket para interagir com o shell
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    shell = pexpect.spawn("ash", encoding="utf-8", echo=False)
    shell.logfile = sys.stdout  # Log para depuração

    try:
        # Definir um prompt único
        shell.sendline('export PS1="PROMPT> "')
        shell.expect("PROMPT> ")

        while True:
            data = await websocket.receive_json()
            if data["type"] == "command":
                shell.sendline(data["data"])

                # Loop para capturar a saída do shell até que o prompt retorne
                output = ""
                while True:
                    try:
                        shell.expect(r'PROMPT> ', timeout=0.5)  # Padrão do nosso prompt personalizado
                        output_part = shell.before.strip()
                        output += output_part + "\n"
                    except pexpect.exceptions.TIMEOUT:
                        print("Timeout atingido; saindo do loop de captura.")
                        break
                    
                await websocket.send_json({"type": "data", "data": output.strip()})
    except Exception as e:
        print("WebSocket connection closed:", e)