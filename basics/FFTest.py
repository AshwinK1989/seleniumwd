from selenium import webdriver


class FFTest():

    def test(self):
        #Initializing Firefox
        driver = webdriver.Firefox()
        #Opening Google site
        driver.get("http://www.google.com")


run = FFTest()
run.test()

