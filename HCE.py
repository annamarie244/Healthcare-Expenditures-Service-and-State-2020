import pandas as pd
import altair as alt
import streamlit as st

st.title ("Healthcare Expenditures by Service and State 2020")

healthcaredata = pd.read_csv ('/Users/annahowell/Documents/programming_directory/dsba5122/Healthcare-Expenditures-Service-and-State-2020/Untitled/HCE.py')
healthcaredata
