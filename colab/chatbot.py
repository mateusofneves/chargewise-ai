!pip install openai

from IPython.display import clear_output

# system prompt
SYSTEM_PROMPT = """
Você é o ChargeWise AI, um assistente inteligente especializado
na gestão de carregadores veiculares elétricos em condomínios.
"""

# base das respostas (treino)
respostas = {

    "carregadores": """
Atualmente existem 2 carregadores disponíveis no condomínio.
""",

    "melhor horário": """
O melhor horário para recarga é entre 22h e 6h,
quando a demanda energética é menor.
""",

    "sobrecarga": """
Sim. O sistema realiza balanceamento inteligente
de potência para evitar sobrecarga elétrica.
""",

    "tempo": """
O tempo médio de recarga varia entre 2 e 6 horas,
dependendo da bateria do veículo.
""",

    "qualquer carregador": """
O uso depende das regras internas do condomínio
e da disponibilidade atual.
""",

    "app": """
Verifique se o carregador está conectado corretamente
à rede do condomínio e tente atualizar o aplicativo.
""",

    "consumo": """
O sistema monitora o consumo energético para evitar
sobrecarga e melhorar a eficiência da recarga.
"""
}

# funcao do chat bot
def perguntar_chatbot(pergunta):

    pergunta_lower = pergunta.lower()

    for chave in respostas:

        if chave in pergunta_lower:

            return respostas[chave]

    return """
Desculpe, não encontrei essa informação no sistema.
"""

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
