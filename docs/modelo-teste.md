# Modelo de Testes — ChargeWise AI

## Objetivo

Este documento apresenta perguntas e respostas esperadas para validar o comportamento do chatbot dentro do contexto do EV Challenge 2026 da GoodWe.

O objetivo é garantir que o sistema responda corretamente dúvidas relacionadas à gestão comercial de estações de recarga para veículos elétricos.

---

# Cenários de Teste

| Pergunta | Resposta Esperada |
|---|---|
| Quantos carregadores estão disponíveis agora? | Existem 2 carregadores disponíveis no momento. |
| Qual o melhor horário para realizar recargas? | O horário recomendado é durante períodos de menor demanda energética para otimizar o consumo elétrico. |
| O sistema evita sobrecarga elétrica? | Sim. O sistema realiza balanceamento inteligente de potência para evitar sobrecarga elétrica. |
| Qual o status atual da estação de recarga? | A estação está operando normalmente no momento. |
| Quanto tempo leva para carregar um veículo? | O tempo médio varia entre 2 e 6 horas dependendo da capacidade da bateria e potência disponível. |

---

# Comportamento Esperado do Chatbot

O chatbot deve responder de forma:

- clara;
- objetiva;
- contextualizada;
- profissional;
- relacionada ao ambiente comercial de eletropostos.

Além disso, o sistema não deve inventar informações inexistentes.

---

# Critérios de Validação

O teste será considerado válido caso o chatbot:

- compreenda perguntas operacionais;
- mantenha contexto sobre estações de recarga;
- responda corretamente dúvidas sobre energia e carregamento;
- demonstre comportamento coerente com o cenário GoodWe/FIAP.

---

# Testes Após atualização do System Prompt, adição do histórico e few-shot

