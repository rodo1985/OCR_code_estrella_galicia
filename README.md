# Optical Character Recognition for Estrella Galicia 0,0 Promotional Codes
This script automates the process of entering promotional codes for Estrella Galicia 0,0 products using Optical Character Recognition (OCR) and Selenium.

The script is specifically designed for the website <a href="https://00emisiones.estrellagalicia00.es/customer/pincode" target="_new">https://00emisiones.estrellagalicia00.es/customer/pincode</a> and uses Selenium to automate the login process.

## Installation
1. Clone the repository to your local machine.

2. Install the required packages using the following command:

```python
pip install -r requirements.txt
```

### Pytesseract and PaddleOCR
This script requires both `pytesseract` and `PaddleOCR` for OCR. You can install them using pip:

```
pip install pytesseract paddlepaddle paddleocr

```
### Selenium Drivers
This script uses Selenium for browser automation. You need to download the appropriate driver for your browser and operating system. Here are the links for some common browsers:

- Chrome: <a href="https://sites.google.com/a/chromium.org/chromedriver/downloads" target="_new">https://sites.google.com/a/chromium.org/chromedriver/downloads</a>
- Firefox: <a href="https://github.com/mozilla/geckodriver/releases" target="_new">https://github.com/mozilla/geckodriver/releases</a>
- Safari: <a href="https://webkit.org/blog/6900/webdriver-support-in-safari-10/" target="_new">https://webkit.org/blog/6900/webdriver-support-in-safari-10/</a>


Make sure the driver executable is in your system's PATH in resources folder

## Usage

1. Clone this repository.
2. Put your Estrella Galicia 0,0 promotional code images in the `images/new` directory.
3. Add your Estrella Galicia 0,0 account credentials to `credentials.yaml`.

```yaml
username: YOUR_USERNAME
password: YOUR_PASSWORD
```
4. Run the script:

```python
python main.py
```

<ol start="5">The script will automatically navigate to the Estrella Galicia 0,0 website and enter the promotional codes. Any images that are successfully decoded will be moved to the `images/decoded` directory.</li></ol>


## Contributing
1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push to your forked repository.
5. Create a pull request.

## License
This project is licensed under the MIT License - see the <a href="LICENSE" target="_new">LICENSE</a> file for details.

