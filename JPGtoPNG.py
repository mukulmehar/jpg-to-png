import sys
import os
from PIL import Image

#We are going to covert all the images inside the image folder to PNG format.

# 1. Grab first and second argument

image_folder=sys.argv[1]
output_folder=sys.argv[2]

# 2.Check if the output folder exists or not. And if it doesn't exists then create it.

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 3. Loop through all the files inside the folder.
# 4. Convert the images to PNG.
# 5. Save the images to the new folder.
for image in os.listdir(image_folder):
    img=Image.open(f'{image_folder}{image}')
    clean_name=os.path.splitext(image)[0]
    img.save(f'{output_folder}{clean_name}.png','png')
    print(f'All the images inside the {image_folder} have been converted to PNG format.')

