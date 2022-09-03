import streamlit as st
import pandas as pd

st.sidebar.radio(
    "Select an option",
    ("Medal Tally", "Overall analysis", "Country wise analysis", "Athlete wise analysis")
)

