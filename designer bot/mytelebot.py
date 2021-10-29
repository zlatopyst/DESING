import telebot
from telebot import types
import botconfig

bot = telebot.TeleBot(botconfig.TOKKEN)
print(botconfig.TOKKEN)
print("Пока всё работает\nПока...")

#обработчик тестовых приколов
@bot.message_handler(commands=['devtest'])
def dev_test(message):
	try:
		bot.send_message(message.from_user.id, "1:next step handler\n2menu features\n3register")
		loop_switch = 0
		while loop_switch == 0:
			if message.text == "1" or message.text == "2" or message.text == "3":
				loop_switch = 1
				bot.register_next_step_handler(message,devtest_first)
			else:
				bot.send_message(message.from_user.id, "Неправильная комманда")
	except Exception:
		print ("Ты всё сломал нахер,придурок")

def devtest_first(message):
	try:	
		if message.text == "1":
			bot.send_message(message.from_user.id, "напиши что-нибудь")
			bot.register_next_step_handler(message,devtest_second)
		if message.text == "2":
			bot.send_message(message.from_user.id, "пока нихера не сделал")
		if message.text == "3":
			bot.send_message(message.from_user.id, "пока нихера не сделал")
	except Exception:
		print ("Ты всё сломал нахер,придурок")

def devtest_second(message):
	try:
		bot.send_message(message.from_user.id, "Ты написал " + message.text)
	except Exception:
		print ("Ты всё сломал нахер,придурок")

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