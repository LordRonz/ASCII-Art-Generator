import numpy as np
from PIL import Image

from draw import draw


def generate_art(filename, out, color: bool):
    try:
        im = Image.open(filename).convert("RGB")
    except FileNotFoundError as e:
        print(e)
        print("Cannot load image!")
        return
    # asc = '`^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
    asc = " .'`^\",:;Il!i><~+_-?][}{1)(|\\ tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    im.thumbnail((300, 300))
    img_arr = np.array(im)

    avg_arr = [
        [
            y if np.isscalar(y) else 0.2126 * y[0] + 0.7152 * y[1] + 0.0722 * y[2]
            for y in x
        ]
        for x in img_arr
    ]

    asc_sz = len(asc) - 1

    art = [[asc[int(y / 255 * asc_sz)] * 2 for y in x] for x in avg_arr]

    draw(art, img_arr, out, color)
