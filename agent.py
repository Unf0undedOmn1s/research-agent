import sys
import requests
from bs4 import BeautifulSoup

def search_google(query):
    print(f"Searching for: {query}")
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}&hl=en"
    response = requests.get(url, headers=headers)

    print(f"Response status: {response.status_code}")
    soup = BeautifulSoup(response.text, 'html.parser')
    
    results = []
    for g in soup.find_all('div', class_='tF2Cxc')[:5]:
        title_tag = g.find('h3')
        snippet_tag = g.find('div', class_='VwiC3b')
        if title_tag and snippet_tag:
            results.append({
                'title': title_tag.get_text(),
                'snippet': snippet_tag.get_text()
            })
    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a search query")
        sys.exit(1)
    query = ' '.join(sys.argv[1:])
    results = search_google(query)
    if not results:
        print("No results found.")
    else:
        for idx, r in enumerate(results, 1):
            print(f"{idx}.
