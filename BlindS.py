import scrapy
import random
import hashlib
import array

linksn = []
namen = []

class BItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()

class BlindSpider(scrapy.Spider):
    name = "blind_spider"
    start_urls = ['https://www.w3schools.com/']
    
    
    
    #def print_it(self,link):
        #item = BItem()
        #yield
        #{
                
            #'link':link
            #}
        
    def parse(self, response):
        links = response.xpath('//a/@href').extract()
        text = response.xpath('//a/text()').extract()
        
        namen.append(text)
        linksn.append(links)
        item = BItem()
        
        print("listst")
        print(linksn)
        print(namen)
            
        item['name'] = text
        item['link'] = links
        
        disp = []
        term = input('Enter the search')
        nonce = random.randint(1,100000)
        nonce = str(nonce)
        l = [ord(a) ^ ord(b) for a,b in zip(nonce, term)]
        l = ''.join(str(e) for e in l)
        #print(l)
        hash_object = hashlib.md5(l.encode())
        for  name in namen:
            for idx, n in enumerate(name):
                for t in n.split():
                    l2 = [ord(a) ^ ord(b) for a,b in zip(nonce, t)]
                    l2 = ''.join(str(e) for e in l2)
                    new_ciph = hashlib.md5(l2.encode())
                    if new_ciph.hexdigest() == hash_object.hexdigest():
                        print(t)
                        disp.append(linksn[0][idx])
                    
                    
            
                
                
        print("Displayyy")
        print(disp)
        yield item
        #print(links)
        #crawled = []
        

        
        #for link in links:
      ## If it is a proper link and is not checked yet, yield it to the Spider
            #if  not link in crawled:
                #link = "https://www.w3schools.com/" + link
                #crawled.append(link)
                #yield scrapy.Request(url= link, callback = self.print_it)
                

    
