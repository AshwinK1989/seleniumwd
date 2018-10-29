from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class ChromeTest():

    def test(self):
        #Initializing Chrome
        driver = webdriver.Chrome(ChromeDriverManager().install())
        #Opening Google Site
        driver.get("https://www.google.com")


run = ChromeTest()
run.test()

