# GitHub Actions Weather and Finance Notifier

This repository contains a GitHub Actions workflow that automatically fetches weather data, financial exchange rates, Bitcoin halving countdown, and sends the information to a specified Telegram chat at regular intervals.

## Features

- **Weather Updates:** Get the current weather details for a specified city.
- **Financial Data:** Receive exchange rates for USD to RUB, EUR to RUB, and Bitcoin rates.
- **Bitcoin Halving Countdown:** Keep track of the days remaining until the next Bitcoin halving event.
- **Telegram Notifications:** Receive all the gathered information conveniently in your Telegram chat.

## Usage

1. **Set Up Telegram Bot:**
   - Create a Telegram bot and obtain the bot token.
   - Find your chat ID by talking to the "IDBot" on Telegram.

2. **Configure GitHub Secrets:**
   - Add the following secrets to your GitHub repository:
     - `TELEGRAM_BOT_TOKEN`: Your Telegram bot token.
     - `TELEGRAM_CHAT_ID`: Your Telegram chat ID.
     - `OPENWEATHER_API_KEY`: API key from OpenWeatherMap.
     - `CITY_WEATHER`: name of the city for which you want to receive weather updates.

3. **Run Workflow:**
   - The GitHub Actions workflow is scheduled to run every 7 hours. You can customize the schedule in the `.github/workflows/main.yml` file.

Now, sit back, relax, and let GitHub Actions keep you informed about the latest weather conditions, financial exchange rates, and the countdown to the next Bitcoin halving!
