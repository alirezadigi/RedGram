# 786
from requests import session
import json
from urllib.parse import quote_plus

class Bot:
    def __init__(self, token, proxies={}):
        self.token = token
        self.proxies = proxies
        self.session = session()        
        self.base_url = f'https://api.telegram.org/bot{self.token}/'

    def get_updates(self, offset=None):
        endpoint_url = self.base_url + 'GetUpdates'
        endpoint_data = {'offset': offset}
        req = self.session.get(
            endpoint_url, proxies=self.proxies, data=endpoint_data)
        return req.json()

    def get_updates_result(self, offset=None):
        raw_res = self.get_updates(offset=offset)
        #print(raw_res)
        return raw_res.get('result', [])

    def send_message(self, chat_id, text, keyboard=None):
                endpoint_url = self.base_url + 'SendMessage'
                endpoint_data = {'chat_id': str(chat_id), 'text': str(text)}
                if keyboard != None:
                    jsoned_keyboard = json.JSONEncoder().encode(keyboard)
                    endpoint_data.update({'reply_markup': jsoned_keyboard})

                req = self.session.get(
            endpoint_url, proxies=self.proxies, data=endpoint_data)
                return req.json()

    def delete_message(self, chat_id, message_id):
        endpoint_url = self.base_url + 'DeleteMessage'
        endpoint_data = {'chat_id': str(chat_id), 'message_id': str(message_id)}
        req = self.session.get(
            endpoint_url, proxies=self.proxies, data=endpoint_data)
        return req.json()

    def send_video(self, chat_id, video, caption=None, is_filename=False):
        endpoint_url = self.base_url + 'SendVideo'
        if is_filename == False:
            endpoint_data = {'chat_id': str(
                chat_id), 'video': video, 'caption': caption}
            req = self.session.get(
                endpoint_url, proxies=self.proxies, data=endpoint_data)
        else:
            endpoint_data = {'chat_id': str(chat_id), 'caption': caption}
            req_files = {'video': open(video, 'rb')}
            req = self.session.get(endpoint_url, proxies=self.proxies,
                                   data=endpoint_data, files=req_files)

        return req.json()

    def send_photo(self, chat_id, photo, caption=None, is_filename=False):
        endpoint_url = self.base_url + 'SendPhoto'
        if is_filename == False:
            endpoint_data = {'chat_id': str(
                chat_id), 'photo': photo, 'caption': caption}
            req = self.session.get(
                endpoint_url, proxies=self.proxies, data=endpoint_data)
        else:
            endpoint_data = {'chat_id': str(chat_id), 'caption': caption}
            req_files = {'photo': open(photo, 'rb')}
            req = self.session.get(endpoint_url, proxies=self.proxies,
                                   data=endpoint_data, files=req_files)

        return req.json()

    def send_animation(self, chat_id, animation, caption=None, is_filename=False):
        endpoint_url = self.base_url + 'SendAnimation'
        if is_filename == False:
            endpoint_data = {'chat_id': str(
                chat_id), 'animation': animation, 'caption': caption}
            req = self.session.get(
                endpoint_url, proxies=self.proxies, data=endpoint_data)
        else:
            endpoint_data = {'chat_id': str(chat_id), 'caption': caption}
            req_files = {'animation': open(animation, 'rb')}
            req = self.session.get(endpoint_url, proxies=self.proxies,
                                   data=endpoint_data, files=req_files)

        return req.json()

    def send_voice(self, chat_id, voice, caption=None, is_filename=False):
        endpoint_url = self.base_url + 'SendVoice'
        if is_filename == False:
            endpoint_data = {'chat_id': str(
                chat_id), 'voice': voice, 'caption': caption}
            req = self.session.get(
                endpoint_url, proxies=self.proxies, data=endpoint_data)
        else:
            endpoint_data = {'chat_id': str(chat_id), 'caption': caption}
            req_files = {'voice': open(voice, 'rb')}
            req = self.session.get(endpoint_url, proxies=self.proxies,
                                   data=endpoint_data, files=req_files)

        return req.json()

    def send_audio(self, chat_id, audio, caption=None, is_filename=False):
        endpoint_url = self.base_url + 'SendAudio'
        if is_filename == False:
            endpoint_data = {'chat_id': str(
                chat_id), 'audio': audio, 'caption': caption}
            req = self.session.get(
                endpoint_url, proxies=self.proxies, data=endpoint_data)
        else:
            endpoint_data = {'chat_id': str(chat_id), 'caption': caption}
            req_files = {'audio': open(audio, 'rb')}
            req = self.session.get(endpoint_url, proxies=self.proxies,
                                   data=endpoint_data, files=req_files)

        return req.json()

    def send_sticker(self, chat_id, audio, caption=None, is_filename=False):
        endpoint_url = self.base_url + 'SendSticker'
        if is_filename == False:
            endpoint_data = {'chat_id': str(
                chat_id), 'audio': audio, 'caption': caption}
            req = self.session.get(
                endpoint_url, proxies=self.proxies, data=endpoint_data)
        else:
            endpoint_data = {'chat_id': str(chat_id), 'caption': caption}
            req_files = {'audio': open(audio, 'rb')}
            req = self.session.get(endpoint_url, proxies=self.proxies,
                                   data=endpoint_data, files=req_files)

        return req.json()

    def send_document(self, chat_id, document, caption=None, is_filename=False):
        endpoint_url = self.base_url + 'SendDocument'
        if is_filename == False:
            endpoint_data = {'chat_id': str(
                chat_id), 'document': document, 'caption': caption}
            req = self.session.get(
                endpoint_url, proxies=self.proxies, data=endpoint_data)
        else:
            endpoint_data = {'chat_id': str(chat_id), 'caption': caption}
            req_files = {'document': open(document, 'rb')}
            req = self.session.get(endpoint_url, proxies=self.proxies,
                                   data=endpoint_data, files=req_files)

        return req.json()

    def get_file_link(self, file_id):
        endpoint_url = self.base_url + 'GetFile'
        endpoint_data = {'file_id': str(file_id)}
        req = self.session.get(
            endpoint_url, proxies=self.proxies, data=endpoint_data)
        req_file = req.json().get('result', {}).get('file_path', None)
        if req_file == None:
            return ''
        else:
            return self.base_url + req_file

    def edit_keyboard(self, chat_id, message_id, keyboard=None):
        endpoint_url = self.base_url + "editMessageReplyMarkup"
        endpoint_data = {'chat_id': str(
            chat_id), "message_id": str(message_id)}
        if keyboard != None:
            jsoned_keyboard = json.JSONEncoder().encode(keyboard)
            endpoint_data.update({'reply_markup': jsoned_keyboard})

        req = self.session.get(
            endpoint_url, proxies=self.proxies, data=endpoint_data)
        return req.json()


    def edit_message(self, chat_id, message_id, text):
        endpoint_url = self.base_url + "editMessageText"
        endpoint_data = {'chat_id': str(chat_id), "message_id": str(
            message_id), 'text': str(text)}
        req = self.session.get(
            endpoint_url, proxies=self.proxies, data=endpoint_data)
        return req.json()


