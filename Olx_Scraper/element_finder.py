"""
Element finding utilities for web scraping.
"""

from selenium.webdriver.common.by import By
from config import SELECTORS


class ElementFinder:
    """Handles finding elements on web pages with fallback selectors."""
    
    def __init__(self, driver):
        self.driver = driver
    
    def find_elements_with_fallback(self, selector_list):
        """Try multiple selectors until one returns elements."""
        for selector in selector_list:
            elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
            if elements:
                return elements
        return []
    
    def find_listing_elements(self):
        """Find all listing elements (titles, prices, descriptions)."""
        elements = {}
        
        for key, selector_list in SELECTORS.items():
            elements[key] = self.find_elements_with_fallback(selector_list)
        
        return elements
    
    def extract_text_safely(self, element):
        """Safely extract text from an element."""
        try:
            text = element.text.strip()
            return text if text else "N/A"
        except:
            return "N/A"