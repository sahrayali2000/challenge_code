import cv2
import os
import shutil
from PIL import Image
from change_handler import change, change_and_crop


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


def crop(x1, y1):
    if not os.path.exists('cropped_2k'):
        os.makedirs('cropped_2k')
    if not os.path.exists('cropped_1080'):
        os.makedirs('cropped_1080')
    if not os.path.exists('cropped_720'):
        os.makedirs('cropped_720')
    crop_2k = change_and_crop('cropped_2k', 2048, x1, y1)
    crop_1080 = change_and_crop('cropped_1080', 1080, x1, y1)
    crop_720 = change_and_crop('cropped_720', 720, x1, y1)
    return crop_720, crop_1080, crop_2k



# collect_24_pics('sample.mp4')
# change_quality()
# crop(100, 150)

cv2.destroyAllWindows()

