from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", 24010108))
    API_HASH = environ.get("API_HASH", "8d89700b2fc09a3aa6c906cbed65b040")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6739598823:AAFGJyIubVfxivFPbnUuKV1UtAnfbOvFI1M") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://lajihi2115:lgAEiuZHs917nZgy@cluster0.lx88eg8.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5764988016').split()]
    
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
