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


session_string = "BADK7tsAGX2RVBI-3IJxamHISTwVH7VdLJ3d0VTwPWxND-MSvkehUDjzBn6EVS9FIRw6-dK4JVxOEFgawsKu8F5l2BZsg5nr3l4x323P9Ssr2HBQcqhfv9LJL6EmusZrQvD16a--GojMoVntSRYqaRe1Sf1-XSF_qEUIQgC1OIgb7PcU0rxuGojIv6wkMIsSh_ZfwBr6MHGlP3HxNCRb9VY_D2KA1MrP5P91-bGatBGja-bAsZPgUFcq8Usc0wGjBFVYqBNE1l9BBwzmY8eQckf8MGAROW3i2QouxJve-v5Jslv1-vy6c9h-tdNSpnZB-d2vMq2z3jqabmWpgGv5ouRPWWvXVAAAAAFE1lFcAA"
botcli = Client("alphadl-leecher", api_id=Config.APP_ID, api_hash=Config.API_HASH, session_string= session_string, in_memory = True)
