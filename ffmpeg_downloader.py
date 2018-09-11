
from urllib.request import urlopen, Request
import zipfile
import shutil
import os

reg_url = "https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-20180909-404d21f-win64-static.zip"
file_name = "ffmpeg-20180909-404d21f-win64-static.zip"
original_directory_name = "ffmpeg-20180909-404d21f-win64-static"
desired_directory_name = "ffmpeg"
headers = {'User-Agent': 'Mozilla/5.0'}


def download_ffmpeg():
    req = Request(url=reg_url, headers=headers)

    with urlopen(req) as response, open(file_name, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

    zip_ref = zipfile.ZipFile(file_name, 'r')
    zip_ref.extractall()
    zip_ref.close()

    os.rename(original_directory_name, desired_directory_name)
    os.remove(file_name)


if __name__ == '__main__':
    print('do nothing...')
