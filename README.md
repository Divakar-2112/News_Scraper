# Tamil News Web Scraper  

# Description
A simple Python project that scrapes Tamil news headlines from websites (e.g., DailyThanthi, Dinamalar, BBC Tamil, etc.) and saves them into a text file.

# How to run 
1. Save the code as "news_scraper.py".
2. Open terminal or powershell.
3. Install required libraries.
    pip install requests beautifulsoup4
4. Run the program using: python news_scraper.py


# Featuers
1. Automatic News Scraping
2. Multi-Tag Extraction
Extracts content from:
`<h1>` headlines  
`<h2>` sub-headlines  
`<h3>` section titles  
`<p>` summary paragraphs  
3. Duplicate Removal Automatically removes repeated headlines for clean output.
4. Saves Headlines to File Stores all collected headlines in a `headlines.txt` file.
5. Uses only requests + BeautifulSoup.
6. Error Handling
7. Reusable for Any Tamil News Website With minor changes, the same scraper works for:
 Dinamalar, DailyThanthi, BBC Tamil, News18 Tamil, Puthiya Thalaimurai, OneIndia Tamil and more!
