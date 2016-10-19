from __future__ import print_function
from sys import argv
from lxml import html
import requests
import getopt
import random

# logging
import logging
logging.basicConfig(filename='log/exception_logging.txt', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

# constants
COMPANY_URL = "http://www.shopping.com/products"


def results_count(page):
    tree = html.fromstring(page.content)
    upper = 100
    lower = 1
    pivot = random.randint(1, 100)
    while True:
        if len(tree.xpath(".//*[@id='nameQA%s']" % pivot)) > 0:
            if len(tree.xpath(".//*[@id='nameQA%s']" % (pivot + 1))) == 0:
                return pivot
            else:
                pivot += 1
        else:
            pivot -= 1


def crawler(keyword, page_number=None):
    global COMPANY_URL
    try:
        if keyword and page_number:
            page = requests.get('%s~PG-%s?KW=%s' %
                                (COMPANY_URL, page_number, keyword))
        page = requests.get('%s?KW=%s' %
                            (COMPANY_URL, keyword))
        return results_count(page)
    except Exception as err:
        logger.error(err)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hg:d", ["help", "grammar="])
        print(opts, args)
        keyword = args[1]
        if len(args) == 3:
            page_number = args[2]
            print(crawler(keyword, page_number))
        print(crawler(keyword))

    except getopt.GetoptError:
        #usage()
        #sys.exit(2)a
        pass


if __name__ == '__main__':
    main(argv)
