from PIL import Image
import numpy as np
from draw import draw

def generate_art(filename, out):
    try:
        im = Image.open(filename)
    except FileNotFoundError as e:
        print(e)
        print('Cannot load image!')
        return
    asc = '`^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
    im.thumbnail((300, 300))
    img_arr = np.array(im)

    avg_arr = [[y if np.isscalar(y) else 0.2126*y[0] + 0.7152*y[1] + 0.0722*y[2] for y in x] for x in img_arr]

    art = [[asc[int(y / 255 * 64)] * 2 for y in x] for x in avg_arr]

    draw([''.join(x) for x in art], out)
