from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time


class WhatsappBot:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://web.whatsapp.com/")
        self.xpath = "//div[contains(@class,'copyable-text selectable-text')]"
        time.sleep(15)

    def __find_contact(self, contact):
        search_field = self.driver.find_element_by_xpath(self.xpath)
        time.sleep(3)
        search_field.click()
        search_field.send_keys(contact)
        search_field.send_keys(Keys.ENTER)

    def __send_message(self, message):
        message_field = self.driver.find_elements_by_xpath(self.xpath)
        message_field[1].click()
        time.sleep(3)
        message_field[1].send_keys(message)
        message_field[1].send_keys(Keys.ENTER)

    def execute(self, contacts, message):
        for contact in contacts:
            self.__find_contact(contact)
            self.__send_message(message)
