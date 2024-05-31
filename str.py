import streamlit as st
from datetime import datetime, time

st.header('Slider')
#1
st.subheader('AGE')
age = st.slider('How old are you', 1, 100, 18)
st.write('I am', age,'years old')
#2
st.subheader('RANGE')
values = st.slider('Select a range of values', 0.00, 100.00, (25.00, 75.00))

#3
st.subheader('TIME RANGE')
appointment = st.slider('Select your appointment time:', value = (time(11,30), time(12,45)))
st.write('Youre scheduled for:', appointment)

#4
 st.subheader('Datetime Slider')
                        start_time = st.slider('When do we start?', value = datetime(2020, 1, 1, 9, 30),
                                               format = 'MM/DD/YY - hh:mm')
st.write('start time:', start_time)
                                               
                        

