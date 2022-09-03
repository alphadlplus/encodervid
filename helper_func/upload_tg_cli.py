#AlphaDL
from pyrogram import Client
from config import Config




async def up_to_telegram(file_loc, from_user, custom_name):
    session_string = "BADTy8EAm_XxRBPTSlz6ADvwvblbXrWDpp5ZT9ARg6TCRnXdHxczHK9G90XkZlg0mhmNJXGMWsGRYVVECQL3qLowOvuXYB9xxaVM2IEusQzwKnToYOrKvaW5BXfakJuFOHLKqaxxb6-sooFdDQB-5SUNk2MA754yV9LCAEgLvdTz2FxFmlzqQomoDBmOCABx7R6P29GTFGxWq_kUmaaVmSyJp94RBozZbm-PzIChED9M2SPODmSBBxIwQavEFZiGorZ4dSLJg3B5CoWR0lNylawpIe_WaFmIIii5NwQRLBxGGx8nfQk3OhtpCl71eDr7Ja_kv1vIh5IoDe-nZCjRxc7cM8ypPAAAAAFQ20LQAA"
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
