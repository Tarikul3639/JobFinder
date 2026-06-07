import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from googlesearch import search
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "Hello! I am your Professional JobFinder Bot.\n\n"
        "I am looking for Full-Stack (Next.js, NestJS, MongoDB, Redux) "
        "Junior/Associate positions in Dhaka.\n\n"
        "Use /search to get the latest matches."
    )
    await context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_text)

async def search_jobs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Searching for Junior/Entry-level Full-Stack jobs in Dhaka (Next.js, NestJS, MongoDB)..."
    )
    
    # Optimized search query for Junior roles in Dhaka
    query = ('(site:linkedin.com/jobs OR site:bdjobs.com OR site:indeed.com) '
             '"Junior" OR "Entry-level" OR "Associate" '
             '"Full Stack Developer" AND ("Next.js" OR "NestJS" OR "MongoDB" OR "Redux") '
             'AND "Dhaka" job')
    
    try:
        results = list(search(query, num_results=10, advanced=True))
        
        message_text = "🎯 *Best Job Matches for You in Dhaka:*\n\n"
        if results:
            for result in results:
                message_text += f"• [{result.title}]({result.url})\n\n"
        else:
            message_text = "No job updates found currently. Try again later!"
            
    except Exception as e:
        message_text = "Search error occurred."
        logging.error(f"Search error: {e}")

    await context.bot.send_message(chat_id=update.effective_chat.id, text=message_text, parse_mode='Markdown')

if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('search', search_jobs))
    application.run_polling()
