import requests
from bs4 import BeautifulSoup

# URL of the BBC Tamil news page
url = "https://www.bbc.com/tamil"

# Fetch the page content
try:
    response = requests.get(url, timeout=10)
except Exception as e:
    print(f"Error fetching the URL: {e}")

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# BBC headlines are usually inside <h3> tags with specific classes
headlines = soup.find_all("h1")
subheadlines = soup.find_all("h2")
headlines.extend(subheadlines)
content = soup.find_all("p")
headlines.extend(content)

# Remove duplicates and empty values
cleaned_headlines = set()


for h in headlines:
    text = h.get_text(strip=True)
    if text:
        cleaned_headlines.add(text)

# Write headlines to file
with open("headlines.txt", "w", encoding="utf-8") as file:
    for line in cleaned_headlines:
        file.write(line + "\n")

print("Headlines have been written to headlines.txt")

