import telebot
from telebot import types

# Telegram botunuzun API anahtarını buraya yazın
TOKEN = '6750148691:AAHrWphE5rf10Kxjtw9sqS70upUPu0njAF0'

# Bot nesnesini oluşturun
bot = telebot.TeleBot(TOKEN)

# /start komutuna cevap veren fonksiyon
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Başlangıç mesajını gönder
    bot.reply_to(message, "Hello KAMİRAN.SNDİ")

# /me komutuna cevap veren fonksiyon
@bot.message_handler(commands=['me'])
def send_links(message):
    # Butonları oluştur
    markup = types.InlineKeyboardMarkup(row_width=1)
    instagram_btn = types.InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/k4miran.sndi?igsh=bmZ4eTBtZ2dxcHJo")
    tiktok_btn = types.InlineKeyboardButton(text="TikTok", url="https://www.tiktok.com/@kamiran..sndi?_t=8lAa5PKxQs1&_r=1")
    telegram_btn = types.InlineKeyboardButton(text="Telegram", url="https://t.me/k4miran_sndi")
    snapchat_btn = types.InlineKeyboardButton(text="Snapchat", url="https://www.snapchat.com/add/k4miran.sndi?share_id=mCMe8-mm0h8&locale=tr-IQ")

    # Butonları markup'a ekle
    markup.add(instagram_btn, tiktok_btn, telegram_btn, snapchat_btn)

    # Mesajı gönder
    bot.send_message(message.chat.id, "kamiran sndi scl account:", reply_markup=markup)

# Sonsuz döngü
bot.infinity_polling()
