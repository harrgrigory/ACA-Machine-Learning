from object import Item
from bs4 import BeautifulSoup
import pandas as pd

class Parser:

    def parse_object(self, content): # parse_data
        property_1 = self.get_property_1(content)
        property_2 = self.get_property_2(content)
        property_3 = self.get_property_3(content)
        property_4 = self.get_property_4(content)
        property_5 = self.get_property_5(content)

        return pd.concat([property_1, property_2, property_3, property_4, property_5], axis=1)

    def get_property_1(self, content): # Names
        names = []
        soup = BeautifulSoup(content, 'html.parser')
        for listing in soup.find_all('tr', attrs={'class': 'simpTblRow'}):
            for name in listing.find_all('td', attrs={'aria-label': 'Name'}):
                names.append(name.text)

        return pd.Series(names, name='Names')

    def get_property_2(self, content): # Prices
        prices = []
        soup = BeautifulSoup(content, 'html.parser')
        for listing in soup.find_all('tr', attrs={'class': 'simpTblRow'}):
            for price in listing.find_all('td', attrs={'aria-label': 'Price (Intraday)'}):
                prices.append(price.find('span').text)

        return pd.Series(prices, name='Prices')

    def get_property_3(self, content): # Changes
        changes = []
        soup = BeautifulSoup(content, 'html.parser')
        for listing in soup.find_all('tr', attrs={'class': 'simpTblRow'}):
            for change in listing.find_all('td', attrs={'aria-label': 'Change'}):
                changes.append(change.text)

        return pd.Series(changes, name='Changes')

    def get_property_4(self, content): # PercentChanges
        percentChanges = []
        soup = BeautifulSoup(content, 'html.parser')
        for listing in soup.find_all('tr', attrs={'class': 'simpTblRow'}):
            for percentChange in listing.find_all('td', attrs={'aria-label': '% Change'}):
                percentChanges.append(percentChange.text)

        return pd.Series(percentChanges, name='PercentChanges')

    def get_property_5(self, content):
        circulatingSupplys = []
        soup = BeautifulSoup(content, 'html.parser')
        for listing in soup.find_all('tr', attrs={'class': 'simpTblRow'}):
            for circulatingSupply in listing.find_all('td', attrs={'aria-label': 'Circulating Supply'}):
                circulatingSupplys.append(circulatingSupply.text)

        return pd.Series(circulatingSupplys, name='CirculatingSupplys')
