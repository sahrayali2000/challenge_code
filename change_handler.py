from PIL import Image
import shutil


def change(pics_dir, resolution):
    for pic in range(1, 25):
        pic_name = f'pic_{pic}.jpg'
        image = Image.open(f'pics/{pic_name}')
        pic_height = resolution / 2
        new_image = image.resize((int(resolution), int(pic_height)))
        new_image.save(f'./{pics_dir}/{resolution}_{pic}.jpg')
    zip_file = shutil.make_archive(f'{resolution}_pics', 'zip', f'{pics_dir}')
    return zip_file


def change_and_crop(pics_dir, resolution, x1, y1):
    for pic in range(1, 25):
        pic_name = f'pic_{pic}.jpg'
        image = Image.open(f'pics/{pic_name}')
        width, height = image.size
        left = y1
        top = 0
        right = width - x1
        bottom = height - y1
        image = image.crop((left, top, right, bottom))
        pic_height = resolution / 2
        new_image = image.resize((int(resolution), int(pic_height)))
        new_image.save(f'./{pics_dir}/{resolution}_{pic}.jpg')
    zip_file = shutil.make_archive(f'{resolution}_cropped_pics', 'zip', f'{pics_dir}')
    return zip_file

