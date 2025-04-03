# Telegram Config Bot

A Telegram bot that allows users to download configuration files for different countries.

## Features

- Interactive button interface
- Support for multiple country configurations
- Tracks user downloads and usage
- Easy to use commands

## Available Commands

- `/start` - Start the bot and display country selection menu
- `/help` - Show help message with available commands

## Configuration Files

The bot provides configuration files for:
- 🇫🇷 France
- 🇩🇪 Germany
- 🇬🇧 UK
- 🇺🇸 USA

## Setup

1. Clone this project on Replit
2. Install dependencies (automatically handled by Replit)
3. Create a new bot with @BotFather on Telegram
4. Get your bot token from @BotFather
5. Replace the token in `main.py` with your bot token
6. Click the Run button to start the bot

## File Structure

```
├── attached_assets/     # Configuration files
├── main.py             # Main bot code
├── users.json          # User tracking data
└── README.md           # This file
```

## Usage

1. Start a chat with the bot
2. Use the `/start` command
3. Click on the country button for your desired configuration
4. The bot will send you the corresponding configuration file

## Built With

- python-telegram-bot
- Python 3.11
