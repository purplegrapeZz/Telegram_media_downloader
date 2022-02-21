### Overview:
Download photos and videos from a conversation or a channel that you are a member of from telegram.

### Support:
| Category             | Support                 |
| -------------------- | ----------------------- |
| Language             | `Python 3.6 ` and above |
| Download media types | photo, video, files     |

### Installation

For *nix os distributions with `make` availability
```sh
$ git clone https://github.com/purplegrapeZz/Telegram_media_downloader.git
$ cd Telegram_media_downloader
$ make install
```
For Windows which doesn't have `make` inbuilt 
```sh
$ git clone https://github.com/purplegrapeZz/Telegram_media_downloader.git
$ cd Telegram_media_downloader
$ pip3 install -r requirements.txt
```

## Configuration 

All the configurations are  passed to the Telegram Media Downloader via `cfg.py` file.

Proxy

`Socks5` proxy is supported in this project currently. To use it, simply config `cfg.py` file in the path of this project, and edit it with your proxy server info as follow:

```cfg.py
# cfg.py L11

# Proxy
HOST : str = '127.0.0.1'
PORT : int = 7890
```

API_ID && API_HASH

To use it, simply config `cfg.py` file in the path of this project, and edit it with your API_ID and API_HASH info as follow:

```cfg.py
# cfg.py L2

# Vist https://my.telegram.org/auth to get api_id & api_hash.
API_ID : int = 1234
API_HASH : str = 'your_hash'
```

PHONE_NUMBER

To use it, simply config `cfg.py` file in the path of this project, and edit it with your PHONE_NUMBER info as follow:

```cfg.py
# cfg.py L6

# Phone number of Telegram
PHONE_NUMBER : str = '86123456'
```

OPTIONS

To use it, simply config `cfg.py` file in the path of this project, and edit it with your options info as follow:

```cfg.py
# cfg.py L19

# Chose media type you what
opts = {
	1:'photo',	# Photos
	2:'video',	# Videos
	#3:'document'	# Files
}
```



**Getting your API Keys:**
The very first step requires you to obtain a valid Telegram API key (API id/hash pair):
1.  Visit  https://my.telegram.org/auth.
2.  Fill out the form to register a new Telegram application. 
3.  Done! The API key consists of two parts:  **api_id**  and  **api_hash**.


**Getting chat id:**

**1. Execucting  get_chat_id.py:**

You will get channels' name and id.

`$ python3 get_chat_id.py`

## Execution
```sh
$ python3 get_chat_id.py
$ python3 main.py
```