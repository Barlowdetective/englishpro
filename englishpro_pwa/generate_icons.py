from PIL import Image, ImageDraw, ImageFont
import os

sizes = [192, 512]
os.makedirs('icons', exist_ok=True)

for size in sizes:
    img = Image.new('RGB', (size, size), color='#2d5a3d')
    draw = ImageDraw.Draw(img)

    # Background circle / rounded feel via border
    margin = size * 0.08
    draw.rounded_rectangle(
        [margin, margin, size - margin, size - margin],
        radius=size * 0.22,
        fill='#3d7a55'
    )

    # Letter "E" large, centered
    font_size = int(size * 0.52)
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf', font_size)
    except:
        font = ImageFont.load_default()

    text = 'E'
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = (size - tw) / 2 - bbox[0]
    y = (size - th) / 2 - bbox[1] - size * 0.03
    draw.text((x, y), text, fill='#faf9f5', font=font)

    # Small "Pro" label
    try:
        small_font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', int(size * 0.13))
    except:
        small_font = ImageFont.load_default()
    label = 'Pro'
    lb = draw.textbbox((0, 0), label, font=small_font)
    lw = lb[2] - lb[0]
    draw.text(((size - lw) / 2, size * 0.72), label, fill='#a8d5b5', font=small_font)

    img.save(f'icons/icon-{size}.png')
    print(f'Generated icon-{size}.png')

print('Done.')
