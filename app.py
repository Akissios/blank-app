
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ajla Tomljanovic Shot Recorder", layout="centered")

st.title("🎾 Ajla Tomljanovic Shot Recorder")

# Initialize session state
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Opponent", "Penultimate Shot", "Ending Shot", "Final Result"])

# Input Form
with st.form("match_form"):
    col1, col2 = st.columns(2)

    opponent = col1.selectbox("Opponent", ["Burrage", "Pegula", "Okamura"])
    penultimate = col2.selectbox("Penultimate Shot", ["Backhand", "Forehand"])

    ending = col1.selectbox("Ending Shot", ["Backhand", "Forehand"])
    result = col2.selectbox("Final Result", ["Won", "Lost"])

    submitted = st.form_submit_button("Add Entry")
    if submitted:
        new_row = pd.DataFrame([[opponent, penultimate, ending, result]], columns=st.session_state.data.columns)
        st.session_state.data = pd.concat([st.session_state.data, new_row], ignore_index=True)
        st.success("Match entry added.")

# Show current data
st.subheader("📋 Recorded Entries")
st.dataframe(st.session_state.data, use_container_width=True)

# Save and Load
st.subheader("💾 Save / Load Data")

col3, col4 = st.columns(2)

with col3:
    csv = st.session_state.data.to_csv(index=False).encode("utf-8")
    st.download_button("Download CSV", csv, "match_data.csv", "text/csv")

with col4:
    uploaded = st.file_uploader("Upload CSV", type="csv")
    if uploaded:
        st.session_state.data = pd.read_csv(uploaded)
        st.success("Data loaded from CSV.")
