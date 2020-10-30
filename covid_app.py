import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

st.title("BC Covid Stats")

CASE_DATA_URL = (
    'http://www.bccdc.ca/Health-Info-Site/Documents/BCCDC_COVID19_Dashboard_Case_Details.csv'
)
LAB_DATA_URL = (
    'http://www.bccdc.ca/Health-Info-Site/Documents/BCCDC_COVID19_Dashboard_Lab_Information.csv'
)

def load_data():
    case_data = pd.read_csv(CASE_DATA_URL)
    lab_data = pd.read_csv(LAB_DATA_URL)
    return case_data, lab_data


# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
case_data, lab_data = load_data()
# Notify the reader that the data was successfully loaded.
data_load_state.text("Loading data... Done!")

#positivity = lab_data[['HA', 'Positivity']].groupby('HA').count()

st.header("BC, New daily cases")
bc_cases = case_data.groupby('Reported_Date').size()
bc_cases = bc_cases.rename_axis('Date')
bc_cases.name = 'New cases'

st.sidebar.subheader(
    'New cases, ' + str(bc_cases.index.values[-2]) + ': ' + str(bc_cases.iloc[-2])
)
#st.sidebar(st.write(bc_cases[-1]))

st.line_chart(bc_cases)
st.table(bc_cases.tail(10))

st.table(lab_data.tail(10))
st.table(case_data.tail())


