# ChargeWise AI

Assistente inteligente especializado em carregadores veiculares GoodWe, mobilidade elétrica e infraestrutura de recarga.

Projeto desenvolvido para o EV Challenge 2026 — GoodWe em parceria com a FIAP.

---

# Integrantes

| Nome | RM |
|---|---|
| Mateus de Oliveira Fernandes Neves | RM 572431 |
| Pedro Soares de Souza | RM 571285 |
| Paulo Henrique Lira Bilac de Araujo | RM 569496 |
| Olavo Dadario Vianna Barreto | RM 569272 |
| Angela Sousa Takezawa | RM 570797 |

---

# Sobre o Projeto

O ChargeWise AI é um chatbot inteligente desenvolvido para auxiliar usuários, síndicos, administradores de condomínio, operadores e profissionais da área elétrica com informações relacionadas a carregadores veiculares, infraestrutura de recarga e soluções GoodWe.

Durante a Sprint 2 foram implementadas técnicas de Inteligência Artificial Generativa para tornar as respostas mais contextualizadas, coerentes e alinhadas ao cenário do EV Challenge 2026.

O sistema utiliza o modelo Llama 3.2 1B executado localmente através do Ollama, permitindo interações em linguagem natural e respostas especializadas no contexto de mobilidade elétrica.

- Link para o vídeo com funicionamento e testes: [ChargeWise-AI](https://youtu.be/Utbi84uknSo)

---

# Problema Abordado

Com o crescimento da adoção de veículos elétricos, surgem desafios relacionados à instalação, gerenciamento e utilização de carregadores veiculares.

Entre os principais desafios estão:

Falta de suporte automatizado aos usuários;
Dúvidas sobre instalação e utilização dos carregadores;
Gerenciamento da demanda energética;
Compartilhamento da infraestrutura em condomínios;
Integração com sistemas de energia solar;
Eficiência energética e balanceamento de carga.

O ChargeWise AI foi desenvolvido para auxiliar na solução desses desafios através de atendimento automatizado e contextualizado.

---

# Objetivos

- Responder dúvidas sobre carregadores GoodWe;
- Auxiliar usuários de veículos elétricos;
- Fornecer orientações sobre infraestrutura de recarga;
- Apoiar síndicos e administradores de condomínio;
- Explicar conceitos de eficiência energética;
- Fornecer informações sobre integração com energia solar;
- Melhorar a experiência dos usuários através de IA Generativa.
- Funcionalidades Implementadas
- Contextualização especializada através de System Prompt;
- Memória conversacional utilizando histórico de mensagens;
- Few-Shot Prompting para direcionamento das respostas;
- Adaptação da linguagem conforme o perfil do usuário;
- Controle de escopo para evitar respostas fora do contexto do projeto;
- Histórico de conversa para diálogos contínuos;
- Respostas especializadas no contexto GoodWe;
- Escalonamento para suporte técnico quando necessário.
- Personas Atendidas
- Usuário Final

Busca informações sobre carregamento, horários recomendados e utilização dos carregadores.

## Síndico ou Administrador

Necessita avaliar viabilidade de instalação, compartilhamento da infraestrutura e gestão energética.

## Técnico ou Eletricista

Precisa de informações relacionadas à infraestrutura elétrica, dispositivos de proteção e boas práticas de instalação.

---

# Tecnologias Utilizadas

|Tecnologia	| Função |
|---|---|
|Python	| Desenvolvimento do chatbot |
|Ollama	| Execução local do modelo de IA |
|Llama 3.2 1B	| Modelo de linguagem |
|Google Colab	| Ambiente de desenvolvimento |
|Markdown	| Documentação |
|Draw.io	| Fluxograma |
|GitHub	| Versionamento |

---

# Arquitetura da Solução
```text
Usuário
   ↓
Interface Conversacional
   ↓
System Prompt
   ↓
Few-Shot Prompting
   ↓
Base de Conhecimento GoodWe
   ↓
Histórico de Conversa
   ↓
Llama 3.2 1B (Ollama)
   ↓
Resposta Contextualizada
   ↓
Usuário
```

---

# Técnicas de IA Aplicadas

### System Prompt

Define o comportamento do assistente e restringe sua atuação ao contexto GoodWe, mobilidade elétrica e infraestrutura de recarga.

### Few-Shot Prompting

Utilização de exemplos de perguntas e respostas para orientar o comportamento esperado do modelo.

### Memória Conversacional

Implementação de histórico de mensagens para permitir conversas contínuas e contextualizadas.

### Context Injection

Inserção de informações específicas relacionadas ao cenário GoodWe e ao EV Challenge.

### Ajuste de Parâmetros

Configuração de temperatura e limite de geração de tokens para melhorar consistência e desempenho.

---

# Base de Conhecimento Utilizada

O chatbot foi configurado utilizando informações relacionadas a:

Carregadores GoodWe;
Veículos elétricos;
Infraestrutura de recarga;
Gestão energética;
Balanceamento inteligente de carga;
Integração com energia solar;
Utilização de carregadores em condomínios.

---

# Resultados Obtidos

- Responde adequadamente perguntas relacionadas ao contexto GoodWe;
- Mantém o escopo definido pelo projeto;
- Utiliza memória de conversa para melhorar a continuidade das interações;
- Adapta respostas ao perfil do usuário;
- Recusa perguntas fora do domínio do projeto;
- Mantém coerência durante diálogos contínuos.
- Melhorias Implementadas Durante a Sprint 2
- Refinamento do System Prompt;
- Implementação de memória conversacional;
- Inclusão de Few-Shot Prompting;
- Ajuste dos parâmetros do modelo;
- Otimização do contexto enviado ao LLM;
- Controle de escopo para respostas fora do domínio.

---

# Como Executar

### Pré-requisitos
Python 3.10+
Ollama instalado
Instalação
pip install ollama
Download do Modelo
ollama pull llama3.2:1b

### Execução

Abra o notebook disponível na pasta:

colab/chatbot_teste.ipynb

ou execute o script Python principal do projeto.

Para encerrar o chatbot:

sair

---

# Estrutura do Projeto

```text
chargewise-ai/
│
├── docs/
│   ├── goodwe chatbot.drawio.png
│   ├── modelo-teste.md
│   └── system-prompt.md
│
├── colab/
│   ├── chatbot.py
│   └── chatbot_charge.py
│
├── assets/
│   ├── chatbot-demo-1.jpeg
│   ├── chatbot-demo-2.jpeg
│   ├── chatbot-demo-3.jpeg
│   └── chatbot-demo-4.jpeg
|
└── README.md
```

---

## EV Challenge 2026 — GoodWe

Projeto acadêmico desenvolvido para o EV Challenge 2026 da GoodWe em parceria com a FIAP, com foco na aplicação de Inteligência Artificial Generativa para suporte a usuários de carregadores veiculares e soluções de mobilidade elétrica.
