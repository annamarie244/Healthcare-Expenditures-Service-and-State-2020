import pandas as pd
import altair as alt
import streamlit as st

st.title("HCE")

Healthcare_Expenditure = pd.read_csv("Healthcare Expenditures.csv")
Healthcare_Expenditure
