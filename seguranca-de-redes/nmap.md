# Nmap - Network Mapper

O Nmap, ou Network Mapper, é uma ferramenta de código aberto usada para escanear redes e realizar auditorias de segurança. Criada inicialmente por Fyodor em 1997, o Nmap se tornou uma das ferramentas mais populares entre administradores de redes e profissionais de segurança. Seu principal propósito é ajudar na identificação de dispositivos e serviços ativos em uma rede, além de identificar vulnerabilidades e portas abertas que poderiam ser exploradas.

## Funcionalidades principais do Nmap

1. **Escaneamento de Portas**: O Nmap é amplamente usado para escanear portas abertas em dispositivos de uma rede. Com ele, é possível verificar quais portas estão ativas e disponíveis em um host, o que é útil para identificar serviços e potenciais pontos de entrada.

2. **Identificação de Serviços**: Além de escanear portas, o Nmap consegue identificar os serviços que estão rodando nessas portas, como HTTP, FTP, SSH, etc. Ele também tenta descobrir as versões dos serviços para facilitar a identificação de possíveis vulnerabilidades específicas.

3. **Detecção de SO (Sistema Operacional)**: O Nmap consegue identificar o sistema operacional de um dispositivo remoto por meio de uma técnica de fingerprinting (impressão digital) baseada nas respostas de rede. Essa função é útil em auditorias e na compreensão do ambiente da rede.

4. **Scripts NSE (Nmap Scripting Engine)**: O Nmap possui um motor de scripts embutido que permite a execução de scripts Lua, ajudando a realizar verificações mais avançadas, como detectar vulnerabilidades específicas, fazer brute force e até automações personalizadas.

5. **Escaneamento em Massa**: O Nmap é otimizado para escanear grandes redes e fazer auditorias em massa, o que é útil para empresas que precisam monitorar suas redes internas ou externas de forma recorrente.

6. **Modos Stealth e Scan Evasivo**: Ele também suporta técnicas para fazer escaneamentos furtivos, evitando ser detectado em algumas redes, o que é útil em testes de intrusão.

## Como Instalar o Nmap no Windows e Linux (Debian/Ubuntu)

### Instalação no Windows

1. **Baixe o Instalador Oficial**:
   - Acesse o site oficial do Nmap: [https://nmap.org](https://nmap.org) e baixe o instalador mais recente para Windows.

2. **Instale o Nmap**:
   - Execute o instalador e siga as instruções de instalação. Durante a instalação, você pode optar por instalar o **Zenmap** (interface gráfica para o Nmap no Windows).

3. **Execute o Nmap**:
   - Após a instalação, abra o Nmap pelo Prompt de Comando ou PowerShell. Se preferir, pode abrir o Zenmap para uma interface gráfica mais amigável.

### Instalação no Linux (Debian/Ubuntu)

1. **Atualize os Repositórios**:
   ```bash
   sudo apt update
   ```
   
2. **Instale o Nmap**:
   ```bash
   sudo apt install nmap
   ```
   
2. **Verifique a Instalação**:
   - Após a instalação, você pode confirmar que o Nmap foi instalado corretamente verificando sua versão:

   ```bash
   nmap --version
   ```
 
 ## Fundamentos do Nmap e Configuração de Ambiente

1. **Instalação e Configuração**:
   - Instale o Nmap nas duas máquinas (scanner e alvo).
   - Certifique-se de que ambas as máquinas estão na mesma rede local.
   
2. **Comandos Básicos do Nmap**:
   - Execute um simples comando para escanear o IP da máquina alvo:
     ```bash
     nmap <IP_da_máquina_alvo>
     ```
   - Experimente as opções `-v` (modo verbose) e `-Pn` (ignora a verificação se o host está ativo).

3. **Explorar Portas e Protocolos**:
   - Use o Nmap para identificar portas abertas em sua máquina alvo:
     ```bash
     nmap -p 1-1000 <IP_da_máquina_alvo>
     ```
   - Tente escanear portas específicas (por exemplo, porta 22 para SSH, porta 80 para HTTP).

## Escaneamento de Versões e Detecção de Sistema Operacional

1. **Detecção de Versões de Serviços**:
   - Use o comando para detectar versões de serviços em portas abertas:
     ```bash
     nmap -sV <IP_da_máquina_alvo>
     ```

2. **Detecção de Sistema Operacional**:
   - Execute um escaneamento para tentar identificar o sistema operacional da máquina alvo:
     ```bash
     nmap -O <IP_da_máquina_alvo>
     ```

3. **Escaneamento Completo com Informação Detalhada**:
   - Combine várias opções para um escaneamento mais detalhado:
     ```bash
     nmap -A <IP_da_máquina_alvo>
     ```
   - Observe as informações coletadas, como OS, versão de serviços, e trace a rota dos pacotes.

## Host Discovery e Escaneamento de Rede

1. **Descoberta de Hosts na Rede**:
   - Escaneie uma faixa de IPs para descobrir todos os dispositivos na rede:
     ```bash
     nmap -sn <IP_rede>/24
     ```
   - Use `-sn` (scan without port) para identificar os dispositivos ativos sem escanear portas.

2. **Escaneamento em Intervalos de IPs**:
   - Escaneie múltiplos hosts ou um intervalo específico:
     ```bash
     nmap <IP_inicial>-<IP_final>
     ```
   
3. **Escaneamento de Rede com Serviço e Versão**:
   - Combine a descoberta de rede com detecção de versão e serviço:
     ```bash
     nmap -sV <IP_rede>/24
     ```

## Nmap Scripting Engine (NSE) e Automação de Escaneamentos

1. **Introdução ao NSE**:
   - Leia sobre o Nmap Scripting Engine e explore alguns scripts úteis.
   - Execute scripts para coletar informações adicionais, como vulnerabilidades:
     ```bash
     nmap --script=vuln <IP_da_máquina_alvo>
     ```

2. **Escaneamento de Vulnerabilidades**:
   - Use scripts de vulnerabilidades específicos para escanear a máquina alvo:
     ```bash
     nmap --script=http-vuln* <IP_da_máquina_alvo>
     ```
   - Teste scripts de força bruta em serviços como SSH (cuidado com o impacto na máquina alvo).

3. **Automação e Agendamento de Escaneamentos**:
   - Crie um pequeno script para automatizar escaneamentos e gerar relatórios.
   - Agende o script para rodar em horários específicos (usando `cron` no Linux ou `Task Scheduler` no Windows).

## Análise de Resultados e Relatórios

1. **Interpretação dos Resultados**:
   - Revise os relatórios de cada tipo de escaneamento e interprete os dados coletados (versões, portas, vulnerabilidades, etc.).

2. **Exportação de Resultados**:
   - Pratique exportar resultados para diferentes formatos:
     ```bash
     nmap -oN normal_output.txt -oX xml_output.xml <IP_da_máquina_alvo>
     ```

3. **Geração de Relatórios e Documentação**:
   - Organize os resultados dos seus escaneamentos em um relatório.
   - Compare as configurações e serviços da máquina alvo com as vulnerabilidades detectadas.

## Documentação Oficial

- Leia a [documentação do Nmap](https://nmap.org/book/) para entender melhor as opções.