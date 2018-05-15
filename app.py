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
    if event.message.text == "Hadiah":
        lk1 = ['obat nyamuk','istimewa','yah dapet zonk','duit mini']
        kk1 = random.choice(lk1)
        buttons_template = TemplateSendMessage(
            alt_text='Hadiah Kejutan',
            template=ButtonsTemplate(
                title='Hadiah Kejutan',
                text='Ayo buka kejutanmu!!!',
                thumbnail_image_url='https://imgur.com/CVpvIdt.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Buka Sekarang!!',
                        text=kk1
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "Kontak Pgrs":    
        carousel_template_message = TemplateSendMessage(
            alt_text='Kontak Pengurus',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://imgur.com/cUO27Yd.jpg',
                        title='Kontak Pengurus',
                        text='Pilih salah satu',
                        actions=[
                            MessageTemplateAction(
                                label='Leader',
                                text='Leader ori'
                            ),
                            MessageTemplateAction(
                                label='Colead',
                                text='Colead ori'
                            ),
                            MessageTemplateAction(
                                label='Admin',
                                text='Admin ori'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://imgur.com/23TcxK5.jpg',
                        title='Kontak Pengurus',
                        text='Pilih salah satu',
                        actions=[
                            MessageTemplateAction(
                                label='Penasehat',
                                text='Penasehat ori'
                            ),
                            MessageTemplateAction(
                                label='Staff',
                                text='Staff ori'
                            ),
                            MessageTemplateAction(
                                label='Emak',
                                text='Emak ori'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, carousel_template_message)
        return 0
    if event.message.text == "About bot":
        buttons_template = TemplateSendMessage(
            alt_text='About ORI Bot',
            template=ButtonsTemplate(
                title='About ORI Bot',
                text='Pilih salah satu menu dibawah ini',
                thumbnail_image_url='https://imgur.com/qNOi0Qu.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Developer',
                        text='Bot developer'
                    ),
                    MessageTemplateAction(
                        label='Version',
                        text='Version'
                    ),
                    MessageTemplateAction(
                        label='Info ORI Bot',
                        text='Info bot'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "Key":
        buttons_template = TemplateSendMessage(
            alt_text='Key ØRI',
            template=ButtonsTemplate(
                title='Key ØRI',
                text='Pilih salah satu menu dibawah ini',
                thumbnail_image_url='https://imgur.com/CVpvIdt.jpg',
                actions=[
                    MessageTemplateAction(
                        label='About ORI',
                        text='ORI grup'
                    ),
                    MessageTemplateAction(
                        label='More Keyword',
                        text='Help'
                    ),
                    MessageTemplateAction(
                        label='About ORI Bot',
                        text='About bot'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "ORI grup":
        buttons_template = TemplateSendMessage(
            alt_text='About ORI',
            template=ButtonsTemplate(
                title='About ORI',
                text='Pilih salah satu menu dibawah ini',
                thumbnail_image_url='https://imgur.com/vNZlfOA.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Pengurus',
                        text='Pengurus'
                    ),
                    MessageTemplateAction(
                        label='Rules',
                        text='Rules'
                    ),
                    URITemplateAction(
                        label='Guild',
                        uri='http://line.me/R/home/public/post?id=wnq1836k&postId=1151441933104021159'
                    ),
                    URITemplateAction(
                        label='Filosofi',
                        uri='http://line.me/R/home/public/post?id=wnq1836k&postId=1152422979304029812'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "Pengurus":
        buttons_template = TemplateSendMessage(
            alt_text='Pengurus ØRI',
            template=ButtonsTemplate(
                title='Pengurus ØRI',
                text='Mau lihat pengurus lewat apa?',
                thumbnail_image_url='https://imgur.com/ea72IkU.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Kontak',
                        text='Kontak Pgrs'
                    ),
                    URITemplateAction(
                        label='Gambar',
                        uri='http://line.me/R/home/public/post?id=wnq1836k&postId=1151442178104024988'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "Rules":
        buttons_template = TemplateSendMessage(
            alt_text='Rules ØRI',
            template=ButtonsTemplate(
                title='Rules ØRI',
                text='Dalam versi apa?',
                thumbnail_image_url='https://imgur.com/8udTsks.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Teks',
                        text='Rules full'
                    ),
                    URITemplateAction(
                        label='Gambar',
                        uri='http://line.me/R/home/public/post?id=wnq1836k&postId=1151442807704026737'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
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
