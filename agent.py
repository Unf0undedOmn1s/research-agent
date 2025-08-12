import sys
import requests
from bs4 import BeautifulSoup

def search_bing(query):
    print(f"Searching for: {query}")
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}&hl=en"
    response = requests.get(url, headers=headers)

    print(f"Response status: {response.status_code}")
    soup = BeautifulSoup(response.text, 'html.parser')
    
    results = []
    for li in soup.find_all('li', class_='b_algo')[:5]:
        title_tag = li.find('h2')
        snippet_tag = li.find('p')
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
    results = search_bing(query)
    if not results:
        print("No results found.")
    else:
        for idx, r in enumerate(results, 1):
            print(f"{idx}. {r['title']}\n{r['snippet']}\n")
