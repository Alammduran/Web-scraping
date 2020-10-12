# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class InmuCasaVtaGdlItem(scrapy.Item):
    titulo = scrapy.Field()
    direccion = scrapy.Field()
    precio = scrapy.Field()
    descripcion = scrapy.Field()
 
    construido = scrapy.Field()
    terreno = scrapy.Field()
    fecha  = scrapy.Field()
    ide = scrapy.Field()
    
    pass
