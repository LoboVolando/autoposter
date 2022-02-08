import random
import threading
import time

import vk_post
import insta_post
import os
import shutil
import requests
flags = dict()


def karamba(flag: int, message: str):
    if flag == 1:
        flags['message'] = message
        print('Message added')
        print(flags)
    elif flag == 2:
        if 'photo' not in flags:
            flags['photo'] = [message]
        else:
            flags['photo'].append(message)
            print('Photo added')
            print(flags)
    elif flag == 3:
        if 'message' in flags and 'photo' in flags:
            flags['Post'] = message
            print(flags)
        else:
            print(flags)
            print('Nothing added')
            return 'Message of photo(s) are missing'

    if 'message' in flags and 'photo' in flags and 'Post' in flags:
        print(flags['message'])
        print(flags['photo'])
        vk_post.vk_post(flags['message'], flags['photo'])
        # requests.get(f'https://0.0.0.0/{flags["message"]}/{flags["photo"]}')

        shutil.rmtree('config', ignore_errors=True)
        insta_post.insta_post(flags['message'], flags['photo'])
        time.sleep(3)

        shutil.rmtree('photos', ignore_errors=True)
        time.sleep(2)
        os.mkdir('photos')
        flags.clear()

        return 'Successfully posted'

    return 'Yeah'
