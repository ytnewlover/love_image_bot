from PIL import Image, ImageDraw, ImageFont

def generate_love_image(name1, name2, output_path="love_output.jpg"):
    img = Image.new("RGB", (800, 400), color=(255, 192, 203))  # pink bg
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("arial.ttf", 40)  # आप कोई Hindi font भी दे सकते हैं

    text = f"{name1} ❤️ {name2}"
    w, h = draw.textsize(text, font=font)
    draw.text(((800-w)/2, (400-h)/2), text, fill="black", font=font)

    img.save(output_path)
    return output_path
