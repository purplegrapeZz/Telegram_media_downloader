# Vist https://my.telegram.org/auth to get api_id & api_hash.
API_ID : int = 1234
API_HASH : str = 'your_hash'

# Phone number of Telegram
PHONE_NUMBER : str = '86123456'

# Telegram bot_token
BOT_TOKEN : str = 'your_token'

# Proxy
HOST : str = '127.0.0.1'
PORT : int = 7890

# Chat_id
TARGET : int = -100123456	# Exec "python3 get_chat_id.py" to get the chat_id.

# Chose media type you what
opts = {
	1:'photo',	# Photos
	2:'video',	# Videos
	3:'document'	# Files
}