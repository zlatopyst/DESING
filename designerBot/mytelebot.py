import telebot
import pyfiglet
import time
from rich.console import Console
from telebot import types
import botconfig

con=Console()
banner = pyfiglet.figlet_format("designer bot ",font="banner3-D")
bot = telebot.TeleBot(botconfig.TOKKEN)
con.print(banner)
print("bot tokken:" + botconfig.TOKKEN)

print("Пока всё работает\nПока...")

#обработчик тестовых приколов
@bot.message_handler(commands=['devtest'])
def dev_test(message):
	try:
		bot.send_message(message.from_user.id, "Введите ориентаию дисплея, номер категорию и количество обоев.\nПример: Горизонтальная Аниме 5")
		bot.send_message(message.from_user.id, "Категории:\n1:Аниме\n2:Автомобили\n3:Ещё какая нибудь хуйня")
		bot.register_next_step_handler(message,sendWallpaper)
	except Exception:
		print ("Ты всё сломал нахер,придурок")

def sendWallpaper(message):
		bot.send_message(message.from_user.id, str(message.from_user.id) + ":" + str(message.text))
		print(str(message.from_user.id) + ":" + str(message.text))

#кнопка старт
@bot.message_handler(commands=['start'])
def send_welcome(message):
	try:
		#кнопки
		markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
		wallpaperButton=types.KeyboardButton("Обои")
		ringtoneButton=types.KeyboardButton("Рингтоны")
		fontButton=types.KeyboardButton("Шрифты")
		markup.add(wallpaperButton)
		markup.add(ringtoneButton)
		markup.add(fontButton)

		bot.send_message(message.from_user.id, "Приветствую, с помощью этого бота ты сможешь персонализировать своё устройство")
		bot.send_message(message.from_user.id, "Список команд:\nОбои\nРингтоны\nШрифты", reply_markup=markup)
		
	except Exception:
		print ("Ты всё сломал нахер,придурок")

#обработчики комманд
@bot.message_handler(commands=['help'])
def send_help(message):
	try:
		bot.send_message(message.from_user.id, "Список команд:\nОбои\nРингтоны\nШрифты")
	except Exception:
		print ("Ты всё сломал нахер,придурок")


#обратотчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def send_textmessage(message):
	try:
		if message.text == "Обои":
			bot.send_message(message.from_user.id, "Вот твои обои:")
			#bot.send_photo(message.from_user.id, "https://i.redd.it/2z39d50ag7w71.jpg")
			bot.send_photo(message.from_user.id, open('profilepicture.jpg', 'rb')) 
		elif message.text == "Рингтоны":
			bot.send_message(message.from_user.id, "Вот твой рингтон:")
		elif message.text == "Шрифты":
			bot.send_message(message.from_user.id, "Вот твой шрифт:")
		elif message.text == "IDDQD":
			bot.send_message(message.from_user.id, "мальцев душнила")
		else:
			bot.send_message(message.from_user.id, "Список команд:\nОбои\nРингтоны\nШрифты")
	except Exception:
		print ("Ты всё сломал нахер,придурок")	
	
bot.infinity_polling()
