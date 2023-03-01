# Shadow-Search
A basic search engine in terminal that prints top 5 lings based upon your search input

This is a Python program that allows users to search the web using a variety of search engines, including Google, Bing, DuckDuckGo, Yahoo, Qwant, Yandex, Ask Jeeves, AOL Search, Baidu, Ecosia, StartPage, Wolfram Alpha, Quora, Wikipedia, YouTube, IMDb, Stack Overflow, and GitHub.

When the program is run, it first prints a welcome message and a reminder that it is a safe way to search the web. It then defines a list of dictionaries, with each dictionary representing a search engine. Each dictionary contains information about the search engine, including its name, URL format, HTML class for search results, and HTML tag and attribute for search result links.

The program then determines the default browser based on the current platform (e.g. Safari for macOS, Edge for Windows, or xdg-open for Linux). It then enters a while loop that prompts the user to enter a search query and searches for that query using each search engine in the list of dictionaries. For each search engine, the program constructs the search URL by formatting the URL string with the user's query using the .format() method. It then sends a GET request to the search URL using the requests library and stores the response in a variable.

The program then uses BeautifulSoup, a library for parsing HTML and XML documents, to parse the response HTML and find all instances of the search results HTML class. For each search result, the program extracts the link URL using the specified HTML tag and attribute and prints it to the console. If no results are found for a given search engine, the program moves on to the next search engine in the list.

After searching all of the search engines, the program prompts the user to choose a search result to open in their default browser. If the user enters a valid number corresponding to a search result, the program uses the default browser to open the selected link. If the user enters "q", the program exits the while loop and terminates.



