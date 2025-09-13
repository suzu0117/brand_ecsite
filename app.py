import streamlit as st
import os
import psycopg2

st.title("Streamlit + Render DB接続テスト")

try:
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST"),
        database=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASS")
    )
    st.success("DB接続成功！")
    conn.close()
except Exception as e:
    st.error(f"接続エラー: {e}")
