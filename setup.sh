#!/bin/bash

# Run this script to set up the development environment for the Telegram bot project. It will create a virtual environment, activate it, and install the necessary libraries.

#--------------------------------------------------------
#----------------- "bash setup.sh" ------------------------
#--------------------------------------------------------

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install libraries
pip install python-telegram-bot

# Install google search library
pip install googlesearch-python

# Install environment variables library
pip install python-dotenv

echo "Virtual environment created and packages installed successfully!"


# Run the bot
# ------------------------------------
# ----------"python main.py"----------
# ------------------------------------