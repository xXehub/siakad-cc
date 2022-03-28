import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# Login Account
Email = "muhammad_izzul_28rpl@student.smktelkom-mlg.sch.id"
Password = "muham"
# Website logger
Website_url = "https://siswa.smktelkom-mlg.sch.id"
Website_url_absen = "https://siswa.smktelkom-mlg.sch.id/presnow"
Website_key = "6Lc7NmoUAAAAAJAgPU2_TypLL0H1UG_Fj9vUMl3O"
Captcha_api = "e4c1e7117adc63591e28c387080e7f9e"

# =====================================
# DON'T CHANGE THIS SETUP!
def account():
    return Email, Password

def sitelogger():
    return Website_url, Website_key, Captcha_api, Website_url_absen

def browser():
    chromes = webdriver.ChromeOptions()
    # chromes.binary_location = "/usr/bin/google-chrome-stable"
    chromes.add_argument("--no-sandbox") # Bypass OS security model
    chromes.add_argument("--headless")
    chromes.add_argument("--disable-extensions") # disabling extensions
    chromes.add_argument("--disable-gpu") # applicable to windows os only
    chromes.add_argument("--disable-dev-shm-usage") # overcome limited resource problems

    # Release
    # browser = webdriver.Chrome(executable_path=os.environ.get(
        # "CHROMEDRIVER_PATH"), chrome_options=chromes)

    ## Development
    # browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=chromes)
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=chromes)
    
    return browser