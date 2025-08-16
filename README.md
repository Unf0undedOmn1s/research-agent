# Research Agent

**Research Agent** is a privacy-focused, web-based search tool built with Python (Flask) and JavaScript. It allows users to search the web using the [DuckDuckGo Instant Answer API](https://duckduckgo.com/api) and displays concise, relevant results in a clean, responsive interface.


## Features

- **Privacy-first:** Uses DuckDuckGo's API, so your searches are not tracked.
- **Instant Answers:** Fetches summaries and related topics for your queries.
- **Modern UI:** Responsive, mobile-friendly design with a clean look.
- **Open Source:** Easily customizable for your own needs.
- **Hosted on Render:** Ready for cloud deployment.


## How It Works

1. **Frontend:**  
   Users enter a search query in the web interface (`research-agent.html`).  
2. **Backend:**  
   The Flask backend (`main.py`) receives the query, calls the DuckDuckGo API, and returns results as JSON.
3. **Display:**  
   JavaScript dynamically displays the results on the page, including instant answers and related links.


## File Structure

- `main.py` — Flask backend serving the HTML and handling search requests.
- `agent.py` — Contains the DuckDuckGo search logic.
- `research-agent.html` — The frontend interface (responsive and mobile-friendly).


## Credits

- Built and maintained by **Marios Grivas**
- Dept of Informatics & Telecommunications, University of Ioannina
- Hosted on [Render](https://render.com/)


## License

MIT License


## Links

- [DuckDuckGo Instant Answer API Documentation](https://duckduckgo.com/api)
- [Research Agent GitHub Repository](https://github.com/Unf0undedOmn1s/research-agent)
- [Render Hosting Platform](https://render.com/)
