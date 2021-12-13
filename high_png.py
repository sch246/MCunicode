import os
from PIL import Image


def file_expand_pic(file,font_height):
    img = Image.open(file)
    w, h = img.size
    line_count = int(h/font_height)
    to_img = Image.new(mode='RGBA',size=(w,line_count*256))
    for line in range(line_count):
        to_img.paste(img.crop(box=(0, font_height*line, w, font_height*(line+1))),
                     (0, 256*line))
    to_img.save(file)



for root, dirs, files in os.walk(r'textures\font_plus'):
    for name in files:
        file_path = os.path.join(root, name)
        if 'unicode_page_' in name:
            file_expand_pic(file_path,16)
        elif name == 'accented.png':
            file_expand_pic(file_path, 12)
        else:
            file_expand_pic(file_path, 8)
