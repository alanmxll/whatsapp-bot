from whatsapp_bot import WhatsappBot

contacts = ["Arwen", "Jey"]
message = "Hey! I love you. <3"

if __name__ == "__main__":
    bot = WhatsappBot()
    bot.execute(contacts, message)
