# merger_cite_scrapper
 
This repository contains a Python script that uses Selenium to scrape data from the MergerCite (https://www.mergercite.eu/), which provides a database of notified mergers in Europe since the 90's.

The script opens a browser window and navigates to the MergerCite. It then uses BeautifulSoup to parse the HTML of the search results pages, extracting information such as the names of the merging companies, the decision code, among others. The scraped data is then saved to a CSV file for further analysis.

In addition to the scraper script (mergercite_scraper.py), this repository also includes a sample CSV file (mergercite_data.csv) with data that was scraped using the default settings of the script. You can customize the script to scrape different pages or to extract different types of information by modifying the code as needed.

This code can be useful for researchers, analysts, or anyone interested in tracking mergers and acquisitions in Europe. Feel free to fork this repository and adapt the code for your own purposes.
