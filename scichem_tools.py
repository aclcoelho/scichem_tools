import pandas as pd
import numpy as np
from requests import RequestException
from scihub import SciHub
import pubchempy as pcp
import os
from tqdm import tqdm
import pdfkit
from tenacity import *

def download_pdf(list_of_urls):
    """
    Downloads scientific articles using an unofficial API for Sci-Hub and stores it in a folder called 'Articles'
    Link for API = https://github.com/zaytoun/scihub.py

    Parameters
    ----------
    
    list_of_urls: list 
        A list containing url links to make requests

    """
    sh = SciHub()

    if not os.path.exists('Articles'):
        os.mkdir('Articles')

    for url in list_of_urls:
        if "sciencedirect" in url:
            identifier =  url.split('/')
            result = sh.download(url, path= f"Articles/{identifier[6]}")
            if not os.path.exists(f"Articles/{identifier[6]}"):
                try:
                    pdfkit.from_url(url, f"Articles/{identifier[6]}")
                except OSError:
                    pass
        else:
            identifier =  url.split('/')
            result = sh.download(url, path= f"Articles/{identifier[-1]}")

            if not os.path.exists(f"Articles/{identifier[-1]}"):
                try:
                    pdfkit.from_url(url, f"Articles/{identifier[-1]}")
                except OSError:
                    pass


@retry(retry=retry_if_exception_type(IOError) | retry_if_exception_type(ConnectionRefusedError) | retry_if_exception_type(ConnectionAbortedError) | retry_if_exception_type(ConnectionError) | retry_if_exception_type(ValueError))
def conversion(list_of_pubchem):
    smiles_list = []
    for id in tqdm(list_of_pubchem[:]):
        try:
            c = pcp.Compound.from_cid(id)
            smiles_list.append(c.isomeric_smiles)
            list_of_pubchem.remove(id)
        except:
            raise TryAgain

    df_smiles = pd.DataFrame(smiles_list)
    df_smiles.to_csv("df_smiles.csv", index=False)


