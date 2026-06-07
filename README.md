# JobFinder: Tech-Stack Focused Job Assistant

**JobFinder** is a smart and automated Telegram bot designed for software developers and tech professionals. It streamlines the job-hunting process by fetching real-time, relevant job listings based on specific tech stacks and target locations in Bangladesh.

## 🚀 Key Features

* **Targeted Search:** Specifically filters for roles involving **Next.js, Node.js, NestJS, and Tailwind CSS**.
* **Location Aware:** Prioritizes job opportunities in **Gazipur, Dhaka, and across Bangladesh**.
* **Clickable Results:** Delivers job titles and direct links in a clean, professional format directly to your Telegram chat.
* **Secure Architecture:** Uses environment variables (`.env`) to ensure your Telegram Bot Token remains private and secure.

## 🛠 Project Overview

This bot is built using **Python** and the **python-telegram-bot** library. It utilizes the Google Search engine to aggregate real-time job data, ensuring that users receive the most up-to-date listings available.

## ⚙️ Setup Guide

### 1. Install Dependencies

Ensure your virtual environment is activated, then install the required libraries:

```bash
pip install python-telegram-bot googlesearch-python python-dotenv

```

### 2. Configuration

Create a `.env` file in the root directory of your project and add your Telegram Bot Token:

```text
TELEGRAM_BOT_TOKEN=your_bot_token_here

```

### 3. Run the Bot

Start the bot by running the following command in your terminal:

```bash
python3 bot.py

```

## 🤖 How to Use

* **/start**: Initialize the bot and receive a welcome message.
* **/search**: Trigger a real-time search for the latest jobs matching your tech stack (Next.js, Node.js, NestJS, Tailwind CSS) and preferred locations (Gazipur/Dhaka/Bangladesh).

---

Does this English version cover everything you need for your project documentation?