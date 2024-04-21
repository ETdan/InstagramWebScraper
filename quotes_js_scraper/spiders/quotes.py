# import scrapy
from quotes_js_scraper.items import QuoteItem
from scrapy_splash import SplashRequest
import base64

# class QuotesSpider(scrapy.Spider):
#     name = 'quotes'

#     # lua_script = """
#     # function main(splash, args)
#     #     local max_scrolls = 10   -- Maximum number of scrolls
#     #     local scroll_count = 0   -- Counter for scroll attempts

#     #     assert(splash:go(args.url))
        
#     #     -- Scroll the page until the <article> element is found or the maximum number of scrolls is reached
#     #     while scroll_count < max_scrolls do
#     #         -- Check if the <article> element is present
#     #         if splash:select('article') then
#     #             break  -- Exit the loop if the <article> element is found
#     #         end

#     #         -- Scroll the page
#     #         splash:runjs("window.scrollBy(0, window.innerHeight)")  -- Scroll down by the height of the viewport
#     #         scroll_count = scroll_count + 1

#     #         splash:wait(0.5)  -- Wait for 0.5 seconds after each scroll
#     #         print('Scrolling...')
#     #     end
        
#     #     return {html=''}
#     # end


#     # """

#     def start_requests(self):
#         url = 'https://www.instagram.com/dagigimaxmo/'
        
#         # yield SplashRequest(url, callback=self.parse, endpoint='execute', args={'wait': 2, 'lua_source': self.lua_script, 'url': url})
#         yield SplashRequest(url, callback=self.parse, endpoint='render.json', args={'wait':2,'html':1,'png':1,'width':1000})
        
#     def parse(self, response):
#         self.logger.info("////////////////////////////////////////////////////////////////////////////")
#         image = base64.b64decode(response.data['png'])
#         with open('modified_page.png', 'wb') as file:
#             file.write(response.text)
#     # def parse(self, response):
#     #     self.logger.info("////////////////////////////////////////////////////////////////////////////")
#     #     with open('modified_page.html', 'w', encoding='utf-8') as file:
#     #         file.write(response.text)
            
#     #     item = QuoteItem()
#     #     yield {"html": response.text}
import scrapy
import re
# /////////////////////////
# class QuotesSpider(scrapy.Spider):
#     name = 'quotes'

#     def start_requests(self):
#         url = 'https://www.instagram.com/dagigimaxmo/'
#         yield scrapy.Request(url, self.parse)
        
#     def parse(self, response):
#         self.logger.info("////////////////////////////////////////////////////////////////////////////")

#         # Your code
#         cookies = response.headers.getlist('Set-Cookie')
#         print(cookies)
#         csrftoken_match = re.search(r'csrftoken=(\w+)', cookies[0].decode('utf-8'))

#         if csrftoken_match:
#             csrftoken = csrftoken_match.group(1)
#             with open('response_headers.txt', 'w') as file:
#                 file.write(str(csrftoken))
#         else:
#             print("No csrftoken found in cookies.")

#         response =  SplashRequest('https://www.instagram.com/dagigimaxmo/', self.parse,cookies=csrftoken)
        # print(response.text
# ////////////////////////////////////////////////
import scrapy
# from scrapy_splash import SplashRequest

# class InstagramSpider(scrapy.Spider):
#     name = 'instagram'

#     def start_requests(self):
#         url = 'https://www.instagram.com/'
#         cookies = {
#             'csrftoken': 'MIGgAtsynhJcnVuK7J5X7AhaBjNwByB8',
#             'sessionid': '26317102907%3AxrxFFWv0cPmyhN%3A12%3AAYdTUePOdHC1tRw3_ubpggYkJoQfBHoVVakzG2NnMMw'
#         }
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
#         }
#         yield SplashRequest(url, self.parse, args={'wait': 2})
#         # yield SplashRequest(url, callback=self.parse, endpoint='render.json', args={'wait':2,'html':1,'png':1,'width':1000})

#     def parse(self, response):
#         # Print out the response headers
#         self.logger.info("Response Headers: %s", response.headers)
#         filename = 'response.html'
#         with open(filename, 'wb') as f:
#             f.write(response.body)
#         self.log(f'Saved file {filename}')
        # imgdata = base64.b64decode(response.data['png'])
        # filename = 'some_image.png'
        # with open(filename, 'wb') as f:
        #     f.write(imgdata)
# class PlaywrightSpider(scrapy.Spider):
import scrapy
from scrapy_playwright.requests import PlaywrightRequest


class InstagramSpider(scrapy.Spider):
    name = "spider"

    def start_requests(self):
        yield PlaywrightRequest("https://www.instagram.com/")

    def parse(self, response):
        self.logger.info("Response Headers: %s", response.headers)
        filename = 'response.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
