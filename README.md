# README

### Run it

### step 1. install python and packages

- download and install python from https://www.python.org/downloads/
- install package from requirements.txt

```sh
pip install -r requirements.txt
```

### step 2. run the match algorithm

```sh
python .\match.py --invoice INVOICE_FILENAME --supplier SUPPLIER_FILENAME
# eg.
python .\match.py --invoice "data/invoice.txt" --supplier "data/suppliernames.txt"
```