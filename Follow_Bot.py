from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from time import sleep


class Follow_Bot:
    def __init__(self, path, target, user, password):
        self.driver = webdriver.Chrome(executable_path=path)
        self.website = "https://www.instagram.com/" + target
        self.user = user
        self.password = password
        self.target = target
        self.main_window_handle = None

    def sign_in(self):
        self.driver.get(self.website)
        sleep(3)
        try:
            log_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button')
            log_button.click()
        except:
            pass
        sleep(3)
        username_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
        username_input.click()
        username_input.send_keys(self.user)
        pass_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        pass_input.click()
        pass_input.send_keys(self.password)
        log_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
        sleep(2)
        log_button.click()
        sleep(2)
        try:
            sleep(2)
            dont_save = self.driver.find_element(By.CLASS_NAME, "cmbtv")
            dont_save.click()
            sleep(2)
        except:
            pass

    def find_followers(self):
        self.driver.implicitly_wait(5)
        page_followers = self.driver.find_element(By.CSS_SELECTOR, f'a[href="/{self.target}/followers/"')
        page_followers.click()
        sleep(2)

    def add_follower(self):
        follower_window = self.driver.find_element(By.CLASS_NAME, "_aano")
        for i in range(10):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', follower_window)
            sleep(2)

        while True:
            followers = self.driver.find_elements(By.XPATH, '//*[text()="Follow"]')
            if followers == []:
                break
            for item in followers:
                item.click()
                sleep(1)
