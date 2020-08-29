# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
import os
import re
from .image_item import ImageItem
from functools import partialmethod

# site to pokemon wiki
site_url = 'https://www.wassilykandinsky.net/images/works/826.jpg?version=7'

class KandinskySpider(scrapy.Spider):
	name = 'kandinsky'

	def __init__(self):
		self.urls = []
		for i in range(1, 827):
			self.urls.append('https://www.wassilykandinsky.net/images/works/' + str(i) + '.jpg?version=7')

	def parse(self, response):
		url = response.url
		item = ImageItem()
		item['image_urls'] = [url]

		return item

	def start_requests(self):
		for url in self.urls:
			yield scrapy.Request(url, self.parse)


	
