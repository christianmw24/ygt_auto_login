# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Twitter4(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_twitter4(self):
        driver = self.driver
        driver.get("https://twitter.com/de")
        driver.find_element_by_xpath("//a[@id='signin-link']/small").click()
        driver.find_element_by_name("session[username_or_email]").click()
        driver.find_element_by_name("session[username_or_email]").clear()
        driver.find_element_by_name("session[username_or_email]").send_keys("mail@mail.com")		# login einfügen
        driver.find_element_by_name("session[password]").click()
        driver.find_element_by_name("session[password]").clear()
        driver.find_element_by_name("session[password]").send_keys("1234isnotsecure")				# passwort einfügen
        driver.find_element_by_xpath("//input[@value='Log in']").click()
        driver.find_element_by_xpath("//li[@id='global-nav-home']/a/span[3]").click()
        driver.find_element_by_id("tweet-box-home-timeline").click()
        # ERROR: Caught exception [unknown command [editContent]]
        driver.find_element_by_xpath("(//button[@type='button'])[23]").click()
        driver.find_element_by_id("tweet-box-home-timeline").click()
        # ERROR: Caught exception [unknown command [editContent]]
        driver.find_element_by_xpath("(//button[@type='button'])[23]").click()
        driver.find_element_by_id("user-dropdown-toggle").click()
        driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
