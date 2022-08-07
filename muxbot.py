
# (c) mohdsabahat

import logging
logging.basicConfig(level = logging.DEBUG,
                     format="%(asctime)s - %(name)s - %(message)s - %(levelname)s")

logger = logging.getLogger(__name__)

import os

if os.path.exists('testconfig.py'):
    from testconfig import Config
else:
    from config import Config

from helper_func.dbhelper import Database as Db
db = Db().setup()

from pyrogram import idle
from botclient import botcli, app
logging.getLogger('pyrogram').setLevel(logging.WARNING)


if __name__ == '__main__':

    if not os.path.isdir(Config.DOWNLOAD_DIR):
        os.mkdir(Config.DOWNLOAD_DIR)
    
    app.run()
    botcli.start()
idle()
app.stop()
