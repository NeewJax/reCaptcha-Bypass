
# Bypass for Google reCaptcha with buster chrome extension using selenium.

That script provides a method to bypass Google reCaptcha using the Buster Chrome extension in combination with the Selenium library. This tool can be used for various automation tasks that require bypassing reCaptcha, thereby streamlining workflows that involve web scraping, automated testing, or any application where captcha challenges pose a hurdle.
## Dependencies
Ensure you have the following software installed:
```bash
Python3
Selenium
ChromeDriver
```
you can get ChromeDriver [here](https://getwebdriver.com/chromedriver), After that, configure the file "bypass_captcha.py" and set your "chrome_driver_path".

## Installation

```bash
git clone https://github.com/NeewJax/reCaptcha-Bypass
cd reCaptcha-Bypass
```
Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage

To run the script, execute the following command:
```bash
python3 bypass_captcha.py
```


## Troubleshooting

#### ChromeDriver not found:

Ensure ChromeDriver is in your PATH or specify its exact location.

#### reCaptcha challenges not bypassed:

Ensure the Buster extension is functioning and has the necessary permissions.

