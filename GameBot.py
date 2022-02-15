import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.key)

class Characteristic:
    money = 0
    streght = 1
class Cost:
    helmet = 5
    armor = 5
    pants = 5
    boots = 5
    sword = 5
    streght = 5
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Играть")
    item2 = types.KeyboardButton("Авторы")
    
    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Данил Бебровски", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def game(message):
    if message.text == "Играть":
        markup = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton(text = "Работать", callback_data = "work")
        item2 = types.InlineKeyboardButton(text = "Улучшение снаряжения", callback_data = "upgrade s")
        item3 = types.InlineKeyboardButton(text = "Улучшение Данилы", callback_data = "upgrade d")

        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id,f"{Characteristic.money} Бебракоин", reply_markup=markup)
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == "work":
            Characteristic.money += Characteristic.streght
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton(text = "Работать", callback_data = "work")
            item2 = types.InlineKeyboardButton(text = "Улучшение снаряжения", callback_data = "upgrade s")
            item3 = types.InlineKeyboardButton(text = "Улучшение Данилы", callback_data = "upgrade d")

            markup.add(item1, item2, item3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text = f"{Characteristic.money} Бебракоин", reply_markup=markup)
        elif call.data == "upgrade s":
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton(text = "Работать", callback_data = "work")
            item2 = types.InlineKeyboardButton(text = "Улучшение снаряжения", callback_data = "upgrade s")
            item3 = types.InlineKeyboardButton(text = "Улучшение Данилы", callback_data = "upgrade d")
            helmet = types.InlineKeyboardButton(text = f"Улучшить шлем {Cost.helmet} Бебракоинов ", callback_data = "upgrade helmet")
            item5 = types.InlineKeyboardButton(text = f"Улучшить нагрудник {Cost.armor} Бебракоинов", callback_data = "upgrade armor")
            item6 = types.InlineKeyboardButton(text = f"Улучшить поножи {Cost.pants} Бебракоинов", callback_data = "upgrade pants")
            item7 = types.InlineKeyboardButton(text = f"Улучшить ботинки {Cost.boots} Бебракоинов", callback_data = "upgrade boots")
            item8 = types.InlineKeyboardButton(text = f"Улучшить меч {Cost.sword} Бебракоинов", callback_data = "upgrade sword")

            markup.add(item1, item2, item3, helmet, item5, item6, item7, item8)  
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text = f"Осталось {Characteristic.money} Бебракоинов", reply_markup=markup)  
        elif call.data == "upgrade d":
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton(text = "Работать", callback_data = "work")
            item2 = types.InlineKeyboardButton(text = "Улучшение снаряжения", callback_data = "upgrade s")
            item3 = types.InlineKeyboardButton(text = "Улучшение Данилы", callback_data = "upgrade d")
            item4 = types.InlineKeyboardButton(text = f"Улучшить силу {Cost.streght} Бебракоинов", callback_data = "upgrade streght")

            markup.add(item1, item2, item3,item4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text = f"Осталось {Characteristic.money} Бебракоинов", reply_markup=markup)
        elif call.data == "upgrade streght":
            if Characteristic.money >= Cost.streght:
                Characteristic.money -= Cost.streght
                Characteristic.streght += 1
                Cost.streght += 5
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton(text = "Работать", callback_data = "work")
            item2 = types.InlineKeyboardButton(text = "Улучшение снаряжения", callback_data = "upgrade s")
            item3 = types.InlineKeyboardButton(text = "Улучшение Данилы", callback_data = "upgrade d")
            item4 = types.InlineKeyboardButton(text = f"Улучшить силу {Cost.streght} Бебракоинов", callback_data = "upgrade streght")

            markup.add(item1, item2, item3,item4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text = f"Осталось {Characteristic.money} Бебракоинов", reply_markup=markup)
        elif call.data == "upgrade helmet":
            if Characteristic.money >= Cost.helmet:
                Characteristic.money -= Cost.helmet
                Characteristic.streght += 1
                Cost.helmet += 5
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton(text = "Работать", callback_data = "work")
            item2 = types.InlineKeyboardButton(text = "Улучшение снаряжения", callback_data = "upgrade s")
            item3 = types.InlineKeyboardButton(text = "Улучшение Данилы", callback_data = "upgrade d")
            helmet = types.InlineKeyboardButton(text = f"Улучшить шлем {Cost.helmet} Бебракоинов ", callback_data = "upgrade helmet")
            item5 = types.InlineKeyboardButton(text = f"Улучшить нагрудник {Cost.armor} Бебракоинов", callback_data = "upgrade armor")
            item6 = types.InlineKeyboardButton(text = f"Улучшить поножи {Cost.pants} Бебракоинов", callback_data = "upgrade pants")
            item7 = types.InlineKeyboardButton(text = f"Улучшить ботинки {Cost.boots} Бебракоинов", callback_data = "upgrade boots")
            item8 = types.InlineKeyboardButton(text = f"Улучшить меч {Cost.sword} Бебракоинов", callback_data = "upgrade sword")

            markup.add(item1, item2, item3, helmet, item5, item6, item7, item8)  
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text = f"Осталось {Characteristic.money} Бебракоинов", reply_markup=markup)
        elif call.data == "upgrade armor":
            if Characteristic.money >= Cost.armor:
                Characteristic.money -= Cost.armor
                Characteristic.streght += 1
                Cost.armor += 5
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton(text = "Работать", callback_data = "work")
            item2 = types.InlineKeyboardButton(text = "Улучшение снаряжения", callback_data = "upgrade s")
            item3 = types.InlineKeyboardButton(text = "Улучшение Данилы", callback_data = "upgrade d")
            helmet = types.InlineKeyboardButton(text = f"Улучшить шлем {Cost.helmet} Бебракоинов ", callback_data = "upgrade helmet")
            item5 = types.InlineKeyboardButton(text = f"Улучшить нагрудник {Cost.armor} Бебракоинов", callback_data = "upgrade armor")
            item6 = types.InlineKeyboardButton(text = f"Улучшить поножи {Cost.pants} Бебракоинов", callback_data = "upgrade pants")
            item7 = types.InlineKeyboardButton(text = f"Улучшить ботинки {Cost.boots} Бебракоинов", callback_data = "upgrade boots")
            item8 = types.InlineKeyboardButton(text = f"Улучшить меч {Cost.sword} Бебракоинов", callback_data = "upgrade sword")

            markup.add(item1, item2, item3, helmet, item5, item6, item7, item8)  
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text = f"Осталось {Characteristic.money} Бебракоинов", reply_markup=markup)
        elif call.data == "upgrade pants":
            if Characteristic.money >= Cost.pants:
                Characteristic.money -= Cost.pants
                Characteristic.streght += 1
                Cost.pants += 5
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton(text = "Работать", callback_data = "work")
            item2 = types.InlineKeyboardButton(text = "Улучшение снаряжения", callback_data = "upgrade s")
            item3 = types.InlineKeyboardButton(text = "Улучшение Данилы", callback_data = "upgrade d")
            helmet = types.InlineKeyboardButton(text = f"Улучшить шлем {Cost.helmet} Бебракоинов ", callback_data = "upgrade helmet")
            item5 = types.InlineKeyboardButton(text = f"Улучшить нагрудник {Cost.armor} Бебракоинов", callback_data = "upgrade armor")
            item6 = types.InlineKeyboardButton(text = f"Улучшить поножи {Cost.pants} Бебракоинов", callback_data = "upgrade pants")
            item7 = types.InlineKeyboardButton(text = f"Улучшить ботинки {Cost.boots} Бебракоинов", callback_data = "upgrade boots")
            item8 = types.InlineKeyboardButton(text = f"Улучшить меч {Cost.sword} Бебракоинов", callback_data = "upgrade sword")

            markup.add(item1, item2, item3, helmet, item5, item6, item7, item8)  
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text = f"Осталось {Characteristic.money} Бебракоинов", reply_markup=markup)
        elif call.data == "upgrade boots":
            if Characteristic.money >= Cost.boots:
                Characteristic.money -= Cost.boots
                Characteristic.streght += 1
                Cost.boots += 5
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton(text = "Работать", callback_data = "work")
            item2 = types.InlineKeyboardButton(text = "Улучшение снаряжения", callback_data = "upgrade s")
            item3 = types.InlineKeyboardButton(text = "Улучшение Данилы", callback_data = "upgrade d")
            helmet = types.InlineKeyboardButton(text = f"Улучшить шлем {Cost.helmet} Бебракоинов ", callback_data = "upgrade helmet")
            item5 = types.InlineKeyboardButton(text = f"Улучшить нагрудник {Cost.armor} Бебракоинов", callback_data = "upgrade armor")
            item6 = types.InlineKeyboardButton(text = f"Улучшить поножи {Cost.pants} Бебракоинов", callback_data = "upgrade pants")
            item7 = types.InlineKeyboardButton(text = f"Улучшить ботинки {Cost.boots} Бебракоинов", callback_data = "upgrade boots")
            item8 = types.InlineKeyboardButton(text = f"Улучшить меч {Cost.sword} Бебракоинов", callback_data = "upgrade sword")
        
            markup.add(item1, item2, item3, helmet, item5, item6, item7, item8)  
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text = f"Осталось {Characteristic.money} Бебракоинов", reply_markup=markup)
        elif call.data == "upgrade sword":
            if Characteristic.money >= Cost.sword:
                Characteristic.money -= Cost.sword
                Characteristic.streght += 1
                Cost.sword += 5
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton(text = "Работать", callback_data = "work")
            item2 = types.InlineKeyboardButton(text = "Улучшение снаряжения", callback_data = "upgrade s")
            item3 = types.InlineKeyboardButton(text = "Улучшение Данилы", callback_data = "upgrade d")
            helmet = types.InlineKeyboardButton(text = f"Улучшить шлем {Cost.helmet} Бебракоинов ", callback_data = "upgrade helmet")
            item5 = types.InlineKeyboardButton(text = f"Улучшить нагрудник {Cost.armor} Бебракоинов", callback_data = "upgrade armor")
            item6 = types.InlineKeyboardButton(text = f"Улучшить поножи {Cost.pants} Бебракоинов", callback_data = "upgrade pants")
            item7 = types.InlineKeyboardButton(text = f"Улучшить ботинки {Cost.boots} Бебракоинов", callback_data = "upgrade boots")
            item8 = types.InlineKeyboardButton(text = f"Улучшить меч {Cost.sword} Бебракоинов", callback_data = "upgrade sword")

            markup.add(item1, item2, item3, helmet, item5, item6, item7, item8)  
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text = f"Осталось {Characteristic.money} Бебракоинов", reply_markup=markup)
bot.polling(none_stop=True)
