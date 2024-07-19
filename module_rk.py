from pyrogram import Client, filters
import requests
import random

with open("userbot.info", "r") as file:
    lines = file.readlines()
    prefix_userbot = lines[2].strip()

cinfo = f"🐱`{prefix_userbot}rk`/`{prefix_userbot}randkomaru`"
ccomand = " кидает рандомную гифку с кошкей Комару."


def command_example(app):
    @app.on_message(filters.command(["randkomaru", "rk"], prefixes=prefix_userbot))
    async def send_random_komaru_gif(_, message):
        url = 'https://raw.githubusercontent.com/Blaing-7542/BD_Telery/main/komarugifbd'
        response = requests.get(url)
        if response.status_code == 200:
            gifs = response.text.split('\n')
            random_gif = random.choice(gifs)
            await message.reply_animation(random_gif)
        else:
            await message.reply('**😢Не удалось получить гифку. Попробуйте позже.**')
            last_command_time[user_id] = current_time


print("Модуль rk загружен!")
