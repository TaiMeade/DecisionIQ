import streamlit as st
from streamlit import Page

# Page config
st.set_page_config(layout="wide")

# Create pages for navigation
jobOfferPage = st.Page("jobOfferPage.py", title="Job Offer Comparison", icon="💼")
qualityOfLifePage = st.Page("qualityOfLifePage.py", title="Quality of Life Comparison", icon="😀")
costOfLivingPage = st.Page("costOfLivingPage.py", title="Cost of Living Comparison", icon="💰")

# Create navigation
currentPage = st.navigation({
    "Pages" : [
        jobOfferPage,
        qualityOfLifePage,
        costOfLivingPage
    ]
})

currentPage.run()