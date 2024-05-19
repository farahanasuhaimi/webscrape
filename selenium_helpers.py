from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import pandas as pd
import re

# install the libraries for webpages interactions
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LeagueScraper:
    def __init__(self, headless=True):
        """
        Initialize the LeagueScraper class.
        """
        self.driver = None
        self.headless = headless

    def setup_selenium(self):
        chromedriver_autoinstaller.install()
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        if self.headless:
            options.add_argument("--headless")  # Enable headless mode

        service = Service(executable_path=chromedriver_autoinstaller.install()) 
        driver = webdriver.Chrome(service=service, options=options)
        return self.driver
    
    def accept_cookies(self, url):
        try:
            self.driver.get(url)
            cookie_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            cookie_button.click()
            print("Cookies accepted successfully")
        except Exception as e:
            print("Cookies button not found")
            print(e)
            
    def get_data(self):
        # get the webpage
        self.driver.get(self.url)
        # wait for the webpage to load
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'EventCard')))
        # get the data from the webpage
        self.get_matches()
        # close the webdriver
        self.driver.quit()
        return self.df
    
    def get_matches(self):
        # get the matches from the webpage
        matches = self.driver.find_elements_by_class_name('EventCard')
        # iterate over the matches
        for match in matches:
            # get the match details
            match_details = match.find_element_by_class_name('EventCard__eventCard')    

    