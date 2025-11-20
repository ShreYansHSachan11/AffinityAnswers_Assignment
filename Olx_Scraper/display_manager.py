"""
Display and output formatting utilities.
"""

from tabulate import tabulate
from config import TABLE_FORMAT, TABLE_HEADERS


class DisplayManager:
    """Handles formatting and displaying scraped data."""
    
    def display_results(self, listings, price_analysis=None):
        """Display listings in a formatted table with analysis."""
        if not listings:
            print("No listings found.")
            return
        
        # Display main table
        print(tabulate(
            listings,
            headers=TABLE_HEADERS,
            tablefmt=TABLE_FORMAT
        ))
        
        # Display summary
        print(f"\nTotal listings: {len(listings)}")
        
        # Display price analysis if available
        if price_analysis:
            self._display_price_analysis(price_analysis)
    
    def _display_price_analysis(self, analysis):
        """Display price analysis information."""
        print(f"Price range: ₹{analysis['min_price']:,} - ₹{analysis['max_price']:,}")
        print(f"Average price: ₹{analysis['avg_price']:,}")
        print(f"Listings with valid prices: {analysis['count']}")
    
    def display_filtered_results(self, all_listings, filtered_listings):
        """Display both all results and filtered car cover results."""
        print("=== ALL LISTINGS ===")
        self.display_results(all_listings)
        
        if filtered_listings and len(filtered_listings) != len(all_listings):
            print(f"\n=== FILTERED CAR COVERS ONLY ({len(filtered_listings)} items) ===")
            self.display_results(filtered_listings)
    
    def display_error(self, message):
        """Display error message."""
        print(f"Error: {message}")
    
    def display_status(self, message):
        """Display status message."""
        print(message)