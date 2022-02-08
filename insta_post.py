from instagrapi import Client
import os
# from flask import Flask
#
# app = Flask(__name__)
#
# # image = 'scale_1200.jpg'
# # text = 'some test text'
#
# HOST = '0.0.0.0'
# PORT = 5500

# REMOVE = 'C:/Users/Mike/PycharmProjects/bot_testing/config/log/test_digitalinform_uuid_and_cookie.json'

# @app.route('/<message>/<photo>')
def insta_post(message, photos):
    # bot = Bot()
    # os.remove(REMOVE)

    # photo = '/photos/' + photo

    username = 'test_digitalinform'
    password = 'dinform2207'
    # bot.login(username=username, password=password, is_threaded=True)
    # for photo in photos:
    #     print(photo)
    #     bot.upload_photo(photo, message)
    # bot.logout()



    bot = Client()
    bot.login(username, password)
    bot.album_upload(
        photos,
        caption=message
    )
