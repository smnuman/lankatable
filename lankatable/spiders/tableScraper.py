import scrapy

from lankatable.items import LankatableItem

class TableScraper(scrapy.Spider):
    """docstring for TableScraper."""
    name = "table"
    allowed_domains = ["lankabd.com"]
    start_urls = [
        "http://lankabd.com/dse/stock-market/GSPFINANCE/gsp-finance-company-(bangladesh)-limited-/financial-statements?companyId=300&stockId=287",
    ]

    def parse(self,response):
        Item = LankatableItem()
        Item['industry'] = response.css('.portalTitleL2 ::text').extract_first().split(' - ')[-2]
        Item['ticker']   = response.css('.portalTitle.companyTitle ::text').extract_first().split(' (')[-1].strip(')')
        Item['yearEnd']  = response.css('.note>font::text').extract_first()
        # text in a row-cell
        # Item['summery'] = {}
        # for tr in response.xpath(".//*[@id='summery']/table/tbody/tr"):
        #     Item['summery']['title'] = tr.xpath('.//td[1]/text()').extract_first().strip()
        #     Item['summery']['y2011'] = tr.xpath('.//td[2]/span/text()').extract_first().strip()
        #     print Item

        trs=response.xpath("//*[@id='summery']/table/tr")
        Item['summery']=[]
        for tr in trs:
            td1=tr.xpath('normalize-space(.//td[@class="data-Fincell01"]/text())').extract()
            if (not td1[0]):
                td1=tr.xpath('normalize-space(.//th[@class="summ-head"]/text())').extract()
            td=tr.xpath('.//td[@class="data-Fincell02"]/span/text()')       # collect cell-contents
            xtd = [x.strip() for x in td.extract() if x.strip()]            # remove garbage spaces
            xtd = [''.join(x.split(',')) for x in xtd if x ]                # remove commas for number formatting
            xtd = ['-'.join(x.split('(')).strip(')') for x in xtd if x ]    # remove parentheses for negative number
            if (not td):
                # print("Empty td found !!!")
                Item['summery'].append([td1[0]])
            else:
                Item['summery'].append([td1[0],[ float(x) for x in xtd if x ] ])          # convert and store simplified numbers
        yield Item

        print "Hello World!"
