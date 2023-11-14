# python3 -m venv PIXELART
# source PIXELART/bin/activate
# pip install --upgrade pip

# https://www.pixilart.com/gallery

# https://ru.stackoverflow.com/questions/807259/%D0%9A%D0%B0%D0%BA-%D1%81%D0%B4%D0%B5%D0%BB%D0%B0%D1%82%D1%8C-%D0%BF%D0%B8%D0%BA%D1%81%D0%B5%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8E-%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D1%83%D1%8F-%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C-pil
# pip install Pillow


# deactivate


from PIL import Image


def pixelate(image, pixel_size=9, draw_margin=True):
    margin_color = (0, 0, 0)

    image = image.resize((image.size[0] // pixel_size, image.size[1] // pixel_size), Image.NEAREST)
    image = image.resize((image.size[0] * pixel_size, image.size[1] * pixel_size), Image.NEAREST)
    pixel = image.load()

    # Draw black margin between pixels
    if draw_margin:
        for i in range(0, image.size[0], pixel_size):
            for j in range(0, image.size[1], pixel_size):
                for r in range(pixel_size):
                    pixel[i+r, j] = margin_color
                    pixel[i, j+r] = margin_color

    return image

image_name = '14.jpg'

import time
start_time = time.time()

image = Image.open(f'image/{image_name}').convert('RGB')

# image_pixelate = pixelate(image)
image_pixelate = pixelate(image, pixel_size=16)
image_pixelate.save(f'image/{image_name[:-4]}_output.jpg')

# for size in (16, 32, 48):
#     image_pixelate = pixelate(image, pixel_size=size)
#     image_pixelate.save('image/{}_output_{}.jpg'.format(image_name[:-4],size))

print("--- %s seconds ---" % (time.time() - start_time))