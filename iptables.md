
# iptables
---

## Fundamentos do iptables e Configuração do Ambiente

1. **Configuração do Ambiente**:
   - Certifique-se de que ambas as máquinas estejam na mesma rede para facilitar o teste de conectividade.

2. **Instalação do iptables**:
   - Verifique se o `iptables` está instalado em ambas as máquinas (muitas distribuições já vêm com ele por padrão).
   - Em distribuições baseadas em Debian/Ubuntu:
     ```bash
     sudo apt-get update
     sudo apt-get install iptables
     ```

3. **Comandos Básicos**:
   - Familiarize-se com comandos básicos, como listar regras (`-L`), adicionar regras (`-A`), e apagar regras (`-D`).
   - Exemplo de listagem de regras:
     ```bash
     sudo iptables -L
     ```

4. **Introdução às Cadeias e Políticas**:
   - Estude as três principais cadeias: `INPUT`, `OUTPUT`, e `FORWARD`.
   - Defina uma política padrão para cada cadeia:
     ```bash
     sudo iptables -P INPUT DROP
     sudo iptables -P OUTPUT ACCEPT
     sudo iptables -P FORWARD DROP
     ```

---

## Controle de Acesso Básico

1. **Permitir e Bloquear Conexões SSH**:
   - Crie uma regra para permitir conexões SSH (porta 22) à máquina configurada com iptables, usando a outra máquina para testar.
     ```bash
     sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
     ```
   - Teste a regra conectando-se à máquina via SSH a partir da máquina de teste. Em seguida, bloqueie o SSH para verificar o impacto.

2. **Permitir o Ping (ICMP)**:
   - Adicione uma regra para permitir ICMP (ping):
     ```bash
     sudo iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT
     ```
   - Teste a regra pingando a máquina configurada com iptables a partir da máquina de teste. Em seguida, bloqueie o ICMP e observe a diferença.

3. **Registrar Pacotes Bloqueados**:
   - Adicione uma regra para registrar tentativas de conexão bloqueadas:
     ```bash
     sudo iptables -A INPUT -j LOG --log-prefix "Pacote Bloqueado: "
     ```

---

## Controle de Serviços e Portas

1. **Bloquear e Permitir Serviços Específicos**:
   - Experimente bloquear o tráfego HTTP (porta 80) e HTTPS (porta 443) para aprender como as regras afetam o acesso aos serviços web.
     ```bash
     sudo iptables -A INPUT -p tcp --dport 80 -j DROP
     sudo iptables -A INPUT -p tcp --dport 443 -j DROP
     ```

2. **Permitir Conexões de Rede Interna e Bloquear Externa**:
   - Adicione uma regra que permita conexões apenas da rede local (exemplo para IPs na faixa `192.168.1.0/24`):
     ```bash
     sudo iptables -A INPUT -s 192.168.1.0/24 -j ACCEPT
     ```

3. **Testes de Conectividade**:
   - Use a máquina de teste para acessar diferentes serviços e verifique o impacto das regras.

---

## Filtragem Avançada e Controle de Conexão

1. **Controle de Conexões Estabelecidas e Relacionadas**:
   - Use o módulo de rastreamento de conexões (`conntrack`) para permitir apenas conexões estabelecidas e relacionadas, bloqueando novas conexões de entrada:
     ```bash
     sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
     ```

2. **Limitar Taxa de Conexão (Rate Limiting)**:
   - Implemente limitação de taxa para evitar ataques de força bruta em SSH:
     ```bash
     sudo iptables -A INPUT -p tcp --dport 22 -m limit --limit 5/min -j ACCEPT
     ```

3. **Criar Regras para Diferentes Protocolos**:
   - Pratique a criação de regras para UDP, TCP e ICMP, observando como cada uma afeta o tráfego.

---

## Salvando Regras e Automatização

1. **Salvar e Restaurar Regras**:
   - Salve as regras iptables para que persistam após reinicialização:
     - Em distribuições Debian/Ubuntu:
       ```bash
       sudo iptables-save > /etc/iptables/rules.v4
       ```

2. **Criar Scripts para Regras**:
   - Crie um script simples para aplicar as regras automaticamente.
   - Exemplo de script:
     ```bash
     #!/bin/bash
     sudo iptables -P INPUT DROP
     sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
     sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
     ```

3. **Testar Reinicialização com Regras Persistentes**:
   - Reinicie a máquina e verifique se as regras foram aplicadas corretamente.

---

## Documentação do iptables

- Leia a [documentação oficial](https://netfilter.org/projects/iptables/index.html) para mais detalhes sobre cada módulo e configuração.