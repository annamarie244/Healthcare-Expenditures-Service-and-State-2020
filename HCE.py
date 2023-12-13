import streamlit as st
import pandas as pd
import altair as alt
import streamlit as st

st.title ("Distribution of Health Care Expenditures by Service by State of Residence in 2020 (in millions)")

file_path = pd.read_csv("/Users/annahowell/Documents/programming_directory/dsba5122/Healthcare-Expenditures-Service-and-State-2020/Untitled/Healthcare Expenditures.csv",delimiter='\t')


def create_page1():
    st.title("Introduction")
    st.subheader("Overview of the US Healthcare System")
    text = "The US healthcare system is one of the most expensive in the world due to a variety of factors. One of the main reasons is the high cost of medical care and prescription drugs, which is driven by a lack of price regulation and negotiation, as well as the complexity of the healthcare system. Additionally, hospital fees have been increasing over time for a number of reasons. Some of the main factors contributing to rising hospital costs include technological advancements, administrative costs, and insurance coverage."
    st.write(text)
    


