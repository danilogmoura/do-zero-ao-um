
# Projeto: Terminais WebSocket com Python

## Visão Geral

Este projeto configura um ambiente com terminais interativos que se comunicam via WebSocket utilizando containers Docker. A aplicação exibe duas interfaces de terminal no navegador, conectadas a diferentes portas, permitindo a interação com uma shell Linux dentro dos containers.

## Arquitetura do Projeto

- **Frontend**: Uma página HTML que exibe os terminais usando [xterm.js](https://xtermjs.org/), uma biblioteca de emulação de terminal.
- **Backend (Python)**: Servidor Python com FastAPI para gerenciar conexões WebSocket, executando comandos no shell e retornando a saída para o frontend.
- **Containers Docker**: Dois containers distintos configurados com Docker Compose, cada um escutando uma porta WebSocket diferente, permitindo comunicação interativa com cada terminal.

## Estrutura dos Arquivos

- `index.html`: Interface web que renderiza dois terminais conectados aos WebSockets nas portas 3001 e 3002.
- `docker-compose.yml`: Configuração do Docker Compose para orquestrar os dois containers.
- `Dockerfile`: Define o ambiente com Python, utilizando Alpine Linux como base.
- `requirements.txt`: Lista as dependências Python (FastAPI, Uvicorn, etc.) necessárias para o backend.
- `server.py`: Servidor Python que gerencia as conexões WebSocket e executa comandos shell recebidos.

## Pré-requisitos

- Docker e Docker Compose instalados
- Navegador com suporte a WebSocket para acessar a interface dos terminais

## Como Funciona

### Frontend

- A página HTML usa `xterm.js` para renderizar os terminais e se conectar aos WebSockets nas portas 3001 e 3002.
- Comandos digitados são enviados para o backend, e a resposta é exibida no terminal.

### Backend

- O `server.py` define um servidor WebSocket com FastAPI, que gerencia a comunicação com o shell dentro do container.
- Cada comando enviado pelo frontend é executado no shell do container, e a saída é enviada de volta ao terminal correspondente.

### Containers

- Cada terminal conecta-se a um container diferente, isolando os ambientes.
- A configuração do Dockerfile utiliza Alpine Linux, proporcionando um ambiente leve e eficiente.

## Tecnologias Utilizadas

- **Docker** e **Docker Compose**
- **FastAPI** e **Uvicorn** para o backend Python
- **xterm.js** para o frontend interativo
- **Alpine Linux** como base dos containers para um ambiente otimizado
