from numpy import isscalar
from PIL import Image, ImageDraw


def draw(art, im, out, color):
    img = Image.new("RGB", (1, 1))
    d = ImageDraw.Draw(img)
    char_width, char_height = d.textsize(art[0][0][0])
    char_height = char_width * 2
    img = Image.new(
        "RGB", (char_width * len(art[0][0]) * len(art[0]), char_height * len(art))
    )
    d = ImageDraw.Draw(img)

    for i, strings in enumerate(art):
        for j, string in enumerate(strings):
            r, g, b = 255, 255, 255
            if color:
                r, g, b = (
                    (im[i, j], im[i, j], im[i, j]) if isscalar(im[i, j]) else im[i, j]
                )
            d.text((j * char_width * 2, i * char_height), string, fill=(r, g, b))

    img.save(out)
