import requests
import vk_api
import json

ID = 695209325
ALBUM = 695209325
CLUB = 209756961
PUBLIC = '-209775360'
# token = '6b8f5c1f861924ba371585ae015ca09019be637c60ebb42fe337978232038816e4e0fa575f1d2118a6611'
token = 'c45e0773983a2b9244060414b38bd608c7168895fe87b59b6e80a5614942c41d79752ae026ed39e54789d'
vk_session = vk_api.VkApi('+79522252644', 'Qerk121212$', token)
vk_session.auth()

ses = vk_session.get_api()
upload = vk_api.VkUpload(vk_session)
# result = upload.photo_profile(photo='photos/file_0.jpg', owner_id=CLUB)
# upload.photo_wall(photos='photos/file_0.jpg', group_id=CLUB, caption='Guilty')
# upload.photo(photos='photots/file_13.jpg', album_id=695209325)
# upload.photo_cover(photo='photots/file_13.jpg', group_id=CLUB, crop_x=795, crop_y=795, crop_x2=1000, crop_y2=1000)
# upload.photo_market_album(photo='photots/file_13.jpg', group_id=CLUB)
vk = vk_session.get_api()


# print(result)


def vk_post(message, photos):
    attachments = []
    for photo in photos:
        img = {'photo': (photo, open(f'{photo}', 'rb'))}

        upload_url = vk.photos.getWallUploadServer(access_token=token)['upload_url']
        print(upload_url)

        response = requests.post(upload_url, files=img)
        result = json.loads(response.text)
        save_photo = vk.photos.saveWallPhoto(access_token=token, photo=result['photo'], hash=result['hash'], server=result['server'])
        result = save_photo[0]
        print(result)
    # attachments = 'photo' + str(CLUB[1:]) + '_' + str(result['id']) + ', ' + str(result['sizes'][4]['url'])
        attachments.append('photo' + str(result['owner_id']) + '_' + str(result['id']))
        print(attachments)
    # attachments = 'https://vk.com/photo695209325_457239151'

    result = vk.wall.post(access_token=token, owner_id=-CLUB, from_group=1, message=message, attachments=attachments)
    print(result)

# vk_post('Hello', 'file_24.jpg')
