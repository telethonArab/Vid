# Copyright (C) 2021 Veez Project

import re
import uuid
import socket
import psutil
import platform
from config import BOT_USERNAME
from driver.filters import command
from pyrogram import Client, filters
from driver.decorators import sudo_users_only, humanbytes


@Client.on_message(command(["الاوامر", "اوامر"]) & ~filters.edited)
@sudo_users_only
async def give_sysinfo(client, message):
    somsg = """**اوامر المكالمات :**
1 - (.تشغيل + الرد على الصوتية او كتابة اسم الصوت بجانب الأمر) 
2 - (.تشغيل فيديو + الرد على الفيديو او كتابه اسم الفيديو )
3 - ( .ايقاف ) : لأيقاف الصوت او الفيديو في المكالمة
4 - ( .استئناف ) : لأيقاف الفديو او الصوت مؤقتا في المكالمة
5 - ( .اعاده تشغيل ) : لتشغيل الصوت او الفيديو بعد استئنافة
6 - ( .تحميل فيديو + رابط من اليوتيوب او اسم الفيديو )
7 - ( .تحميل + اسم الصوت او رابط من اليوتيوب )"""
    await message.reply(somsg)
