
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

import pyrogram
logging.getLogger('pyrogram').setLevel(logging.WARNING)


if __name__ == '__main__':

    if not os.path.isdir(Config.DOWNLOAD_DIR):
        os.mkdir(Config.DOWNLOAD_DIR)

    plugins = dict(root='plugins')

    app = pyrogram.Client(
        'Subtitle Muxer',
        bot_token = Config.BOT_TOKEN,
        api_id = Config.APP_ID,
        api_hash = Config.API_HASH,
        plugins = plugins
    )
    app.run()

    session_string = "BAAI5fQAPfZG2HEX2Y2pW2DboB10t0Wp--4YIpE4zNL_TX6yls92HnG15v4byShwXBLdISNuhU0xahOKxP-L6cxWOigQN5QxA9kaj-j24EolRvPq9S05C_vk7IWqLcIdJO6YhgKd_PvuHMltWs3uP4oObYE8xpLWJWwYDjIfM3LtdcW1thINk-w2JrsELNUh9CLKUXCrssixPZzx9QuSK6ncqaAyJgpkD5x8mDicItNZBh6C_VojaA58FNQN-MgRghAwPdL3HO2lT-G1721ah1czix4TldNYMCExTbtGlnrCPkvCVysGHay1GjOi80jyJ5DZmcuHVUwFNEcK0WxVpb6NHf8POgAAAAFE1lFcAA"
    botcli = pyrogram.Client("alphadl-leecher", api_id=Config.APP_ID, api_hash=Config.API_HASH, session_string= session_string, in_memory = True)

    botcli.run()