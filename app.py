import streamlit as st
from datetime import datetime

st.title("Simple CI/CD Python Dashboard")
st.write("Status: Active & Deployed via GitHub Actions!")
st.metric(label="Server Load", value="15%", delta="+3%")
st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

