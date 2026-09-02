import os
import telebot

TOKEN = "8428439895:AAH11iI7_G4K4J4jlvWH-Jx4-RtvSBmK_VI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
 def send_welcome(message):
    bot.reply_to(message, "أهلاً بك يا ياسين، Railway")
 

@bot.message_handler(func=lambda message: True)
def echo_all(message):
  bot.reply_to(message, f"أهلاً بك! لقد استقبلت رسالتك: {message.text}")


bot.infinity_polling()
