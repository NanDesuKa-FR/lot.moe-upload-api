import requests
import sys


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
        response = requests.post(self.api_url, files=self.get_data())
        return response.text


if __name__ == '__main__':
    file_path = sys.argv[sys.argv.index("-file") + 1]
    upload = UploadAPI("https://api.lot.moe/files", file_path)
    print(upload.make_request())
