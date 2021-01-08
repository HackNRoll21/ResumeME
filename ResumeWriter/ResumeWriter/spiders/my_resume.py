import scrapy
import time
import re
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class ResumeSpider(scrapy.Spider):
    name = "my-resume-spider"
    def __init__(self,link='',driver=''):
        self.start_urls = [f'{link}']
        opt = webdriver.ChromeOptions()
        opt.add_argument('disable-popup-blocking')
        self.driver = webdriver.Chrome(f'{driver}',chrome_options=opt)
    def parse(self, response):
        self.driver.get(response.url)
        desc = response.xpath('//*[text()="Job Description"]/../div/p/text()').getall()
        words = "".join(desc)
        out = {}
        out["1"] = words
        #words = []
        #for item in desc:
        #    words.append(re.split(',| |-|&|.', item))
        yield out
