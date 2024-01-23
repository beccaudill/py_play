'''
READ CSV FILE INTO PANDAS DATAFRAME,
TRIM THE 'LOINC Related Names' FIELD TO 255 CHARS,
AND WRITE DATAFRAME DATA BACK INTO THE CSV FILE.
1/10/2024, Rebecca Caudill
'''

import pandas as pd

df = pd.read_csv('C:\\py_files\\CSV Files\\LabOrder_SpecSrc_to_LOINC.csv')

for x in df.index:
    a = df.loc[x, "LOINC Related Names"]
    b = df.loc[x, "Order Code"]
    c = a[0:255]
    if len(a) > 255:
        print(a)
        df.loc[x, "LOINC Related Names"] = c
        print(c)
        df.to_csv('C:\\py_files\\CSV Files\\LabOrder_SpecSrc_to_LOINC.csv', index=False)
        print(b)


