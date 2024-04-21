# import scrapy
# # from scrapy_playwright.page import PageCoroutine

# class InstagramspiderSpider(scrapy.Spider):
#     name = "instagramSpider"
#     # allowed_domains = ["instagram.com"]
#     # start_urls = ["https://www.instagram.com/semu9304/"]
    
#     custom_settings = {
# 		'DOWNLOAD_DELAY': 2 # 2 seconds of delay
# 		}
    
#     # def start_requests(self):
#     #     # GET request
#     #     yield scrapy.Request("https://www.instagram.com/semu9304/", 
#     #           meta=dict(
#     #           playwright=True,
#     #           playwright_include_page=True,
#     #           playwright_page_methods=[
#     #               PageMethod("wait_for_selector", "article")
#     #               ]
#     #     ))
    

#     # async def  parse(self, response, **kwargs):
#     #     # 'response' contains the page as seen by the browser
#     #     return {
#     #       "url": response.url,
#     #       "text": response.tetx
#     #       }
#     def start_requests(self):
#         # GET request
#         yield scrapy.Request("https://shoppable-campaign-demo.netlify.app/#/", meta={"playwright": True})
     

#     def parse(self, response):
#         # 'response' contains the page as seen by the browser
#         yield {
#             # "url": response.url,
#             "text": response.text
#           }
import scrapy

class InstagramspiderSpider(scrapy.Spider):
    name = "instagramSpider"
    
    custom_settings = {
        'DOWNLOAD_DELAY': 2  # Add any other custom settings here
    }
    
    def start_requests(self):
        # GET request using Playwright
        yield scrapy.Request("https://shoppable-campaign-demo.netlify.app/#/", meta={"playwright": True})

    def parse(self, response):
        # 'response' contains the page as seen by the browser
        yield {
            "url": response.url,
            "text": response.text
        }
