from selenium import webdriver
import time


def create_user_profile():
    user_options = webdriver.ChromeOptions()
    user_options.add_argument(r"--user-data-dir=C:\Users\qqerm\AppData\Local\Google\Chrome\User Data")
    user_options.add_argument("--profile-directory=Profile 1")
    user_options.add_argument("--start-maximized")

    return user_options

def test_open_browser():
    user_options = create_user_profile()
    driver = webdriver.Chrome(options=user_options)
    driver.get("https://dev-neo-bank-b2b.vercel.app/wallet")    #https://dev-neo-bank-b2b.vercel.app/wallet
    time.sleep(5)

    driver.quit()
    print("Браузер закрыт")
    

test_open_browser()


