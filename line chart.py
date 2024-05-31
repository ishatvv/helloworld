import streamlit as st
import pandas as pd
import numpy as np

st.header('line chart')
chart_data = pd.dataframe(np.random.randn(20, 3),
                          columns=['a','b','c'])
st.line_chart(chart_data)
                          
                          

