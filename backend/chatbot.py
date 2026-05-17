from openai import OpenAI

client = OpenAI(api_key="SUA_API_KEY_AQUI")

SYSTEM_PROMPT = """
Você é o ChargeWise AI, um assistente inteligente especializado na gestão de carregadores veiculares elétricos em condomínios.

Seu objetivo é auxiliar síndicos, administradores e moradores com informações relacionadas a:
- disponibilidade de carregadores;
- sessões de recarga;
- consumo energético;
- regras de utilização;
- balanceamento de potência.

Responda de forma clara, objetiva e profissional.
"""


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


if __name__ == "__main__":
    while True:
        pergunta = input("Você: ")

        if pergunta.lower() == "sair":
            break

        resposta = perguntar_chatbot(pergunta)
        print("\nChargeWise AI:")
        print(resposta)
        print()
