import numpy as np
import pandas as pd
import pdfplumber


with pdfplumber.open("final.pdf") as pdf:
    data = []
    for page in pdf.pages:
        text = page.extract_text()

        lines = text.split('/n')
        data.extend([line.split(',') for line in lines])

df = pd.DataFrame(data, columns=['data'])

df.head(10)



