# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/mrjoker/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 10449735  # integer value, dont use ""
    API_HASH = "bcf5ea3ad86b2767e62495aa82a04e74"
    BOT_ID = "5391643063"
    TOKEN = "5391643063:AAEIBqQzCQ1IAM4J-kNWUQArztEXiv1v57s"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 2131613077  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "ayanokoji_kunUwU"
    SUDO_USERS = "1719179612"
    SUPPORT_USERS = "1719179612"
    SUPPORT_CHAT = "perobot_support"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001634308319
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001634308319
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://gmjblmwutoacix:46ff66a6d3cea71dd8c7626601ea125e3b9e47f0e53994d634ac045d7b3914f0@ec2-52-203-118-49.compute-1.amazonaws.com:5432/d1b2f02k1tuu66"  # needed for any database modules
    REDIS_URI = " "
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    INFOPIC = True
    URL = None
    HEROKU_API_KEY = ""
    HEROKU_APP_NAME = ""
    BOT_USERNAME = ""
    SPAMWATCH_API = "JD3s4u1~lxl5KTsxq18yL0WdBjj7QjjLFW6FYfbrHr2KKBBeAVDRrQ6yOkOQPH84"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    ARQ_API_KEY = "GBVANC-POIBJH-XAYVHT-XZBPTG-ARQ"
    ARQ_API_URL = "https://thearq.tech/"
    TEMP_DOWNLOAD_DIRECTORY = "./"
    OPENWEATHERMAP_ID = ""
    VIRUS_API_KEY = ""
    REDIS_URL = ""
    LASTFM_API_KEY = ""
    

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    ALLOW_CHATS = ""
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    WHITELIST_USERS = get_user_list("elevated_users.json", "whitelists")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "BVDSG5YDPDAR0OXW"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "80UKIECA3BLE"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "xyz"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = ""  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    REM_BG_API_KEY = ""
    GENIUS_API_TOKEN = ""
    MONGO_DB = ""
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
