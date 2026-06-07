import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Set up logging configuration
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO
)

async def search_jobs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handles the /search command. 
    Provides a curated list of junior-friendly full-stack job opportunities in Dhaka.
    """
    response = "🎯 *Junior/Entry-Level Full Stack Jobs in Dhaka:*\n\n"
    response += "Skills: Next.js, NestJS, MongoDB, Redux Toolkit, Tailwind CSS\n\n"
    
    # Curated job opportunities for entry-level developers in Dhaka
    response += "1. [BrainStation-23](https://brainstation-23.com/career/) (Focus: Junior/Internship roles)\n"
    response += "2. [BJIT](https://bjitgroup.com/career/) (Focus: Entry-level tracks)\n"
    response += "3. [Cefalo Bangladesh](https://cefalo.com/careers/) (Focus: Junior Engineer)\n"
    response += "4. [Dcastalia](https://dcastalia.com/careers/) (Focus: Junior Developer)\n"
    response += "5. [Selise Digital Platforms](https://selise.ch/careers/) (Focus: Associate Engineer)\n\n"
    
    response += "_Note: Emphasize your GitHub projects and technical documentation in your resume to stand out._"
    
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response, parse_mode='Markdown')

if __name__ == '__main__':
    # Initialize the Telegram bot application
    if not BOT_TOKEN:
        logging.error("BOT_TOKEN is missing. Please check your .env file.")
    else:
        application = ApplicationBuilder().token(BOT_TOKEN).build()
        application.add_handler(CommandHandler('search', search_jobs))
        application.run_polling()
