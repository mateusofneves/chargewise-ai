# ChargeWise AI

Assistente inteligente para gestão de carregadores veiculares elétricos em condomínios.

---

# Integrantes

| Nome | RM |
|---|---|
| Mateus de Oliveira Fernandes Neves | RM 572431 |
| Pedro Soares de Souza | RM 571285 |
| Paulo Henrique Lira Bilac de Araujo | RM 569496 |
| Olavo Dadario Vianna Barreto | RM 569496 |
| Angela Sousa Takezawa | RM 570797 |

---

# Sobre o Projeto

O projeto **ChargeWise AI** foi desenvolvido para o EV Challenge 2026 da GoodWe com o objetivo de auxiliar condomínios na gestão inteligente de carregadores de veículos elétricos.

A proposta consiste em um chatbot com inteligência artificial capaz de responder dúvidas operacionais, fornecer informações sobre recarga, orientar usuários e auxiliar administradores na organização do uso compartilhado dos eletropostos.

---

# Problema Abordado

Condomínios que utilizam carregadores compartilhados enfrentam problemas como:

- Falta de controle sobre o uso dos carregadores;
- Sobrecarga energética;
- Ausência de monitoramento inteligente;
- Dificuldade de comunicação com moradores;
- Falta de transparência no consumo individual;
- Organização manual do sistema de recarga.

O chatbot busca reduzir esses problemas através de atendimento automatizado e contextualizado.

---

# Objetivo do Chatbot

O ChargeWise AI tem como objetivo:

- Informar disponibilidade dos carregadores;
- Responder dúvidas sobre recarga;
- Auxiliar no controle de potência;
- Informar regras de utilização;
- Melhorar a experiência de moradores e síndicos;
- Facilitar o gerenciamento operacional dos eletropostos.

---

# Persona Principal

## Síndico / Administrador Condominial

A solução foi pensada principalmente para síndicos e administradores responsáveis pela gestão dos carregadores compartilhados.

O chatbot ajudará na redução de conflitos, organização do uso e monitoramento operacional do sistema.

---

# Tecnologias Selecionadas

| Tecnologia | Função |
|---|---|
| OpenAI API | Processamento de linguagem natural |
| LangChain | Orquestração do chatbot |
| Python | Backend principal |
| FastAPI | Criação da API |
| MongoDB | Armazenamento de dados |
| React | Interface web |
| GitHub | Versionamento do projeto |

---

# Justificativa Técnica

A utilização de IA generativa permite criar respostas contextualizadas e mais naturais para usuários do sistema.

O LangChain facilitará a integração entre contexto operacional, histórico de conversas e futuras integrações com sensores e banco de dados.

O MongoDB foi escolhido devido à flexibilidade no armazenamento de informações relacionadas às sessões de recarga e conversas do chatbot.

---

# Funcionalidades Previstas

- Consulta de disponibilidade de carregadores;
- Informações sobre sessões de recarga;
- Respostas automáticas para dúvidas frequentes;
- Orientações de consumo energético;
- Informações sobre regras de utilização;
- Alertas relacionados à potência elétrica.

---

# Fluxo Básico do Sistema

```text
Usuário
   ↓
Frontend
   ↓
API FastAPI
   ↓
LangChain
   ↓
Contexto do Condomínio
   ↓
Modelo OpenAI
   ↓
Resposta Inteligente
```

---

# Estrutura Inicial do Projeto

```text
chargewise-ai/
│
├── README.md
├── docs/
├── backend/
├── frontend/
└── assets/
```

---

# Modelo de Testes

| Pergunta | Resposta Esperada |
|---|---|
| Quantos carregadores estão disponíveis? | Existem carregadores disponíveis no momento. |
| Qual o melhor horário para recarga? | O horário recomendado é durante períodos de menor demanda energética. |
| O sistema evita sobrecarga? | Sim, o sistema realiza controle inteligente de potência. |
| Posso utilizar qualquer carregador? | O uso depende das regras e disponibilidade do condomínio. |
| Quanto tempo leva a recarga? | O tempo varia conforme bateria e potência disponível. |

---

# System Prompt Base

```text
Você é o ChargeWise AI, um assistente especializado na gestão de carregadores veiculares em condomínios.

Seu objetivo é auxiliar moradores e administradores com informações sobre:
- disponibilidade de carregadores;
- sessões de recarga;
- consumo energético;
- regras de utilização;
- balanceamento de potência.

Responda de forma clara, objetiva e profissional.

Nunca invente informações inexistentes.
```

---

# EV Challenge 2026 — GoodWe

Projeto acadêmico desenvolvido para o desafio EV Challenge 2026 da GoodWe em parceria com a FIAP.
