
import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.subheader("Mahboobe Naserian Project.")
st.write("Read Data From PUBLIC shared google sheet.")

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

url = "https://docs.google.com/spreadsheets/d/13nMKSygHlORJKpvmKOrzicKRvb4gWyCoay0S-EtdHM0/edit?usp=sharing"

df = conn.read(spreadsheet=url, usecols=[0, 1])

st.dataframe(df)

# Print results.
for row in df.itertuples():
    st.write(f"Name : {row.name} ,Famil:{row.famil}:")