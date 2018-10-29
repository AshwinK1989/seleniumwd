from selenium import webdriver


class ChromeTest():

    def test(self):
        #Initializing Chrome
        driver = webdriver.Chrome()
        #Opening Google Site
        driver.get("https://www.google.com")


run = ChromeTest()
run.test()

