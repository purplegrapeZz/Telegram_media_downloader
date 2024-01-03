import os
from datetime import datetime as dt

from pyrogram import Client

import cfg


app = Client(
	name = 'user',
	api_id = cfg.API_ID,
	api_hash = cfg.API_HASH,
	phone_number = cfg.PHONE_NUMBER,
	# proxy = dict(scheme = 'socks5', hostname = cfg.HOST,port = cfg.PORT),
	# bot_token = cfg.BOT_TOKEN,
)
target = cfg.TARGET

PATH = os.path.dirname(os.path.abspath(__file__))+'/downloads/'

async def main():
	file_name = ''
	await app.start()
	async for msg in app.get_chat_history(target):
		try:
			if msg.photo and cfg.opts[1]=='photo':
				date = msg.photo.date
				file = 'photo_'+str(date)[:10]+'_'+msg.photo.file_unique_id+'.jpg'		
			elif msg.video and cfg.opts[2]=='video':
				date = msg.video.date
				file = 'video_'+str(date)[:10]+'_'+msg.video.file_unique_id+msg.video.file_name
			elif msg.document and cfg.opts[3]=='document':
				date = msg.document.date
				file = 'file_'+str(date)[:10]+'_'+msg.document.file_unique_id+msg.document.file_name
			
			if not os.path.exists(PATH+file):
				print(await app.download_media(msg,file_name=file))
		except Exception as e:
			# print(e)
			continue

app.run(main())
