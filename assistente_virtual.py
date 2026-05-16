#=====================================================================
# CHATBOT COM MEMÓRIA (O Chat Contínuo) - Passo a Passo
#=====================================================================

from openai import OpenAI

# ====================================================================
# PASSO 1: AUTENTICAÇÃO E CONEXÃO
# ====================================================================
meu_token = input("Insira o seu token para conversar: ")

cliente = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=meu_token,
)

# ====================================================================
# PASSO 2: A BASE DA MEMÓRIA
# ====================================================================
# A lista começa apenas com a instrução do sistema.
# Durante a conversa, ela vai crescer e guardar tudo o que for dito!
historico_conversa = [
    {"role": "system", "content": "Você é um assistente prestativo. Responda de forma clara e curta."}
]

print("\n🤖 Chatbot iniciado! (Digite 'sair' para encerrar)")
print("-" * 50)

# ====================================================================
# PASSO 3: O LAÇO INFINITO (O motor da conversa)
# ====================================================================
# O 'while True' faz o programa rodar em círculo, permitindo uma
# conversa contínua. Ele só para se ativarmos o comando 'break'.
while True:
    
    # O programa pausa e espera a pergunta do usuário
    pergunta_usuario = input("Você: ")
    
    # A Válvula de Escape: 
    # O '.lower()' garante que funciona mesmo se o aluno digitar 'SAIR' maiúsculo.
    if pergunta_usuario.lower() == 'sair':
        print("Encerrando o chat. Até logo!")
        break 
        
    # ====================================================================
    # PASSO 4: GUARDANDO A PERGUNTA NA MEMÓRIA
    # ====================================================================
    # Adicionamos a pergunta atual no final da nossa lista de histórico.
    historico_conversa.append({"role": "user", "content": pergunta_usuario})
    
    # ====================================================================
    # PASSO 5: O DISPARO PARA A NUVEM
    # ====================================================================
    # Enviamos o histórico INTEIRO (tudo o que foi dito até agora).
    # É assim que a IA "lembra" do contexto do passado.
    response = cliente.chat.completions.create(
        model="gpt-4o-mini",
        messages=historico_conversa
    )
    
    # ====================================================================
    # PASSO 6: RECEBENDO A RESPOSTA
    # ====================================================================
    # Mergulhamos no pacote devolvido pela API e pegamos apenas o texto.
    resposta_ia = response.choices[0].message.content
    print(f"IA: {resposta_ia}\n")
    
    # ====================================================================
    # PASSO 7: O PULO DO GATO (MEMÓRIA DUPLA)
    # ====================================================================
    # Para a memória funcionar perfeitamente, a própria resposta da IA 
    # tem que ser guardada na lista, mas com o papel (role) de "assistant".
    historico_conversa.append({"role": "assistant", "content": resposta_ia})
    
    # Um pequeno charme visual para indicar o fim do turno.
    print("🙌")