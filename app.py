import streamlit as st
import pandas as pd
from PIL import Image
df = pd.read_excel('trasn_cost.xlsx')

image = Image.open('favicon-300x300.png')

st.set_page_config(page_title='Cyprus Referees',
                   page_icon='favicon-300x300.png',)


col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(image, width=200)
with col2:
    st.title('Οδοιπορικά Διαιτητών που Δημοσιευθήκαν το 2022')
# st.write('omorfa')
# st.table(df)
# st.dataframe(df)
# df["No"].unique().sort()
mylist = list(df["City"].unique())
mylist.insert(0, 'None')

mylist.sort()

field_list = list(df)[1:]
field_list.sort()
field_list.insert(0, 'None')
st.sidebar.header('Please Filter Here')
city = st.sidebar.selectbox("Select City:", options=mylist,)
field = st.sidebar.selectbox("Select Stadium:", field_list,)

try:
    df_select = df.query("City == @city")[['City', field]]
    # st.dataframe(df_select)
    val = str(df_select[[field]])

    value2 = df_select[field].tolist()
    # st.info(f' From {city} to {field} €{value2[-1]} ')
    # st.title(f'{val[-2:]}')

    st.info(f' From  -{city}- to  -{field}- is €{value2[-1]} ')
    # st.info(f' {value2} ')

    columns = ['City', 'Stadium', 'Amount']
    data_for_df = [(city, field, value2[-1])]
    table_df = pd.DataFrame(data_for_df, columns=columns)
    st.table(table_df)
except:
    st.info(f'Select A Value To Sort ')
