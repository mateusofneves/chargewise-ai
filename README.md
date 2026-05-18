# ChargeWise AI

Assistente inteligente para gestão comercial de carregadores veiculares elétricos.

Projeto desenvolvido para o **EV Challenge 2026 — GoodWe** em parceria com a **FIAP**.

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

O projeto **ChargeWise AI** foi desenvolvido com o objetivo de auxiliar operadores comerciais na gestão inteligente de estações de recarga para veículos elétricos.

A proposta consiste em um chatbot contextualizado com inteligência artificial capaz de responder dúvidas operacionais, fornecer informações sobre sessões de recarga, auxiliar no gerenciamento energético e melhorar a comunicação com usuários dos eletropostos.

O sistema foi pensado como uma solução operacional real para o contexto comercial do EV Challenge 2026 da GoodWe.

---

# Problema Abordado

Empresas e operadores comerciais que utilizam eletropostos enfrentam diversos desafios operacionais, como:

- Falta de monitoramento inteligente das estações;
- Dificuldade no gerenciamento de potência elétrica;
- Ausência de comunicação automatizada com usuários;
- Controle manual de sessões de recarga;
- Dificuldade na organização operacional dos eletropostos;
- Falta de suporte automatizado para usuários.

O ChargeWise AI busca reduzir esses problemas através de atendimento automatizado e contextualizado.

---

# Objetivo do Chatbot

O ChargeWise AI tem como principais objetivos:

- Informar disponibilidade dos carregadores;
- Responder dúvidas sobre recarga;
- Auxiliar operadores comerciais;
- Informar status das estações;
- Melhorar a experiência dos usuários;
- Facilitar o gerenciamento operacional dos eletropostos.

---

# Persona Principal

## Operador Comercial

A solução foi pensada principalmente para operadores responsáveis pela administração de estações de carregamento veicular.

O chatbot auxiliará no monitoramento operacional, organização do sistema e atendimento automatizado aos usuários.

---

# Tecnologias Utilizadas

| Tecnologia | Função |
|---|---|
| Python | Desenvolvimento do chatbot |
| Google Colab | Ambiente de testes |
| Markdown | Documentação do projeto |
| Draw.io | Desenvolvimento do fluxograma |
| GitHub | Versionamento e organização |

---

# Justificativa Técnica

A utilização de um chatbot contextualizado permite criar respostas mais naturais e específicas para o ambiente comercial de carregamento veicular.

O protótipo desenvolvido na Sprint 1 foi pensado para validar:

- fluxo de funcionamento do sistema;
- experiência do usuário;
- contexto operacional;
- comportamento esperado do chatbot.

A estrutura criada também prepara o projeto para futuras integrações com APIs de IA e sistemas reais de monitoramento de eletropostos.

---

# Funcionalidades Previstas

- Consulta de disponibilidade de carregadores;
- Informações sobre sessões de recarga;
- Respostas automáticas para dúvidas frequentes;
- Informações sobre consumo energético;
- Status operacional das estações;
- Alertas relacionados à potência elétrica.

---

# Fluxo Básico do Sistema

```text
Usuário
   ↓
Chatbot ChargeWise AI
   ↓
Processamento da Pergunta
   ↓
Contexto Operacional
   ↓
Geração da Resposta
   ↓
Usuário
```

---

# Modelo de Testes

| Pergunta | Resposta Esperada |
|---|---|
| Quantos carregadores estão disponíveis? | Existem carregadores disponíveis no momento. |
| Qual o melhor horário para recarga? | O horário recomendado é durante períodos de menor demanda energética. |
| O sistema evita sobrecarga? | Sim, o sistema realiza controle inteligente de potência. |
| Qual o status da estação de recarga? | A estação está operando normalmente. |
| Quanto tempo leva a recarga? | O tempo varia conforme bateria e potência disponível. |

---

# System Prompt Base

```text
Você é o ChargeWise AI, um assistente especializado na gestão comercial de carregadores veiculares elétricos.

Seu objetivo é auxiliar operadores comerciais e usuários com informações sobre:
- disponibilidade de carregadores;
- sessões de recarga;
- consumo energético;
- status operacional das estações;
- balanceamento de potência.

Responda de forma clara, objetiva e profissional.

Nunca invente informações inexistentes.
```

---

# Estrutura do Projeto

```text
chargewise-ai/
│
├── README.md
├── entregavel.txt
│
├── docs/
│   ├── fluxograma.png
│   ├── modelo-testes.md
│   └── system-prompt.md
│
├── colab/
│   └── chatbot_teste.ipynb
│
└── assets/
```

# EV Challenge 2026 — GoodWe

Projeto acadêmico desenvolvido para o desafio EV Challenge 2026 da GoodWe em parceria com a FIAP.
