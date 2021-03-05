import streamlit as st
import altair as alt

# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

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


case_data, lab_data = load_data()

bc_cases = case_data.groupby('Reported_Date').size()
bc_cases = bc_cases.rename_axis('Date')
bc_cases.name = 'New cases'
ref_date = bc_cases.index.values[-2]
one_week = bc_cases.index.values[-9]


st.title("BC Covid Stats as of " + ref_date)

bc_lab_data = lab_data.loc[lab_data['Region']=='BC']

left_column, right_column = st.beta_columns(2)
left_column.subheader('New cases:')
left_column.header(str(bc_cases.iloc[-2]))

avg_positivity = round(bc_lab_data.loc[(bc_lab_data['Date'] > one_week) & (bc_lab_data['Date'] <=
                ref_date), 'Positivity'].mean(), 2)
right_column.subheader('7-day positivity:')
right_column.header('{0:.2%}'.format(avg_positivity/100))

#st.sidebar(st.write(bc_cases[-1]))

#TODO: improve chart
st.subheader('New cases')
bc_cases = bc_cases.reset_index()
bc_cases['7 day rolling'] = bc_cases.rolling(window=7).mean()
case_melt = pd.melt(
    bc_cases, id_vars='Date', value_vars=['New cases', '7 day rolling']
)

def line_chart(df, x, y, y_title, color):
    c = alt.Chart(df).mark_line().encode(
        alt.X(x, axis=alt.Axis(
                labelOverlap=True, 
                ticks=False)),
        alt.Y(y, axis=alt.Axis(
                title=y_title)),
        color=alt.Color(color, legend=alt.Legend(title=None))
    )
    return c

c = line_chart(case_melt, 'Date', 'value', 'Count', 'variable')
st.altair_chart(c, use_container_width=True)

st.subheader('7 day rolling positivity rate')
bc_lab_data['rolling_pos'] = bc_lab_data['Positivity'].rolling(window=7).mean()

pos_melt = pd.melt(
    bc_lab_data, id_vars=['Date'], value_vars=['Positivity', 'rolling_pos']
)

d = line_chart(pos_melt, 'Date', 'value', 'Percent', 'variable')
st.altair_chart(d, use_container_width=True)


st.table(lab_data.tail())
st.table(case_data.tail())


