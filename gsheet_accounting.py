
import streamlit as st
import pandas as pd
import numpy as np

from streamlit_gsheets import GSheetsConnection

def AddNewRow():
    conn = st.connection("gsheets", type=GSheetsConnection)

    existing_entries = conn.read(worksheet="Sheet1",usecols=[0,1,2,3])

    current_seat = {
     'Date': '2024/06/12',
     'Description': 'Test',
     'Credit': 1000,
    'Debit': 0
    }


    #current_seat = ['2024/06/12','Test', 1000, 0]
    

    st.write("New seats")
    st.dataframe(current_seat)
    st.write("existing_entries seats")
    st.dataframe(existing_entries)

    updated_seats = existing_entries | current_seat    
    bookit = conn.update(worksheet="Sheet1", data=current_seat)

def DrawbarChart():
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.bar_chart(chart_data)

st.subheader("Mahboobe Naserian Accounting Project.")
st.write("Show List")

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(usecols=[0,1,2,3])
st.dataframe(df)

chart_data = pd.DataFrame(df)
st.bar_chart(chart_data,x="Description",y=["Credit","Debit"])
