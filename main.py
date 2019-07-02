from telethon import TelegramClient, sync
from config import *
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime
from utils import *
import time

client = TelegramClient('TimeAvatar', api_id, api_hash)
client.start()


prev_update_time = ""

while True:
    if time_has_changed(prev_update_time):
        if addTimeToName:
            client(UpdateProfileRequest(
                first_name = f"Eugene ({prev_update_time})"
            ))
        prev_update_time = convert_time_to_string(datetime.now())
        photos = client.get_profile_photos('me')
        file = client.upload_file(f"{images_dir}/{prev_update_time.replace(':', '-')}.jpg")
        client(UploadProfilePhotoRequest(file))
        client(DeletePhotosRequest(photos))
    time.sleep(10)
