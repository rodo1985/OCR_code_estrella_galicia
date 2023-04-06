import pytesseract
import cv2
import re
import os

# set up the input and output directories
input_dir = 'images/new'
output_dir = 'images/decoded'

# make sure the output directory exists
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# loop through all the images in the input directory
for filename in os.listdir(input_dir):
    # read the image with OpenCV
    img = cv2.imread(os.path.join(input_dir, filename))

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(img_rgb)

    # search for all occurrences of 8 uppercase letters and/or digits
    matches = re.findall(r'\b[A-Z0-9]{8}\b', text)

    if matches:
        # select the last match
        code = matches[-1]
        print('Code:', code)

        # move the image to the output directory
        os.rename(os.path.join(input_dir, filename), os.path.join(output_dir, filename))
        
    else:
        print('No code found')