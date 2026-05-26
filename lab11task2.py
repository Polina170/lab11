import os
from PIL import Image
name = input("введите имя файла: ")
if name.lower().endswith((".jpg", ".jpeg", ".png")):
    try:
        img = Image.open(name)
        img.show()
        print(f"Размер: {img.size}")
        print(f"Формат: {img.format}")
        print(f"Цветовая модель: {img.mode}")
else:
    print("Ошибка! Можно открыть JPG, JPEG или PNG файлы"")