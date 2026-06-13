import subprocess
import time
from IPython.display import clear_output

# Instala dependências necessárias para execução do Ollama no Colab
!apt-get install -y zstd -q

# Instala o Ollama
!curl -fsSL https://ollama.com/install.sh | sh

# Inicia o servidor Ollama em segundo plano
subprocess.Popen(
    ["ollama", "serve"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

# Aguarda alguns segundos para garantir que o servidor esteja disponível
time.sleep(10)

print("🟢 Servidor Ollama iniciado!")

# Instala a biblioteca Python utilizada para comunicação com o Ollama
!pip install -q ollama

# Realiza o download do modelo (necessário apenas na primeira execução)
!ollama pull llama3.2:1b

# Importa a biblioteca após a instalação
import ollama

print("✅ Modelo carregado com sucesso!")

# Define o comportamento especializado do ChargeWise AI
# e limita as respostas ao contexto GoodWe e mobilidade elétrica
SYSTEM_PROMPT = """
Você é o ChargeWise AI, assistente virtual especializado em carregadores veiculares GoodWe, mobilidade elétrica e infraestrutura de recarga.

MISSÃO:
Auxiliar usuários com informações relacionadas a carregamento de veículos elétricos, infraestrutura elétrica, energia solar, gestão energética e soluções GoodWe.

PERFIS DE USUÁRIO:

- Usuários leigos: responda de forma simples e didática.
- Proprietários de veículos elétricos: explique tempos de recarga, consumo e boas práticas.
- Moradores e síndicos: destaque viabilidade, compartilhamento de infraestrutura e gestão energética.
- Técnicos e eletricistas: forneça explicações mais detalhadas e precisas.

TEMAS QUE VOCÊ DEVE RESPONDER:

- Veículos elétricos.
- Carros elétricos.
- Baterias.
- Recarga de veículos.
- Carregadores GoodWe.
- Infraestrutura elétrica.
- Energia solar aplicada ao carregamento.
- Condomínios com carregadores.
- Eficiência energética.
- Balanceamento de carga.
- Consumo energético.

ESCALONAMENTO:

Para dúvidas relacionadas a defeitos físicos, garantia, falhas de hardware, manutenção corretiva ou riscos elétricos, recomende suporte técnico autorizado.

PRECISÃO:

- Não invente informações.
- Quando não souber, informe claramente.
- Diferencie fatos de estimativas.

FORA DO ESCOPO:

Se a pergunta for claramente sobre assuntos sem relação com mobilidade elétrica, energia ou carregadores veiculares, responda:

"Sou especializado em carregadores veiculares GoodWe, mobilidade elétrica e infraestrutura de recarga. Não possuo conhecimento especializado sobre esse assunto."

QUALIDADE DAS RESPOSTAS:

- Seja claro e objetivo.
- Forneça explicações completas quando necessário.
- Utilize exemplos práticos.
- Considere informações mencionadas anteriormente na conversa.
- Adapte o nível técnico ao perfil do usuário.
"""

# Exemplos utilizados para orientar o modelo sobre o padrão esperado
# das respostas (técnica de Few-Shot Prompting)
FEW_SHOT_EXAMPLES = """
Usuário:
Tenho um Tesla Model Y. Quanto tempo leva para carregar?

Assistente:
O tempo depende da capacidade da bateria e da potência do carregador utilizado. Em carregadores residenciais AC o carregamento normalmente ocorre ao longo de algumas horas.

---

Usuário:
Sou síndico. Vale a pena instalar carregadores compartilhados?

Assistente:
A instalação pode atender à crescente demanda por veículos elétricos e otimizar a infraestrutura do condomínio. Recomenda-se avaliar a capacidade elétrica disponível e a forma de cobrança individual.

---

Usuário:
Sou eletricista. O que devo verificar antes da instalação?

Assistente:
Verifique tensão disponível, capacidade do circuito, dispositivos de proteção, aterramento e possibilidade de balanceamento de carga.

---

Usuário:
Qual o melhor horário para recarregar meu veículo?

Assistente:
Horários de menor demanda energética, como o período noturno, costumam ser mais adequados para reduzir impactos na infraestrutura elétrica.
"""

# Base de conhecimento utilizada como contexto para respostas
# relacionadas ao cenário do condomínio e soluções GoodWe
contexto = """
INFORMAÇÕES DO SISTEMA

- Existem 2 carregadores disponíveis.
- Horário recomendado para recarga: 22h às 6h.
- Balanceamento inteligente de carga.
- Tempo médio de recarga: entre 2 e 6 horas.
- Monitoramento de consumo energético.

GOODWE

- Carregadores para aplicações residenciais.
- Soluções para condomínios.
- Integração com energia solar.
- Gestão inteligente de energia.
- Monitoramento remoto.

VEÍCULOS ELÉTRICOS

- O tempo de recarga depende da bateria e da potência do carregador.
- O carregamento noturno reduz impactos na demanda energética.
- Sistemas de balanceamento ajudam a evitar sobrecarga elétrica.
"""

# Histórico responsável por manter a memória da conversa.
# Todo o histórico é enviado ao modelo a cada interação.
historico = [
    {
        "role": "system",
        "content": f"""
{SYSTEM_PROMPT}

EXEMPLOS DE INTERAÇÃO:

{FEW_SHOT_EXAMPLES}

BASE DE CONHECIMENTO:

{contexto}
"""
    }
]

# Função para verificar se a pergunta é coerente
def fora_do_contexto(pergunta):

    palavras = [
      "carregador",
      "carregamento",
      "recarga",
      "recarregar",
      "veículo",
      "veiculo",
      "carro",
      "elétrico",
      "eletrico",
      "tesla",
      "byd",
      "volvo",
      "gwm",
      "bateria",
      "energia",
      "potência",
      "potencia",
      "goodwe",
      "solar",
      "fotovoltaico",
      "condomínio",
      "condominio",
      "eletroposto",
      "instalação",
      "instalacao",
      "infraestrutura",
      "wallbox"
  ]

    pergunta = pergunta.lower()

    return not any(p in pergunta for p in palavras)

# Função responsável por enviar perguntas ao modelo
# e atualizar o histórico da conversa
def perguntar_chatbot(pergunta):

    if fora_do_contexto(pergunta):
      return (
        "Sou especializado em carregadores veiculares GoodWe, "
        "mobilidade elétrica e infraestrutura de recarga. "
        "Não possuo conhecimento especializado sobre esse assunto."
      )

    global historico

    historico.append(
        {
            "role": "user",
            "content": pergunta
        }
    )

    try:

        resposta = ollama.chat(
            model="llama3.2:1b",
            messages=historico,
            options={
              "temperature": 0.1,
              "num_predict": 100
            }
        )

        texto = resposta["message"]["content"]

        historico.append(
            {
                "role": "assistant",
                "content": texto
            }
        )

        if len(historico) > 7:
            historico[:] = [historico[0]] + historico[-6:]

        return texto

    except Exception as erro:

        return f"""
Erro ao conectar com o Ollama.

Verifique se:
- o Ollama está instalado;
- o modelo foi baixado corretamente;
- o servidor Ollama está ativo.

Detalhes do erro:
{erro}
"""

# Limpa a saída do Colab antes de iniciar a interface
clear_output()

print("=" * 50)
print("⚡ CHARGEWISE AI")
print("=" * 50)

print("\nAssistente virtual especializado em")
print("carregamento veicular e soluções GoodWe.\n")

print("Posso ajudar com:")
print("• Carregadores GoodWe")
print("• Infraestrutura de recarga")
print("• Condomínios e eletropostos")
print("• Eficiência energética")
print("• Integração com energia solar\n")

print("Digite sua dúvida ou 'sair' para encerrar.\n")

# Mantém o chatbot em execução até que o usuário solicite encerramento
while True:

    pergunta = input("👤 Você: ")

    if pergunta.lower() == "sair":

        print("\n🔌 Encerrando ChargeWise AI...")
        break

    resposta = perguntar_chatbot(pergunta)

    print("\n🤖 ChargeWise AI:")
    print(resposta)

    print("\n" + "-" * 50 + "\n")
