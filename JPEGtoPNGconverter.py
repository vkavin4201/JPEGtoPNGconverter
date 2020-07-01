import sys
import os
from PIL import Image

# grab first and second arguements
img_folder = sys.argv[1]
output_folder = sys.argv[2]
# check if output_folder exists, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
# loop through source folder
for file in os.listdir(img_folder):
    if img_folder[-1] == '/':
        img = Image.open(f'{img_folder}{file}')
    else:
        img = Image.open(f'{img_folder}/{file}')
    clean_name = os.path.splitext(file)[0]  # extract filename without the extension
    if output_folder[-1] == '/':
        img.save(f'{output_folder}{clean_name}.png', 'png')  # convert images to png and save to the output folder
    else:
        img.save(f'{output_folder}/{clean_name}.png', 'png')
    print('all done!')
