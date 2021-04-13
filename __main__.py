import requests
import sys

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json',
    'Cache-Control': 'no-cache',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Sec-GPC': '1',
    'Origin': 'https://lot.moe',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://lot.moe/',
    'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'dnt': '1',
}



class UploadAPI:
    def __init__(self, api_url, file_path):
        """

        :param api_url:
        :param file_path:
        """
        self.api_url = api_url
        self.file_path = file_path

    def get_data(self):
        byte_file = open(self.file_path, "rb")
        return_data = {'file[]': byte_file}
        return return_data

    def make_request(self):
        response = requests.post(self.api_url, headers=headers, files=self.get_data())
        return response.text


if __name__ == '__main__':
    file_path = sys.argv[sys.argv.index("-file") + 1]
    upload = UploadAPI("https://api.lot.moe/files", file_path)
    print(upload.make_request())