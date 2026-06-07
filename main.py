import requests
from bs4 import BeautifulSoup
import os
import datetime
from dotenv import load_dotenv

# Load variables
load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
LAST_RUN_FILE = "last_run.txt"

def get_today_date():
    return datetime.date.today().isoformat()

def check_already_run():
    if os.path.exists(LAST_RUN_FILE):
        with open(LAST_RUN_FILE, "r") as f:
            return f.read().strip() == get_today_date()
    return False

def mark_as_run():
    with open(LAST_RUN_FILE, "w") as f:
        f.write(get_today_date())

def fetch_jobs():
    # Simple example for BDJobs Full Stack search
    url = "https://jobs.bdjobs.com/jobsearch.asp?fcatId=8&txtsearch=Full%20Stack%20Developer"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    jobs = []
    # Simplified scraper for demo
    for job in soup.select('.job-title-text')[:5]:
        title = job.get_text(strip=True)
        link = "https://jobs.bdjobs.com/" + job.find('a')['href']
        jobs.append(f"• {title}\n  {link}")
    
    return "\n\n".join(jobs) if jobs else "No new jobs found today."

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, data=payload)

if __name__ == "__main__":
    if not check_already_run():
        print("Running job search...")
        job_list = fetch_jobs()
        msg = f"🎯 *Today's Full Stack Jobs:*\n\n{job_list}"
        send_telegram(msg)
        mark_as_run()
        print("Done.")
    else:
        print("Already ran today. Exiting.")