class Message:
    def __init__(self, message):
        self.message = message
        self.update_id = None
        self.message_id = None
        self.message_place = None
        self.chat_info = None
        self.from_info = None
        self.text = None
        self.photoes = None
        self.video = None
        self.audio = None
        self.sticker = None
        self.animation = None
        self.caption = None
        self.caption_entities = None
        self.is_vote = False
        self.is_callback = False
        self.is_channel_post = False
        self.is_edited = False
        self.deep_message = None
        self.callback_id = None
        self.callback_data = None
        self.from_id = None
        self.chat_id = None
        self.sender_chat = None
        self.sender_chat_id = None
        self.forward_from_chat = None
        self.forward_from_id = None
        self.reply_to_message = None
        self.date = None
        self.edit_date = None
        self.forward_sender_name = None
        self.forward_date = None
        self.forward_from_message_id = None
        self.author_signature = None

        self.get_update_id()
        self.get_deep_message()
        self.get_message_id()
        self.get_from_chat_info()
        self.get_text()
        self.get_caption()
        self.get_photoes()
        self.get_video()
        self.get_audio()
        self.get_animation()
        self.get_vote()
        self.get_sticker()
        self.get_callback()
        self.get_other_info()

    def get_update_id(self):
        try:
            self.update_id = self.message['update_id']
        except:
            pass

    def get_deep_message(self):
        self.message_place = 'group_or_pv_message'
        try:
            self.deep_message = self.message['message']
            return self.deep_message
        except:
            pass

        try:
            self.deep_message = self.message['callback_query']
            self.is_callback = True
            return self.deep_message
        except:
            pass

        try:
            self.deep_message = self.message['edited_message']
            self.is_edited = True
            return self.deep_message
        except:
            pass

        try:
            self.deep_message = self.message['channel_post']
            self.is_channel_post = True
            self.message_place = 'channel_post'
            return self.deep_message
        except:
            pass

        try:
            self.deep_message = self.message['edited_channel_post']
            self.is_channel_post = True
            self.is_edited = True
            self.message_place = 'channel_post'
            return self.deep_message
        except:
            pass

        try:
            self.deep_message = self.message['my_chat_member']
            return self.deep_message
        except:
            pass
        
        if self.deep_message == None:
            self.deep_message = {}
            
            
    def get_message_id(self):
        if self.is_callback:
            self.message_id = self.deep_message.get('message',{}).get('message_id')
        else:
            self.message_id = self.deep_message.get('message_id')
        self.forward_from_message_id = self.deep_message.get('forward_from_message_id',None)
        

    def get_from_chat_info(self):
        self.from_info = self.deep_message.get('from')      
        self.forward_from = self.deep_message.get('forward_from')
        self.forward_from_chat = self.deep_message.get('forward_from_chat')
        if self.is_callback:
            self.chat_info = self.deep_message.get('message',{}).get('chat')
        else:
            self.chat_info = self.deep_message.get('chat')
        self.sender_chat_info = self.deep_message.get('sender_chat')
        try:
            self.chat_id = self.chat_info.get('id')
        except:
            pass
        try:
            self.forward_from_id = self.forward_from.get('id')
        except:
            pass
        try:
            self.from_id = self.from_info.get('id')
        except:
            pass
        try:
            self.sender_chat_id =  self.sender_chat_info.get('id')
        except:
            pass
        try:
            self.forward_from_chat_id = self.forward_from_chat.get('id')
        except:
            pass

    def get_text(self):
        self.text = self.deep_message.get('text',None)
        
    def get_caption(self):
        self.caption = self.deep_message.get('caption',None)
        self.caption_entities = self.deep_message.get('caption_entities',None)
        
    def get_photoes(self):
        self.photoes = self.deep_message.get('photo',None)
            
    def get_video(self):
        self.video = self.deep_message.get('video',None)
   
    def get_audio(self):
        self.audio = self.deep_message.get('audio',None)

    def get_sticker(self):
        self.video = self.deep_message.get('sticker',None)

    def get_animation(self):
        self.animation = self.deep_message.get('animation',None)

    def get_vote(self):
        self.vote = self.deep_message.get('poll',None)
        if self.vote != None:
            self.is_vote = True
    
    def get_callback(self):
        self.callback_id = self.deep_message.get('id',None)
        self.callback_data = self.deep_message.get('data',None)
    
    def get_other_info(self):
        self.date = self.deep_message.get('date',None)
        self.edit_date = self.deep_message.get('edit_date',None)
        self.forward_date = self.deep_message.get('forward_date',None)
        self.forward_sender_name = self.deep_message.get('forward_sender_name',None)
        self.author_signature = self.deep_message.get('author_signature',None)
        self.reply_to_message = self.deep_message.get('reply_to_message',None)
