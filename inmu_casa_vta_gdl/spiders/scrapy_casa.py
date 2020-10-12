#%% 
import scrapy, time, datetime
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from inmu_casa_vta_gdl.items import InmuCasaVtaGdlItem



class InmuCasaVtaGdlItemm(CrawlSpider):
    a = time.strftime("%d%m%y")
    name = "inmu_casa_vta_gdl_" + a
    item_count = 0
    allowed_domain = "www.inmuebles24.com"
    start_urls = [
            "https://www.inmuebles24.com/casas-en-venta-en-guadalajara.html"
            ]
    
    rules = {
            Rule(LinkExtractor(allow =(), restrict_xpaths = ('//li[@class="pag-go-next"]/a'))),
            Rule(LinkExtractor(allow =(), restrict_xpaths = ('//h3[@class = "posting-title"]')), callback = 'parse_item', follow = False)
      
    }

    def parse_item(self, response):
        mi_item = InmuCasaVtaGdlItem()
        
        
        mi_item['titulo'] = response.xpath('//div[@class="section-title"]/h1/text()').extract()
        mi_item['direccion'] = response.xpath('normalize-space(//h2[@class="title-location"]').extract()
        mi_item['precio'] = response.xpath('normalize-space(//*[@id="sidebar-price-container"]/div/div[1]/div[2]/span/text())').extract()
        mi_item['descripcion'] = response.xpath('normalize-space(//*[@id="verDatosDescripcion"])').extract()
        mi_item['construido'] = response.xpath('normalize-space(//*[@id="article-container"]/section[1]/ul/li[2]/b/text())').extract()
        mi_item['terreno'] = response.xpath('normalize-space(//*[@id="article-container"]/section[1]/ul/li[1]/b/text())').extract()
        mi_item['fecha'] = response.xpath('normalize-space(//*[@id="article-container"]/section[1]/h5//text()[2])').extract()
        mi_item['ide'] = response.xpath('normalize-space(//*[@id="article-container"]/section/span[2]/text())').extract()


        
        self.item_count += 1
        if self.item_count > 5000 :
            raise CloseSpider('item_exceeded')
        yield mi_item
#%%
        