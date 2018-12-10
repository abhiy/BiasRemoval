import scrapy
import json

class CricAUSpider(scrapy.Spider):
    name = "cricau"
    start_urls = ["https://www.cricket.com.au/players"]
    base_url = "https://www.cricket.com.au"

    def parse(self, response):
        response_men = response.css('div.filter-men')
        response_women = response.css('div.filter-women')
        
        for item in response_men:
            link = item.css('a::attr(href)').extract()
            player_url = self.base_url+link[0]
            name = link[0].split('/')[2]
            yield scrapy.Request(url=player_url, callback=self.parse_inner,meta={'gender': "M" , 'name':name})

        for item in response_women:
            link = item.css('a::attr(href)').extract()
            player_url = self.base_url+link[0]
            name = link[0].split('/')[2]
            yield scrapy.Request(url=player_url, callback=self.parse_inner,meta={'gender': "F",'name':name})

    def parse_inner(self, response):
        gender = response.meta.get('gender')
        name = response.meta.get('name')
        img_url = self.base_url + response.css('img.player-img::attr(src)').extract()[0]
        age_div = response.css('div.player-physical-bio > .col-padding-right')[0]
        age = age_div.css('.stats-container::text').extract()[0].strip()
        if (age == ""):
            age = "TBD"
        yield {'name': name, 'age': age , "gender": gender , "img_url" : img_url}
