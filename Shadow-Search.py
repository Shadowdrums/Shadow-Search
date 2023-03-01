import requests
from bs4 import BeautifulSoup
import platform

print("welcome to Shadow Search")

print("This is a safe way to search the web :D")
# Define search engines to use
search_engines = [
    {
        "name": "Google",
        "url": "https://www.google.com/search?q={query}",
        "results_class": "rc",
        "link_tag": "a",
        "link_attr": "href"
    },
    {
        "name": "Bing",
        "url": "https://www.bing.com/search?q={query}",
        "results_class": "b_algo",
        "link_tag": "a",
        "link_attr": "href"
    },
    {
        "name": "DuckDuckGo",
        "url": "https://duckduckgo.com/html/?q={query}",
        "results_class": "result__url",
        "link_tag": "a",
        "link_attr": "href"
    },
    {
        "name": "Yahoo",
        "url": "https://search.yahoo.com/search?p={query}",
        "results_class": "algo-sr",
        "link_tag": "a",
        "link_attr": "href"
    },
    {
        "name": "Qwant",
        "url": "https://www.qwant.com/?q={query}",
        "results_class": "result--url",
        "link_tag": "a",
        "link_attr": "href"
    },
    {
        "name": "Yandex",
        "url": "https://www.yandex.com/search/?text={query}",
        "results_class": "organic__url",
        "link_tag": "a",
        "link_attr": "href"
    },
    {
        "name": "Ask Jeeves",
        "url": "https://www.ask.com/web?q={query}",
        "results_class": "PartialSearchResults-item",
        "link_tag": "a",
        "link_attr": "href"
    },
    {
        "name": "AOL Search",
        "url": "https://search.aol.com/aol/search?q={query}",
        "results_class": "algo-sr",
        "link_tag": "a",
        "link_attr": "href"
    },
    {
        "name": "Baidu",
        "url": "https://www.baidu.com/s?wd={query}",
        "results_class": "result-op",
        "link_tag": "a",
        "link_attr": "href"
    },
    {
        "name": "Ecosia",
        "url": "https://www.ecosia.org/search?q={query}",
        "results_class": "js-result",
        "link_tag": "a",
        "link_attr": "href"
    },
    {
        "name": "StartPage",
        "url": "https://www.startpage.com/do/search?q={query}",
        "results_class": "w-gl__result",
        "link_tag": "a",
        "link_attr": "href"
    },
    {
        "name": "Wolfram Alpha",
        "url": "https://www.wolframalpha.com/input/?i={query}",
        "results_class": "wa",
        "link_tag": "a",
        "link_attr": "href"
    },
    {
        "name": "Quora",
        "url": "https://www.quora.com/search?q={query}",
        "results_class": "pagedlist_item",
        "link_tag": "a",
        "link_attr": "href"
    },
    {
        "name": "Wikipedia",
        "url": "https://en.wikipedia.org/w/index.php?title=Special:Search&search={query}",
        "results_class": "mw-search-results",
        "link_tag": "a",
        "link_attr": "href"
    },
    {
        "name": "YouTube",
        "url": "https://www.youtube.com/results?search_query={query}",
        "results_class": "yt-lockup-content",
        "link_tag": "a",
        "link_attr": "href"
    },
    {
        "name": "IMDb",
        "url": "https://www.imdb.com/find?q={query}&s=tt",
        "results_class": "findResult",
        "link_tag": "a",
        "link_attr": "href"
    },
    {
        "name": "Stack Overflow",
        "url": "https://stackoverflow.com/search?q={query}",
        "results_class": "question-summary search-result",
        "link_tag": "a",
        "link_attr": "href"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/search?q={query}",
        "results_class": "repo-list-item",
        "link_tag": "a",
        "link_attr": "href"
    }
]

# Get default browser based on the current platform
if platform.system() == 'Darwin':
    default_browser = 'open'
elif platform.system() == 'Windows':
    default_browser = 'start'
else:
    default_browser = 'xdg-open'

while True:
    # Get search query from user
    query = input("Enter your search query :) > ")

    # Search for query in each search engine
    found_results = False
    for engine in search_engines:
        print(f"Searching {engine['name']}...")
        url = engine['url'].format(query=query)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
        }

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.content, "html.parser")

        search_results = soup.find_all("div", class_=engine['results_class'])

        # If query is found, print the first 5 links and exit loop
        if search_results:
            print(f"{engine['name']} results found!")
            for idx, result in enumerate(search_results[:5], start=1):
                link = result.find(engine['link_tag'])[engine['link_attr']]
                title = result.find(engine['link_tag']).get_text()
                print(f"{title}:\n {link}")
            found_results = True

        # If query is not found in the current search engine, try the next one
        else:
            print(f"{engine['name']} sorry i couldnt find results for that. :(")

    # If query is not found in any search engine, print message
    if not found_results:
        print("No results found in any search engine.")
    else:
        print("Links printed. To open a link, run the script again and choose a link number.")

    # Ask user if they want to search again
    search_again = input("Would you like to continue searching or did you find everything you need?(y/n): ")
    if search_again.lower() != 'y':
        break
