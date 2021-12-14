import soundfile as sf
import numpy as np
import requests
import math
import telebot
#y, sr = soundfile.read(audio_data)
#print (len(y), sr)
API_TOKEN = '5077768407:AAEX9ANgjSd30YmuFeprEv4ZcB8qHJGBEcg'
bot = telebot.TeleBot('5077768407:AAEX9ANgjSd30YmuFeprEv4ZcB8qHJGBEcg')
audio_data = 0
def audio_reworker(audio_data):
    y, sr = sf.read(audio_data)
    print(y[1])
    #for i in range(len(y)//100):
       #print(y[i])

    for i in range (len(y)):
        if abs(y[i][0]) > 0.5:
             y[i][0] = 0.5 #(y[i-10][0] + y[i+10][0]) / 2
        if abs(y[i][1]) > 0.5:
             y[i][1] = 0.5 #(y[i-10][1] + y[i+10][1]) / 2
    sf.write('new_file.wav', y, sr)
    print("done")
    return ('new_file.wav')
#audio_reworker("sound.ogg")

@bot.message_handler(content_types=['text','audio'])
def get_text_messages(message):
    print(message)
    #print(m)
    #bot.reply_to(message,"Бот временно не работает")
    if message.content_type == "text":
        if message.text == "/start":
            bot.reply_to(message, "send me audiofile \".ogg\" format")
    if message.content_type == "audio":
        bot.reply_to(message, "processing...")
        #file_info = bot.get_file(message.audio.file_id)
        #audio_data = bot.download_file(file_info.file_path)
        file_info = bot.get_file(message.audio.file_id)
        print(file_info)
        audio_request_path = f'https://api.telegram.org/file/bot{API_TOKEN}/{file_info.file_path}'
        audio_data = requests.get(audio_request_path)
        file = open(f'sound.ogg', 'wb')  # создаем файл для записи результатов
        file.write(audio_data.content)  # записываем результат
        file.close()  # закр
        data = audio_reworker('sound.ogg')
        audio = open(f'{data}', 'rb')
        ## sendAudio with duration, performer and title.
        bot.send_audio(message.from_user.id, audio, 1, 'neurobot', 'bass')
        #print(audio_data.content)
        #audio_reworker(audio_data)
        #y, sr = sf.read(audio_data)
        #print(len(y), sr)
    ##print(len(y),sr)



bot.polling()
# ipd.Audio(audio_data)

