import os
import shutil
from PIL import Image

src = r'C:\Users\lich\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'

dst = r"C:\Users\lich\YandexDisk\Картинки\Windows Spotlight"

for item in os.listdir(src):
    s = os.path.join(src, item)
    try:
        img = Image.open(s)
        width, height = img.size
        if width >= 1920:
            d = os.path.join(dst, item+'.jpg')
            print('Копируем файл', d)
            shutil.copyfile(s, d)
    except OSError as ose:
        print(ose)
