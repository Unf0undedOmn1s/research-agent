import requests

def search_duckduckgo(query):
    url = "https://api.duckduckgo.com/"
    params = {
        "q": query,
        "format": "json",
        "no_redirect": 1,
        "no_html": 1,
        "skip_disambig": 1
    }
    response = requests.get(url, params=params)
    data = response.json()
    results = []

    # Add the instant answer if available
    if data.get("AbstractText"):
        results.append({
            "title": data.get("Heading", "DuckDuckGo Instant Answer"),
            "snippet": data["AbstractText"]
        })

    # Add related topics as results
    for topic in data.get("RelatedTopics", []):
        if "Text" in topic and "FirstURL" in topic:
            results.append({
                "title": topic["Text"],
                "snippet": topic["FirstURL"]
            })
        elif "Topics" in topic:
            for subtopic in topic["Topics"]:
                if "Text" in subtopic and "FirstURL" in subtopic:
                    results.append({
                        "title": subtopic["Text"],
                        "snippet": subtopic["FirstURL"]
                    })

    return results[:5]  # Return up to 5 results
