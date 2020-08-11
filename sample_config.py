import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    # Your Telegram Id
    OWNER_ID = int(os.environ.get('OWNER_ID') or 0)

