# Don't Remove Credit @Opleech
# Telegram @Opleech
# Copyright (c) 2023 WOODcraft


import pymongo
from info import DATABASE_URI, DATABASE_NAME
from pyrogram import enums
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

myclient = pymongo.MongoClient(DATABASE_URI)
mydb = myclient[DATABASE_NAME]



async def add_gfilter(gfilters, text, reply_text, btn, file, alert):
    myangel = mydb[str(gfilters)]
    # myangel.create_index([('text', 'text')])

    data = {
        'text':str(text),
        'reply':str(reply_text),
        'btn':str(btn),
        'file':str(file),
        'alert':str(alert)
    }

    try:
        myangel.update_one({'text': str(text)},  {"$set": data}, upsert=True)
    except:
        logger.exception('Some error occured!', exc_info=True)
             
     
async def find_gfilter(gfilters, name):
    myangel = mydb[str(gfilters)]
    
    query = myangel.find( {"text":name})
    # query = myangel.find( { "$text": {"$search": name}})
    try:
        for file in query:
            reply_text = file['reply']
            btn = file['btn']
            fileid = file['file']
            try:
                alert = file['alert']
            except:
                alert = None
        return reply_text, btn, alert, fileid
    except:
        return None, None, None, None


async def get_gfilters(gfilters):
    myangel = mydb[str(gfilters)]

    texts = []
    query = myangel.find()
    try:
        for file in query:
            text = file['text']
            texts.append(text)
    except:
        pass
    return texts


async def delete_gfilter(message, text, gfilters):
    myangel = mydb[str(gfilters)]
    
    myquery = {'text':text }
    query = myangel.count_documents(myquery)
    if query == 1:
        myangel.delete_one(myquery)
        await message.reply_text(
            f"'`{text}`'  deleted. I'll not respond to that gfilter anymore.",
            quote=True,
            parse_mode=enums.ParseMode.MARKDOWN
        )
    else:
        await message.reply_text("Couldn't find that gfilter!", quote=True)

async def del_allg(message, gfilters):
    if str(gfilters) not in mydb.list_collection_names():
        await message.edit_text("Nothing to Remove !")
        return

    myangel = mydb[str(gfilters)]
    try:
        myangel.drop()
        await message.edit_text(f"All gfilters has been removed !")
    except:
        await message.edit_text("Couldn't remove all gfilters !")
        return

async def count_gfilters(gfilters):
    myangel = mydb[str(gfilters)]

    count = myangel.count()
    return False if count == 0 else count


async def gfilter_stats():
    collections = mydb.list_collection_names()

    if "CONNECTION" in collections:
        collections.remove("CONNECTION")

    totalcount = 0
    for collection in collections:
        myangel = mydb[collection]
        count = myangel.count()
        totalcount += count

    totalcollections = len(collections)

    return totalcollections, totalcount
