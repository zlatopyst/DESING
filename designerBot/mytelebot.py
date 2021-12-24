import telebot
import pyfiglet
import time
from rich.console import Console
from telebot import types
import botconfig

category_list = {
'1':'автомобили',
'2':'минимализм',
'3':'аниме',
'4':'видеоигры',
'5':'сериалы'}

def getCategory():
	categ_str = "Доступные категории:\n"
	for i in range(len(category_list)):
		categ_str += str(i+1) + ":" + str(category_list[str(i+1)]) + "\n"
	return categ_str


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


#обработчики шагов
def sendWallpaper(message):
		bot.send_message(message.from_user.id, str(message.from_user.id) + ":" + str(message.text))
		print(str(message.from_user.id) + ":" + str(message.text))


def wallHandler(message):
	orientAllias = ['горизонтальная','вертикальная']
	query = message.text.split(" ")

	try:
		if (len(query) != 3 or orientAllias.count(query[1]) == 0 or int(query[0]) > 5 or int(query[2]) > 10):
			bot.send_message(message.from_user.id, "Неверный формат")
		else:
			bot.send_message(message.from_user.id,"Категория:" + str(category_list[str(query[0])]) + "\nОриентация:" + query[1] + "\nКоличество:" + query[2])
	except Exception:
		bot.send_message(message.from_user.id, "Неверный формат")

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
			bot.send_message(message.from_user.id, "Введите номер категории, ориентацию и количество")
			bot.send_message(message.from_user.id, "Пример: 3 горизонтальная 5")
			bot.send_message(message.from_user.id, getCategory())
			bot.register_next_step_handler(message,wallHandler)				

		elif message.text == "Рингтоны":
			bot.send_message(message.from_user.id, "Функция в разработке")
		elif message.text == "Шрифты":
			bot.send_message(message.from_user.id, "Функция в разработке")
		elif message.text == "IDDQD":
			bot.send_message(message.from_user.id, "мальцев душнила")
		else:
			bot.send_message(message.from_user.id, "Список команд:\nОбои\nРингтоны\nШрифты")
	except Exception:
		print ("Ты всё сломал нахер,придурок")	
	
bot.infinity_polling()
