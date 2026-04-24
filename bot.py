import os
import logging
import random
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)
TOKEN = os.environ.get("BOT_TOKEN", "7972245570:AAHvYgyXArhi0dQ__Zoi6NCkVbYQeX189-c")
reminders = []

async def start(update, context):
    name = update.effective_user.first_name or "do'stim"
    await update.message.reply_text(f"Salom {name}! 👋\nMen Abdusattor — Mirodilning yordamchisiman.\n\n/hazil — hazil\n/eslatma [matn] — eslatma\n/eslatmalar — ro'yxat\n/yordam — yordam")

async def yordam(update, context):
    await update.message.reply_text("/hazil — hazil aytaman\n/eslatma [matn] — eslatma qo'sh\n/eslatmalar — barcha eslatmalar\n/tozala — tozalash")

async def hazil(update, context):
    hazillar = ["Matematika o'qituvchisi: '2+2?' Mirodil: 'Doim 4' 😄","Telefon zaryadi 1% — hamma narsani saqlash rejimi 😂","Institut: 'Nima o'qiysiz?' Mirodil: 'Pul ishlashni' Institut: 'Bu fan emas' 😅","Do'stim: 'Sen hech o'zgarmaysan' Men: 'Rahmat' Do'stim: 'Maqtov emas edi' 😂"]
    await update.message.reply_text(random.choice(hazillar))

async def eslatma(update, context):
    if not context.args:
        await update.message.reply_text("❗ Misol: /eslatma Dars soat 14:00")
        return
    matn = " ".join(context.args)
    reminders.append({"matn": matn, "vaqt": datetime.now().strftime("%d.%m.%Y %H:%M")})
    await update.message.reply_text(f"✅ Eslatma saqlandi:\n📝 {matn}")

async def eslatmalar(update, context):
    if not reminders:
        await update.message.reply_text("📋 Eslatma yo'q.")
        return
    text = "📋 Eslatmalar:\n\n"
    for i, r in enumerate(reminders, 1):
        text += f"{i}. {r['matn']} — {r['vaqt']}\n"
    await update.message.reply_text(text)

async def tozala(update, context):
    reminders.clear()
    await update.message.reply_text("🗑️ Tozalandi!")

async def xabar(update, context):
    await update.message.reply_text("Tushundim! /yordam — buyruqlar ro'yxati 😄")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("yordam", yordam))
    app.add_handler(CommandHandler("hazil", hazil))
    app.add_handler(CommandHandler("eslatma", eslatma))
    app.add_handler(CommandHandler("eslatmalar", eslatmalar))
    app.add_handler(CommandHandler("tozala", tozala))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, xabar))
    app.run_polling()

if __name__ == "__main__":
    main()
