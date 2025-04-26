import telebot
import os, random
from review import information 

def sovet():
    save = ['Не выбрасывайте мусор на землю', 'Исползуюте менше машину']
    return random.choice(save)


bot = telebot.TeleBot("")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот который поможет вам помогать природу. Вот мои команды:  1 - /information  2 - /tips  3 - /photo")
    
@bot.message_handler(commands=['information'])
def send_hello(message):
    bot.reply_to(message, "Вот информация:" + information()) 
    
@bot.message_handler(commands=['tips'])
def send_bye(message):
    bot.reply_to(message, "Вот совет:" + sovet()) 



@bot.message_handler(commands=['photo'])
def send_photo(message):
    file = random.choice(os.listdir('images'))
    with open(f'images\\{file}', 'rb') as f:
        bot.send_photo(message.chat.id, f)



    


print('start')   
bot.polling()
