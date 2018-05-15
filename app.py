import requests
import re
import random
import configparser
from bs4 import BeautifulSoup
from flask import Flask, request, abort
from imgurpython import ImgurClient

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)
config = configparser.ConfigParser()
config.read("config.ini")

line_bot_api = LineBotApi(config['line_bot']['Channel_Access_Token'])
handler = WebhookHandler(config['line_bot']['Channel_Secret'])
client_id = config['imgur_api']['Client_ID']
client_secret = config['imgur_api']['Client_Secret']
album_id = config['imgur_api']['Album_ID']
API_Get_Image = config['other_api']['API_Get_Image']


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # print("body:",body)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'ok'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("event.reply_token:", event.reply_token)
    print("event.message.text:", event.message.text)
    if event.message.text == "Jones":
        quote = ('Udah takdir itu mah...','Yang barusan ngetik itu orangnya...')
        jwbn = random.choice(quote)
        text_message = TextSendMessage(text=jwbn)
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif "/lr" in event.message.text:
        text_message = TextSendMessage(text='Gak ada po disini\nLewat personal chat aja ya...\nNih kontaknya\nhttp://line.me/R/ti/p/~@qik6373h\nhttp://line.me/R/ti/p/~@qik6373h')
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif event.message.text in ['obat nyamuk','very istimewa','yah dapet zonk','duit mini']:
        text_message = TextSendMessage(text='Ayo coba lagi kak. ketik Hadiah')
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    if event.message.text == "Event":
        imagemap_message = ImagemapSendMessage(
            base_url='https://imgur.com/TSk3Wrq.jpg',
            alt_text='Event LR Hari ini',
            base_size=BaseSize(height=1040, width=1040),
            actions=[
                MessageImagemapAction(
                    text='Dibaca ya bukan di klik gambarnya',
                    area=ImagemapArea(
                        x=1, y=0, width=10, height=10
                    )
                )
            ]
        )
        line_bot_api.reply_message(event.reply_token, imagemap_message)
        return 0
    if event.message.text == "Wexm":
        buttons_template = TemplateSendMessage(
            alt_text='Isi data diri',
            template=ButtonsTemplate(
                title='isi formnya ya. diberi wkt 1x24 jam',
                text='lewat dari wkt yg di tentukan akan di kick',
                thumbnail_image_url='https://imgur.com/CVpvIdt.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Dapatkan form',
                        text='Minta form dong min...'
                    ),
                    MessageTemplateAction(
                        label='Baca juga rulesnya',
                        text='Rules'
                    ),
                    MessageTemplateAction(
                        label='Keyword ORI',
                        text='Key'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0


if __name__ == '__main__':
    app.run()
