"""
A simple selenium test example written by python
"""

import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException

class TestTemplate(unittest.TestCase):
    """Include test cases on a given url"""

    def setUp(self):
        """Start web driver"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        """Stop web driver"""
        self.driver.quit()

    def test_case_1(self):
        """Login and play arbitrary playlist"""
        try:
            self.driver.get('https://accounts.spotify.com/de/login/')
            self.driver.save_screenshot('./01_login.png')
            input_username = self.driver.find_element_by_name('username')
            input_username.send_keys(os.environ['LOGIN_MINE_USERNAME'])
            input_password = self.driver.find_element_by_name('password')
            input_password.send_keys(os.environ['LOGIN_MINE_PW'])
            
            time.sleep(2)
            print("Logging in")
            self.driver.save_screenshot('./02_user_data.png')
            
            login_button = self.driver.find_element_by_id('login-button')
            login_button.click()
            
            time.sleep(2)
            print("Logged in")
            self.driver.save_screenshot('./03_logged_in.png')
            
            self.driver.get('https://open.spotify.com/album/2auiRkQwGGHkVaWTjchszO?si=cvqQ0RxTTJuRi3twtDvq-w') # just some test playlist
            time.sleep(3)
            print("Opening Playlist and Clicking Top Play Button")
            self.driver.save_screenshot('./04_playlist.png')
            ##play_button = self.driver.find_element_by_xpath("//button[@aria-label='Play']")
            #play_button = self.driver.find_element_by_xpath("//button[@data-testid='play-button']")
            #action = ActionChains(self.driver)
            #action.move_to_element(play_button).perform()
            #action.click(play_button).perform()
            play_button_bottom = self.driver.find_element_by_xpath("//button[@data-testid='control-button-play']")
            action = ActionChains(self.driver)
            action.move_to_element(play_button_bottom).perform()
            action.click(play_button_bottom).perform()
            time.sleep(2)
            print("Listening")
            self.driver.save_screenshot('./05_listening.png')
            
            time.sleep(2)
            self.driver.save_screenshot('./06_check_running_01.png')
            time.sleep(2)
            self.driver.save_screenshot('./06_check_running_02.png')
            time.sleep(2)
            self.driver.save_screenshot('./06_check_running_03.png')
            time.sleep(2)
            self.driver.save_screenshot('./06_check_running_04.png')
            print("That was nice")
            time.sleep(2)
            self.driver.get('https://accounts.spotify.com/de/logout/')
            self.driver.save_screenshot('./07_logout.png')
            time.sleep(2)
        except NoSuchElementException as ex:
            self.fail(ex.msg)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplate)
    unittest.TextTestRunner(verbosity=2).run(suite)

