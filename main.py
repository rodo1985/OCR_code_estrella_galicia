import cv2
import re
import os
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
import yaml
import paddleocr
from paddleocr import PaddleOCR


# set up the input and output directories
input_dir = 'images/new'
output_dir = 'images/decoded'

# Load credentials from YAML file
with open("credentials.yaml", "r") as file:
    credentials = yaml.safe_load(file)

# Get username and password
username = credentials["username"]
password = credentials["password"]

sleep_time = 2

# make sure the output directory exists
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

ocr = PaddleOCR()


# loop through all the images in the input directory
for filename in os.listdir(input_dir):

    try:
        
        # read the image with OpenCV
        img = cv2.imread(os.path.join(input_dir, filename))

        # convert the image to RGB
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # resize the image
        img_resized = cv2.resize(img_rgb, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

        # create a ROI from the image
        x, y, w, h = cv2.selectROI(img_resized)

        # resize coordinates to match the original image
        x *= 2
        y *= 2
        w *= 2
        h *= 2

        # crop the image based on the ROI coordinates
        img_rgb = img_rgb[y:y+h, x:x+w]

        # recognize text in the image using PaddleOCR
        result = ocr.ocr(img_rgb)

        # extract the recognized text from the result
        text = ''
        for line in result:
            for word in line:
                text += str(word[1])
            text += '\n'

        # search for all occurrences of 8 uppercase letters and/or digits
        matches = re.findall(r'\b[A-Z0-9]{8}\b', text)


        if matches:
            # select the last match
            code = matches[-1]
            print('Code:', code)
            
            # Set the path for the Chrome driver executable
            chrome_driver_path = "resources/chromedriver_linux64/chromedriver"

            # Create a new instance of the Chrome driver
            driver = webdriver.Chrome(chrome_driver_path)

            # Navigate to the web page you want to automate
            driver.get('https://00emisiones.estrellagalicia00.es/customer/pincode')

            # Wait for the page to load
            time.sleep(sleep_time)

            # Submit the form to log in
            driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()

            # Wait for the page to load
            time.sleep(sleep_time)

            # locate the element by its CSS selector
            driver.find_element(By.CSS_SELECTOR, "a.nav-link.link-light.text-uppercase.gigya-login-screen").click()

            # Wait for the page to load
            time.sleep(sleep_time)

            # locate the element by its name attribute
            driver.find_element(By.NAME, "username").send_keys(username)
            driver.find_element(By.NAME, "password").send_keys(password)

            # locate the element by its CSS selector
            submit_button = driver.find_element(By.CSS_SELECTOR, "input.gigya-input-submit").click()

            # Wait for the page to load
            time.sleep(sleep_time)

            # Navigate to the web page you want to automate
            driver.get('https://00emisiones.estrellagalicia00.es/customer/pincode')

            # Wait for the page to load
            time.sleep(sleep_time)

            # locate the element by its name attribute
            driver.find_element(By.ID, "pincode").send_keys(code)

            # Wait for the page to load
            time.sleep(sleep_time)

            # locate the element by its name attribute
            driver.find_element(By.ID, "zip").send_keys('08205')

            # Wait for the page to load
            time.sleep(sleep_time)

            select_fr = Select(driver.find_element(By.ID, "store"))
            select_fr.select_by_index(19)
            
            # Wait for the page to load
            time.sleep(sleep_time)

            # locate the button element by its CSS selector
            driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()

            # Wait for the page to load
            time.sleep(sleep_time)

            # Close the browser window
            driver.quit()

            # move the image to the output directory
            os.rename(os.path.join(input_dir, filename), os.path.join(output_dir, filename))
            
        else:
            print('No code found')
        
    except Exception as e:
        print('Error:', e)
    



