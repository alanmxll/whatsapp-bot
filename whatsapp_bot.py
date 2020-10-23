from selenium import webdriver
import time


class WhatsappBot:
    def __init__(self):
        self.message = "Annihilation is always the answer. We destroy parts of ourselves every day. We Photoshop our warts away. We edit the parts we hate about ourselves, modify the parts we think people hate. We curate our identity, carve it, distill it. Annihilation is all we are."
        self.groups = ["Coronapru", "SB // A New Hope "]
        options = webdriver.ChromeOptions()
        options.add_argument("lang=eng")
        self.driver = webdriver.Chrome(executable_path=r"./chromedriver")

    def sendMessages(self):
        self.driver.get("https://web.whatsapp.com/")
        time.sleep(30)

        for group in self.groups:
            group = self.driver.find_element_by_xpath(
                f"//span[@title='{group}']")
            time.sleep(3)
            group.click()
            chat_box = self.driver.find_element_by_class_name("_3uMse")
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.message)
            send_button = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(3)
            send_button.click()
            time.sleep(5)


whatsapp_bot = WhatsappBot()
whatsapp_bot.sendMessages()
