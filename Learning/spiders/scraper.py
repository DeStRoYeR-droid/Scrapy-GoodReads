# Scraping GoodReads
from distutils import text_file
import scrapy

class GoodReadsSpider(scrapy.Spider):
    name = "GoodReads"
    start_urls = ["https://www.goodreads.com/book/show/40121378-atomic-habits" , 
                  "https://www.goodreads.com/book/show/11468377-thinking-fast-and-slow" ,
                  "https://www.goodreads.com/book/show/43306206-the-courage-to-be-disliked",
                  "https://www.goodreads.com/book/show/32998876-101-essays-that-will-change-the-way-you-think"]
    
    def parse(self, response):
        try:
            description = ""
            complete_description = response.css('div#description');
            for text in complete_description.css('span::text').getall():
                description += text + " "
                
            yield {
                'name' : response.css('h1#bookTitle::text').get().strip(),
                'image_url' : response.css('img').attrib['src'],
                'description' : description
            }
        except:
            yield{
                'name': None,
                'image_url' : None,
                'description' : None
            }