import streamlit as st
import pandas as pd
from connect_db import connect_db

# 1. DB接続
connection = connect_db()
cursor = connection.cursor()

# 2. データ取得
cursor.execute("SELECT * FROM PRODUCTS;")
rows = cursor.fetchall()  # データを取得
columns = [desc[0] for desc in cursor.description]  # カラム名取得

# 3. pandas DataFrame に変換
df = pd.DataFrame(rows, columns=columns)

# 4. Streamlit で表示
st.title("商品一覧")
st.dataframe(df)

# 5. 後片付け
cursor.close()
connection.close()