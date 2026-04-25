# =====================================================================
# CHATBOT - PERGUNTA ÚNICA (Com explicações passo a passo)
# =====================================================================

# Importa a biblioteca oficial da OpenAI.
# É ela que traz as ferramentas prontas para o Python "conversar" com a Inteligência Artificial.
from openai import OpenAI

# ====================================================================
# PASSO 1: A CHAVE DE ACESSO (O seu "Crachá" de identificação)
# ====================================================================
# Para usar a Inteligência Artificial, o servidor precisa saber quem está pedindo.
# O token (ou API Key) funciona como uma senha exclusiva.
meu_token = input("Insira o seu token para conversar: ")

# Aqui nós configuramos o nosso "rádio de comunicação".
# Passamos o endereço de onde a IA está hospedada (base_url) e a nossa senha (api_key).
cliente = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=meu_token,
)

# ====================================================================
# PASSO 2: DEFININDO A PERSONALIDADE DA IA
# ====================================================================
# A IA precisa de uma lista organizada para ler as mensagens.
# A primeira mensagem dessa lista sempre recebe o papel (role) de "system" (sistema).
# É como dar um roteiro para um ator: aqui dizemos como ela deve se comportar.
historico_conversa = [
    {
        "role": "system",
        "content": "Você é um assistente prestativo. Responda de forma clara e curta.",
    }
]

print("\n🤖 Chatbot iniciado! (Modo Pergunta Única)")
print("-" * 50)

# O programa pausa aqui e espera você digitar a sua pergunta no terminal.
pergunta_usuario = input("Você: ")

# ====================================================================
# PASSO 3: EMPACOTANDO A SUA PERGUNTA
# ====================================================================
# Não podemos enviar o texto solto. Precisamos empacotar a sua pergunta
# avisando que o papel (role) de quem está falando agora é o "user" (usuário).
# O '.append()' adiciona esse pacote no final da nossa lista 'historico_conversa'.
historico_conversa.append({"role": "user", "content": pergunta_usuario})

# ====================================================================
# PASSO 4: O ENVIO PELA INTERNET (O processamento)
# ====================================================================
# Agora enviamos a lista completa para o cérebro da IA (neste caso, o modelo gpt-4o-mini).
# O programa vai aguardar alguns segundos enquanto a informação viaja
# até os servidores, é processada e a resposta é enviada de volta.
response = cliente.chat.completions.create(
    model="gpt-4o-mini", messages=historico_conversa
)

# ====================================================================
# PASSO 5: DESEMPACOTANDO E LENDO A RESPOSTA
# ====================================================================
# A IA não nos devolve apenas o texto, ela devolve um pacote gigante com vários
# dados técnicos (hora, tokens usados, etc).
# O caminho 'choices[0].message.content' serve para "mergulhar" nesse pacote
# e extrair unicamente o texto da resposta que nos interessa.
resposta_ia = response.choices[0].message.content

# Finalmente, imprimimos a resposta limpa na tela!
print(f"😁\nIA: {resposta_ia}\n")

# Aviso de que o programa terminou a sua tarefa única.
print("😘 Fim da execução.")
