"""
This crawler is looking for car offers from mobile.bg! You can pass links with saved searches from mobile 
through -a arguments. The arguments need to be in the format -a NAME=VALUE. You can then see them in the 
**kwargs argument in the __init__() method of the spider. You can also save these links in the file 
mobile_links.json in the same directory and use them for later searches. To save a link you need to specify 
car brand which will be used as a key to save the link under in the json file.

Optional arguments:
    -a car_brand=<car brand> -> the brand of the car
    -a link=<link for above car brand> -> link that will be used to search for car offers
    -a save_link=<true/false> -> a flag that will tell the spider to either save the link in the links file 
or not, default is to save the link if a car_brand is given, otherwise it does not save it; that applies even 
if the flag is set to true, without a car_brand argument specified, the link won't be saved

Usage: scrapy crawl mobile_bg -a car_brand=huyndai -a link='test-link.bg' -a save_link=true
"""

import time
import json
import scrapy


class MobileBGSpider(scrapy.Spider):
    name = 'mobile_bg'
    _page = 1
    _top_level_flag = True
    _offer_links = []
    # main_url = ['https://www.mobile.bg/pcgi/mobile.cgi']

    def __init__(self, *args, **kwargs):
        self.links = self._load_mobile_saved_links()
        print('*'*40)
        # print('*args: ', args)
        # print('**kwargs: ', kwargs.items())
        self.arguments = self._load_command_args(kwargs.items())
        self.start_urls = self._build_start_urls()

        if self.arguments.get('car_brand', None) and self.arguments.get('link', None) and self.arguments.get('save_link', 'false') == 'true':
            self._update_saved_links()

    
    def parse(self, response):
        """
        Need to crawl links from 2 levels deep:
            - first we crawl to filtered pages for the links to the different offers
            - the second step is to open each link and retrieve the information from there
        """
        car_offers_subjects = response.css(".mmm").extract()

        print('response: ', response)
        start_url = str(response).split(' ')[1][:-2]
        print('response start_url: ', start_url)
        offer_count = 1
        print('len(car_offers_subjects): ', len(car_offers_subjects))
        if len(car_offers_subjects) == 2:
            print('*********No More Pages To Crawl With This Filter**********')
            return
        for offer in car_offers_subjects:
            print(f'Offer number {offer_count} -> {offer}')
            print('type(offer): ', type(offer))
            offer_parts = offer.split('"')
            print('offer_parts: ', offer_parts)
            offer_link = 'https:' + offer_parts[1]
            print('offer_link: ', offer_link)

            # self._offer_links.append(offer)
            if offer_count == 3:
                print('Offer Count is 3***************************In If Blocks\n\n\n')
                inner_response = yield response.follow(offer_link, callback=self.parse_offer)
                print('Inner response: ', inner_response)
                time.sleep(1)
            
            offer_count += 1
        
        # go to the next page
        self._page += 1
        if self._page > 3:
            self._top_level_flag = False
            
        next_page = start_url + str(self._page)
        print('next_page: ', next_page)
        yield response.follow(next_page, callback=self.parse)


    def parse_offer(self, response):
        print('&&&&&&Parse Offer&&&&&&&&&')
        print('response: ', response)
        return response
    

    def _load_mobile_saved_links(self):
        with open('mobile_links.json', 'r') as f:
            links = json.load(f)
        
        print('Loaded links: ', links)
        return links

    
    def _save_new_link(self, links_dict):
        with open('mobile_links.json', 'w') as f:
            f.write(json.dumps(links_dict))


    def _load_command_args(self, args):
        values = {}
        for item in args:
            print(item)
            values[item[0]] = item[1]
        
        print('Unpacked args: ', values)
        return values


    def _update_saved_links(self):
        self.links[self.arguments.get('car_brand', 'empty')] = self.arguments.get('link', None)
        self._save_new_link(self.links)
    

    def _build_start_urls(self):
        start_urls = []
        if self.arguments.get('link', None):
            start_urls.append(self.arguments.get('link'))
        else:
            for item in self.links.values():
                start_urls.append(item)
        
        print('start_urls: ', start_urls)
        return start_urls
