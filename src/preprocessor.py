import re

import pandas as pd


class Preprocessor(object):
    def __init__(self, input_object: object):
        self._preprocessed = self.preprocess(input_object)

    @property
    def preprocessed(self):
        return self._preprocessed

    def preprocess(self, input_object: object):
        pass


class SupplierPreprocessor(Preprocessor):
    """
    input is pandas dataframe
    1. lowercase the supplier name
    2. keep only digital and alphabet
    3. split string into list
    """

    def preprocess(self, input_object: pd.DataFrame) -> pd.DataFrame:
        """
        preprocess pandas dataframe series
        :return: pandas dataframe
        """
        df = input_object
        df['SupplierNameTokens'] = df['SupplierName'].str.lower().apply(self.tokenize)
        return df

    @staticmethod
    def tokenize(word: str) -> list(str):
        """
        keep only digital and alphabet
        :param word: supplier names
        :return: preprocessed supplier names
        """
        regx = '\W+'
        return re.split(regx, word)


class InvoicePreprocessor(Preprocessor):
    """
    Preprocess the invoice file text list
    1. unique the list
    """
    def preprocess(self, input_object: dict) -> dict:
        output = {}
        for i, words in input_object.items():
            output[i] = list(set(filter(None, [re.sub("[^0-9a-z]", "", word.lower()) for word in words])))

        return output
