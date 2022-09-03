#AlphaDL
from pyrogram import Client
from config import Config




async def up_to_telegram(file_loc, from_user, custom_name):
    session_string = "BADK7tsAGX2RVBI-3IJxamHISTwVH7VdLJ3d0VTwPWxND-MSvkehUDjzBn6EVS9FIRw6-dK4JVxOEFgawsKu8F5l2BZsg5nr3l4x323P9Ssr2HBQcqhfv9LJL6EmusZrQvD16a--GojMoVntSRYqaRe1Sf1-XSF_qEUIQgC1OIgb7PcU0rxuGojIv6wkMIsSh_ZfwBr6MHGlP3HxNCRb9VY_D2KA1MrP5P91-bGatBGja-bAsZPgUFcq8Usc0wGjBFVYqBNE1l9BBwzmY8eQckf8MGAROW3i2QouxJve-v5Jslv1-vy6c9h-tdNSpnZB-d2vMq2z3jqabmWpgGv5ouRPWWvXVAAAAAFE1lFcAA"
    botcli = await Client(
        "alphadl-leecher",
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        session_string= session_string,
        sleep_threshold=60,
        in_memory = True,
        no_updates=True,
        ).start()
    
    sent_message = await botcli.send_document(
        chat_id=-1001698534477,
        document=file_loc,
        # caption=caption_str,
        # parse_mode="html",
        # duration=duration,
        # width=width,
        # height=height,
        # thumb=thumb,
        # supports_streaming=True,
        file_name=custom_name,
        disable_notification=True,
        # progress=prog.progress_for_pyrogram,
        # progress_args=(
        #     f"**• Uploading :** `{os.path.basename(local_file_name)}`",
        #     start_time,
        # ),
    )
    return sent_message
