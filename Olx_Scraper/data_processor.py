"""
Data processing utilities for scraped listings.
"""

import re
from typing import List, Tuple


class DataProcessor:
    """Processes and analyzes scraped listing data."""
    
    def extract_listings(self, elements):
        """Extract listings from found elements."""
        titles = elements.get('titles', [])
        prices = elements.get('prices', [])
        descriptions = elements.get('descriptions', [])
        
        max_items = min(len(titles), len(prices), len(descriptions))
        
        if max_items == 0:
            return []
        
        listings = []
        for i in range(max_items):
            title = self._safe_extract_text(titles[i])
            price = self._safe_extract_text(prices[i])
            desc = self._safe_extract_text(descriptions[i])
            listings.append([title, desc, price])
        
        return listings
    
    def _safe_extract_text(self, element):
        """Safely extract text from an element."""
        try:
            text = element.text.strip()
            return text if text else "N/A"
        except:
            return "N/A"
    
    def analyze_prices(self, listings):
        """Analyze price data from listings."""
        prices = []
        
        for _, _, price_str in listings:
            numeric_price = self._extract_numeric_price(price_str)
            if numeric_price > 0:
                prices.append(numeric_price)
        
        if not prices:
            return None
        
        return {
            'min_price': min(prices),
            'max_price': max(prices),
            'avg_price': sum(prices) // len(prices),
            'count': len(prices)
        }
    
    def _extract_numeric_price(self, price_str):
        """Extract numeric value from price string."""
        try:
            # Remove currency symbols and extract digits
            digits = ''.join(filter(str.isdigit, price_str))
            return int(digits) if digits else 0
        except:
            return 0
    
    def filter_car_covers(self, listings):
        """Filter listings to focus on actual car covers."""
        car_cover_keywords = [
            'car cover', 'body cover', 'vehicle cover', 'auto cover',
            'seat cover', 'wheel cover', 'mirror cover'
        ]
        
        filtered = []
        for listing in listings:
            title = listing[0].lower()
            if any(keyword in title for keyword in car_cover_keywords):
                # Exclude real estate listings
                if not any(word in title for word in ['bhk', 'flat', 'apartment', 'house']):
                    filtered.append(listing)
        
        return filtered