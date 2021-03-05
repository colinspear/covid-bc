# covid-bc

A locally hosted (though I am currently on the waitlist for free Streamlit hosting, so should be public-facing soon) Streamlit dashboard showing daily and weekly rolling average Covid case counts and positivity rate for British Columbia. Uses BCCDC [case data]('http://www.bccdc.ca/Health-Info-Site/Documents/BCCDC_COVID19_Dashboard_Case_Details.csv') and [lab data]('http://www.bccdc.ca/Health-Info-Site/Documents/BCCDC_COVID19_Dashboard_Lab_Information.csv').

To host locally, make sure you have python >= 3.6 and pip installed. Then you can either just `pip install streamlit` or `pip install -r requirements.txt` and fire it up using `streamlit run covid_app.py`. 

I did this after reading about [Streamlit](https://docs.streamlit.io/en/stable/) and wanted a quick reference to some up to date covid information. This seemed like a good use case and indeed it was! It really is amazing how easy Streamlit is to use. I definitely recommend checking it out. 
