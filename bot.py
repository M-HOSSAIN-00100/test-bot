# bot.py

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7889212922:AAEJbzIT6KQrchZWnqahsBPC5rPpmAv7J2Q"  # <-- এখানে তোমার বট টোকেন বসাও

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(f"আসসালামু আলাইকুম {user.first_name}! আমি চালু আছি ✅")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("✅ Bot is running...")
    app.run_polling()
