## Introdução às Áreas de Segurança

### 1. Segurança da Informação

**Definição:** Segurança da informação é a prática de proteger dados e sistemas contra acessos não autorizados, uso indevido, divulgação, destruição e modificação. Ela se baseia em garantir três pilares fundamentais: confidencialidade, integridade e disponibilidade (CIA). Esses pilares são os princípios básicos para evitar que informações sejam comprometidas ou alteradas por terceiros.

- **Firewalls:** Dispositivos ou software que filtram e monitoram o tráfego de rede com base em regras de segurança predefinidas. Eles protegem redes e sistemas contra acessos não autorizados.
- **VPN (Virtual Private Network):** Uma rede privada virtual que cria uma conexão segura entre o dispositivo de um usuário e a internet. VPNs são usadas para proteger a privacidade e criptografar dados em trânsito.
- **Criptografia:** O processo de codificar dados para que apenas partes autorizadas possam acessá-los. A criptografia protege a confidencialidade das informações, tornando-as ilegíveis para quem não possui as credenciais de acesso.

### 2. Análise de Malware

**Definição:** Malware é qualquer software projetado para prejudicar, explorar ou obter acesso não autorizado a sistemas ou redes. A análise de malware visa investigar esses programas para entender seu comportamento, identificar vetores de ataque e desenvolver defesas.

**Tipos de Malware:**
- **Vírus:** Malware que se replica ao infectar outros programas.
- **Ransomware:** Software que criptografa dados e exige pagamento para sua liberação.
- **Spyware:** Malware que coleta dados do usuário sem permissão.

**Análise Estática e Dinâmica:**
- **Análise Estática:** Consiste em examinar o código do malware sem executá-lo, verificando arquivos e estruturas para identificar padrões maliciosos.
- **Análise Dinâmica:** Envolve a execução do malware em um ambiente controlado (como uma sandbox) para observar seu comportamento em tempo real.

### 3. Engenharia Reversa

**Definição:** Engenharia reversa é o processo de desmontar um sistema ou software para entender sua estrutura interna e funcionamento. Na segurança, é usada para investigar o comportamento de programas maliciosos ou identificar vulnerabilidades em software.

- **Assembly:** Uma linguagem de baixo nível próxima à linguagem de máquina. No contexto da engenharia reversa, o assembly é essencial para analisar a estrutura de código que foi compilado.
- **Desmontagem (Disassembly):** Processo de converter um programa executável em código de assembly, permitindo que os analistas vejam instruções de baixo nível e compreendam o funcionamento de softwares e malwares.
- **Ghidra e Radare2:** Ferramentas de engenharia reversa que permitem visualizar, desmontar e analisar código binário de programas. São amplamente utilizadas para entender o comportamento de malware.

### 4. Internet das Coisas (IoT) e Segurança

**Definição:** IoT refere-se a dispositivos conectados que coletam e compartilham dados, como sensores, eletrodomésticos e veículos. Esses dispositivos operam em rede e frequentemente carecem de recursos de segurança, tornando-se vulneráveis a ataques.

- **Protocolos IoT:** Protocolos de comunicação (como MQTT e CoAP) que permitem a troca de dados entre dispositivos IoT. Cada protocolo tem suas particularidades, o que afeta as práticas de segurança.
- **Análise de Firmware:** O firmware é o software básico que opera o hardware de um dispositivo. A análise de firmware identifica vulnerabilidades em dispositivos IoT, como falhas de autenticação e brechas de acesso.
- **Wireshark:** Ferramenta de captura de pacotes de rede usada para monitorar e analisar o tráfego de dispositivos IoT. Com o Wireshark, é possível identificar anomalias e tentativas de acesso não autorizado.

### 5. DevSecOps

**Definição:** DevSecOps é uma abordagem que integra práticas de segurança no ciclo de desenvolvimento de software, desde a concepção até a operação. O termo combina “Desenvolvimento” (Dev), “Segurança” (Sec) e “Operações” (Ops), representando um fluxo de trabalho contínuo onde a segurança é automatizada e integrada.

- **Docker e Jenkins:** Docker é uma plataforma de contêinerização que permite criar e gerenciar aplicativos em contêineres isolados, melhorando a consistência e a segurança. Jenkins é uma ferramenta de automação CI/CD (Integração Contínua/Entrega Contínua) que facilita a automação de testes e deploys de código. Na abordagem DevSecOps, Docker e Jenkins são usados para automatizar testes de segurança e monitoramento durante o desenvolvimento.
- **CI/CD (Continuous Integration/Continuous Deployment):** Práticas que integram alterações de código de forma contínua e automatizada. No DevSecOps, a CI/CD inclui testes de segurança automatizados, garantindo que o código seja seguro antes de ser implementado em produção.
- 
## Profissão de AppSec (Application Security)

A profissão de AppSec (Application Security) é focada na segurança de software, englobando práticas e metodologias que protegem aplicativos contra ameaças e vulnerabilidades. Profissionais de AppSec têm como principal objetivo assegurar que softwares e sistemas estejam protegidos contra ataques maliciosos que possam comprometer dados, funcionalidades ou a integridade do sistema.

## Principais Atividades de um Profissional de AppSec

