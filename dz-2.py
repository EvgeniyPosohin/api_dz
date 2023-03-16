import requests
import os


class YandexD:

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json',
                'Authorization': 'OAuth {}'.format(self.token)}

    def get_href(self, path_f):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': path_f, 'overwrite': 'true'}
        response = requests.get(url, headers=self.get_headers(), params=params)
        return response.json()['href']

    def upload_file(self, file_name):
        href = self.get_href('test/{}'.format(file_name))
        current = os.getcwd()
        full_path = os.path.join(current, file_name)
        with open(full_path, 'rb') as file:
            response = requests.put(href, file)
            if response.status_code == 201:
                print('успешно')


ya_d_upload = YandexD('ваш токен')
ya_d_upload.upload_file('1.txt')
