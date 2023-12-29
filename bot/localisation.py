#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AbirHasan2005

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = f"""<b>
    • Hi There; {m.from_user.mention} !

    -I'm Video encoder bot, I can Encode video or Compress video.
    -Hit /help to find out more about how to use me to my full potential.
    
    -Bot Developer- <a href='t.me/stupidboi69'>Stupidboi69</a> </b>
    """
   
    ABS_TEXT = "**-Please don't be selfish.**"
    
    FORMAT_SELECTION = """<b>
    -Select the desired format: <a href='{}'>file size might be approximate</a>.
    
    -If you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.
    -Hit /deletethumbnail to delete the auto-generated thumbnail.</b>
    """
    
    
    DOWNLOAD_START = "**-Downloading is about to start**\n"
    
    UPLOAD_START = "**Uploading is about to start**\n"
    
    COMPRESS_START = "**-Encoding is about to start**\n"
    
    RCHD_BOT_API_LIMIT = "**-Size should be greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = """<b>
    -Downloaded in {} seconds.
    -Detected File Size: {}
    -Sorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations.</b>
    """
    
    COMPRESS_SUCCESS = "@StupidBoi"

    COMPRESS_PROGRESS = "<b>-ETA     : {}\n-Progress: {}%</b>"

    SAVED_CUSTOM_THUMB_NAIL = "**-Custom video / file thumbnail saved. This image will be used in the video / file.**"
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "-Custom thumbnail cleared succesfully.**"
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "**-Media cleared succesfully.**"
    
    SAVED_RECVD_DOC_FILE = "**-Downloaded Successfully.**"
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "**-No Custom ThumbNail found.**"
    
    NO_VOID_FORMAT_FOUND = "**no-one gonna help you\n-{}**"
    
    USER_ADDED_TO_DB = "<b>User <a href='tg://user?id={}'>{}</a> added to {} till {}.</b>"
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = """<b>
    -Already one Process going on!
    -Check Live Status on Updates Channel.</b>
    """
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        """<b>-Hi, I am Video Compressor Bot
        
        1. Send me your telegram big video file,
        2. Reply to the file with: /compress 50.
        
        -Bot Developer- @StupidBoi
        """
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
