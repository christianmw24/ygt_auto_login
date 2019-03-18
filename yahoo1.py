# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Yahoo1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_yahoo1(self):
        driver = self.driver
        driver.get("https://mail.yahoo.com/?.intl=de&.lang=de-DE&.partner=none&.src=fp")
        driver.find_element_by_id("login-username").click()
        driver.find_element_by_id("login-username").clear()
        driver.find_element_by_id("login-username").send_keys("name@yahoo.com")							# login einfügen
        driver.find_element_by_xpath("//form[@id='login-username-form']/p[2]/span/label").click()
        driver.find_element_by_id("login-signin").click()
        driver.find_element_by_id("login-passwd").click()
        driver.find_element_by_id("login-passwd").clear()
        driver.find_element_by_id("login-passwd").send_keys("1234isnotsecure")							# passwort einfügen
        driver.find_element_by_id("login-signin").click()
        driver.find_element_by_link_text("Verfassen").click()
        driver.find_element_by_id("message-to-field").clear()
        driver.find_element_by_id("message-to-field").send_keys("f")
        driver.find_element_by_xpath("//div[@id='ybar']/div[3]/div/div/label").click()
        driver.find_element_by_xpath("//div[@id='ybarAccountMenuBody']/a[3]/span").click()
    
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
