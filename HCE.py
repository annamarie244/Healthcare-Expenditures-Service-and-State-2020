import pandas as pd
import altair as alt
import streamlit as st

st.title ("Healthcare Expenditures by Service and State 2020")

HealthcareE = st.file_uploader("upload file", type={"csv", "txt"})
if HealthcareE is not None:
    HealthcareE_df = pd.read_csv(HealthcareE)
st.write(HealthcareE_df)