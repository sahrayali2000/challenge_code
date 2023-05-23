import cv2
import os
import shutil
from PIL import Image
from change_handler import change


def collect_24_pics(video_path):

    video = cv2.VideoCapture(video_path)
    if not os.path.exists('pics'):
        os.makedirs('pics')
    for frame in range(1, 25):
        result, pic = video.read()
        if result:
            pic_name = f'./pics/pic_{frame}.jpg'
            cv2.imwrite(pic_name, pic)
    video.release()
    return shutil.make_archive('pics', 'zip', 'pics')


def change_quality():
    if not os.path.exists('2k_pics'):
        os.makedirs('2k_pics')
    if not os.path.exists('1080_pics'):
        os.makedirs('1080_pics')
    if not os.path.exists('720_pics'):
        os.makedirs('720_pics')

    pics_2k = change('2k_pics', 2048)
    pics_1080 = change('1080_pics', 1080)
    pics_720 = change('720_pics', 720)

    return pics_720, pics_1080, pics_2k


def crop(pic_path, x1, y1):
    if not os.path.exists('cropped'):
        os.makedirs('cropped')
    image = Image.open(pic_path)
    width, height = image.size
    left = y1
    top = 0
    right = width - x1
    bottom = height - y1
    image = image.crop((left, top, right, bottom))
    image_2k = image.resize((2048, 1080))
    image_2k.save('./cropped/2k_cropped.jpg')
    image_1080 = image.resize((1080, 720))
    image_1080.save('./cropped/1080_cropped.jpg')
    image_720 = image.resize((20, 480))
    image_720.save('./cropped/720_cropped.jpg')

    return shutil.make_archive('cropped', 'zip', 'cropped')


# collect_24_pics('sample.mp4')
# change_quality()
# crop('./pics/pic_1.jpg', 100, 150)

cv2.destroyAllWindows()

