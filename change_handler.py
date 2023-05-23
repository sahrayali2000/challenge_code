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
