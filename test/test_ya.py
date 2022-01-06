import requests

class TestYandex:

    def setup(self):
        self.token = ''
        self.headers = {'Authorization': f'OAuth {self.token}'}
        self.dir_name =  'test1'


    def teardown(self):
        requests.delete(url=f'https://cloud-api.yandex.net/v1/disk/resources/?path={self.dir_name}', headers=self.headers)


    def test_new_folder(self):
        new_folder = requests.put(url=f'https://cloud-api.yandex.net/v1/disk/resources/?path={self.dir_name}', headers=self.headers)
        assert new_folder.status_code == 201, new_folder.json()["message"] 
