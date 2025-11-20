"""
Configuration settings for the OLX scraper.
"""

# Chrome browser paths for different installations
CHROME_PATHS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"~\AppData\Local\Google\Chrome\Application\chrome.exe"
]

# Chrome options for headless scraping
CHROME_OPTIONS = [
    "--headless",
    "--no-sandbox", 
    "--disable-dev-shm-usage",
    "--disable-gpu",
    "--window-size=1920,1080",
    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
]

# Selenium wait timeouts
PAGE_LOAD_TIMEOUT = 10
ELEMENT_WAIT_TIMEOUT = 5

# CSS selectors for OLX elements (multiple fallbacks)
SELECTORS = {
    'titles': [
        "[data-aut-id='itemTitle']",
        "h6._2cVuZ", 
        ".title", 
        "h3", "h4", "h5", "h6"
    ],
    'prices': [
        "[data-aut-id='itemPrice']",
        "span._2Ks63", 
        ".price",
        "[class*='price']"
    ],
    'descriptions': [
        "[data-aut-id='item-location']",
        "span._2TWi1", 
        ".location",
        "[class*='location']"
    ]
}

# Default search URL
DEFAULT_SEARCH_URL = "https://www.olx.in/items/q-car-cover?isSearchCall=true"

# Table formatting
TABLE_FORMAT = "github"
TABLE_HEADERS = ["Title", "Location/Description", "Price"]