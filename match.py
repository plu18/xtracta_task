import pandas as pd

from src.dataloader import SupplierDataLoader, InvoiceDataLoader
from src.preprocessor import SupplierPreprocessor, InvoicePreprocessor

import argparse


def match_suppliers(words: list(str), suppliernames: pd.DataFrame) -> dict:
    matched_names = {}

    # check from the supplier name list
    for _, supplier in suppliernames.iterrows():
        # for each word in one page
        for word in words:
            # check from the supplier name list
            if word in supplier['SupplierNameTokens']:
                if supplier["SupplierName"] not in matched_names:
                    matched_names[supplier["SupplierName"]] = [1] * len(supplier['SupplierNameTokens'])
                matched_names[supplier["SupplierName"]][supplier['SupplierNameTokens'].index(word.lower())] = 0
                # if the all supplier name token have matched with words
                # return the supplier name
                if sum(matched_names[supplier["SupplierName"]]) == 0:
                    return supplier["SupplierName"]

    # if no matched supplier name return emtpy dict
    return matched_names


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Match supplier names from OCR results from invoice file.')

    parser.add_argument("--invoice", help="invoice file name", type=str, required=True)
    parser.add_argument("--supplier", help="supplier names file name", type=str, required=True)

    args = parser.parse_args()

    # load data
    sdl = SupplierDataLoader(args.supplier)
    idl = InvoiceDataLoader(args.invoice)

    # preprocess data
    sp = SupplierPreprocessor(sdl.data)
    ip = InvoicePreprocessor(idl.data)

    # match words with supplier names
    results = {}
    for page_id, words in ip.preprocessed.items():
        matched_suppliers = match_suppliers(words=words,
                                            suppliernames=sp.preprocessed)
        results[page_id] = matched_suppliers

    print("Found matched suppliers")
    print(results)
