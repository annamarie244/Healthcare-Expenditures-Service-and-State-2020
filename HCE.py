import pandas as pd
import altair as alt
import streamlit as st

st.title ("Healthcare Expenditures by Service and State 2020")

healthcare = pd.DataFrame(pd.read_csv("Healthcare_Expedintures.csv"))
print(healthcare)

