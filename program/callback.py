# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)





@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer(" تحتاج صلاحية مشرف.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 تحتاج صلاحية مشرف !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              "الاعدادات",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("انهاء", callback_data="cbstop"),
                      InlineKeyboardButton("استئناف", callback_data="cbpause"),
                      InlineKeyboardButton("ابدء", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("كتم", callback_data="cbmute"),
                      InlineKeyboardButton("الغاء كتم", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("اغلاق 🗑 ", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ لايوجد شيئ", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 تحتاج صلاحية مشرف !", show_alert=True)
    await query.message.delete()
