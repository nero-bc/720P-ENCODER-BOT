from bot.get_cfg import get_config

class Config(object):from bot.get_cfg import get_config

class Config(object):

    # You can keep this default

    SESSION_NAME = get_config("SESSION_NAME", "SJCompressorBot")

    # AHCompressBot....

    # sucks Dude

    APP_ID = get_config("APP_ID", "25695562")

    API_HASH = get_config("API_HASH", "0b691c3e86603a7e34aae0b5927d725a")

    LOG_CHANNEL = get_config("LOG_CHANNEL", "-1001955639051")

    UPDATES_CHANNEL = get_config("UPDATES_CHANNEL", None) # Without @ LOL

     # Get these values from my.telegram.org

    AUTH_USERS = set(

        int(x) for x in get_config(

            "AUTH_USERS", "1895952308 5522433014"

        ).split()

    )

# array , simplest method was AUTH_USERS = [] ; AUTH_USERS.append(your telegram id) 🤣

    # array to store the channel ID who are authorized to use the bot

    # dont u fucking remove this id 😤

    TG_BOT_TOKEN = get_config("TG_BOT_TOKEN", "6358741541:AAF3DT6hP2T5wKnxRdqxAv2lK-GBHsz7bjg")

    # the download location, where the HTTP Server runs

    DOWNLOAD_LOCATION = get_config("DOWNLOAD_LOCATION", "downloads/")

    # Telegram maximum file upload size

    BOT_USERNAME = get_config("BOT_USERNAME", "videos_converter_bot")

    MAX_FILE_SIZE = 2097152000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 2097152000

    # default thumbnail to be used in the videos

    DEF_THUMB_NAIL_VID_S = get_config("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    # proxy for accessing youtube-dl in GeoRestricted Areas

    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061

    HTTP_PROXY = get_config("HTTP_PROXY", None)

    # maximum message length in Telegram

    MAX_MESSAGE_LENGTH = 4096

    # add config vars for the display progress

    FINISHED_PROGRESS_STR = get_config("FINISHED_PROGRESS_STR", "▣")

    UN_FINISHED_PROGRESS_STR = get_config("UN_FINISHED_PROGRESS_STR", "▢")

    LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "Log.txt")

      # because, https://t.me/c/1494623325/5603
