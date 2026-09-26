import math
import tkinter as tk


def draw(shader, width, height):
    image = bytearray((0, 0, 0) * width * height)
    for y in range(height):
        for x in range(width):
            pos = (width * y + x) * 3
            color = shader(x / width, y / height)
            normalized = [max(min(int(c * 255), 255), 0) for c in color]
            image[pos:pos + 3] = normalized
    header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
    return header + image


def main(shader):
    label = tk.Label()
    img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)
    label.pack()
    label.config(image=img)
    tk.mainloop()

def noise(x, y):
    x = int(x * 50 + 0.5) / 50
    y = int(y * 50 + 0.5) / 50
    f = ((float(x) + 20) ** (float(y) + 85) % 38) ** 0.7 * math.pi  # pseudorandom
    return f - int(f)

def val_noise(x, y):
    x0 = int(x * 50)
    y0 = int(y * 50)
    x1 = x0 + 1
    y1 = y0 + 1
    n00 = noise(x0 / 50, y0 / 50)
    n10 = noise(x1 / 50, y0 / 50)
    n01 = noise(x0 / 50, y1 / 50)
    n11 = noise(x1 / 50, y1 / 50)

    frac_x = x * 50 - x0
    frac_y = y * 50 - y0
    nx0 = n00 * (1 - frac_x) + n10 * frac_x
    nx1 = n01 * (1 - frac_x) + n11 * frac_x
    return nx0 * (1 - frac_y) + nx1 * frac_y

def shader(x, y):
    t = val_noise(x, y)
    return t, t, t

main(shader)