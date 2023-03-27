import streamlit as st
import pandas as pd

df = pd.read_excel('trasn_cost.xlsx')


st.set_page_config(page_title='my page', page_icon=':car:',)
st.title('Odoiporika Diathtwn 2022-2023')
st.write('omorfa')
# st.table(df)
# st.dataframe(df)
st.sidebar.header('Please Filter Here')
city = st.sidebar.selectbox("Select City:", options=df["No"].unique(),)
field = st.sidebar.selectbox("Select Stadium:", list(df)[1:],)
st.write(field)

st.info(f' From {city} to {field}')
df_select = df.query("No == @city")[['No', field]]
st.dataframe(df_select)
st.title('test')
