import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains


class ActionsExamples:

    def mouse_hover(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("http://toolsqa.com/")

        action = ActionChains(driver)
        action\
            .move_to_element(driver.find_element(By.XPATH,"//nav//span[text()='Tutorial']"))\
            .perform()
        time.sleep(2.0)


ae = ActionsExamples()
ae.mouse_hover()



