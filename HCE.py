import streamlit as st
import pandas as pd
import altair as alt
import streamlit as st
import plotly.express as px
import geopandas as gpd

st.title ("Distribution of Health Care Expenditures by Service by State of Residence in 2020 (in millions)")

df = pd.DataFrame(pd.read_csv("HealthcareExpenditures2020.csv"))

def main():
    menu = ["United States", "North Carolina", "Focus on Care"]
    choice = st.sidebar.selectbox("Navigate", menu)

    if choice == "United States":
        home_page()
    elif choice == "North Carolina":
        page1()
    elif choice == "Focus on Care":
        page2()


def home_page():
    st.title("Total Healthcare Expenditures by State in 2020")
    st.subheader("This graph allows you to see the different states amounts of total healthcare expenditures from the year 2020")
    text = "California has the highest amount of healthcare expenditures and Wyoming has the lowest amount of healthcare expenditures."
    st.write(text)  
    
    st.write(df)
    
    state_selector = st.selectbox("Select a State", ['All'] + df['Location'].unique().tolist())

    if state_selector != 'All':
        filtered_df = df[df['Location'] == state_selector]
    else:
        filtered_df = df  

    fig = px.bar(filtered_df, x='Location', y='Total', text='Total', title=f'Total Expenditure for {state_selector}')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')

    st.plotly_chart(fig)


def page1():
    st.title("North Carolina Healthcare Expenditures")
    st.subheader("Here is a breakdown of the different healthcare services and their expenditures")
    text = "From this you can see we spend the most on blank and the least on blank2."
    st.write(text)
    
    data = {
    'Location': ['North Carolina'],
    'Hospital Care': [35243],
    'Physicians': [26322],
    'Prescriptions': [15251],
    'Nursing Home': [5484],
    'Dental Services': [4800],
    'Home Health Care': [2715],
    'Medical Durables': [1532],
    'Other': [3185]
        }

    df = pd.DataFrame(data)

    service_names = ["Hospital Care", "Physicians", "Prescriptions", "Nursing Home", "Dental Services",
                 "Home Health Care", "Medical Durables", "Other"]

    st.title("Bar Chart Selector")
    
    selected_service = st.selectbox("Select a Service", service_names)

    fig = px.bar(df, x='Location', y=selected_service, title=f'{selected_service} in North Carolina')
    st.plotly_chart(fig)

    
def page2():
    st.title("A New Focus on Care")
    st.subheader("The highest expense for healthcare in North Carolina is spent in Hospitals")
    text = "Having a focus on primary care (Physicians) can improve individuals health. In turn this will keep people healthy and allow them to stay out of hospitals. This will allow for North Carolina's healthcare expenditures to decrease"
    st.write(text)


if __name__ == "__main__":
    main()



    
    

