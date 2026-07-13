import streamlit as st

st.set_page_config(page_title="ETL Dashboard", page_icon="📊", layout="wide")

st.title("📊 Customer Orders ETL Dashboard")

st.markdown("---")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("total orders", "0")

with col2:
    st.metric("Total Reveniue", "$0")

with col3:
    st.metric("Pipeline status", "🟢 Ready")

st.markdown("---")

st.subheader("orders")

st.info("Database data will appear here in the next step..")
