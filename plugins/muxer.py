from pydoc import cli
from pyrogram import Client, filters
from helper_func.progress_bar import progress_bar
from helper_func.dbhelper import Database as Db
from helper_func.mux import softmux_vid, hardmux_vid, softremove_vid
from helper_func.renamer import Renamer_TG
from helper_func.imdb_data import IMDB
from helper_func.upload_tg_cli import up_to_telegram
from config import Config
import time
import requests
import json
import os

db = Db()

def insert(typ, messageid, filename, filesize, imdbid):
    url = f"{Config.API_URL}type={typ}&&input=insert-v3&&message_id={messageid}&&file_name={filename}&&file_size={filesize}&&imdbID={imdbid}"
    size = float(filesize.replace("MB","").strip())/1000 if "MB" in filesize else float(filesize.replace("GB","").strip())
    url2 = f"{Config.API_URL}input=updateC&&newID={size}"
    response = requests.get(url)
    call_back = response.content
    info = json.loads(call_back)
    response = requests.get(url2)
    return info

def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2 ** 10
    n = 0
    Dic_powerN = {0: " ", 1: "K", 2: "M", 3: "G", 4: "T"}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + "B"

async def _check_user(filt, c, m):
    chat_id = str(m.from_user.id)
    if chat_id in Config.ALLOWED_USERS:
        return True
    else :
        return False

check_user = filters.create(_check_user)

@Client.on_message(filters.command('softmux') & check_user & filters.private)
async def softmux(client, message):
    channel_id = None
    if "|" in message.text:
        message_data = message.text.split('|')
        if len(message_data) ==2 :
            channel_id = Config.CHANNEL_MOVIE if IMDB(message_data[1]) == "movie" else Config.CHANNEL_SERIES
    chat_id = message.from_user.id
    og_vid_filename = db.get_vid_filename(chat_id)
    og_sub_filename = db.get_sub_filename(chat_id)
    text = ''
    if not og_vid_filename :
        text += 'First send a Video File\n'
    if not og_sub_filename :
        text += 'Send a Subtitle File!'

    if not (og_sub_filename and og_vid_filename) :
        await client.send_message(chat_id, text)
        return

    text = 'Your File is Being Soft Subbed. This should be done in few seconds!'
    sent_msg = await client.send_message(chat_id, text)

    softmux_filename = await softremove_vid(og_vid_filename, sent_msg)
    softmux_filename = await softmux_vid(softmux_filename, og_sub_filename, sent_msg)
    if not softmux_filename:
        return

    final_filename = db.get_filename(chat_id)
    os.rename(Config.DOWNLOAD_DIR+'/'+softmux_filename,Config.DOWNLOAD_DIR+'/'+final_filename)

    start_time = time.time()
    chat_id_file = channel_id if channel_id else chat_id
    custom_name = Renamer_TG(final_filename)
    filesize = os.path.getsize(os.path.join(Config.DOWNLOAD_DIR, final_filename))
    filesize = humanbytes(filesize)
    try:
        sent_message = await client.send_document(
                                                    chat_id_file, 
                                                    progress = progress_bar,
                                                    file_name = custom_name,
                                                    progress_args = (
                                                        'Uploading your File!',
                                                        sent_msg,
                                                        start_time
                                                        ), 
                                                    document = os.path.join(Config.DOWNLOAD_DIR, final_filename),
                                                    caption = final_filename
                                                )
        text = 'File Successfully Uploaded!\nTotal Time taken : {} seconds'.format(round(time.time()-start_time))
        await sent_msg.edit(text)
    except Exception as e:
        if str(e) == "Can't upload files bigger than 2000 MiB":
            sent_message = await up_to_telegram(os.path.join(Config.DOWNLOAD_DIR, final_filename), chat_id_file, custom_name)
            await client.copy_message(chat_id=chat_id_file, from_chat_id=-649006164, message_id=sent_message.id)
        else:
            print(e)
            await client.send_message(chat_id, 'An error occured while uploading the file!\nCheck logs for details of the error!')
    if chat_id_file == Config.CHANNEL_MOVIE or chat_id_file == Config.CHANNEL_SERIES:
        typ = "series" if chat_id_file == Config.CHANNEL_SERIES else "movie"
        insert_data = insert(typ, sent_message.id, custom_name, filesize , message_data[1])
    path = Config.DOWNLOAD_DIR+'/'
    os.remove(path+og_sub_filename)
    os.remove(path+og_vid_filename)
    try :
        os.remove(path+final_filename)
    except :
        pass

    db.erase(chat_id)


