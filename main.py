#!/usr/bin/env python
# -*- coding: utf-8 -*-
#coding=utf-8
from scrapy import cmdline
def main(name):
    if name:
        cmdline.execute(name.split())
if __name__ == '__main__':
    name = "scrapy crawl flipkartSpider"
    main(name)
