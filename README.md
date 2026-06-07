# JobFinder Telegram Bot

A Telegram bot designed to assist with junior-level full-stack job hunting. It provides curated opportunities and is being upgraded for real-time job scraping.

## Prerequisites

- Python 3.11+
- [Telegram Bot Token](https://t.me/botfather)

## Installation

1. Clone the repository to your local machine.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # For Git Bash/Windows
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the project root and add your Telegram bot token:
   ```text
   TELEGRAM_BOT_TOKEN=your_actual_token_here
   ```

## Usage

Run the bot using the following command:
```bash
python main.py
```
Once the bot is running, you can interact with it on Telegram using the `/search` command.
