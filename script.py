# import necessary libraries
import requests
import datetime
from pytz import timezone
from bs4 import BeautifulSoup
from telegram import Bot
from telegram import constants
from telegram.error import TelegramError
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter

# Function to get weather information
def get_weather(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

# Function to get exchange rates
def get_exchange_rates():
    c = CurrencyRates()
    usd_rate = c.get_rate('USD', 'RUB')
    eur_rate = c.get_rate('EUR', 'RUB')
    b = BtcConverter()
    btc_rate = b.get_latest_price('USD') 

    return usd_rate, eur_rate, btc_rate

# Function to get days until Bitcoin halving
def get_days_until_halving():
    # Add logic to calculate days until Bitcoin halving
    return days_until_halving

# Function to send message to Telegram
def send_telegram_message(bot_token, chat_id, message):
    bot = Bot(token=bot_token)
    try:
        bot.send_message(chat_id=chat_id, text=message, parse_mode=constants.ParseMode.MARKDOWN)
    except TelegramError as e:
        print(f"Error sending Telegram message: {e}")

# GitHub Actions entry point
if __name__ == "__main__":
    # Replace with your GitHub repository secrets
    TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
    TELEGRAM_CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"
    OPENWEATHER_API_KEY = "YOUR_OPENWEATHER_API_KEY"
    CITY = "YOUR_CITY"

    # Get weather information
    weather_data = get_weather(OPENWEATHER_API_KEY, CITY)

    # Get exchange rates
    usd_rate, eur_rate, btc_rate = get_exchange_rates()

    # Get days until Bitcoin halving
    days_until_halving = get_days_until_halving()

    # Create a message
    message = (
        f"Weather in {CITY}:\n"
        f"Temperature: {weather_data['main']['temp']}°C\n"
        f"Description: {weather_data['weather'][0]['description']}\n\n"
        f"Exchange Rates:\n"
        f"USD to RUB: {usd_rate}\n"
        f"EUR to RUB: {eur_rate}\n"
        f"Bitcoin Rate: {btc_rate}\n\n"
        f"Days until Bitcoin halving: {days_until_halving}"
    )

    # Send message to Telegram
    send_telegram_message(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, message)
