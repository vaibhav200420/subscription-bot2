from pyrogram import Client
from handlers import register_handlers
from config import API_ID, API_HASH, BOT_TOKEN

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

def main():
    register_handlers(app)
    app.run()

if __name__ == "__main__":
    main()
