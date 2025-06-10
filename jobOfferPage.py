import streamlit as st

# title
st.title("Job Offers:")

# Separate page into columns (going to attempt to make it versatile via a icon that the user can press)
# numColumns = st.number_input("Number of Jobs to Compare:", min_value=3, max_value=6, value="min", step=1,)
# NOTE: I decided to abandon this idea as a user should never really need to compare more than 2-3 jobs at a time

# Create the columns
categories, jobA, jobB, jobC = st.columns(4)

with categories:
    st.subheader("Categories")
    
    st.write("")
    st.write("")
    st.write("Base Salary:")

    st.write("")
    st.write("")
    st.write("Hours Worked:")
    st.write("Retirement Match:")
    st.write("Signing Bonus:")
    st.write("Employee Stock Participation Plan:")
    st.write("Bonus Expectation:")
    st.write("Long Term Incentive:")
    st.write("Paid Time Off:")
    st.write("Professional Development Funds:")
    st.write("Work Setting")
    st.write("Space/Environment")
    st.write("Other Resources/Stipends:")

with jobA:
    st.subheader("Job A")

    st.text_input("")

with jobB:
    st.subheader("Job B")

with jobC:
    st.subheader("Job C")