from PIL import Image, ImageDraw

def draw(strings, out):
    img = Image.new('RGB', (1, 1))
    d = ImageDraw.Draw(img)
    char_width, char_height = d.textsize(strings[0][0])
    char_height = char_width * 2
    img = Image.new('RGB', (char_width * len(strings[0]), char_height * len(strings)))
    d = ImageDraw.Draw(img)

    for i, string in enumerate(strings):
        d.text((0, i * char_height), string, fill=(255, 255, 255))

    img.save(out)