### 1. Análise de Vulnerabilidades  
Identificação de falhas em aplicações através de ferramentas e técnicas específicas. As principais incluem:

- **SAST (Static Application Security Testing)**: Teste de segurança aplicado diretamente ao código fonte de uma aplicação sem executá-la. O SAST identifica problemas no código (como variáveis inseguras e falhas de validação de entrada) antes mesmo da aplicação ser executada. Ideal para detectar vulnerabilidades desde o início do desenvolvimento.
  
- **DAST (Dynamic Application Security Testing)**: Teste de segurança realizado enquanto a aplicação está em execução. Simula ataques para identificar como a aplicação responde em tempo real a possíveis explorações, sem precisar do acesso ao código fonte.
  
- **SCA (Software Composition Analysis)**: Técnica que verifica a segurança de componentes de software de terceiros, como bibliotecas e frameworks externos, identificando vulnerabilidades conhecidas (CVEs) que podem afetar a aplicação.

### 2. Modelagem de Ameaças  
Técnica usada para antecipar possíveis ataques, identificando e documentando as ameaças mais prováveis a uma aplicação ou sistema. Esse processo permite que o time de segurança construa uma defesa eficaz considerando as ameaças e riscos antes do desenvolvimento ou durante o planejamento do projeto.

### 3. Testes de Intrusão (Pentests)  
Também conhecido como "pentesting", o teste de intrusão simula ataques controlados para identificar vulnerabilidades que poderiam ser exploradas em um ataque real. Isso é feito através de metodologias de hacking ético, onde profissionais de segurança tentam acessar o sistema de forma não autorizada, como um invasor faria, para descobrir falhas.

### 4. Implementação de SDLC Seguro (Secure SDLC)  
O SDLC (Ciclo de Vida de Desenvolvimento de Software) Seguro é uma prática que integra a segurança em cada fase do desenvolvimento do software, desde o planejamento até a manutenção. O **Secure SDLC** inclui:

- **Planejamento**: Análise de requisitos de segurança e definição de políticas.
- **Desenvolvimento**: Uso de práticas seguras de codificação para evitar vulnerabilidades comuns.
- **Testes**: Verificação de segurança em cada estágio, com técnicas de SAST, DAST e pentesting.
- **Lançamento e Manutenção**: Monitoramento contínuo de segurança e atualização de patches para corrigir vulnerabilidades.

### 5. Uso de Ferramentas de Segurança  
Utilização de ferramentas específicas para verificar a segurança do aplicativo, automatizando processos que identificam vulnerabilidades. Algumas das mais usadas incluem:

- **Burp Suite**: Ferramenta usada para testar a segurança de aplicativos web, permitindo interceptação e manipulação de requisições HTTP.
- **OWASP ZAP**: Ferramenta gratuita para testes de segurança em aplicativos web, ideal para iniciantes e compatível com DAST.
- **Fortify**: Solução de segurança empresarial usada para SAST, integrando-se ao SDLC.
- **Checkmarx**: Plataforma de segurança que realiza SAST e SCA para encontrar falhas de segurança no código-fonte.

### 6. Integração com DevOps (DevSecOps)  
DevSecOps é a prática de incorporar segurança em cada estágio do processo DevOps, unindo desenvolvimento (Dev), operações (Ops) e segurança (Sec) para criar um ciclo de desenvolvimento ágil e seguro. As equipes DevSecOps integram ferramentas de segurança (como SAST e DAST) nos pipelines de CI/CD, automatizando a verificação de segurança em cada versão do código.

### 7. Gerenciamento de Vulnerabilidades  
Processo de coordenação para tratar e corrigir vulnerabilidades identificadas. Inclui:

- **Priorizar correções**: Avaliação da gravidade das vulnerabilidades e priorização da correção com base no impacto e na facilidade de exploração.
- **Implementação de correções**: Trabalho em conjunto com desenvolvedores para aplicar correções.
- **Monitoramento contínuo**: Revisão e acompanhamento para novas ameaças e vulnerabilidades.

## Habilidades e Competências Necessárias

- **Conhecimento em linguagens de programação e frameworks de desenvolvimento**: É essencial entender como o código é escrito e como diferentes frameworks funcionam para poder identificar falhas de segurança.
  
- **Familiaridade com normas e padrões de segurança** (como OWASP Top 10, CIS Controls): Conhecimento das normas de segurança mais usadas no mercado, como o **OWASP Top 10** (lista das dez vulnerabilidades mais críticas em segurança de aplicações web) e **CIS Controls** (práticas recomendadas para melhorar a segurança organizacional).

- **Experiência em ferramentas de análise de segurança** (SAST, DAST, SCA): Familiaridade com ferramentas que realizam análises estáticas, dinâmicas e de componentes externos, o que permite identificar falhas de segurança rapidamente.

- **Entendimento profundo de protocolos de rede, criptografia, autenticação e autorização**: Compreensão de como os dados trafegam entre sistemas e são protegidos, essencial para evitar interceptações e acessos não autorizados.

- **Capacidade analítica e atenção aos detalhes** para identificar e avaliar riscos de segurança: Habilidade para revisar código e comportamento da aplicação, identificando pontos vulneráveis e potenciais riscos.