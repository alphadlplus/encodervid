from pyrogram import Client
from config import Config



plugins = dict(root='plugins')

app = Client(
        'Subtitle Muxer',
        bot_token = Config.BOT_TOKEN,
        api_id = Config.APP_ID,
        api_hash = Config.API_HASH,
        plugins = plugins
    )


session_string = "BAAI5fQAPfZG2HEX2Y2pW2DboB10t0Wp--4YIpE4zNL_TX6yls92HnG15v4byShwXBLdISNuhU0xahOKxP-L6cxWOigQN5QxA9kaj-j24EolRvPq9S05C_vk7IWqLcIdJO6YhgKd_PvuHMltWs3uP4oObYE8xpLWJWwYDjIfM3LtdcW1thINk-w2JrsELNUh9CLKUXCrssixPZzx9QuSK6ncqaAyJgpkD5x8mDicItNZBh6C_VojaA58FNQN-MgRghAwPdL3HO2lT-G1721ah1czix4TldNYMCExTbtGlnrCPkvCVysGHay1GjOi80jyJ5DZmcuHVUwFNEcK0WxVpb6NHf8POgAAAAFE1lFcAA"
botcli = Client("alphadl-leecher", api_id=13299419, api_hash="9f24e49201ca03be304807916474e35b", session_string= session_string, in_memory = True)
