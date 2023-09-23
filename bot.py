import asyncio
from pyrogram import Client, compose,idle
import os

from main.rename import app as Client2

TOKEN = os.environ.get("BOT_TOKEN", "6590979468:AAHevTgpJIBWC0mKKcqeG-a40YvYk8aIKSw")

API_ID = int(os.environ.get("API_ID", "59202"))

API_HASH = os.environ.get("API_HASH", "b3901895dc193c30c808ba4f1b550ed0")

STRING = os.environ.get("STRING", "BQFVK_4AqAg9m9-MCnjh364qEo3vc0EuGI6LmsvPPabm1oxgxMxAtlfkQt_Msu5AlnRV5bVcOSNJWNgoi-DBhjYLpw5bYTzoytITd1rFvv91o2BUMT0eI4CxS2vwPEu_CUlU5p7jxvVKn6gtE6XvHtEUr053dCiLhCUuvaLyfcHtNuAd3n3eBs_03Mb4z4vzZ3DIR4CKk_yGRqz1Jl6FV0RXw7S7ekTE9szPd3Au_rPxCw_mKSPNzUSO3rOmjpad0sSDrkwpQoLQEo2MxG1ZAhWH0Y1BYIbWSGriCfoMi-HVLDdDiS9mMcXBFcJrRGbxUtHuxflTJ9mRESsmtOMZ_D_VHOdAFwAAAAFJs2jlAA")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='main'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
