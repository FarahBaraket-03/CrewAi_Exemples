# tools/browser_tools.py
import requests
from crewai.tools import tool
from bs4 import BeautifulSoup

@tool("Scrape website content")
def scrape_and_summarize_website(website: str) -> str:
    """Useful to scrape and summarize a website content"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(website, headers=headers, timeout=10)
        
        if response.status_code != 200:
            return f"Error: Failed to access website. Status code: {response.status_code}"
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove scripts and styles
        for script in soup(["script", "style"]):
            script.decompose()
        
        # Get clean text content
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        clean_text = ' '.join(chunk for chunk in chunks if chunk)
        
        # Return first 1500 characters as summary
        if len(clean_text) > 1500:
            return clean_text[:1500] + "..."
        return clean_text
        
    except Exception as e:
        return f"Error scraping website {website}: {str(e)}"