# Mini Bot de Perguntas sobre Futebol


print("🤖: Olá! Eu sou o FutBot, seu assistente de Futebol.")
print("Digite 'sair' para encerrar a conversa.\n")


while True:
    pergunta = input("Você: ").strip().lower()


    if pergunta == "sair":
        print("FutBot: Até mais! Bons estudos! 👋")
        break


    # Respostas pré-definidas
    elif "passe" in pergunta:
        print("🤖:É quando um jogador toca a bola para um companheiro de equipe.")


    elif "impedimento" in pergunta:
        print("🤖: É quando um jogador está à frente da linha da defesa adversária no momento em que recebe o passe, ganhando vantagem injusta.")


    elif "gol" in pergunta:
        print("🤖: É quando a bola cruza completamente a linha de gol, entre as traves e por baixo do travessão.")


    elif "escanteio" in pergunta:
        print("🤖: Quando a bola sai pela linha de fundo e foi tocada por último por um defensor, o adversário cobra o escanteio do canto do campo.")


    elif "falta" in pergunta:
        print("🤖:Quando um jogador comete uma infração, como chutar ou empurrar o adversário de forma ilegal.")


    else:
        print("🤖: Hmmm... não entendi. Pergunte sobre passes, impedimentos, gol, escanteio ou.")


