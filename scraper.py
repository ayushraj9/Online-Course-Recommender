import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://ec2-13-233-68-92.ap-south-1.compute.amazonaws.com:9000/',
        'http://ec2-13-233-68-92.ap-south-1.compute.amazonaws.com/mlearning.css'
    ]
    
    
    def parse(self, response):
        
        for navbar in response.css('div.row'):
            yield {
                 'author':navbar.css('div.main h2::text').extract(),
                 'test':navbar.css('div.side p::text').extract(),
                 'ah':navbar.css('div.side a::text').extract(),
            }

        for navbar in response.css('div.navbar'):
            yield {
                 'nav':navbar.css('a::attr(href)').extract()
            }
           # next_page = response.css('a::attr(href)').extract_first()
           # if next_page:
            #    yield scrapy.Request(
             #   response.urljoin(next_page),
              #  callback=self.parse
               # )

        

        

