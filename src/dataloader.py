import pandas as pd
import json


class DataLoader(object):
    def __init__(self, filename):
        self._data = self.load(filename)

    @property
    def data(self):
        return self._data

    @staticmethod
    def load(filename):
        return filename


class SupplierDataLoader(DataLoader):
    """
    supplier names data loader
    """
    @staticmethod
    def load(filename):
        """
        load data from data file
        :param filename: filename
        :return: data
        """
        return pd.read_csv("data/suppliernames.txt")


class InvoiceDataLoader(DataLoader):
    """
    invoice data loader
    """
    @staticmethod
    def load(filename):
        """
        load data from data file
        :param filename: filename
        :return: data
        """
        words_dict = {}
        with open(filename) as f:
            for rows in f.readlines():
                dict_row = json.loads(rows.replace("'", "\"").replace("\n", ""))
                if dict_row["page_id"] not in words_dict:
                    words_dict[dict_row["page_id"]] = []
                words_dict[dict_row["page_id"]].append((dict_row["word"]))
        return words_dict
