#!/usr/bin/env python3
"""
OLX Car Cover Scraper 

This is the main entry point that uses modular components:
- browser_manager: Chrome WebDriver management
- element_finder: Element location with fallback selectors  
- data_processor: Data extraction and analysis
- display_manager: Output formatting and display
- config: Configuration settings

Dependencies:
- selenium
- tabulate
- Chrome browser (automatically detected)

Usage:
    python olx_scraper.py
"""

from scraper import OLXScraper
from config import DEFAULT_SEARCH_URL


def main():
    print("=== OLX Car Cover Scraper (Modular) ===\n")
    
    # Initialize scraper
    scraper = OLXScraper()
    
    # Scrape and display results with filtering
    scraper.scrape_and_display(DEFAULT_SEARCH_URL, filter_results=True)


if __name__ == "__main__":
    main()