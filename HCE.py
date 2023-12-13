import streamlit as st
import pandas as pd
import altair as alt
import streamlit as st
import plotly.express as px
import json

st.title ("Distribution of Health Care Expenditures by Service by State of Residence in 2020 (in millions)")

HealthcareData = pd.read_csv("/Users/annahowell/Documents/programming_directory/dsba5122/Healthcare-Expenditures-Service-and-State-2020/Untitled/Healthcare Expenditures.csv",delimiter='\t')

pd.DataFrame(HealthcareData)

def main():
    st.title("Home)")

    menu = ["Home", "Page 1", "Page 2"]
    choice = st.sidebar.selectbox("Navigate", menu)

    if choice == "Home":
        home_page()
    elif choice == "US Map of Total Healthcare Expenditures for Each State":
        page1()
    elif choice == "Breakdown of Each Service Total Expenditures":
        page2()
    elif choice == "Breakdown of Each Service Total Expenditures for Each State":
        page3()

def home_page():
    st.subheader("Home Page")
    st.write("Need More Words")

def page1():
    st.subheader("Page 1")
    st.write("write a desc")
    fig = px.choropleth_mapbox(HealthcareData,
         geojson=geomap,
        featureidkey='properties.NAME',
        locations='state',
        color='val',
        color_continuous_scale="YlOrRd",
        mapbox_style="carto-positron",
        zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
        opacity=0.5)
    fig.update_layout(margin={"r":0, "t":0, "l":0, "b":0})
    
    st.plotly_chart(fig)







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

def create_page1():
    st.title("Opening Page")
    st.bar_chart(HealthcareData)
    text = "Here are words for this page."
    st.write(text)
    
    

