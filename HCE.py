import streamlit as st
import pandas as pd
import altair as alt
import streamlit as st
import plotly.express as px

st.title ("Distribution of Health Care Expenditures by Service by State of Residence in 2020 (in millions)")

HealthcareData = pd.read_csv("/Users/annahowell/Documents/programming_directory/dsba5122/Healthcare-Expenditures-Service-and-State-2020/Untitled/Healthcare Expenditures.csv",delimiter='\t')

pd.DataFrame(HealthcareData)

def main():
    st.title("Multi-Page Streamlit App")

    menu = ["Home", "Page 1", "Page 2"]
    choice = st.sidebar.selectbox("Navigate", menu)

    if choice == "Home":
        home_page()
    elif choice == "Page 1":
        page1()
    elif choice == "Page 2":
        page2()

def home_page():
    st.subheader("Home Page")
    st.write("Welcome to the home page!")

def page1():
    st.subheader("Page 1")
    st.write("This is Page 1.")
    st.plotly_chart({"data": [{"x": [1, 2, 3], "y": [1, 3, 2], "type": "scatter"}], "layout": {"title": "Page 1 Chart"}})

def page2():
    st.subheader("Page 2")
    st.write("This is Page 2.")
    st.map([[0, 0], [1, 1], [2, 2], [3, 3]])

if __name__ == "__main__":
    main()

def create_page1():
    st.title("Opening Page")
    st.bar_chart(HealthcareData)
    text = "Here are words for this page."
    st.write(text)
    
    

