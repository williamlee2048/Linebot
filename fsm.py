from transitions.extensions import GraphMachine
import os
from utils import send_text_message
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
import message

name = []
content = []
count = 0

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "menu"

    def is_going_to_GA_menu(self, event):
        text = event.message.text
        return text.lower() == "先不要"

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "go to state1"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"

    def is_going_to_wordcard(self, event):
        text = event.message.text
        return text == "wordcard"

    def is_going_to_wordsave(self, event):
        text = event.message.text
        return text == "wordsave_activate"

    def is_going_to_saving(self, event):
        text = event.message.text
        return text != ""

    def is_going_to_def(self, event):
        text = event.message.text
        return text != ""

    def next_word(self, event):
        text = event.message.text
        return text == "next"

    def end_of_saving(self, event):
        text = event.message.text
        return text != "next"
        
    def list_showing(self, event):
        text = event.message.text
        return text == "wordlist"

    def on_enter_menu(self, event):
        id = event.source.user_id
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        message_packet = message.main_menu
        reply_message = FlexSendMessage("主選單", message_packet)
        line_bot_api.push_message(id, reply_message)

    def on_enter_GA_menu(self, event):
        id = event.source.user_id
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        message_packet = message.GA_menu
        reply_message = FlexSendMessage("主選單", message_packet)
        line_bot_api.push_message(id, reply_message)


    def on_enter_state1(self, event):
        id = event.source.user_id
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(id, TextSendMessage(text="目前的State : State1"))
        line_bot_api.push_message(id, TextSendMessage(text="輸入menu 可以進到menu"))


    def on_enter_state2(self, event):
        id = event.source.user_id
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        message_packet = message.test_package
        reply_message = FlexSendMessage("主選單", message_packet)
        line_bot_api.push_message(id, reply_message)

    def on_enter_wordcard(self, event):
        id = event.source.user_id
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        message_packet = message.wordcard_interface
        reply_message = FlexSendMessage("主選單", message_packet)
        line_bot_api.push_message(id, reply_message)

    def on_enter_wordsave(self, event):
        id = event.source.user_id
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(id, TextSendMessage(text="開始單字卡紀錄"))
        line_bot_api.push_message(id, TextSendMessage(text="輸入一個單字"))

    def on_enter_saving(self, event):
        global count
        id = event.source.user_id
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        print("user : ",event.message.text)
        name.append(event.message.text)
        line_bot_api.push_message(id, TextSendMessage(text="儲存單字 = " + event.message.text))
        line_bot_api.push_message(id, TextSendMessage(text="輸入定義"))

    def on_enter_saving2(self, event):
        id = event.source.user_id
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        print("user2 : ",event.message.text)
        content.append(event.message.text)
        line_bot_api.push_message(id, TextSendMessage(text="儲存定義 = " + event.message.text))
        line_bot_api.push_message(id, TextSendMessage(text="輸入 next 來存下個字"))
        line_bot_api.push_message(id, TextSendMessage(text="隨意輸入已結束單字儲存"))

    def on_enter_saving_end(self, event):
        id = event.source.user_id
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        message_packet = message.Saving_End
        reply_message = FlexSendMessage("主選單", message_packet)
        line_bot_api.push_message(id, reply_message)

    def on_enter_list_show(self, event):
        id = event.source.user_id
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(id, TextSendMessage(text="單字表 : "))
        for i in range(len(name)):
            line_bot_api.push_message(id, TextSendMessage(text="WORD : " +name[i]))
            line_bot_api.push_message(id, TextSendMessage(text="DEF : \t"+content[i]))