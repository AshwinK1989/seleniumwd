from selenium import webdriver


class SafariTest:

    def test(self):
        driver = webdriver.Safari()
        driver.get("https://www.google.com")


run = SafariTest()
run.test()
