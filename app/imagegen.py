from PIL import Image, ImageDraw, ImageColor
from app import prime

def medium(a, b):
    return (a+b)/2

def mabs(n):
    if n<0:
        return n * -1
    else:
        return n

def loop360(n):
    if n > 360:
        n = n%360
    if n == 1:
        n = 0
    return n

def drawCorners(im):
    width, height = im.size
    draw = ImageDraw.Draw(im)
    rgb_im = im.convert('RGB')
    for y in range(1, height-1):
        for x in range(1, width-1):
            if rgb_im.getpixel((x, y)) != (0, 0, 0):
                if (rgb_im.getpixel((x-1, y-1)) != (0, 0, 0) and rgb_im.getpixel((x+1, y+1)) != (0, 0, 0)) \
                    or (rgb_im.getpixel((x-1, y+1)) != (0, 0, 0) and rgb_im.getpixel((x+1, y-1)) != (0, 0, 0)) \
                    or (rgb_im.getpixel((x-1, y)) != (0, 0, 0) and rgb_im.getpixel((x+1, y)) != (0, 0, 0)) \
                    or (rgb_im.getpixel((x, y-1)) != (0, 0, 0) and rgb_im.getpixel((x, y+1)) != (0, 0, 0)):
                    continue
                else:
                    draw.point((x, y), fill='rgb(255, 255, 0)')
    return im

def generateAnimateXOR(width=0, height=0, pixel_size=1, colorK=(1,1,1), n=1, folder="."):
    for num in range(0, n):
        print("Generating image #{}. Internal image size: {}x{}".format(num, width//pixel_size, height//pixel_size))
        image = Image.new("RGBA", (width, height), (0,0,0,0))
        draw = ImageDraw.Draw(image)
        for y in range(0, height//pixel_size):
            for x in range(0, width//pixel_size):
                temp = (x+num) ^ (y+num)
                color = 0
                if prime.isPrime(temp):
                    color = 255
                draw.rectangle([(x*pixel_size, y*pixel_size), (x*pixel_size+pixel_size, y*pixel_size+pixel_size)], \
                    (int(color*colorK[0]), int(color*colorK[1]), int(color*colorK[2])))
        del draw
        image.save("{}/{}.png".format(folder, num), "PNG")

def generateAnimateColorXOR(width=0, height=0, pixel_size=1, n=1, folder="."):
    from math import sin, cos, tan
    for z in range(0, n):
        print("Generating image #{}. Internal image size: {}x{}".format(z, width//pixel_size, height//pixel_size))
        image = Image.new("RGBA", (width, height), (0,0,0,0))
        draw = ImageDraw.Draw(image)
        for y in range(0, height//pixel_size):
            for x in range(0, width//pixel_size):
                temp = x ^ y
                color = "hsv(0, 100%, 0%)"
                if prime.isPrime(temp):
                    h = loop360(int(mabs(sin(temp))*360)+z*2)
                    color = 'hsv({}, 100%, {}%)'.format(h, 100)
                draw.rectangle([(x*pixel_size, y*pixel_size), (x*pixel_size+pixel_size, y*pixel_size+pixel_size)], fill=color)
        del draw
        image.save("{}/{}.png".format(folder, z), "PNG")