# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline


class KandinskyPipeline(ImagesPipeline):
	abs_image_path = 'C:/Users/James/projects/kandinsky-abstract-art/images'

	def file_path(self, request, response=None, info=None):
		return request.url.split('/')[-1].split('?')[0]

	def get_media_requests(self, item, info):
		for url in item['image_urls']:
			yield scrapy.Request(url)

    # def process_item(self, item, spider):
    #     return item
