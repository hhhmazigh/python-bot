import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🇫🇷 France", callback_data='fr'),
            InlineKeyboardButton("🇩🇪 Germany", callback_data='de')
        ],
        [
            InlineKeyboardButton("🇬🇧 UK", callback_data='gb'),
            InlineKeyboardButton("🇺🇸 USA", callback_data='us')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Please choose your config:', reply_markup=reply_markup)

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    file_mapping = {
        'fr': 'attached_assets/ooredoo 🇨🇵🪶.ehi',
        'de': 'attached_assets/ooredoo 🇩🇪🪶.ehi',
        'gb': 'attached_assets/ooredoo 🇬🇧🪶.ehi',
        'us': 'attached_assets/ooredoo 🇺🇸🪶.ehi'
    }
    
    file_path = file_mapping.get(query.data)
    if file_path:
        try:
            await query.message.reply_document(document=open(file_path, 'rb'))
        except Exception as e:
            await query.message.reply_text(f"Error sending config: {str(e)}")
    else:
        await query.message.reply_text("Config not found")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """Available commands:
/start - Start bot and choose config
/help - Show this help message"""
    await update.message.reply_text(help_text)

def main():
    # Replace with your bot token
    application = ApplicationBuilder().token('8055945068:AAH4RI8kwFf8ctWsnHv5yCNQ-D4Amxjn4OU').build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CallbackQueryHandler(button_click))

    # Start the Bot
    print("Starting bot...")
    application.run_polling()

if __name__ == '__main__':
    main()
