# OpenAI Text Generation Bot for Telegram

## Overview

This project is a simple implementation of an OpenAI text generation model integrated with Telegram as a bot. With this bot, you can generate text using OpenAI's powerful language model and interact with it through Telegram. This README will guide you through setting up and running the bot.

## Prerequisites

Before getting started, make sure you have the following prerequisites installed:

1. **Python 3:** You will need Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **OpenAI API Key:** You'll need an API key from OpenAI. You can sign up for one on the [OpenAI website](https://beta.openai.com/signup/).

3. **Telegram Bot Token:** You'll need a Telegram Bot Token. You can create a new bot and get the token by talking to the [BotFather](https://core.telegram.org/bots#botfather) on Telegram.

## Setup

```bash
# Clone this repository to your local machine:
git clone https://github.com/yourusername/openai-telegram-bot.git
cd openai-telegram-bot

# Install the required Python packages using pip:
pip install -r requirements.txt

# Create a .env file in the project root directory and add your OpenAI API key and Telegram Bot Token as follows:
echo "OPENAI_API_KEY=your_openai_api_key" > .env
echo "TELEGRAM_BOT_TOKEN=your_telegram_bot_token" >> .env

# Configure the model settings in config.py if needed. You can adjust parameters like temperature and max tokens to control the text generation.

# Run the bot:
python bot.py
