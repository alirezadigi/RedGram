# RedGram
A Simple yet Powerfull TelegramBotApi Lib!

# Installation
- By Pip
```bash
pip3 install redgram
```


# Usage
```python
from redgram import RedGram as rg

TOKEN = 'PUT YOUR TOKEN HERE'

bot = rg.Bot(TOKEN)

messages = bot.get_updates_result()
if messages != []:
    print('New Messages!')
    for message in messages:
        message_obj = rg.Message(message)
        print('From',message_obj.from_id)
        print('==>',message_obj.text)
 else:
     print('No Messages Yet!')
 ```
 
 
 
## Available Methods for Message Obj
- update_id
- message_id
- message_place
- chat_info
- from_info
- text
- photoes
- video
- audio
- sticker
- animation
- caption
- caption_entities
- is_vote
- is_callback
- is_channel_post
- is_edited
- callback_id
- callback_data
- from_id
- chat_id
- sender_chat
- sender_chat_id
- forward_from_chat
- forward_from_id
- reply_to_message
- date
- edit_date
- forward_sender_name
- forward_date
- forward_from_message_id
- author_signature
