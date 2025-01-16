#Cheatsheet https://docs.streamlit.io/develop/quick-reference/cheat-sheet
import pandas as pd
import streamlit as st
import numpy as np
st.title('For Title: st.title')
st.write('For Line: st.write')
slider=st.slider('For Slide', 0, 100, 10) #10 for default value
st.write(f'You Selected. {slider}')
if st.button('Click on Button'):
    st.write('Opened Successfully')
else:
    st.write('Unsuccessful')
radio=st.radio('Select Option',('Radio','Button'))
st.write(f'You select, {radio}')
#box=st.selectbox('Select Option',('Radio','Button'))
#st.write(f'You select, {box}')
sb=box=st.sidebar.selectbox('Select Option',('Radio','Button'))
#a=st.text_input('Enter Your Name')
#st.write(f'Name is. {a}')
st.sidebar.text_input('Enter Your Whatsapp')
st.sidebar.file_uploader('Chhose File', type='csv')
data=pd.DataFrame({
    'first column': list(range(1,11)),
    'second column': list(range(1,11))
    }) #A range not arrange
st.line_chart(data)



