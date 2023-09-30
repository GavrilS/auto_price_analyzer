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
if the flag is set to true, without a car_brand argument specified, the link won't be save

Usage: scrapy crawl mobile_bg -a car_brand=huyndai -a link='test-link.bg' -a save_link=true
"""

import json
import scrapy


class MobileBGSpider(scrapy.Spider):
    name = 'mobile_bg'
    # main_url = ['https://www.mobile.bg/pcgi/mobile.cgi']

    def __init__(self, *args, **kwargs):
        self._load_mobile_saved_links()
        print('*'*40)
        # print('*args: ', args)
        # print('**kwargs: ', kwargs.items())
        self._load_command_args(kwargs.items())


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
