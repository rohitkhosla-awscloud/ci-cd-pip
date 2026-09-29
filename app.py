import streamlit as st

st.title("Simple CI/CD Python Dashboard")
st.write("Status: Active")
st.metric(label="Server Load", value="12%", delta="-2%")

