import streamlit as st
st.title("Number of Days to Hours")
st.write("Simple calculation to convert days to hours")
from days_to_units import days_to_units
user_input=int(st.text_input("Enter number of days to convert in number of hours::"))
total_hours=days_to_units(user_input)
with st.form(key='my_form.'):
    days_to_units=st.form_submit_button(label="Convert days to hours")
if days_to_units:
    st.write(total_hours)
