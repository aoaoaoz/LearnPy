# -*- coding: utf-8 -*-

' a test module '
__author__ = 'aoaoao'

from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random

def randChar():
    return chr(random.randint(0, 26)+ord('a'))

def randColor1():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def randColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60 * 4
height = 60
img = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)
img.show()
draw = ImageDraw.Draw(img)
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill = randColor1())

for t in range(4):
    draw.text((60*t+10, 10), randChar(), font = font, fill = randColor2())
img = img.filter(ImageFilter.BLUR)
img.show()
img.save('code.jpg', 'jpeg')