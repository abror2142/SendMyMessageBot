from telebot import TeleBot
from telebot.types import Message

bot = TeleBot('7013751805:AAHbjrqM5w49evXFTIF_ko7dStkLVFdr_TM')


@bot.message_handler(['start'])
def handle_start(message: Message):
    full_name = message.from_user.full_name
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Assalomu Alaykum, {full_name}")


@bot.message_handler(['help'])
def handle_help(message: Message):
    chat_id = message.chat.id
    s = (f"SendMyMessageBot ga xush kelibsiz!\n\n\tBuyruqlar ro'yxati:\n"
         f"/start --- Botni ishga tushirish.\n/help --- Buyruqlar ro'yxati.\n"
         f"/info --- Foydalanuvchi ma'lumotlari.")
    bot.send_message(chat_id, s)


@bot.message_handler(['info'])
def handle_info(message: Message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    id = message.from_user.id
    username = message.from_user.username
    is_premium = "Siz premium mijozsiz!" if message.from_user.is_premium else "Siz premium mijoz emassiz."
    s = (f"Sizning ma'lumotlaringiz:\nIsm:{first_name}\nFamilya: {last_name}\n"
         f"Telegram ID: {id}\nUsername: {username}\n{is_premium}")
    bot.send_message(chat_id, s)


@bot.message_handler(content_types=['text', 'photo', 'video', 'animation'])
def handle_send_msg(message: Message):
    chat_id = message.chat.id
    group_id = -1001908192654 #grux idisi mavjud bo'lishi va bot admin bo'lishi kerak
    bot.copy_message(group_id, chat_id, message.message_id)


bot.polling()
