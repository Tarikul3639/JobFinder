import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from googlesearch import search
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the token from .env
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Function for the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "Welcome! I am your JobFinder bot.\n\n"
        "I specialize in finding jobs related to Next.js, Node.js, NestJS, and Tailwind CSS "
        "in Gazipur, Dhaka, and across Bangladesh.\n\n"
        "Use /search to get the latest listings."
    )
    await context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_text)

# Function for the /search command
async def search_jobs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Searching for the latest software jobs in BD (Next.js, Node.js, etc.)... Please wait."
    )
    
    # Updated query to include technologies and locations
    query = '("Next.js" OR "Node.js" OR "NestJS" OR "Tailwind CSS") AND ("Gazipur" OR "Dhaka" OR "Bangladesh") job'
    
    try:
        # Fetching results using googlesearch-python
        results = list(search(query, num_results=7, advanced=True))
        
        message_text = "🎯 *Latest Job Matches:*\n\n"
        if results:
            for result in results:
                # result.title and result.url provide better context than just the URL
                message_text += f"• [{result.title}]({result.url})\n\n"
        else:
            message_text = "Sorry, no specific job updates were found for these technologies."
            
    except Exception as e:
        message_text = "An error occurred while searching. Please try again later."
        logging.error(f"Search error: {e}")

    # Use parse_mode='Markdown' to make the links clickable
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=message_text,
        parse_mode='Markdown'
    )

if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('search', search_jobs))
    
    application.run_polling()