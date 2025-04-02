import logging
import time
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Define command handlers
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
    await send_config(query, context, query.data)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """Available commands:
/start - Start the bot
/help - Show this help message
/config_fr - Get French config
/config_de - Get German config
/config_gb - Get UK config
/config_us - Get US config"""
    await update.message.reply_text(help_text)

async def send_config(update: Update, context: ContextTypes.DEFAULT_TYPE, country_code: str):
    file_mapping = {
        'fr': 'attached_assets/ooredoo 🇨🇵🪶.ehi',
        'de': 'attached_assets/ooredoo 🇩🇪🪶.ehi',
        'gb': 'attached_assets/ooredoo 🇬🇧🪶.ehi',
        'us': 'attached_assets/ooredoo 🇺🇸🪶.ehi'
    }

    file_path = file_mapping.get(country_code.lower())
    if file_path:
        try:
            await update.message.reply_document(document=open(file_path, 'rb'))
        except Exception as e:
            await update.message.reply_text(f"Sorry, couldn't send the config file. Error: {str(e)}")
    else:
        await update.message.reply_text("Config file not found")

async def config_fr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_config(update, context, 'fr')

async def config_de(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_config(update, context, 'de')

async def config_gb(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_config(update, context, 'gb')

async def config_us(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_config(update, context, 'us')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"You said: {update.message.text}")

def main():
    while True:
        try:
            # Replace 'YOUR_BOT_TOKEN' with the API token received from BotFather
            application = ApplicationBuilder().token('7750431478:AAHTVkkKFNOmbq5FnCvMi5DZgy4hoHRpIio').build()

            # Add command handlers
            application.add_handler(CommandHandler("start", start))
            application.add_handler(CommandHandler("help", help_command))
            application.add_handler(CallbackQueryHandler(button_click))

            # Add message handler for non-command messages
            application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

            # Start the Bot
            print("Starting bot...")
            application.run_polling()
        except Exception as e:
            print(f"Error occurred: {e}")
            print("Restarting bot in 10 seconds...")
            time.sleep(10)

if __name__ == '__main__':
    main()
