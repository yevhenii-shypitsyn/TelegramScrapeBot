@author Yevhenii Shypitsyn, 2020

This bot has functionality to scrape data from public group chats, which is a useful feature for marketing professionals and plane business people.

Technologies used: Python, Telegram API, Telebot API, Pyrogram API

1) Install python on your computer and set up virtual environment;

Run the following commands:

$pip install --update pyrogram
$pip install --update telebot

Éetc
2) Register your bot with @BotFather on Telegram (see instructions on web)
3) Register your Telegram App on my.telegram.org (see instructions on web). They will provide you with api id and hash id which you will need to run the bot and pyrogram API.

4) Create two folders in your project environment: one called "session", which will save your login id, and another "chats", where all parsed data will be stored.

5) Run application with command:
python main.py

6) Your application will ask the phone number which you use to login to telegram when the bot is running. This info is safe and used to authenticate and register your device with Telegram.

7) Enjoy!
