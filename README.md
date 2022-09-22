# Scrapy-GoodReads

---

## Description 📝

This repository marks my first attempt at web scraping using [Scrapy](https://scrapy.org/) and what better way
to do it than doing it on GoodReads to yield the details of the books which are described in the start_urls of
/Learning/Spiders file.

[This program is meant to retreive the image URL of the book, Title of the book and the description will be scraped via this crawler](./Learning/GoodReadsWebsite.png)

---

## To run the code 👨🏽‍💻

`pip install -r requirements.txt`

##### Change directory to Learning/spider

\
`scrapy crawl GoodReads -o BooksData.json`\
(to store it in BooksData.json file, please note that this will just append the data in the file)\
\
`scrapy crawl GoodReads`\
(to run it normally and diplay the output)

---

## Future prospects

As of now, we need to manually enter the links in the scraper.py file, which I would like to change to a command-line
argument.
