import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image


def create_running_text_video(text):
    # Настройки видео
    width = 100
    height = 100
    duration = 3
    FPS = 24

    # Настройки текста
    text_color = "#ffffff"
    background_color = "#0000ff"
    font_size = 40
    font = ImageFont.load_default(font_size)
    text_width = font.getbbox(text)[2]
    text_speed = (width + text_width) / FPS / duration
    x, y = width, height // 2

    # Создание видео
    video = cv2.VideoWriter("video.mp4", cv2.VideoWriter_fourcc(*'mp4v'), FPS, (width, height))
    for t in range(FPS * duration):
        # Создание кадра
        img = Image.new("RGB", (width, height))
        drawer = ImageDraw.Draw(img)
        drawer.rectangle(((0, 0), (width, height)), background_color)
        drawer.text((x, y), text, font=font, fill=text_color, anchor="lm")

        # Перемещаю текст
        x -= text_speed

        # opencv работает только с numpy.array
        frame = np.array(img)

        # Записываю кадр в видео
        video.write(frame)

    # Завершаем процесс записи
    video.release()
