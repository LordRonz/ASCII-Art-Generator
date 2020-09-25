from PIL import Image
import numpy


def main():
    try:
        im = Image.open("CS50_cat.jpg")
    except:
        print("Cannot load image!")
        return
    asc = '`^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
    im.thumbnail((300, 300))
    img_arr = numpy.array(im)
    # print(img_arr)
    avg_arr = [[numpy.average(y) for y in x] for x in img_arr]
    art = [[asc[int(y / 255 * 64)] * 3 for y in x] for x in avg_arr]
    for x in art:
        print("".join(x))
    #print(im.size)
    # print(avg_arr)


if __name__ == "__main__":
    main()
