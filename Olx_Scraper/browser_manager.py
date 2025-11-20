"""
Browser management utilities for Chrome WebDriver.
"""

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config import CHROME_PATHS, CHROME_OPTIONS, PAGE_LOAD_TIMEOUT


class BrowserManager:
    """Manages Chrome browser setup and configuration."""
    
    def __init__(self):
        self.driver = None
    
    def check_chrome_installation(self):
        """Check if Chrome is installed on the system."""
        for path in CHROME_PATHS:
            expanded_path = os.path.expanduser(path)
            if os.path.exists(expanded_path):
                return True
        return False
    
    def setup_chrome_options(self):
        """Configure Chrome options for scraping."""
        options = Options()
        for option in CHROME_OPTIONS:
            options.add_argument(option)
        return options
    
    def create_driver(self):
        """Create and configure Chrome WebDriver."""
        if not self.check_chrome_installation():
            raise RuntimeError("Chrome browser not found")
        
        options = self.setup_chrome_options()
        self.driver = webdriver.Chrome(options=options)
        return self.driver
    
    def load_page(self, url):
        """Load a page and wait for it to be ready."""
        if not self.driver:
            raise RuntimeError("Driver not initialized")
        
        self.driver.get(url)
        
        # Wait for page to load
        WebDriverWait(self.driver, PAGE_LOAD_TIMEOUT).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
    
    def quit_driver(self):
        """Safely quit the browser driver."""
        if self.driver:
            try:
                self.driver.quit()
            except:
                pass
            finally:
                self.driver = None
    
    def __enter__(self):
        """Context manager entry."""
        self.create_driver()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.quit_driver()