from selenium import webdriver
import time


class WhatsappBot:
    def __init__(self):
        self.message = 'Annihilation is always the answer. We destroy parts of ourselves every day. We Photoshop our warts away. We edit the parts we hate about ourselves, modify the parts we think people hate. We curate our identity, carve it, distill it. Annihilation is all we are.'
        self.groups = ['Coronapru 💥', 'SB // A New Hope']
        options = webdriver.ChromeOptions()
        options.add_argument('lang=eng')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver')
