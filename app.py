

import streamlit as st
from datetime import datetime

st.title("CI/CD Python Dashboard - Live!")
st.success("Deployment pipeline is fully operational!")
st.metric(label="Server Status", value="Online", delta="Healthy")
st.caption(f"Last deployed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")