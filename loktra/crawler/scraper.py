from __future__ import print_function
from sys import argv
from lxml import html
import requests
import time
import multiprocessing
import getopt

# logging
import logging
logging.basicConfig(filename='log/exception_logging.txt', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

# constants
MIN_PE_THRESHOLD = 0
MAX_PE_THRESHOLD = 15
MIN_EPS_THRESHOLD = 0
COMPANY_URL = "http://www.shopping.com/products"


def _get_company_primary_stats(company, tree):
    pe_ratio = company.get_pe_ratio(tree)
    eps = company.get_eps(tree)
    price_of_stock = company.get_price_of_stock(tree)
    fifty_two_wk_high = company.get_fifty_two_wk_high(tree)
    fifty_two_wk_low = company.get_fifty_two_wk_low(tree)
    return {'pe_ratio': pe_ratio,
            'eps': eps,
            'price_of_stock': price_of_stock,
            'fifty_two_wk_high': fifty_two_wk_high,
            'fifty_two_wk_low': fifty_two_wk_low}


def company_page_analysis(stock_company):
    try:
        page = requests.get('http://money.rediff.com/%s' % stock_company)
        time.sleep(2)
        tree = html.fromstring(page.content)
        company = CompanyPage(tree)
        primary_stats = _get_company_primary_stats(company, tree)
        if all([primary_stats.get('pe_ratio') > MIN_PE_THRESHOLD, primary_stats.get('pe_ratio') < MAX_PE_THRESHOLD, primary_stats.get('eps') > MIN_EPS_THRESHOLD, primary_stats.get('price_of_stock') < ((primary_stats.get('fifty_two_wk_high') + primary_stats.get('fifty_two_wk_low'))/2)]):


            #get all links
            balance_sheet_link = company.get_balance_sheet_link(tree)
            dividend_link = company.get_dividend_link(tree)
            ratio_link = company.get_ratio_link(tree)

            # go to balance sheet page for further analysis
            balance_sheet_page = requests.get('%s' % ''.join(balance_sheet_link))
            balance_sheet_tree = html.fromstring(balance_sheet_page.content)
            balance_sheet = BalanceSheet(balance_sheet_tree)
            current_assets_loans_advances = balance_sheet.get_current_assets_loans_advances(balance_sheet_tree)
            current_liabilities_and_provisions = balance_sheet.get_current_liabilities_and_provisions(balance_sheet_tree)
            total_net_current_assets = balance_sheet.get_total_net_current_assets(balance_sheet_tree)
            if total_net_current_assets > current_liabilities_and_provisions:
                # go to ratio page
                ratio_page = requests.get('%s' % ''.join(ratio_link))
                ratio_tree = html.fromstring(ratio_page.content)
                ratio = Ratio(ratio_tree)
                if ratio.consistent_dividend_payout(ratio_tree):
                    print(stock_company)

    except Exception as err:
        logger.error(err)


    return

def crawler(keyword, page_number=None):
    global COMPANY_URL
    try:
        if keyword and page_number:
            page = requests.get('%s~PG-%s?KW=%s' %
                                (COMPANY_URL, page_number, keyword))
        page = requests.get('%s?KW=%s' %
                            (COMPANY_URL, keyword))
        print(page)
    except Exception as err:
        logger.error(err)

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hg:d", ["help", "grammar="])
        print(opts, args)
        keyword = args[1]
        if len(args) == 3:
            page_number = args[2]
            crawler(keyword, page_number)
        crawler(keyword)
    except getopt.GetoptError:
        #usage()
        #sys.exit(2)a
        pass


if __name__ == '__main__':
    main(argv)
