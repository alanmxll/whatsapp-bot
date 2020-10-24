from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time


class WhatsappBot:
    def __init__(self):
        """
        -> Start the necessary variables to the next methods.
        @param self.
        """
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://web.whatsapp.com/")
        self.xpath = "//div[contains(@class,'copyable-text selectable-text')]"
        time.sleep(15)

    def __find_contact(self, contact):
        """
        -> Finds a contact whose name was passed as a parameter.
        @param self.
        @param contact: str
        """
        search_field = self.driver.find_element_by_xpath(self.xpath)
        time.sleep(3)
        search_field.click()
        search_field.send_keys(contact)
        search_field.send_keys(Keys.ENTER)

    def __send_message(self, message):
        """
        -> Send the message passed by parameter to the found contact.
        @param self.
        @param message: str
        """
        message_field = self.driver.find_elements_by_xpath(self.xpath)
        message_field[1].click()
        time.sleep(3)
        message_field[1].send_keys(message)
        message_field[1].send_keys(Keys.ENTER)

    def execute(self, contacts, message):
        """
        -> Run the __find_contact & __send_message private methods
        @param self.
        @param contacts: list<str>
        @param message: str
        """
        for contact in contacts:
            self.__find_contact(contact)
            self.__send_message(message)
