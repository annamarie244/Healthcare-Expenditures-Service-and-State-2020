import streamlit as st
import pandas as pd
import altair as alt
import streamlit as st
import plotly.express as px

st.title ("Distribution of Health Care Expenditures by Service by State of Residence in 2020 (in millions)")

HealthcareData = pd.read_csv("/Users/annahowell/Documents/programming_directory/dsba5122/Healthcare-Expenditures-Service-and-State-2020/Untitled/Healthcare Expenditures.csv",delimiter='\t')

pd.DataFrame(HealthcareData)

def create_page1():
    st.title("Opening Page")
    st.bar_chart(HealthcareData)


