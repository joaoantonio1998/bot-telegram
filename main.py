import telebot

CHAVE_API = "5874613123:AAErl5tAQxFH4iUPYFKrZWGaZgf1ZTnBe6U"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands= ["Pizza"])
def opcao1(mensagem):
    bot.send_message(mensagem.chat.id,"Saindo a pizza!")

@bot.message_handler(commands=["Hamburguer"])
def opcao1(mensagem):
    bot.send_message(mensagem.chat.id,"Saindo a braba!")

@bot.message_handler(commands=["Salada"])
def opcao1(mensagem):
    bot.send_message(mensagem.chat.id,"Nao tem salada!, clique aqui para /iniciar")

@bot.message_handler(commands= ["opcao1"])
def opcao1(mensagem):
    texto = """
    Qual seu pedido
    /Pizza
    /Hamburguer
    /Salada
    """
    bot.send_message(mensagem.chat.id,texto)

@bot.message_handler(commands= ["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id,"Para enviar uma reclamacao contate o joao")

@bot.message_handler(commands= ["opcao3"])
def opcao3(mensagem):
    bot.reply_to(mensagem, "Valeu! Ele mandou um abraco de volta!")

def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção (clique no item)
    /opcao1 Fazer um pedido
    /opcao2 Reclamar de um pedido
    /opcao3 Mandar um abraco
    Responder qualquer outra coisa nao ira funcionar, clique em uma das opcoes
    """
    bot.reply_to(mensagem, texto)


bot.polling()
