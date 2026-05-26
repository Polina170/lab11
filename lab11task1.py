import os
from PIL import Image, ImageFilter
input_folder = "images"
output_folder = "new_images"

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

files = os.listdir(input_folder)
for file in files:
   
    if file.lower().endswith(".jpg") or file.lower().endswith(".png"):
        img = Image.open(input_folder + "/" + file)
        new_img = img.filter(ImageFilter.CONTOUR)
        new_img.save(output_folder + "/new_" + file)
        print(f"Обработан:", file)