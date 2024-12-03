import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://s.askci.com/data/economy/00031/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# 找到表格
tables = soup.find_all("table")
data = []
for table in tables:
    df = pd.read_html(str(table))[0]
    data.append(df)
    # 保存为csv文件，文件名字从table1到table5
    df.to_csv(f"./data/table{tables.index(table)+1}.csv", index=False)

# # 合并数据并清洗
# combined_data = pd.concat(data)
# combined_data.dropna(inplace=True)
