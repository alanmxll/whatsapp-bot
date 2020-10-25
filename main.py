from whatsapp_bot import WhatsappBot

contacts = ["Contact 1", "Contact 2"]
message = "Message"

if __name__ == "__main__":
    bot = WhatsappBot()
    bot.execute(contacts, message)
