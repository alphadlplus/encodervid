from pyrogram import Client
from pyrogram.raw.types import User
from botclient import botcli





async def up_to_telegram(file_loc, from_user, custom_name):
    sent_message = await botcli.send_document(
        chat_id=from_user,
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
