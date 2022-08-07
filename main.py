from os import environ
import Follow_Bot


EMAIL = environ.get("email")
PASS = environ.get("pass")
SIMILAR_ACCOUNT = environ.get('TARGET_ACCOUNT')

CHROME_DRIVER_PATH = r"C:\Users\ugott\Desktop\Learning Mats\100 Days of Code\Day-48-Selenium-Game Bot\Selenium Drivers for Chrome\chromedriver.exe"
bot = Follow_Bot.Follow_Bot(path=CHROME_DRIVER_PATH,target=SIMILAR_ACCOUNT, user=EMAIL, password=PASS)
bot.sign_in()
bot.find_followers()
bot.add_follower()
print("Done!")
