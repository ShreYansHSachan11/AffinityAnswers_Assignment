# OLX Car Cover Scraper - Modular Version

A production-ready, modular web scraper that extracts car cover listings from OLX India using Selenium WebDriver.

## 🏗️ Modular Architecture

### Core Components

| Module | Purpose | Key Features |
|--------|---------|--------------|
| `config.py` | Configuration settings | Chrome paths, selectors, timeouts |
| `browser_manager.py` | Chrome WebDriver management | Context manager, auto-detection |
| `element_finder.py` | Element location with fallbacks | Multiple selector strategies |
| `data_processor.py` | Data extraction & analysis | Price analysis, filtering |
| `display_manager.py` | Output formatting | Table display, price stats |
| `scraper.py` | Main orchestration class | Coordinates all components |
| `olx_scraper.py` | Entry point | Main execution script |

## 🚀 Features

- **Bypasses Anti-Scraping**: Uses Selenium to avoid OLX blocking
- **Robust Selectors**: Multiple fallback CSS selectors for reliability
- **Smart Filtering**: Separates actual car covers from real estate listings
- **Price Analysis**: Automatic price range and average calculations
- **Modular Design**: Easy to maintain and extend
- **Error Handling**: Graceful failure management

## 📊 Sample Output

```
=== ALL LISTINGS ===
37 total listings including real estate with car parking

=== FILTERED CAR COVERS ONLY (16 items) ===
Pure car cover listings with price analysis
Price range: ₹100 - ₹6,000,000
Average price: ₹1,409,950
```

## 🛠️ Installation

```bash
# Install dependencies
pip install selenium tabulate

# Run the scraper
python olx_scraper.py
```

## 📁 Project Structure

```
├── olx_scraper.py      # Main entry point
├── scraper.py          # Core scraper orchestration
├── config.py           # Configuration settings
├── browser_manager.py  # Chrome WebDriver management
├── element_finder.py   # Element location utilities
├── data_processor.py   # Data extraction & analysis
├── display_manager.py  # Output formatting
└── README.md          # This file
```

## 🔧 Customization

### Change Search Query
Edit `DEFAULT_SEARCH_URL` in `config.py`:
```python
DEFAULT_SEARCH_URL = "https://www.olx.in/items/q-your-search-term"
```

### Add New Selectors
Update `SELECTORS` in `config.py` if OLX changes their HTML structure.

### Modify Filtering
Edit `filter_car_covers()` in `data_processor.py` to adjust filtering logic.

## 🎯 Why Modular?

- **Maintainability**: Each component has a single responsibility
- **Testability**: Individual modules can be tested in isolation
- **Extensibility**: Easy to add new features or data sources
- **Reusability**: Components can be reused for other scraping projects
- **Debugging**: Easier to isolate and fix issues

## ⚠️ Notes

- Requires Chrome browser installation
- Web scraping may be subject to website terms of service
- CSS selectors may need updates if OLX changes their structure
- Consider using official APIs when available