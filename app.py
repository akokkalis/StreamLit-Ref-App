import streamlit as st
import pandas as pd

df = pd.read_excel('trasn_cost.xlsx')


st.set_page_config(page_title='my page', page_icon=':car:',)
st.title('Οδοιπορικά Διαιτητών που Δημοσιευθήκαν το 2022')
st.write('omorfa')
# st.table(df)
# st.dataframe(df)
# df["No"].unique().sort()
mylist = df["City"].unique()
mylist.sort()

field_list = list(df)[1:]
field_list.sort()
st.sidebar.header('Please Filter Here')
city = st.sidebar.selectbox("Select City:", options=mylist,)
field = st.sidebar.selectbox("Select Stadium:", field_list,)
st.write(field)

st.info(f' From {city} to {field} € ')
df_select = df.query("City == @city")[['City', field]]
st.dataframe(df_select)
val = str(df_select[[field]])
st.title(f'{val[-2:]}')

st.title(f' From  -{city}- to  -{field}- is €{val[-2:]} ')
st.info(f' From " {city} " to " {field} " is €{val[-2:]} ')
