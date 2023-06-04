# %%
from bs4 import BeautifulSoup
import pandas as pd
import os
# %%
path = os.path.join(os.getcwd(), 'data', 'watch-history.html')
with open(path, 'r', encoding='utf-8') as file:
    html_data = file.read()
# %%
soup = BeautifulSoup(html_data, 'html.parser')
# %%
