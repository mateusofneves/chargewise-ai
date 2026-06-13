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

# Testes Após atualização do System Prompt

Durante a fase de testes da Sprint 2, foram identificados comportamentos que exigiram ajustes no chatbot para aumentar a precisão das respostas e garantir aderência ao contexto GoodWe.

### Problema Identificado

Inicialmente, o modelo tentava responder perguntas que não estavam relacionadas ao domínio de mobilidade elétrica e carregadores veiculares.

**Exemplo:**

**Pergunta:**
> Quanto tempo leva para cozinhar carne na pressão?

**Resposta obtida inicialmente:**
> O modelo tentou relacionar incorretamente o tema de culinária ao contexto de carregadores elétricos, gerando uma resposta inadequada.

**Avaliação:**
❌ Inadequada

---

### Melhorias Implementadas

Para corrigir esse comportamento, foram realizadas as seguintes alterações:

- Adição de uma regra explícita de rejeição para perguntas fora do escopo do projeto.
- Implementação de validação prévia da pergunta por palavras-chave relacionadas ao contexto GoodWe.
- Redução do tamanho do contexto enviado ao modelo para melhorar o desempenho.
- Otimização dos exemplos de Few-Shot Prompting para aumentar a consistência das respostas.
- Redução do histórico armazenado para evitar crescimento excessivo do contexto.

---

### Resultado Após a Correção

**Pergunta:**
> Quanto tempo leva para cozinhar carne na pressão?

**Resposta obtida:**
> Sou especializado em carregadores veiculares GoodWe, mobilidade elétrica e infraestrutura de recarga. Não possuo conhecimento especializado sobre esse assunto.

**Avaliação:**
✅ Adequada

---

### Benefícios Obtidos

- Melhor aderência ao contexto GoodWe.
- Redução de respostas incorretas ou alucinações do modelo.
- Maior velocidade de resposta.
- Melhor controle sobre o escopo do chatbot.
- Atendimento ao requisito de iteração do system prompt solicitado na Sprint 2.
