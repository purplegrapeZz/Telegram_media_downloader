from pyrogram import Client

import cfg


app = Client(
	name = 'user',
	api_id = cfg.API_ID,
	api_hash = cfg.API_HASH,
	phone_number = cfg.PHONE_NUMBER,
	# proxy = dict(scheme = 'socks5', hostname = cfg.HOST, port = cfg.PORT),
	# bot_token = cfg.BOT_TOKEN,
)
async def main():
	await app.start()
	async for dialog in app.iter_dialogs():
		print((dialog.chat.first_name+' '+dialog.chat.last_name if dialog.chat.last_name else dialog.chat.first_name)or dialog.chat.title, dialog.chat.id)

app.run(main())
