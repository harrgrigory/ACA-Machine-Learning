from abc import ABC, abstractmethod
import codecs
import pandas as pd

class Persistor(): #ABC

    #@abstractmethod
    def read_raw_data(self):
        f = codecs.open('raw_html.html', 'r')
        return f.read()

    #@abstractmethod
    def save_raw_data(self, data):
        html_str = data
        html_file = open('raw_html'+'.html', 'w')
        html_file.write(html_str)
        html_file.close()
        #return None

    #@abstractmethod
    def save_csv(self, data):
        data.to_csv('Coins.csv', index=False)


    #@abstractmethod
    def append_data(self, data):
        return None
