### SciChem Tools
A python module containing a few useful chemistry and scientific oriented tools!

#### download_pdf
Downloads scientific articles by checking first on SciHub and, if not possible to download, by using PDFKit
Saves the articles in a folder named "Articles"
```
>>>from scichem_tools import download_pdf
>>>list_of_pdf = ["http://examplearticle/doi/randomnumbers",]
>>>download_pdf(list_of_pdf)
```

#### conversion
Convert PubChem Ids into SMILES 
Saves the results in a CSV file names "df_smiles.csv"
```
>>>from scichem_tools import conversion
>>>list_of_pdf = ["2244",]
>>>conversion(list_of_pdf)
```