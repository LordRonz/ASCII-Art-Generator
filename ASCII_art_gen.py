from PIL import Image
import numpy as np


def main():
    try:
        im = Image.open("CS50_cat.jpg")
    except:
        print("Cannot load image!")
        return
    asc = '`^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
    im.thumbnail((300, 300))
    img_arr = np.array(im)
    # print(img_arr)
    npav = np.average
    avg_arr = [[npav(y) for y in x] for x in img_arr]
    art = [[asc[int(y / 255 * 64)] * 3 for y in x] for x in avg_arr]
    print("\n".join(["".join(x) for x in art]))


if __name__ == "__main__":
    main()
