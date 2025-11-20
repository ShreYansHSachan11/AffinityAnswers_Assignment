"""
Main scraper class that orchestrates the scraping process.
"""

import time
from browser_manager import BrowserManager
from element_finder import ElementFinder
from data_processor import DataProcessor
from display_manager import DisplayManager
from config import ELEMENT_WAIT_TIMEOUT


class OLXScraper:
    """Main scraper class that coordinates all scraping operations."""
    
    def __init__(self):
        self.browser_manager = BrowserManager()
        self.data_processor = DataProcessor()
        self.display_manager = DisplayManager()
    
    def scrape_listings(self, search_url):
        """Main method to scrape listings from OLX."""
        try:
            with self.browser_manager as browser:
                # Load the page
                self.display_manager.display_status(f"Fetching listings from: {search_url}")
                browser.load_page(search_url)
                
                # Wait for dynamic content to load
                time.sleep(ELEMENT_WAIT_TIMEOUT)
                
                # Find elements
                element_finder = ElementFinder(browser.driver)
                elements = element_finder.find_listing_elements()
                
                # Process data
                listings = self.data_processor.extract_listings(elements)
                
                if not listings:
                    self.display_manager.display_error("No listings found - website structure may have changed")
                    return []
                
                self.display_manager.display_status(f"Successfully scraped {len(listings)} listings!")
                return listings
                
        except Exception as e:
            self.display_manager.display_error(f"Scraping failed: {str(e)[:100]}...")
            return []
    
    def scrape_and_display(self, search_url, filter_results=True):
        """Scrape listings and display results with optional filtering."""
        # Scrape all listings
        all_listings = self.scrape_listings(search_url)
        
        if not all_listings:
            return
        
        # Analyze prices
        price_analysis = self.data_processor.analyze_prices(all_listings)
        
        if filter_results:
            # Filter for actual car covers
            filtered_listings = self.data_processor.filter_car_covers(all_listings)
            self.display_manager.display_filtered_results(all_listings, filtered_listings)
            
            # Show analysis for filtered results if different
            if filtered_listings and len(filtered_listings) != len(all_listings):
                filtered_analysis = self.data_processor.analyze_prices(filtered_listings)
                if filtered_analysis:
                    print(f"\n=== FILTERED PRICE ANALYSIS ===")
                    self.display_manager._display_price_analysis(filtered_analysis)
        else:
            # Display all results
            self.display_manager.display_results(all_listings, price_analysis)