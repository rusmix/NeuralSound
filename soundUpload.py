import soundfile as sf
import numpy as np
import requests
import telebot
#y, sr = soundfile.read(audio_data)
#print (len(y), sr)
API_TOKEN = '5077768407:AAHhN-_LieyC6MapsKMYRJv2MVRoZaFWsQU'
bot = telebot.TeleBot('5077768407:AAHhN-_LieyC6MapsKMYRJv2MVRoZaFWsQU')
audio_data = 0
bot.infinity_polling()
@bot.message_handler(content_types=['audio', 'text'])
def get_text_messages(message):
    print(message.audio)
    if message.content_type == "text":
        print("try to send .ogg file instead")
    if message.content_type == "audio":
        file_info = bot.get_file(message.audio.file_id)
        audio_data = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(API_TOKEN, file_info.file_path))
        #y, sr = sf.read(audio_data)
        #print (len(y), sr)
        print (audio_data)
    #print(message)

#     if message('text')
#     audio_data = 'bensound-creativeminds.ogg'
#     y, sr = soundfile.load(audio_data)
#     print(len(y), sr)


# ipd.Audio(audio_data)
