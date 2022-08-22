from selenium import webdriver
# from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
#from pyvirtualdisplay import Display   # https://stackoverflow.com/questions/16180428/can-selenium-webdriver-open-browser-windows-silently-in-the-background
#display = Display(visible=0, size=(800, 600))


class TestLogin:

    def test_login_to_jira(self):
        #display.start()
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                             options=chrome_options)

        driver.get("https://jira.ithillel.com/secure/Dashboard.jspa")
        assert 'System Dashboard - Jira - Hillel IT School' in driver.title

        driver.find_element(By.ID, "login-form-username").clear()
        driver.find_element(By.ID, "login-form-username").send_keys("webinar5")
        driver.find_element(By.ID, "login-form-password").clear()
        driver.find_element(By.ID, "login-form-password").send_keys("webinar5")
        driver.find_element(By.ID, "login").submit()

        profile_logo_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "header-details-user-fullname")))
        assert profile_logo_element.is_displayed()
        driver.close()
        #display.stop()

    def test_mytest(self):
        assert 1 == 1
