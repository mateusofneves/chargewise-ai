from openai import OpenAI

# configuracao da api
client = OpenAI(
    api_key="SUA_API_KEY_AQUI"
)

# system prompt
SYSTEM_PROMPT = """
Você é o ChargeWise AI, um assistente inteligente especializado
na gestão de carregadores veiculares elétricos em condomínios.

Seu objetivo é auxiliar síndicos, administradores e moradores com:

- disponibilidade de carregadores;
- sessões de recarga;
- consumo energético;
- regras de utilização;
- balanceamento de potência;
- horários recomendados para carregamento.

Você deve responder de forma:
- clara;
- objetiva;
- profissional;
- contextualizada ao ambiente condominial.

Nunca invente informações inexistentes.
"""

# funcao do chatbot
def perguntar_chatbot(pergunta):

    resposta = client.chat.completions.create(
        model="gpt-4.1-mini",

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },

            {
                "role": "user",
                "content": pergunta
            }
        ]
    )

    return resposta.choices[0].message.content


# loop
print("=== ChargeWise AI ===")
print("Digite 'sair' para encerrar.\n")

while True:

    pergunta = input("Você: ")

    if pergunta.lower() == "sair":
        print("\nEncerrando chatbot...")
        break

    resposta = perguntar_chatbot(pergunta)

    print("\nChargeWise AI:")
    print(resposta)
    print()
