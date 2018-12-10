import scrapy
import re
class SportsSpider(scrapy.Spider):
    name = "sports"
    base_url = "https://www.cricbuzz.com/profiles/"
    img_base_url = "https://www.cricbuzz.com"
    def start_requests(self):
        for i in range(14300):
            url = self.base_url + str(i+1)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        name = response.css('h1::text').extract()
        img_url_relative = response.css('img::attr(src)').re(r'/stats/img.*')[0]
        age = response.css('div.cb-lst-itm-sm::text')[1].extract()
        gender = response.css('div.cb-lst-itm-sm::text')[-1].extract()
        if(age == "--"):
            age = "TBD"
        else:
            within_brackets_term = age.split('(')
            if len(within_brackets_term) >= 2:
                remove_space = within_brackets_term[1].split(' ')
                if len(remove_space) >= 1:
                    age = remove_space[0]
                else:
                    age = "TBD"
            else:
                age = "TBD"

        if(gender == "--"):
            gender = "TBA"
        else:
            if re.search('women', gender, re.IGNORECASE):
                gender = "F"
            else:
                gender = "M"

        print("gender final is ",gender)
        self.log(name)
        self.log(img_url_relative)
        
        if name and img_url_relative != "" and age != '--':
            yield {
                'name': name[0],
                'img_url': self.img_base_url + img_url_relative,
                'age' : age,
                'gender': gender
            }