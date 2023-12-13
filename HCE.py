import streamlit as st
import pandas as pd
import altair as alt
import streamlit as st
import plotly.express as px

st.title ("Distribution of Health Care Expenditures by Service by State of Residence in 2020 (in millions)")

HealthcareData = pd.read_csv("/Users/annahowell/Documents/programming_directory/dsba5122/Healthcare-Expenditures-Service-and-State-2020/Untitled/Healthcare Expenditures.csv",delimiter='\t')

pd.DataFrame(HealthcareData)

def main():
    st.title("Home)")

    menu = ["Home", "Page 1", "Page 2", "Page 3"]
    choice = st.sidebar.selectbox("Navigate", menu)

    if choice == "Home":
        home_page()
    elif choice == "name 1":
        page1()
    elif choice == "name 2":
        page2()
    elif choice == "name 3":
        page3()

def home_page():
    st.subheader("Home Page")
    st.write("Need More Words")

def page1():
    st.subheader("Page 1")
    st.write("write a desc")
    selected_state = st.sidebar.selectbox ("Select a State", df['State'].unique())
    filtered_df = df[df['State'] == selected_state]
    st.bar_chart(filtered_df['Total'])







def page2():
    st.subheader("Page 2")
    st.write("This is Page 2.")
    st.map([[0, 0], [1, 1], [2, 2], [3, 3]])






def page3():
    st.subheader("Page 2")
    st.write("This is Page 2.")
    st.map([[0, 0], [1, 1], [2, 2], [3, 3]])



if __name__ == "__main__":
    main()


    
    

