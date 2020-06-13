"""

Your task is to gather data from the Internet,
parse it and save to a csv file

To run the file you can use your ide or terminal:
python3 -m main gather
python3 -m main parse

The logging package helps you to better track how the processes work
It can also be used for saving the errors that arise

"""

import sys
import logging
import pandas as pd



from scraper import Scraper
from storage import Persistor
from parser import Parser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


SCRAPPED_FILE = 'scrapped_data.txt'
TABLE_FORMAT_FILE = 'data.csv'


def gather():
    logger.info("gather")
    storage = Persistor()

    scrapper = Scraper(storage)
    scrapper.scrape()


def parse():
    # parse gathered data and save as csv

    logger.info("parse")
    storage = Persistor()
    parser = Parser()

    raw_data = storage.read_raw_data()
    parsed_file = parser.parse_object(raw_data)
    storage.save_csv(parsed_file)


def stats():
    """ If you have time, you can calculate some statistics on the data gathered """
    logger.info("stats")
    coins = pd.read_csv('Coins.csv')
    coins['Prices'] = coins['Prices'].str.replace(',', '').astype(float)
    a = coins['CirculatingSupplys'].str.extract("(\d+\.\d+)?([MB])")[0].astype(float)
    b = coins['CirculatingSupplys'].str.extract("(\d+\.\d+)?([MB])")[1].fillna(1).replace({'M': 10 ** 6, 'B': 10 ** 7})
    coins['SupplyNum'] = a.multiply(b)
    print('Overall Info:')
    print(pd.DataFrame(coins.describe()))
    print('')
    print('Maximum Price Coin Info:', coins[coins['Prices'] == coins['Prices'].max()])
    print('')
    print('Minimum Price Coin Info:', coins[coins['Prices'] == coins['Prices'].min()])


    # Your code here
    # Load pandas DataFrame and print to stdout different statistics about the data.
    # Try to think about the data and use as different methods applicable to DataFrames.
    # Ask yourself what would you like to know about this data (most frequent word, average price, e.t.c.)


if __name__ == '__main__':
    """
    What does the line above mean
    https://stackoverflow.com/questions/419163/what-does-if-name-main-do
    """
    gather()
    parse()
    stats()
