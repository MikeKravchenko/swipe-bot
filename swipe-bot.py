from selenium import webdriver
from time import sleep
import sys

from secrets import username, password
class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(6)

        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]')
        fb_btn.click()
        sleep(3)
        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        sleep(2)
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()
        sleep(2)

        self.driver.switch_to_window(base_window)

        popup_3 = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        popup_3.click()
        sleep(2)

        sleep(3)
        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]') #//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()
        sleep(2)

        sleep(3)
        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()
        sleep(2)

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()                         

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()

    def auto_swipe(self):
        from random import random
        from random import randint
        from time import sleep
        self.left_count, self.right_count = 0, 0
        while True:
            sleep(randint(1,3))
            rand = random()
            if rand > 0.9977: sleep(randint(1,50))
            try:
                rand = random()
                if rand < .9667:
                    self.like()
                    self.right_count = self.right_count +1
                    print('{}th rightswipe'.format(self.right_count))
                    # delete this if you have paid version
                    if self.right_count % 100 == 0:
                        self.driver.quit()
                        sys.exit()
                        # self.driver.close()
                        # sel.quit()
                        # sel.close()
                else:
                    self.dislike()
                    self.left_count = self.left_count +1
                    print('{}th leftswipe'.format(self.left_count))
            except Exception as err:
                try:
                    self.close_popup()
                except Exception:
                    try:
                        self.close_match()
                    except Exception:
                         print("Error: {0}".format(err))

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

bot = TinderBot()
bot.login()
bot.auto_swipe()
