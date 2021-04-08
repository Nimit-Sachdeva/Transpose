import pandas as pd
import datetime as dt
df=pd.read_excel('Tickets- Data.xlsx')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce').dt.strftime("%d/%m/%Y")
df = df.T
df.to_excel("Tickets- Data-Transpose.xlsx",encoding='utf-8')