import pandas as pd
import altair as alt
import streamlit as st

st.title ("Healthcare Expenditures by Service and State 2020")

healthcaredata = pd.read_csv ('Healthcare Expenditures.csv')
healthcaredata
