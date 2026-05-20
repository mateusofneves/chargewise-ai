!pip install ollama

from IPython.display import clear_output
import ollama

# system prompt
SYSTEM_PROMPT = """
Você é o ChargeWise AI, um assistente inteligente especializado
na gestão comercial de estações de recarga para veículos elétricos.

Seu objetivo é auxiliar operadores comerciais e usuários com:

- disponibilidade de carregadores
- sessões de recarga
- consumo energético
- status operacional
- balanceamento de potência
- horários recomendados
- dúvidas sobre eletropostos

Responda de forma:

- clara
- objetiva
- profissional
- segura

Nunca invente informações.

Caso não saiba algo, informe que o sistema não possui
dados suficientes para responder.

Priorize:

- segurança elétrica
- eficiência energética
- estabilidade operacional
- experiência do usuário
"""

# json para dar contexto à ia
contexto = """
INFORMAÇÕES DO SISTEMA:

- Existem 2 carregadores disponíveis no condomínio.

- O melhor horário para recarga é entre 22h e 6h,
quando a demanda energética é menor.

- O sistema possui balanceamento inteligente de potência
para evitar sobrecarga elétrica.

- O tempo médio de recarga varia entre 2 e 6 horas,
dependendo da bateria do veículo.

- O uso dos carregadores depende das regras internas
do condomínio e da disponibilidade atual.

- Caso o aplicativo apresente falhas,
verifique a conexão do carregador com a rede.

- O sistema monitora o consumo energético
para melhorar a eficiência da recarga.
"""

# funcao principal
def perguntar_chatbot(pergunta):

    prompt = f"""
{SYSTEM_PROMPT}

BASE DE DADOS:
{contexto}

PERGUNTA DO USUÁRIO:
{pergunta}
"""

    resposta = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return resposta["message"]["content"]

# interface
clear_output()

print("=" * 50)
print("⚡ CHARGEWISE AI")
print("=" * 50)

print("\nAssistente inteligente para gestão")
print("de carregadores veiculares.\n")

print("Digite 'sair' para encerrar.\n")

# loop principal
while True:

    pergunta = input("👤 Você: ")

    if pergunta.lower() == "sair":
        print("\n🔌 Encerrando ChargeWise AI...")
        break

    resposta = perguntar_chatbot(pergunta)

    print("\n🤖 ChargeWise AI:")
    print(resposta)

    print("\n" + "-" * 50 + "\n")