@Client.on_message(filters.command('hardmux') & check_user & filters.private)
async def hardmux(client, message):
    channel_id = None
    if "|" in message.text:
        message_data = message.text.split('|')
        if len(message_data) ==2 :
            channel_id = Config.CHANNEL_MOVIE if IMDB(message_data[1]) == "movie" else Config.CHANNEL_SERIES
    chat_id = message.from_user.id
    og_vid_filename = db.get_vid_filename(chat_id)
    og_sub_filename = db.get_sub_filename(chat_id)
    text = ''
    if not og_vid_filename :
        text += 'First send a Video File\n'
    if not og_sub_filename :
        text += 'Send a Subtitle File!'
    
    if not (og_sub_filename or og_vid_filename) :
        return await client.send_message(chat_id, text)
    
    text = 'Your File is Being Hard Subbed. This might take a long time!'
    sent_msg = await client.send_message(chat_id, text)

    softmux_filename = await softremove_vid(og_vid_filename, sent_msg)
    hardmux_filename = await hardmux_vid(softmux_filename, og_sub_filename, sent_msg)
    
    if not hardmux_filename:
        return
    
    final_filename = db.get_filename(chat_id)
    os.rename(Config.DOWNLOAD_DIR+'/'+hardmux_filename,Config.DOWNLOAD_DIR+'/'+final_filename)
    
    start_time = time.time()
    chat_id_file = channel_id if channel_id else chat_id
    custom_name = Renamer_TG(final_filename)
    filesize = os.path.getsize(os.path.join(Config.DOWNLOAD_DIR, final_filename))
    filesize = humanbytes(filesize)
    try:
        sent_message = await client.send_video(
                                                chat_id_file, 
                                                progress = progress_bar,
                                                file_name = custom_name,
                                                progress_args = (
                                                    'Uploading your File!',
                                                    sent_msg,
                                                    start_time
                                                    ), 
                                                video = os.path.join(Config.DOWNLOAD_DIR, final_filename),
                                                caption = final_filename
                                            )
        text = 'File Successfully Uploaded!\nTotal Time taken : {} seconds'.format(round(time.time()-start_time))
        await sent_msg.edit(text)
    except Exception as e:
        if str(e) == "Can't upload files bigger than 2000 MiB":
            sent_message = await up_to_telegram(os.path.join(Config.DOWNLOAD_DIR, final_filename), chat_id_file, custom_name)
            await client.copy_message(chat_id=chat_id_file, from_chat_id=-649006164, message_id=sent_message.id)
        else:
            print(e)
            await client.send_message(chat_id, 'An error occured while uploading the file!\nCheck logs for details of the error!')
    if chat_id_file == Config.CHANNEL_MOVIE or chat_id_file == Config.CHANNEL_SERIES:
        typ = "series" if chat_id_file == Config.CHANNEL_SERIES else "movie"
        insert_data = insert(typ, sent_message.id, custom_name, filesize , message_data[1])
    path = Config.DOWNLOAD_DIR+'/'
    os.remove(path+og_sub_filename)
    os.remove(path+og_vid_filename)
    try :
        os.remove(path+final_filename)
    except :
        pass
    db.erase(chat_id)


@Client.on_message(filters.command('softremove') & check_user & filters.private)
async def softremove(client, message):
    channel_id = None
    if "|" in message.text:
        message_data = message.text.split('|')
        if len(message_data) ==2 :
            channel_id = Config.CHANNEL_MOVIE if IMDB(message_data[1]) == "movie" else Config.CHANNEL_SERIES
    chat_id = message.from_user.id
    og_vid_filename = db.get_vid_filename(chat_id)
    text = ''
    if not og_vid_filename :
        text += 'First send a Video File\n'

    text = 'Your File is Being Soft Subbed. This should be done in few seconds!'
    sent_msg = await client.send_message(chat_id, text)

    softmux_filename = await softremove_vid(og_vid_filename, sent_msg)
    if not softmux_filename:
        return

    final_filename = db.get_filename(chat_id)
    os.rename(Config.DOWNLOAD_DIR+'/'+softmux_filename,Config.DOWNLOAD_DIR+'/'+final_filename)

    start_time = time.time()
    chat_id_file = channel_id if channel_id else chat_id
    custom_name = Renamer_TG(final_filename, False)
    filesize = os.path.getsize(os.path.join(Config.DOWNLOAD_DIR, final_filename))
    filesize = humanbytes(filesize)
    try:
        sent_message = await client.send_document(
                                                    chat_id_file, 
                                                    progress = progress_bar,
                                                    file_name = custom_name,
                                                    progress_args = (
                                                        'Uploading your File!',
                                                        sent_msg,
                                                        start_time
                                                        ), 
                                                    document = os.path.join(Config.DOWNLOAD_DIR, final_filename),
                                                    caption = final_filename
                                                )
        
        text = 'File Successfully Uploaded!\nTotal Time taken : {} seconds'.format(round(time.time()-start_time))
        await sent_msg.edit(text)
    except Exception as e:
        if str(e) == "Can't upload files bigger than 2000 MiB":
            sent_message = await up_to_telegram(os.path.join(Config.DOWNLOAD_DIR, final_filename), chat_id_file, custom_name)
            await client.copy_message(chat_id=chat_id_file, from_chat_id=-649006164, message_id=sent_message.id)
        else:
            print(e)
            await client.send_message(chat_id, 'An error occured while uploading the file!\nCheck logs for details of the error!')
    if chat_id_file == Config.CHANNEL_MOVIE or chat_id_file == Config.CHANNEL_SERIES:
        typ = "series" if chat_id_file == Config.CHANNEL_SERIES else "movie"
        insert_data = insert(typ, sent_message.id, custom_name, filesize , message_data[1])
    path = Config.DOWNLOAD_DIR+'/'
    os.remove(path+og_vid_filename)
    try :
        os.remove(path+final_filename)
    except :
        pass

    db.erase(chat_id)
